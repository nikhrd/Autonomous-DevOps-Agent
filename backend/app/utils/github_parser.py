def parse_repo_name(
    repo_url: str
):

    repo_url = repo_url.rstrip("/")

    parts = repo_url.split("/")

    owner = parts[-2]

    repo = parts[-1]

    return f"{owner}/{repo}"