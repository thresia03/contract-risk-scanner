"""Pre-flight check for the coordinator (Step 0).

Usage: python output/validate_input.py <path>
Prints "OK" and exits 0 if the file looks like a contract.
Otherwise prints one line "ERROR: <reason>" and exits 1.
Read-only: never writes any file.
"""
import re
import sys
from pathlib import Path

MIN_MARKERS = 3  # distinct contract-language signals required

MARKERS = {
    "agreement/contract wording": r"\b(agreement|contract)\b",
    "obligation wording (shall)": r"\bshall\b",
    "party definition": r"\b(by and between|between|party|parties|customer|vendor|licensor|licensee)\b",
    "term/termination wording": r"\b(term|terminat\w*|renew\w*|effective date)\b",
    "payment wording": r"\b(fees?|payment|invoice|pay)\b",
}


def check(path_str: str) -> str | None:
    """Return an error reason, or None if the file passes."""
    path = Path(path_str)
    if not path.is_file():
        return f"{path_str} does not exist or is not a file."
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return f"{path_str} is not readable UTF-8 text."
    if not text.strip():
        return f"{path_str} is empty."
    found = [name for name, rx in MARKERS.items() if re.search(rx, text, re.I)]
    if len(found) < MIN_MARKERS:
        return (
            f"{path_str} contains no recognisable contract language "
            f"(found {len(found)} of {MIN_MARKERS} required signals: parties, obligations, term)."
        )
    return None


def main() -> int:
    if len(sys.argv) != 2:
        print("ERROR: usage: python output/validate_input.py <path>")
        return 1
    reason = check(sys.argv[1])
    if reason:
        print(f"ERROR: {reason}")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
