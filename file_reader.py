def read_log_file(filename):
    try:
        with open(filename, "r") as file:
            
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    