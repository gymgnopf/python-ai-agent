import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, directory))
        valid_target_dir = (
            os.path.commonpath([absolute_path, target_dir]) == absolute_path
        )

        if os.path.isdir(target_dir) == False:
            raise ValueError(f"{target_dir} is not a directory")

        if valid_target_dir == False:
            return f'\tError: Cannot list "{directory}" as it is outside the permitted working directory'
        files = os.listdir(target_dir)

        return_files = []
        for file in files:
            current_file = target_dir + "/" + file
            file_size = os.path.getsize(current_file)
            is_dir = os.path.isdir(current_file)
            return_files.append(f"  - {file}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(return_files)

    except Exception as e:
        return f"\tError {e}"
