# 🤝 Contributing to RepoSmith

Thank you for your interest in contributing! 🚀  
RepoSmith is an open-source Python CLI for bootstrapping projects quickly.  
This document explains how to set up your environment, follow coding style, and submit contributions.

---

## 🛠️ Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/liebemama/RepoSmith.git
   cd RepoSmith
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```

3. **Install requirements (dev)**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run tests**
   ```bash
   python -m unittest discover -s tests -v
   ```

---

## 🧑‍💻 Local Development Usage

When working on RepoSmith, you don’t need to install it from PyPI.  
You can run it **directly from source**:

```bash
py -m reposmith.main init --no-venv --entry run.py --with-gitignore --with-license
```

This executes the CLI from your **local code** instead of the published package.  
It’s useful for testing changes before publishing.

If imports fail, prepend your `PYTHONPATH` with the project root:

```bash
# Linux/Mac
export PYTHONPATH="$(pwd):$PYTHONPATH"

# Windows PowerShell
$env:PYTHONPATH = (Get-Location).Path + ';' + $env:PYTHONPATH
```

---

## 🧷 Try RepoSmith with Editable Install (`pip install -e .`)

If you want RepoSmith to behave like an installed package while still reflecting your local changes, use **editable mode**:

```bash
# Install in editable mode
pip install -e .

# Now you can run the CLI directly
reposmith init --no-venv --entry run.py --with-ci
```

- Any changes you make in `reposmith/` will take effect immediately.  
- This is the recommended way to test updates during development.  
- To uninstall:
  ```bash
  pip uninstall -y reposmith-tol
  ```

💡 If the `reposmith` command is not on PATH, you can always run:
```bash
py -m reposmith.main init --no-venv --entry run.py
```

---

## 📦 Build & Install Locally

1. **Clean and build the package**
   ```bash
   python -m build
   # Outputs dist/*.tar.gz and dist/*.whl
   ```

2. **Install the built package locally**
   ```bash
   pip install --force-reinstall dist/*.whl
   ```

3. **Quick verification**
   ```bash
   reposmith --help
   reposmith init --no-venv --entry run.py
   ```

---

## 📏 Code Style

- Follow **PEP8** formatting.
- Keep functions small with clear docstrings.
- Use **atomic writes + backups** for file operations (`reposmith/core/fs.py`).
- Add type hints where possible.

Recommended tools:

```bash
pip install black ruff
black reposmith/ tests/
ruff check reposmith/ tests/
```

---

## 🧪 Tests

- All new features must include unit tests under `tests/`.
- Run tests locally before submitting a Pull Request.
- CI (GitHub Actions) will run automatically on each PR.

```bash
python -m unittest discover -s tests -v
```

---

## 🔄 Submitting Changes

1. **Fork the repository and create a branch**
   ```bash
   git checkout -b feature/my-new-feature
   ```

2. **Commit your changes with a clear message**
   ```bash
   git commit -m "Add: support for --with-django gitignore preset"
   ```

3. **Push to your fork**
   ```bash
   git push origin feature/my-new-feature
   ```

4. **Open a Pull Request** to the `main` branch.

---

## 💡 Feature Requests & Issues

- Use [GitHub Issues](https://github.com/liebemama/RepoSmith/issues) to report bugs or request features.  
- Provide reproduction steps or expected behavior for clarity.

---

## 🧰 Troubleshooting

- **Imports use installed package instead of local code:**  
  Run `pip uninstall -y reposmith-tol` and set `PYTHONPATH` to your repo root.

- **CLI command not found:**  
  Use `py -m reposmith.main ...` instead of `reposmith ...`.

- **Build fails due to metadata:**  
  Check `pyproject.toml` fields (`license`, `license-files`, `project.urls`).

---

## 📜 License

By contributing, you agree that your code will be licensed under the [License](https://img.shields.io/github/license/TamerOnLine/RepoSmith?style=flat-square)

---

💖 Thanks for making RepoSmith better!
