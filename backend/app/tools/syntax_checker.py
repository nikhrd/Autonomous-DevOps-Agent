import ast


def check_syntax(file_path):

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            ast.parse(
                f.read()
            )

        return None

    except SyntaxError as e:

        return {
            "line": e.lineno,
            "message": str(e)
        }