from copy import error
from file_reader import read_log_file
from log_analyzer import analyze_logs

def show_summary(info_count, warning_count, error_count, unknown_count):
    print("Log summary:")
    print(f"INFO: {info_count}")
    print(f"WARNING: {warning_count}")
    print(f"ERROR: {error_count}")
    print(f"UNKNOWN: {unknown_count}")

def show_errors(error_lines):
    print("\nError lines:")

    if not error_lines:
        print("No errors found.")
        return

    for line in error_lines:
        print(line)

def show_warnings(warning_lines):
    print("\nWarning lines:")

    if not warning_lines:
        print("No warnings found.")
        return

    for line in warning_lines:
        print(line)

def show_unknown(unknown_lines):
    print("\nUnknown lines:")

    if not unknown_lines:
        print("No unknown lines found.")
        return

    for line in unknown_lines:
        print(line)

def main():
    
    filename = input("Enter the log file name: ").strip()
    
    if filename == "":
        print("Error: No file name was entered.")
        return

    lines = read_log_file(filename)

    
    if lines is None:
        return

    if not lines:
        print("Log file is empty.")
        return
    
    
    info_count, warning_count, error_count, warning_lines, error_lines , unknown_lines = analyze_logs(lines)

    show_summary(info_count, warning_count, error_count, len(unknown_lines))
    show_warnings(warning_lines)
    show_errors(error_lines)
    show_unknown(unknown_lines)


main()