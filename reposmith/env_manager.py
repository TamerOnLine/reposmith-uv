# reposmith_tol/env_manager.py
from __future__ import annotations
import os, sys, shutil, subprocess
from pathlib import Path

def _env_python(env_dir: Path) -> Path:
    return env_dir / ("Scripts/python.exe" if os.name == "nt" else "bin/python")

def create_env_with_venv(env_dir: Path) -> None:
    env_dir = env_dir.resolve()
    env_dir.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, "-m", "venv", str(env_dir)], check=True)

def install_deps_with_uv(project_dir: Path, env_dir: Path, req_file: str | None = None) -> None:
    if shutil.which("uv") is None:
        raise RuntimeError("uv غير مثبت. ثبّته: `pip install uv` أو من astral.sh/uv")
    env_py = _env_python(env_dir)
    if req_file:
        subprocess.run(
            ["uv", "pip", "install", "-r", req_file, "--python", str(env_py)],
            cwd=str(project_dir),
            check=True,
        )
    else:
        subprocess.run(
            ["uv", "pip", "install", "-e", ".", "--python", str(env_py)],
            cwd=str(project_dir),
            check=True,
        )

def bootstrap(project_dir: Path, *, use_requirements: bool = False, req_name: str = "requirements.txt") -> Path:
    project_dir = Path(project_dir).resolve()
    env_dir = project_dir / ".venv"
    create_env_with_venv(env_dir)
    req_path = (project_dir / req_name)
    install_deps_with_uv(
        project_dir, env_dir,
        req_file=str(req_path) if use_requirements and req_path.exists() else None
    )
    return env_dir
