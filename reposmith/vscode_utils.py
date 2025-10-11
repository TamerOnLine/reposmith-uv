from __future__ import annotations

import os
import json
from pathlib import Path

from .core.fs import write_file


def get_python_interpreter_path(project_root: Path) -> str:
    """
    Return the Python interpreter path for Visual Studio Code.

    This function determines the appropriate Python interpreter path
    based on the presence of a virtual environment (venv).

    Args:
        project_root (Path): The repository root (where .venv might live).

    Returns:
        str: The path to the Python interpreter.
             - If the venv exists, its interpreter is used.
             - Otherwise, falls back to 'python.exe' (Windows)
               or 'python3' (Linux/Mac).
    """
    venv = project_root / ".venv"
    if os.name == "nt":
        venv_python = venv / "Scripts" / "python.exe"
        fallback = "python.exe"
    else:
        venv_python = venv / "bin" / "python"
        fallback = "python3"

    return str(venv_python) if venv_python.exists() else fallback


def update_vscode_files(project_root: Path) -> None:
    """
    Create or update VS Code files: .vscode/settings.json, .vscode/launch.json,
    and project.code-workspace, choosing the correct Python interpreter path.
    """
    vscode_dir = project_root / ".vscode"
    vscode_dir.mkdir(parents=True, exist_ok=True)

    interpreter = get_python_interpreter_path(project_root)

    # settings.json
    settings = {
        "python.defaultInterpreterPath": interpreter,
        "python.analysis.typeCheckingMode": "basic",
    }
    write_file(vscode_dir / "settings.json", json.dumps(settings, indent=2) + "\n")

    # launch.json
    launch = {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal",
                "python": interpreter,
            }
        ],
    }
    write_file(vscode_dir / "launch.json", json.dumps(launch, indent=2) + "\n")

    # project.code-workspace
    workspace = {
        "folders": [{"path": "."}],
        "settings": {"python.defaultInterpreterPath": interpreter},
    }
    write_file(project_root / "project.code-workspace", json.dumps(workspace, indent=2) + "\n")

    print(
        "VS Code files updated: settings.json, launch.json, project.code-workspace"
    )
