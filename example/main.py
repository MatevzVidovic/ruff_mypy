"""Simple calculator for expressions containing integers, +, and * operators."""

from __future__ import annotations

import argparse


def evaluate_expression(expression: str) -> int:
    """Evaluate an expression containing + and * with standard precedence.

    The parser supports non-negative integers and ignores surrounding whitespace.
    """
    stripped = expression.replace(" ", "")
    if not stripped:
        raise ValueError("Expression is empty.")

    total = 0
    for term in stripped.split("+"):
        if not term:
            raise ValueError("Invalid syntax near '+'.")
        product = 1
        for factor in term.split("*"):
            if not factor:
                raise ValueError("Invalid syntax near '*'.")
            product *= int(factor)
        total += product
    return total


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Evaluate an arithmetic expression with + and *."
    )
    parser.add_argument("expression", help="Expression to evaluate, e.g. '2+3*4'")
    args = parser.parse_args()
    result = evaluate_expression(args.expression)
    print(result)


if __name__ == "__main__":
    main()
