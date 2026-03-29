import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))  # file_path not abs_file_path

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: '{file_path}' is not in the working dir"

    parent_dir = os.path.dirname(abs_file_path)
    try:
        os.makedirs(parent_dir, exist_ok=True)  # exist_ok=True so it doesn't crash if dir already exists
    except Exception as e:
        return f"Could not create the parent dirs: {parent_dir} = {e}"

    try:
        with open(abs_file_path, "w") as f:  # abs_file_path not file_path
            f.write(content)
        return f"Successfully wrote to '{file_path}' ({len(content)} characters written)"
    except Exception as e:
        return f"Failed to write file: {file_path}, {e}"
    

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to a file, creating it if it doesn't exist",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file, relative to working directory"
                },
                "content": {
                    "type": "string",
                    "description": "Content to write to the file"
                }
            },
            "required": ["file_path", "content"]
        }
    }
}