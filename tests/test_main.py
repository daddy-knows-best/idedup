import io
import sys
from contextlib import contextmanager
from idedup.main import main


@contextmanager
def capture_stdout():
    """Capture stdout for testing"""
    new_out = io.StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield new_out
    finally:
        sys.stdout = old_out


@contextmanager
def provide_stdin(content):
    """Provide stdin content for testing"""
    old_stdin = sys.stdin
    sys.stdin = io.StringIO(content)
    try:
        yield
    finally:
        sys.stdin = old_stdin


def test_basic_deduplication():
    """Test basic deduplication functionality"""
    input_data = "apple\nbanana\napple\norange\nbanana\n"
    expected_output = "    1\tapple\n    2\tbanana\n    4\torange\n"

    with provide_stdin(input_data):
        with capture_stdout() as output:
            main()

    assert output.getvalue() == expected_output


def test_empty_input():
    """Test handling of empty input"""
    input_data = ""
    expected_output = ""

    with provide_stdin(input_data):
        with capture_stdout() as output:
            main()

    assert output.getvalue() == expected_output


def test_all_unique_lines():
    """Test handling of input with no duplicates"""
    input_data = "one\ntwo\nthree\nfour\n"
    expected_output = "    1\tone\n    2\ttwo\n    3\tthree\n    4\tfour\n"

    with provide_stdin(input_data):
        with capture_stdout() as output:
            main()

    assert output.getvalue() == expected_output


def test_all_duplicate_lines():
    """Test handling of input with all duplicate lines"""
    input_data = "same\nsame\nsame\nsame\n"
    expected_output = "    1\tsame\n"

    with provide_stdin(input_data):
        with capture_stdout() as output:
            main()

    assert output.getvalue() == expected_output


def test_whitespace_handling():
    """Test handling of whitespace in input"""
    input_data = "  spaces  \n\ttabs\t\n  spaces  \n\ttabs\t\n"
    expected_output = "    1\tspaces\n    2\ttabs\n"

    with provide_stdin(input_data):
        with capture_stdout() as output:
            main()

    assert output.getvalue() == expected_output


def test_line_number_formatting():
    """Test line number formatting with different input sizes"""
    # Create input with 12 lines to test number formatting
    input_data = "\n".join(f"line{i}" for i in range(12))

    with provide_stdin(input_data):
        with capture_stdout() as output:
            main()

    # Check that all line numbers are right-aligned
    lines = output.getvalue().splitlines()
    if lines:
        # All lines should have the same width for the line number part
        line_number_width = len(lines[0].split("\t")[0])
        for line in lines:
            assert len(line.split("\t")[0]) == line_number_width
