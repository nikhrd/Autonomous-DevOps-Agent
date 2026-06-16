from git import Repo


class GitAgent:

    def create_branch(
        self,
        repo_path,
        branch_name
    ):

        repo = Repo(repo_path)

        repo.git.checkout(
            "-b",
            branch_name
        )

        return branch_name

    def commit_all(
        self,
        repo_path,
        message
    ):

        repo = Repo(repo_path)

        repo.git.add(A=True)

        commit = repo.index.commit(
            message
        )

        return commit.hexsha

    def push_branch(
        self,
        repo_path,
        branch_name
    ):

        repo = Repo(repo_path)

        origin = repo.remote(
            name="origin"
        )

        origin.push(branch_name)

        return True