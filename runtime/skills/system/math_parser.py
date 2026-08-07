"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/skills/system/math_parser.py

Purpose:
    Safe mathematical expression parser.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    13.3
==========================================================
"""

from __future__ import annotations

import ast
import operator

from .math_functions import CONSTANTS, FUNCTIONS


_BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

_UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


class MathParser:
    """
    Safely evaluates mathematical expressions.
    """

    def evaluate(
        self,
        expression: str,
    ):

        expression = (
            expression
            .replace("^", "**")
            .strip()
        )

        tree = ast.parse(
            expression,
            mode="eval",
        )

        return self._visit(tree.body)

    def _visit(self, node):

        #
        # Numbers
        #
        if isinstance(node, ast.Constant):

            if isinstance(node.value, (int, float)):
                return node.value

            raise ValueError("Unsupported constant.")

        #
        # Lists
        #
        if isinstance(node, ast.List):

            return [
                self._visit(element)
                for element in node.elts
            ]

        #
        # Tuples
        #
        if isinstance(node, ast.Tuple):

            return tuple(
                self._visit(element)
                for element in node.elts
            )

        #
        # Binary Operators
        #
        if isinstance(node, ast.BinOp):

            left = self._visit(node.left)

            right = self._visit(node.right)

            operator_type = type(node.op)

            if operator_type not in _BINARY_OPERATORS:
                raise ValueError(
                    f"Unsupported operator: {operator_type}"
                )

            return _BINARY_OPERATORS[operator_type](
                left,
                right,
            )

        #
        # Unary Operators
        #
        if isinstance(node, ast.UnaryOp):

            operand = self._visit(node.operand)

            operator_type = type(node.op)

            if operator_type not in _UNARY_OPERATORS:
                raise ValueError(
                    f"Unsupported unary operator: {operator_type}"
                )

            return _UNARY_OPERATORS[operator_type](
                operand
            )

        #
        # Constants
        #
        if isinstance(node, ast.Name):

            if node.id in CONSTANTS:
                return CONSTANTS[node.id]

            raise ValueError(
                f"Unknown constant: {node.id}"
            )

        #
        # Function Calls
        #
        if isinstance(node, ast.Call):

            if not isinstance(node.func, ast.Name):
                raise ValueError(
                    "Unsupported function."
                )

            function_name = node.func.id

            if function_name not in FUNCTIONS:
                raise ValueError(
                    f"Unknown function: {function_name}"
                )

            arguments = [
                self._visit(argument)
                for argument in node.args
            ]

            return FUNCTIONS[
                function_name
            ](
                *arguments
            )

        raise ValueError(
            f"Unsupported AST node: {type(node).__name__}"
        )