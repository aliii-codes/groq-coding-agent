# 🛠️ groq-coding-agent
**Autonomous Python coding agent powered by Groq's LLaMA 3.3-70b**

[![GitHub stars](https://img.shields.io/github/stars/aliii-codes/groq-coding-agent?style=for-the-badge)](https://github.com/aliii-codes/groq-coding-agent/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/aliii-codes/groq-coding-agent?style=for-the-badge)](https://github.com/aliii-codes/groq-coding-agent/network)
[![GitHub issues](https://img.shields.io/github/issues/aliii-codes/groq-coding-agent?style=for-the-badge)](https://github.com/aliii-codes/groq-coding-agent/issues)
[![License](https://img.shields.io/github/license/aliii-codes/groq-coding-agent?style=for-the-badge)](LICENSE)

![Tech Stack](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Tech Stack](https://img.shields.io/badge/Groq-LLaMA%203.3--70b-brightgreen?style=for-the-badge&logo=groq)
![Tech Stack](https://img.shields.io/badge/Package%20Manager-uv-orange?style=for-the-badge)

## 🚀 Highlights
- **Agentic Loop**: Autonomously solves coding tasks through iterative reasoning and action.
- **4 Built-in Tools**: File system navigation, code reading/writing, and Python execution.
- **Groq-Native**: Leverages Groq's high-performance inference for LLaMA 3.3-70b.
- **Production-Ready**: Robust error handling and sandboxed execution environment.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **File System Navigation** | Explore project directories and list files with sizes |
| 📖 **Code Reading** | Retrieve and analyze file contents |
| ✍️ **Code Writing** | Create/edit files with intelligent content generation |
| ▶️ **Python Execution** | Run Python scripts and capture results |
| 🔄 **Iterative Reasoning** | Multi-step problem solving with tool usage |
| 🛡️ **Sandboxed Execution** | Prevents unauthorized file access |

## 🛠️ Tech Stack

| Category | Technologies |
|----------|----------------|
| **LLM** | Groq (LLaMA 3.3-70b) |
| **Language** | Python 3.10+ |
| **Package Manager** | uv |
| **Environment** | python-dotenv |

## 🏃‍♂️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aliii-codes/groq-coding-agent.git
   cd groq-coding-agent
   ```

2. Set up virtual environment and install dependencies:
   ```bash
   uv venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Unix
   uv install groq python-dotenv
   ```

3. Create `.env` file:
   ```
   GROQ_API_KEY=your_key_here
   ```

## 🚀 Usage

```bash
# Basic usage
uv run main.py "fix the bug in calc.py"

# With verbose output
uv run main.py "list files in root" --verbose
```

## 📁 Project Structure

```
groq-coding-agent/
├── functions/          # Tool implementations
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
├── config.py           # Configuration constants
├── main.py             # Main agent loop
├── test.py             # Testing utilities
└── pyproject.toml      # Project metadata
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## 🐞 Bug Reports & Feature Requests

Please use the [issue tracker](https://github.com/aliii-codes/groq-coding-agent/issues) for reporting bugs or requesting features.

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Acknowledgements**: Built with ❤️ using Groq and inspired by the FreeCodeCamp agentic AI course.
