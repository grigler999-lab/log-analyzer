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