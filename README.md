
# groq-coding-agent

A Python coding agent powered by Groq's LLaMA 3.3 model, designed to automate coding tasks with an agentic loop and four core tools: read files, write files, execute Python code, and list directories. Ideal for developers looking to streamline repetitive coding tasks.

## Features

- **Agentic Loop**: Iteratively processes tasks until completion.
- **File Operations**: Reads and writes files programmatically.
- **Python Execution**: Runs Python code within the agent.
- **Directory Listing**: Navigates and lists directory contents.
- **Groq Integration**: Leverages LLaMA 3.3 for advanced reasoning and code generation.

## Tech Stack

- **Language**: Python
- **Model**: Groq (LLaMA 3.3)
- **Dependencies**: `groq`, `os`, `subprocess`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aliii-codes/groq-coding-agent.git
   cd groq-coding-agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Groq API access:
   - Obtain an API key from [Groq](https://groq.com).
   - Set the `GROQ_API_KEY` environment variable:
     ```bash
     export GROQ_API_KEY="your_api_key_here"
     ```

## Usage

1. Run the agent:
   ```bash
   python main.py
   ```

2. Interact with the agent by providing tasks or prompts. Example:
   ```
   Write a Python function to calculate the factorial of a number and save it to a file named `factorial.py`.
   ```

## Project Structure

```
groq-coding-agent/
├── config.py          # Configuration constants
├── functions/         # Tool functions (read, write, execute, list)
│   ├── get_file_content.py
│   ├── write_file.py
│   ├── run_python.py
│   └── list_directory.py
├── main.py            # Entry point for the agent
└── requirements.txt   # Project dependencies
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
