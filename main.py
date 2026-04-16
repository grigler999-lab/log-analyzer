from file_reader import read_log_file
from log_analyzer import analyze_logs
from output import show_summary, show_errors, show_warnings, show_unknown



def main():
    
    while True:
        filename = input("Enter the log file name: ").strip()

        if filename == "":
            print("Error: No file name was entered.")
            continue

        lines = read_log_file(filename)

        if lines is None:
            continue

        if not lines:
            print("Log file is empty.")
            continue

        break

        
    info_count, warning_count, error_count, warning_lines, error_lines, unknown_lines = analyze_logs(lines)

    show_summary(info_count, warning_count, error_count, len(unknown_lines))
    show_warnings(warning_lines)
    show_errors(error_lines)
    show_unknown(unknown_lines)


main()