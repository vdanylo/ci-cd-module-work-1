def filter_lines_by(lines: [str], keyword: str) -> [str]:
    """Filter lines based on a keyword.

    Args:
        lines (list): A list of input lines.
        keyword (str): The keyword used for filtering lines.

    Returns:
        list: A list of filtered lines that contain the keyword (case-insensitive).
    """
    filtered_lines = [line for line in lines if keyword in line.lower()]
    return filtered_lines



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
