#!/usr/bin/env python3
"""Entry for make.fun bounty: one word for your Wi-Fi.

The task: exactly ONE WORD describing your Wi-Fi — funniest and most
accurate. The winning word becomes the sponsor's network name.

The word is "Buffering": every Wi-Fi network in the world spends half its
life buffering, and a network literally called "Buffering" tells every
guest exactly what they are in for before they even connect.

Prints the single word to stdout and also writes it to the output
directory (``/output/entry.txt`` by default, or ``$MAKEFUN_OUTPUT`` when
set), verifying the written file by reading it back.

Python 3.13, stdlib only, deterministic: no network, clock, or randomness.
"""

import os
import sys

ENTRY = "Buffering"

MAX_WORD_LEN = 30


def is_single_word(text: str) -> bool:
    """True only if the text is one token: no whitespace anywhere, and
    splitting on whitespace yields exactly one piece."""
    if not text or text != text.strip():
        return False
    return len(text.split()) == 1 and not any(ch.isspace() for ch in text)


def emit(text: str) -> None:
    """Print the entry to stdout. If print() fails (e.g. a closed pipe),
    fall back to a direct sys.stdout.write so the entry still goes out."""
    try:
        print(text, flush=True)
    except (BrokenPipeError, OSError):
        try:
            sys.stdout.write(text + "\n")
            sys.stdout.flush()
        except OSError:
            # Nothing left to try; the run cannot deliver its entry.
            raise


def validate(text: str) -> None:
    """The entry must be exactly one word: a single token, no spaces,
    no punctuation beyond the word itself, no stray whitespace or control
    characters."""
    if not text:
        raise ValueError("entry must not be empty")
    if len(text) > MAX_WORD_LEN:
        raise ValueError(f"entry must be at most {MAX_WORD_LEN} chars, got {len(text)}")
    if not is_single_word(text):
        raise ValueError("entry must be exactly one word (single token, no spaces)")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not text.isalpha():
        raise ValueError("entry must be a single alphabetic word")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")


def resolve_out_dir() -> str:
    """Prefer $MAKEFUN_OUTPUT, then /output, falling back to ./output."""
    requested = os.environ.get("MAKEFUN_OUTPUT") or "/output"
    try:
        os.makedirs(requested, exist_ok=True)
        probe = os.path.join(requested, ".write_probe")
        with open(probe, "w", encoding="utf-8") as f:
            f.write("ok")
        os.remove(probe)
        return requested
    except OSError:
        fallback = os.path.join(os.getcwd(), "output")
        os.makedirs(fallback, exist_ok=True)
        return fallback


def main() -> int:
    validate(ENTRY)
    # Re-check the exact bytes that will be emitted: the word plus the
    # single trailing newline print() appends, nothing else.
    emitted = (ENTRY + "\n").encode("utf-8")
    if emitted.decode("utf-8").strip() != ENTRY or not is_single_word(ENTRY):
        raise RuntimeError("verification failed: emitted bytes are not the one word")
    # The stdout print is the entry; it must succeed before anything else.
    emit(ENTRY)
    try:
        out_dir = resolve_out_dir()
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        # Verify the written file by reading it back: same text, same
        # length, and byte-identical to the entry (no newline added).
        with open(path, "rb") as f:
            written_bytes = f.read()
        if written_bytes != ENTRY.encode("utf-8"):
            raise RuntimeError("verification failed: written bytes do not match")
        with open(path, "r", encoding="utf-8") as f:
            written = f.read()
        if written != ENTRY:
            raise RuntimeError("verification failed: written entry does not match")
        if len(written) != len(ENTRY):
            raise RuntimeError(
                f"verification failed: written entry is {len(written)} chars, "
                f"expected {len(ENTRY)}"
            )
    except OSError as exc:
        # File output is a convenience copy only; the printed entry is
        # already out, so a failed write must not fail the run.
        print(f"warning: could not write entry.txt: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
