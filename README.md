# groq-coding-agent 

A Python coding agent powered by Groq (LLaMA 3.3-70b) that autonomously solves coding tasks using an agentic loop and 4 built-in tools.

Built as a Groq-native alternative to the Gemini-based FreeCodeCamp agentic AI course.

## What it does

Give it a task in plain English and it will autonomously:
- Explore the project directory
- Read relevant files
- Write or edit code
- Run Python files to verify results
- Loop until the task is complete

## Tools

| Tool | Description |
|------|-------------|
| `get_files_info` | List files and directories with sizes |
| `get_file_content` | Read the contents of any file |
| `write_file` | Create or overwrite files |
| `run_python_file` | Execute Python files and capture output |

## Usage
```bash
# Basic usage
uv run main.py "fix the bug in calc.py"

# With verbose output
uv run main.py "what files are in the root dir?" --verbose
```

## Setup
```bash
git clone https://github.com/aliii-codes/groq-coding-agent
cd groq-coding-agent
uv venv && .venv\Scripts\activate
uv add groq python-dotenv
```

Create a `.env` file:
```
GROQ_API_KEY=your_key_here
```

## Stack

- **LLM**: LLaMA 3.3-70b via Groq
- **Package manager**: uv
- **Language**: Python 3.10+

## License

MIT
