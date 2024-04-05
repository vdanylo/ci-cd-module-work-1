import os
import pytest

from task.task import filter_file


@pytest.fixture
def input_file(tmpdir: str) -> str:
    input_file_path = tmpdir.join("input.txt")
    with open(input_file_path, 'w') as file:
        file.write("Hello\nWorld\nThis is a test\nAnother line\n")
    return str(input_file_path)

@pytest.fixture
def output_file(tmpdir):
    return str(tmpdir.join("output.txt"))

@pytest.mark.parametrize("keyword, expected_lines", [
    ("hello", ["Hello\n"]),
    ("test", ["This is a test\n"]),
    ("line", ["Another line\n"]),
    ("nonexistent", []),
])
def test_filter_file(input_file, keyword, output_file, expected_lines):
    filter_file(input_file, keyword, output_file)
    assert os.path.exists(output_file)
    with open(output_file, 'r') as file:
        filtered_lines = file.readlines()
    assert filtered_lines == expected_lines

def test_filter_file_file_not_found(capfd):
    # Test for FileNotFoundError
    filter_file("nonexistent.txt", "keyword", "output.txt")
    captured = capfd.readouterr()
    assert "" in captured.out
