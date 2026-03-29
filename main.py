import os
import sys
import json
from dotenv import load_dotenv
from groq import Groq
from functions.get_files_info import get_file_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.write_file import write_file, schema_write_file
from functions.run_python_file import run_python_file, schema_run_python_file

WORKING_DIR = "calculator"

def call_function(tool_name, tool_args):
    if tool_name == "get_files_info":
        return get_file_info(WORKING_DIR, tool_args.get("directory"))
    elif tool_name == "get_file_content":
        return get_file_content(WORKING_DIR, tool_args.get("file_path"))
    elif tool_name == "write_file":
        return write_file(WORKING_DIR, tool_args.get("file_path"), tool_args.get("content"))
    elif tool_name == "run_python_file":
        return run_python_file(WORKING_DIR, tool_args.get("file_path"), tool_args.get("args", []))
    else:
        return f"Unknown tool: {tool_name}"

def main():
    load_dotenv()
    api_key = os.environ.get("GROQ_API_KEY")

    if len(sys.argv) < 2:
        print("i need a prompt bro")
        sys.exit(1)

    verbose_flag = "--verbose" in sys.argv
    prompt = sys.argv[1]
    client = Groq(api_key=api_key)

    system_prompt = """You are a helpful AI coding agent.

You have access to these tools:
- get_files_info: list files in a directory
- get_file_content: read a file's contents
- write_file: write or create a file
- run_python_file: execute a python file

Rules:
- Be concise and direct. No unnecessary explanations.
- Do ONLY what is asked, nothing more.
- NEVER create files unless absolutely necessary.
- ALWAYS prefer editing existing files over new ones.
- NEVER leave the working directory.
- Think step by step before acting.
- When done, give a short summary of what you did."""

    available_functions = [
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ]

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]

    # agentic loop
    while True:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            tools=available_functions
        )

        # append assistant response to history
        messages.append(response.choices[0].message)

        if response.choices[0].message.tool_calls:
            for tool_call in response.choices[0].message.tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)

                if verbose_flag:
                    print(f"Calling: {tool_name} ({tool_args})")

                result = call_function(tool_name, tool_args)

                if verbose_flag:
                    print(f"Result: {result}")

                # send result back to LLM
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                })
        else:
            # no more tool calls = agent is done
            print(response.choices[0].message.content)
            break

    if verbose_flag:
        print("User Prompt:", prompt)
        print("Total Tokens:", response.usage.total_tokens)

main()