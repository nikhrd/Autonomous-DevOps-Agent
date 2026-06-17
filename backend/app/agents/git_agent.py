from git import Repo


class GitAgent:
    def init():
        self.commit_count = 0

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
        self.commit_count += 1

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
    
    def get_commit_count(self):
        return self.commit_count