import subprocess


def run_flake8(repo_path):

    cmd = [
        "flake8",
        str(repo_path)
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    return result.stdout.splitlines()
def run_mypy(repo_path):

    cmd = [
        "mypy",
        str(repo_path)
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    return result.stdout.splitlines()
def run_pylint(repo_path):

    cmd = [
        "pylint",
        str(repo_path)
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    return result.stdout.splitlines()