def _commit(repository_path):
    repo = Repository(repository_path)

    commit_changes = defaultdict(lambda: {'added': 0, 'removed': 0, 'equal': 0, 'ref': 0})

    total_equals = 0

    for commit in repo.traverse_commits():
        commit_date = commit.committer_date.date()

        commit_changes[commit_date]['added'] += commit.insertions
        commit_changes[commit_date]['removed'] += commit.deletions

        # if commit.insertions == commit.deletions and commit.insertions > 100:
        #     print(commit.hash, commit.msg)
        #     commit_changes[commit_date]['equal'] += 1
        #     total_equals += 1
        #
        # if 'refactor' in commit.msg.lower():
        #     commit_changes[commit_date]['ref'] += 1

    print(100 * (total_equals / len(commit_changes)))

    return commit_changes
