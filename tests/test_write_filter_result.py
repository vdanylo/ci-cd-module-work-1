import os
import pytest

from task.task import write_filter_result


@pytest.fixture()
def output_file(tmpdir_factory):
    return str(tmpdir_factory.mktemp('data').join('output.txt'))

@pytest.fixture()
def filtered_lines():
    return ["Filtered line 1\n", "Filtered line 2\n"]

@pytest.mark.parametrize("filtered_lines", [
    [],
    ["Single line\n"],
    ["Line 1\n", "Line 2\n", "Line 3\n"]
])
def test_write_filter_result(output_file, filtered_lines):
    write_filter_result(output_file, filtered_lines)

    assert os.path.exists(output_file)

    with open(output_file, 'r') as file:
        result_lines = file.readlines()

    assert result_lines == filtered_lines
