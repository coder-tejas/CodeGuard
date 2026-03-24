import typer
import os

from github_client import get_pr_files
github_token = os.getenv("GITHUB_TOKEN")
app=typer.Typer()

# @app.command
# def get_pr_url():
#     pr_url = string(input("Enter"))
if __name__ == "__main__":
    files = get_pr_files(
        "https://github.com/jitsi/jitsi-meet/pull/17056",
        token=github_token
    )
    for f in files:
        print(f["filename"], f["additions"], f["deletions"])
        print(f["patch"][:200])  # first 200 chars of diff