# GitHub Learning Journal

This file is your guide to getting started with Git and GitHub. Use it to track your progress and jot down important notes as you learn.


## Getting Started

- [ ] Install Git on your computer
- [ ] Sign up for a GitHub account
- [ ] Set up your Git username and email (`git config`)
- [ ] Create your first repository on GitHub

## Essential Git Commands

```bash
git init                # Initialize a new Git repository
git clone <repo-url>    # Clone an existing repository
git status              # Check the status of your files
git add <file>          # Stage changes for commit
git commit -m "message" # Commit your changes
git commit -am "message" # stages and commits all files
git push                # Push changes to GitHub
git pull                # Pull latest changes from GitHub
```

## Helpful Resources

- [GitHub Documentation](https://docs.github.com/)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Kodekloud](https://learn.kodekloud.com/user/courses/git-for-beginners/module/299037d1-d4d5-4d22-8eb3-b8fc6af3f8d2/lesson/feedback)

## Tips

- Create branches for new features or fixes.

## Working with Branches

```bash
git fetch                        # Update local info about remote branches
git branch                       # List all local branches
git branch -d <branch-name>      # Delete a local branch
git checkout <branch-name>       # Switch to an existing branch
git checkout -b <branch-name>    # Create and switch to a new branch
git push -u origin <branch-name> # Push new branch to GitHub and set upstream
```
## Working with Remotes

```bash
git remote -v                 # List remote repositories and their URLs
git clone <repo-url>          # Clone a repository from GitHub
git fetch                     # Download objects and refs from another repository
git merge <branch>            # Merge a branch into your current branch
git pull                      # Fetch and merge changes from the remote repository
```
>

<img width="1006" height="438" alt="Git" src="https://github.com/user-attachments/assets/89e62a8a-9d6b-408d-9d8e-647a6a4e0620" />

- Use `git remote -v` to verify your repository is connected to GitHub.
- `git clone <repo-url>` copies a remote repository to your local machine.
- `git fetch` updates your local copy with changes from the remote, but does not merge them.
- `git merge <branch>` combines changes from another branch into your current branch.
- `git pull` is a shortcut for running `git fetch` followed by `git merge`.

## Working with Merge Conflicts:
When you encounter a merge conflict:

1. Open the conflicted file in your editor (e.g., `vi`, VS Code).
2. Look for conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) and resolve the conflicts by editing the file.
3. Save the file after resolving the conflicts.
4. Stage the resolved file:
    ```bash
    git add Readme.md
    ```
5. Commit the resolution:
    ```bash
    git commit -m "Resolve merge conflict"
    ```
## Working with Fork:
Forking a repository allows you to make changes to someone else's project without affecting the original. To work with forks:

1. Click the **Fork** button on the repository page in GitHub.
2. Clone your fork to your local machine:
    ```bash
    git clone <your-fork-url>
    ```
3. Add the original repository as an upstream remote:
    ```bash
    git remote add upstream <original-repo-url>
    ```
4. Fetch changes from the original repository:
    ```bash
    git fetch upstream
    ```
5. Merge upstream changes into your local branch:
    ```bash
    git merge upstream/main
    ```
6. Push your changes to your fork and create a pull request to contribute back.


- Write clear, descriptive commit messages.
- Always pull before pushing to avoid conflicts.

Happy learning!
