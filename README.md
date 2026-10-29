# GenAI System Design

## Python environment

Initialize Conda for zsh once, then restart the terminal:

```zsh
conda init zsh
```

Create and activate the project environment, then install dependencies:

```zsh
conda create --prefix ./my_env python=3.13 -y
conda activate ./my_env
pip install -r requirements.txt
```

In future terminal sessions, activate the existing environment from the project directory with:

```zsh
conda activate ./my_env
```

## Redis

```sh
docker run -d \
  --name genai-redis \
  -p 6379:6379 \
  redis/redis-stack-server:latest
```

## Initialize this repo on GitHub

From your project folder, run:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

If the repository already exists on GitHub and you want to connect it:

```bash
git remote set-url origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

If you want to create the repo from the GitHub website instead, follow these steps:

1. Open https://github.com/new
2. Enter a repository name and optional description
3. Choose Public or Private
4. Do not initialize with a README, .gitignore, or license if you already have local files
5. Click Create repository
6. Copy the remote URL and run the `git remote add origin ...` command above

## Notes

- The project includes a `.gitignore` to keep local environment and generated files out of version control.
- This repo is intended to be used with a local Conda environment and local Redis instance.

https://github.com/manifoldailearning/Agentic-ai-Industry-Projects/blob/main/architecture.md
