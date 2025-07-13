def print_in_red(text, end='\n'):
    # Set the text color to red using ANSI escape code.
    print(f'\033[31m{text}\033[0m', end=end)


def print_in_bw(text, end='\n'):
    # Set the text color to bright white using ANSI escape code.
    print(f'\033[97m{text}\033[0m', end=end)