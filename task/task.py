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

def write_filter_result(output_file: str, filtered_lines: [str]) -> None:
    """Write filtered lines to an output file.

    Args:
        output_file (str): The path to the output file.
        filtered_lines (list): A list of filtered lines to be written to the output file.

    Returns:
        None
    """
    with open(output_file, 'w') as file:
        file.writelines(filtered_lines)
