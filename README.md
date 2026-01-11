## 🧠 Py Code Reviewer

Py Code Reviewer is a Python-based static code analysis tool designed to help beginners write cleaner, more efficient, and more Pythonic code.
It analyzes Python source code, detects common beginner mistakes, suggests improvements, and estimates algorithmic complexity using Abstract Syntax Tree (AST) analysis.
----------------
## 📌 Why This Project?

Beginner programmers often struggle with:

Inefficient logic

Poor coding practices

Lack of understanding of time complexity

Hard-to-read code

This project acts as a mentor-like code reviewer, providing human-friendly feedback instead of compiler errors.
------------------------
## 🚀 Features

🔍 Static Code Analysis using Python AST

⚠️ Detection of Common Beginner Mistakes

Unused variables

Inefficient loops

Repetitive logic

Deep nesting

💡 Logic Improvement Suggestions

Pythonic alternatives

Cleaner iteration patterns

⏱️ Time Complexity Estimation

Detects nested loops

Estimates Big-O notation

🧑‍🏫 Beginner-Friendly Explanations

Clear, simple, non-technical feedback

🛠️ Tech Stack

Python 3

Abstract Syntax Tree (AST)

Standard Python libraries only
(No external APIs or heavy frameworks)

📂 Project Structure
py-code-reviewer/
│
├── analyzer/
│   ├── __init__.py
│   ├── syntax_checker.py
│   ├── logic_checker.py
│   ├── complexity_analyzer.py
│   ├── suggestions.py
│
├── samples/
│   ├── bad_code.py
│   ├── good_code.py
│
├── reviewer.py
├── requirements.txt
├── README.md
└── LICENSE

▶️ How It Works

The Python code is parsed into an Abstract Syntax Tree

Each analyzer module inspects the AST

Issues, suggestions, and complexity are extracted

A structured review report is generated

▶️ How to Run
1️⃣ Clone the repository
git clone https://github.com/your-username/py-code-reviewer.git
cd py-code-reviewer

2️⃣ Run the reviewer
python reviewer.py
