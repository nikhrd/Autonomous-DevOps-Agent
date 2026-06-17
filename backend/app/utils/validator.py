import ast


def validate_python_code(
    code: str
):

    try:

        ast.parse(code)

        return True

    except Exception:

        return False