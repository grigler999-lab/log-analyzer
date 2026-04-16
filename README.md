# Log Analyzer

## Description

This project is a simple log analyzer written in Python.
It reads a log file, analyzes its content, and displays a summary of log levels.

The program detects:

* INFO messages
* WARNING messages
* ERROR messages
* UNKNOWN lines (lines that do not match known patterns)

---

## How it works

1. The user enters the name of a log file
2. The program reads the file
3. The log is analyzed
4. The result is displayed in the terminal

---

## Project structure

* `main.py` – controls the program flow
* `file_reader.py` – reads the log file
* `log_analyzer.py` – analyzes log content
* `output.py` – prints results to the user

---

## Example output

```text
Log summary:
INFO: 3
WARNING: 2
ERROR: 2
UNKNOWN: 1
```

---

## How to run

1. Open terminal
2. Navigate to the project folder
3. Run:

```bash
python main.py
```

4. Enter the log file name (example: `sample.log`)

---

## Reflection

During this project, I learned:

* how to structure code into multiple modules
* how to separate logic (reading, analysis, output)
* how to use Git and commits step by step

If I had more time, I would:

* add support for more log formats
* improve error handling
* create a graphical interface
