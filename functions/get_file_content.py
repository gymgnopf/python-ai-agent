import os

MAX_CHARS = 10000


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        current_path = os.path.abspath(working_directory)
        current_file = os.path.normpath(os.path.join(current_path, file_path))

        # Die Datei befindet sich im korrekten Ordner wenn der commonpath dem absolutem working directory path
        # entspricht.
        is_valid_file = os.path.commonpath([current_path, current_file]) == current_path
        if not is_valid_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(current_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        file_content_string = ""
        with open(current_file) as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
        return file_content_string
    except Exception as e:
        return f"Error: {e}"
