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