import sys


def read_two_integers() -> tuple[int, int] | None:
    tokens: list[str] = []
    for line in sys.stdin:
        tokens.extend(line.split())
        if len(tokens) >= 2:
            break
    if len(tokens) < 2:
        return None
    try:
        first = int(tokens[0])
        second = int(tokens[1])
    except ValueError:
        return None
    return first, second


def main() -> int:
    result = read_two_integers()
    if result is None:
        print("Failed to read two numbers.", file=sys.stderr)
        return 1
    a, b = result
    print(a * b)
    return 0


if __name__ == "__main__":
    sys.exit(main())
