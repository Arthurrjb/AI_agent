import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, abs_file_path]) == working_dir_abs
        if valid_target_dir == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if file_path[-3:] != ".py": 
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", abs_file_path]
        if args != None:
            command.extend(args)
        completed = subprocess.run(command,capture_output=True,cwd=working_dir_abs,timeout=30,text=True)
        result_list = []
        if completed.returncode != 0:
            result_list.append(f"Process exited with code {completed.returncode}")
        if not completed.stdout and not completed.stderr:
            result_list.append("No output produced")
        if completed.stdout:
            result_list.append(f"STDOUT:\n{completed.stdout}")
        if completed.stderr:
            result_list.append(f"STDERR:\n{completed.stderr}")
        return "\n".join(result_list)

    except Exception as e:
        return f"Error: executing Python file: {e}"