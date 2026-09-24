# Python Foundations for AI (`python-foundations-ai`)

Welcome to my core Python engineering repository. The goal of this project is to build a rock-solid foundation in Python programming, moving from basic script writing to production-grade, AI-ready software engineering. 

Before training complex neural networks or orchestrating large language models (LLMs), an AI Engineer must master data validation, state management, memory-efficient data pipelines, and error handling. This repository documents that journey.

---

## Repository Goals
* **Write AI-Ready Code:** Transitioning from loose scripting to strict type-hinted, modular, and optimized Python.
* **Master Data Pipelines:** Learning how to ingest, sanitize, reshape, and export messy real-world data (the hidden 80% of AI engineering).
* **Handle Edge Cases:** Building robust logic that never crashes when encountering bad, missing, or malicious inputs.

---

## Repository Structure

```text
 python-foundations-ai/
│
├──  01_basics_and_logic/
│   ├──  safe_calculator.py      # Exception handling and mathematical edge cases
│   └──  grade_checker.py         # Range evaluation, input validation, and batch processing
│
├──  02_data_structures/
│   ├──  string_manipulation.py  # First/last character extractors and boundary handling
│   └──  matrix_calculator.py     # Multi-dimensional arrays (pure Python matrix operations)
│
├──  03_data_pipelines/
│   ├──  csv_to_json_sanitizer.py # Cleaning messy tabular files into structured JSON data
│   └──  log_parser.py           # Parsing text data using Regex and counting anomalies
│
└──  README.md                    # Repository documentation
```

---

##  Key Concepts Mastered
* **Defensive Programming:** Using `try/except` blocks and structural conditional bounds to handle corrupted or unexpected user inputs gracefully.
* **Batch Processing:** Moving away from single-user `input()` prompts toward processing massive dictionaries, lists, and file streams simultaneously.
* **Data Cleansing:** Converting raw, human-made files (CSV) into machine-readable, nested data standards (JSON) without losing structural integrity.

---

##  Tech Stack & Requirements
* **Language:** Python 3.10+
* **Libraries:** Pure Python Standard Library (`typing`, `json`, `csv`, `math`) — intentionally avoiding external frameworks to master core algorithmic thinking first.

---
*“Garbage in, garbage out. The quality of an AI is bound by the quality of the pipelines that feed it.”*

