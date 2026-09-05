# calculator/main.py

import sys
import argparse
from pkg.calculator import Calculator
from pkg.render import format_json_output


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calculator App",
        usage="python main.py [options] \"<expression>\"",
    )
    parser.add_argument(
        "expression",
        nargs="*",
        help="the expression to evaluate (e.g., 3 + 5)",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="show step-by-step evaluation details",
    )
    args = parser.parse_args()

    if not args.expression:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        return

    expression = " ".join(args.expression)
    calculator = Calculator()

    if args.verbose:
        print(f"[verbose] Evaluating expression: {expression}", file=sys.stderr)

    try:
        result = calculator.evaluate(expression)
        if result is not None:
            if args.verbose:
                print(f"[verbose] Result: {result}", file=sys.stderr)
            to_print = format_json_output(expression, result)
            print(to_print)
        else:
            if args.verbose:
                print("[verbose] Expression is empty or whitespace only.", file=sys.stderr)
            print("Error: Expression is empty or contains only whitespace.")
    except Exception as e:
        if args.verbose:
            print(f"[verbose] Error occurred: {e}", file=sys.stderr)
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
