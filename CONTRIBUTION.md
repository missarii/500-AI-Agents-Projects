---

## PR process and checklist
Before opening a PR:
- [ ] Fork and create a branch: feat/<short-desc> or fix/<short-desc>
- [ ] Sign off every commit with `git commit -s` (see below)
- [ ] Update README and metadata
- [ ] Paste real sample output from a run into your agent's README
- [ ] Ensure no secrets or private data are included
- [ ] Rebase onto current `main` — README moves fast and stale branches conflict
- [ ] Confirm license compatibility for added assets

### Sign your commits (DCO)

Every commit needs a `Signed-off-by` line. Use `-s` and git adds it for you:

```bash
git commit -s -m "add my agent"
```

Which appends:

```
Signed-off-by: Your Name <you@example.com>
```

Forgot on commits you already pushed? Fix them all at once:

```bash
git rebase --signoff origin/main
git push --force-with-lease
```

Set `git config user.name` and `git config user.email` first, since the sign-off must
match the commit author. A CI check enforces this on every PR.

This is the [Developer Certificate of Origin](https://developercertificate.org/) — by
signing off you're stating that you wrote the contribution, or otherwise have the right
to submit it under this repository's MIT licence. There's no separate form to fill in
and nothing is stored beyond the commit itself.

PR description should include:
- What changed and why
- How to run the example(s) and tests
- Links to related issues or external artifacts (datasets, model hosts)

Suggested minimal PR template (add to .github/PULL_REQUEST_TEMPLATE.md if helpful):
```markdown
## Summary
Short description of change

