import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_function import call_function


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)


    system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories
        - Read file contents
        - Execute Python files with optional arguments
        - Write or overwrite files

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages: list[types.Content] = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]



    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
                ),
            },
        ),
    )

    schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Reads the content of a specified file up to 10000 characters.",
        parameters=types.Schema(
          type=types.Type.OBJECT,
          properties={
              "file_path": types.Schema(
                  type=types.Type.STRING,
                  description="The file to read its content, relative to the working directory"
              )
          }
        ),
    )

    schema_write_file= types.FunctionDeclaration(
        name="write_file",
        description="Writes the content into a specified file.",
        parameters=types.Schema(
          type=types.Type.OBJECT,
          properties={
              "file_path": types.Schema(
                  type=types.Type.STRING,
                  description="The file name to write the content into, relative to the working directory"
              ),
              "content": types.Schema(
                  type=types.Type.STRING,
                  description="The specified content to write into the target file."
              )
          }
        ),
    )

    schema_run_python_file= types.FunctionDeclaration(
        name="run_python_file",
        description="Runs a specified python script with the provided arguments and returns its output.",
        parameters=types.Schema(
          type=types.Type.OBJECT,
          properties={
              "file_path": types.Schema(
                  type=types.Type.STRING,
                  description="The python file to execute in a sub process"
              ),
              "args": types.Schema(
                  type=types.Type.ARRAY,
                  items=types.Schema(
                      type=types.Type.STRING
                  ),
                  description="A list of arguments to provide for the execution of the script"
              )
          }
        ),
    )
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file
        ],
    )

    prompt_config= types.GenerateContentConfig(
        tools = [available_functions],
        system_instruction=system_prompt
    )
    for _ in range(20):
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=messages, config=prompt_config
        )

        if response.candidates:
            for candidate in response.candidates:
                if candidate.content:
                    messages.append(candidate.content)

        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        if response.function_calls:
            function_results = []
            for function_call in response.function_calls:
                function_call_result = call_function(function_call, args.verbose)

                if not function_call_result.parts:
                    raise Exception("Parts in function call results not found.")

                if function_call_result.parts[0].function_response is None:
                    raise Exception("The actual function_response of the function_call_response is not set.")

                if function_call_result.parts[0].function_response.response is None:
                    raise Exception("The response inside the function_response is not set.")

                function_results.append(function_call_result.parts[0])

                if args.verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
            messages.append(types.Content(role="user", parts=function_results))



        if not response.function_calls and response.text:
            print(f"Response:\n{response.text}")
            return

    print("The agent couldn't solve your problem in 20 turns")
    return 1
if __name__ == "__main__":
    main()
