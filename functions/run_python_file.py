import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:

    try:
        abs_path = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_path, file_path))
        is_valid_file = os.path.commonpath([abs_path, abs_file_path]) == abs_path

        if not is_valid_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not abs_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", abs_file_path]
        if args:
            command.extend(args)

        process_result = subprocess.run(
            command,
            cwd=abs_path,
            capture_output=True,
            text=True,
            timeout=30
        )

        output = []
        if process_result.check_returncode != 0:
            output.append(f"Process exited with code {process_result.returncode}")
        if not process_result.stdout and not process_result.stderr:
            output.append("No output produced")
        if process_result.stdout:
            output.append( f"STDOUT: {process_result.stdout}")
        if process_result.stderr:
            output.append(f"STDERR: {process_result.stderr}")
        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"
