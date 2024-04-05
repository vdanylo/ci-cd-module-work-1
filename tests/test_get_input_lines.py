import os
import pytest

from task.task import get_input_lines


@pytest.fixture()
def input_file(tmpdir_factory):
    input_file_path = tmpdir_factory.mktemp('data').join('input.txt')
    with open(input_file_path, 'w') as file:
        file.write("This is a test\n"
                   "Another line with keyword\n"
                   "Some other text\n"
                   "And another line with keyword")
    return str(input_file_path)


def test_get_input_lines(input_file):
    lines = get_input_lines(input_file)
    assert len(lines) == 4
    assert lines == ["This is a test\n",
                     "Another line with keyword\n",
                     "Some other text\n",
                     "And another line with keyword"]


def test_get_input_lines_empty_file(tmpdir_factory):
    empty_file_path = tmpdir_factory.mktemp('data').join('empty.txt')
    open(empty_file_path, 'a').close()  # Create an empty file
    lines = get_input_lines(str(empty_file_path))
    assert lines == []


def test_get_input_lines_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        get_input_lines("nonexistent.txt")
