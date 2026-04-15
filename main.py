from copy import error





def analyze_logs(lines):
    info_count = 0
    warning_count = 0
    error_count = 0
    error_lines = []
    warning_lines = []
    unknown_lines = []

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        if "INFO" in line:
            info_count += 1
        elif "WARNING" in line:
            warning_count += 1
            warning_lines.append(line)
        elif "ERROR" in line:
            error_count += 1
            error_lines.append(line)
        else:
            unknown_lines.append(line)

    return info_count, warning_count, error_count, warning_lines, error_lines ,unknown_lines


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
    from file_reader import read_log_file
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