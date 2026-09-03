import json

def call_function(tool_call, verbose=False):
    function_map = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")

    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    if function_name not in function_map:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps({"error": f"Unknown function: {function_name}"}),
        }

    try:
        function_to_call = function_map[function_name]
        function_result = function_to_call(**function_args)
    except Exception as e:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps({"error": f"Error executing {function_name}: {e}"}),
        }

    return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": json.dumps({"result": function_result}),
    }