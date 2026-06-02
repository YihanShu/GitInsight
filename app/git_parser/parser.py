from git import Repo

class GitParser:
    def __init__(self, repo_path):
        self.repo = Repo(repo_path)

    def get_commits(self, rev_range):
        commits = list(self.repo.iter_commits(rev_range))
        commits.reverse()

        result = []

        for c in commits:
            result.append({
                "hash": c.hexsha,
                "message": c.message.strip(),
                "author": str(c.author),
                "date": str(c.committed_datetime)
            })

        return result

    def get_diff(self, commit_hash):
        commit = self.repo.commit(commit_hash)
        return commit.diff(commit.parents[0] if commit.parents else None, create_patch=True)