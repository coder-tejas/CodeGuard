from urllib.parse import urlparse
def parse_pr_url(pr_url:str)->tuple[str,str,int]:
    path = urlparse(pr_url).path
    parts = path.strip("/").split("/")

    if len(parts) != 4 or parts[2] != "pull":
        raise ValueError(f"Invalid PR URL:{pr_url}")
    owner = parts[0]
    repo = parts[1]
    pr_number = parts[2]

    return owner,repo,pr_number

from github import Github

def get_pr_files(pr_url: str, token: str) -> list[dict]:
    owner, repo, pr_number = parse_pr_url(pr_url)
    
    g = Github(token)
    repo = g.get_repo(f"{owner}/{repo}")
    pr = repo.get_pull(pr_number)
    
    files = []
    for f in pr.get_files():
        files.append({
            "filename": f.filename,
            "status": f.status,        # added, modified, removed
            "additions": f.additions,
            "deletions": f.deletions,
            "patch": f.patch           # the actual diff
        })
    
    return files