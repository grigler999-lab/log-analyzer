def read_log_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines


def analyze_logs(lines):
    info_count = 0
    warning_count = 0
    error_count = 0

    for line in lines:
        line = line.strip()

        if "INFO" in line:
            info_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "ERROR" in line:
            error_count += 1

    return info_count, warning_count, error_count


def show_summary(info_count, warning_count, error_count):
    print("Log summary:")
    print(f"INFO: {info_count}")
    print(f"WARNING: {warning_count}")
    print(f"ERROR: {error_count}")


def main():
    filename = "sample.log"

    lines = read_log_file(filename)
    info_count, warning_count, error_count = analyze_logs(lines)

    show_summary(info_count, warning_count, error_count)


main()