import pytest

from task.task import filter_lines_by


@pytest.fixture
def lines():
    return [
        "This is a test\n",
        "Another line with keyword\n",
        "Some other text\n",
        "And another line with keyword"
    ]

@pytest.mark.parametrize("keyword, expected_lines", [
    ("test", ["This is a test\n"]),
    ("keyword", ["Another line with keyword\n", "And another line with keyword"]),
    ("nonexistent", []),
])
def test_filter_lines_by(lines, keyword, expected_lines):
    filtered_lines = filter_lines_by(lines, keyword)
    assert filtered_lines == expected_lines
