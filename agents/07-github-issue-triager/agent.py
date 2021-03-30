    response = llm.invoke(messages)
    return parse_json_response(response.content)


def fetch_github_issue(url: str) -> tuple[str, str, list]:
    """Fetch issue details from GitHub API."""
    import re
    import requests

    match = re.match(r"https://github.com/([^/]+)/([^/]+)/issues/(\d+)", url)
    if not match:
        raise ValueError(f"Invalid GitHub issue URL: {url}")

    owner, repo, issue_num = match.groups()
    api_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_num}"
    headers = {}
    if token := os.getenv("GITHUB_TOKEN"):
        headers["Authorization"] = f"token {token}"

    r = requests.get(api_url, headers=headers, timeout=10)
    r.raise_for_status()
    data = r.json()
    return data["title"], data.get("body", ""), [l["name"] for l in data.get("labels", [])]


def main():
    parser = argparse.ArgumentParser(description="GitHub Issue Triager")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--issue-url", help="GitHub issue URL")
    group.add_argument("--title", help="Issue title (use with --body)")
    parser.add_argument("--body", default="", help="Issue body text")
