import os

def write_file(working_directory:str, file_path: str, content: str)-> str:
    try:

        abs_path = os.path.abspath(working_directory)
        current_file = os.path.normpath(os.path.join(abs_path, file_path))
        is_valid_file = os.path.commonpath([abs_path, current_file]) == abs_path

        if not is_valid_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(current_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(current_file), exist_ok=True)

        with open(current_file, mode="w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'
