
import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, directory))
        valid_target_dir = os.path.commonpath([absolute_path, target_dir]) == absolute_path
       
        if os.path.isdir(target_dir) == False:
            raise ValueError(f"{target_dir} is not a directory")

        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f"Error {e}"
