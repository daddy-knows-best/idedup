import io
import sys
import pytest

from idedup.main import main as idedup_main


def _simulate_idedup_output(input_data: str, first: bool = True) -> str:
    """Simulate the output of idedup.idedup_alt to compute expected output.

    This mirrors the behavior in `src/idedup/main.py`:
    - lines are read from stdin, stripped with str.strip()
    - when `first` is True, first occurrence is kept; otherwise value is overwritten
    - number width is computed as (last_line // 10) + 5
    - output is each mapping printed as ``{index:>{width}}\t{key}\n`` in insertion order
    """
    indexed = {}
    last_line = 0
    # emulate reading lines as the program does
    buf = io.StringIO(input_data)
    for idx, line in enumerate(buf, start=1):
        key = line.strip()
        last_line = idx
        if first:
            if key in indexed:
                continue
        indexed[key] = idx

    number_of_digit = (last_line // 10) + 5
    parts = []
    for k, v in indexed.items():
        parts.append(f"{v:>{number_of_digit}}\t{k}")
    return "\n".join(parts) + ("\n" if parts else "")


def _run_main_and_get_output(monkeypatch, input_data: str, args=None) -> str:
    args = args or []
    monkeypatch.setattr(sys, "argv", ["idedup"] + args)
    monkeypatch.setattr(sys, "stdin", io.StringIO(input_data))

    # Capture stdout by replacing sys.stdout temporarily
    buf = io.StringIO()
    old_stdout = sys.stdout
    try:
        sys.stdout = buf
        idedup_main()
    finally:
        sys.stdout = old_stdout

    return buf.getvalue()


@pytest.mark.parametrize(
    "input_data,first",
    [
        ("apple\nbanana\napple\norange\nbanana\n", True),
        ("", True),
        ("one\ntwo\nthree\nfour\n", True),
        ("same\nsame\nsame\nsame\n", True),
        ("  spaces  \n\ttabs\t\n  spaces  \n\ttabs\t\n", True),
    ],
)
def test_idedup_behaviour(monkeypatch, input_data, first):
    """Parametrized tests covering the common behaviors of the CLI.

    The expected output is computed with the same algorithm used by the
    implementation so tests remain robust to the number-width calculation.
    """
    out = _run_main_and_get_output(monkeypatch, input_data)
    expected = _simulate_idedup_output(input_data, first=first)
    assert out == expected


def test_line_number_formatting(monkeypatch):
    """Ensure all printed line-number fields have the same width."""
    # 12 lines to force a width change if the algorithm had a bug
    input_data = "\n".join(f"line{i}" for i in range(12)) + "\n"
    out = _run_main_and_get_output(monkeypatch, input_data)
    lines = [ln for ln in out.splitlines() if ln]
    assert lines, "expected non-empty output"

    widths = [len(ln.split("\t")[0]) for ln in lines]
    assert all(w == widths[0] for w in widths), "line number widths are inconsistent"


def test_reverse_mode_updates_indices(monkeypatch):
    """When run with -r the recorded index should be the last occurrence."""
    input_data = "a\na\nb\na\nb\n"
    # run with -r (reverse) as the argument
    out = _run_main_and_get_output(monkeypatch, input_data, args=["-r"])

    # parse output into mapping key -> index
    mapping = {}
    for ln in out.splitlines():
        if not ln:
            continue
        num, key = ln.split("\t", 1)
        mapping[key] = int(num.strip())

    # last occurrences: 'a' last at line 4, 'b' last at line 5
    assert mapping.get("a") == 4
    assert mapping.get("b") == 5
