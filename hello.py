#!/usr/bin/env python3
"""A simple hello world terminal app."""

import sys


def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
