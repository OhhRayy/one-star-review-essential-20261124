"""One-Star Review of Something Essential
(make.fun bounty u-0xb3e689-one-star-review-of-something-essential-c7234629).

Writes one deadpan one-star review to /output/entry.txt. Deterministic:
the same line, byte for byte, on every run. No network, no randomness,
no input.

The line was picked for the judge's brief: a real complaint filed in
earnest against an everyday essential that cannot be fixed (gravity),
deadpan throughout, with the turn in the last word ("Unforgivable") —
after billions of years of flawless service, one dropped phone is
apparently the last straw.
"""

import os

LINE = (
    "One star. Gravity: held everything down perfectly for billions of "
    "years, then dropped my phone once, face-down. Unforgivable."
)


def main() -> None:
    text = LINE
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters,
    # not only white space.
    assert 1 <= len(text) <= 160, "line must be 1-160 Unicode code points"
    assert text == text.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "line must not contain hidden control characters"
    )
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
