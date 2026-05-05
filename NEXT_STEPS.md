# NEXT_STEPS — Paper 10 initial release push

The repo has been built via create-repo. It needs:

1. A GitHub repo to be created (the orchestrator only builds locally; remote creation is a manual step).
2. `git push` from your local machine.

## Step 1: Create the GitHub repo

Visit https://github.com/new and create a repo named exactly: **APF-Paper-10-Calculus-of-Finite-Continuability**

Important: do NOT check the "Initialize this repository with a README/.gitignore/license" checkboxes. The local build is the source of truth and any pre-populated files would create a divergent history.

## Step 2: Push from PowerShell

```powershell
cd "C:\Users\EthanBrooke\My Drive\__APF Library\Codebase\APF-Paper-10-Calculus-of-Finite-Continuability"
git init -b main
git remote add origin https://github.com/Ethan-Brooke/APF-Paper-10-Calculus-of-Finite-Continuability.git
git add -A
git commit -m "Initial release: Paper 10"
git push -u origin main --force
```

## Step 3 (optional): Enable GitHub Pages

After the push lands, visit https://github.com/Ethan-Brooke/APF-Paper-10-Calculus-of-Finite-Continuability → Settings → Pages, set Branch: main, Folder: /docs. The interactive DAG appears at `https://ethan-brooke.github.io/APF-Paper-10-Calculus-of-Finite-Continuability/` within ~30 seconds.

## Step 4 (optional): Mint Zenodo DOI

Log into Zenodo, GitHub tab, find the new repo, flip the toggle on. The next git tag will mint a child version DOI. The current zenodo.json has placeholder DOI fields that will need updating once the deposit is created.

## What this repo bundles

- Paper 10 manuscript (.tex + .pdf)
- `apf/` subset (core spine modules from codebase v7.9)
- `ai_context/` AI-onboarding pack (AGENTS.md, FRAMEWORK_OVERVIEW.md, GLOSSARY.md, etc.)
- `README.md`, `START_HERE.md`, `REVIEWERS_GUIDE.md` — human + AI reading paths
- `docs/index.html` — interactive D3.js derivation DAG (GitHub Pages source)
- `interactive_dag.html` — same DAG at root for discoverability
- `APF_Reviewer_Walkthrough.ipynb` — Colab notebook
- `MANIFEST.custom` — preservation contract for future automated refreshes
- `pyproject.toml`, `run_checks.py`, `zenodo.json`, `LICENSE`

This repo joins the 11-paper core derivational series alongside Papers 0-7, 9, 10, 13.

