"""Keyed substitution cipher.

The key (deduplicated, letters only) forms the start of the cipher alphabet;
the remaining A-Z letters fill the rest in order. Non-letters pass through
unchanged and case is preserved.
"""

from __future__ import annotations

import argparse
import sys

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def build_cipher_alphabet(key: str) -> str:
    cleaned = "".join(ch for ch in key.upper() if ch.isalpha() and ch in ALPHABET)
    seen: set[str] = set()
    result: list[str] = []
    for ch in cleaned + ALPHABET:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return "".join(result)


def _translate(text: str, src: str, dst: str) -> str:
    table = str.maketrans(src + src.lower(), dst + dst.lower())
    return text.translate(table)


def encrypt(text: str, key: str) -> str:
    return _translate(text, ALPHABET, build_cipher_alphabet(key))


def decrypt(text: str, key: str) -> str:
    return _translate(text, build_cipher_alphabet(key), ALPHABET)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Keyed substitution cipher")
    parser.add_argument("key", help="cipher key (letters only; duplicates ignored)")
    parser.add_argument("text", nargs="?", help="text to process; reads stdin if omitted")
    parser.add_argument("-d", "--decrypt", action="store_true", help="decrypt instead of encrypt")
    args = parser.parse_args(argv)

    text = args.text if args.text is not None else sys.stdin.read()
    op = decrypt if args.decrypt else encrypt
    sys.stdout.write(op(text, args.key))
    if args.text is not None:
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
