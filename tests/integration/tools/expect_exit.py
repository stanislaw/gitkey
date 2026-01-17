#!/usr/bin/env python3
import argparse
import subprocess
import sys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("expected", type=int)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    if not args.command:
        print("error: missing command to execute", file=sys.stderr)
        return 2

    result = subprocess.run(args.command, check=False)
    if result.returncode != args.expected:
        print(
            f"error: expected exit {args.expected}, got {result.returncode}",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
