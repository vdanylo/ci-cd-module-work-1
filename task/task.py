def get_input_lines(input_file: str) -> [str]:
    """Read lines from an input file.

    Args:
        input_file (str): The path to the input file.

    Returns:
        list: A list of lines read from the input file.
    """
    with open(input_file, 'r') as file:
        lines = file.readlines()
    return lines