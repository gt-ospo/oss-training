from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK_DIR = ROOT / "notebook-lessons"
KERNEL_OVERRIDES = {
    "03-git-workflows.ipynb": "bash",
}


def discover_notebooks(argv: list[str]) -> list[Path]:
    if argv:
        notebooks = [Path(arg).resolve() for arg in argv]
    else:
        notebooks = sorted(NOTEBOOK_DIR.glob("*.ipynb"))

    missing = [path for path in notebooks if not path.exists()]
    if missing:
        missing_paths = ", ".join(str(path) for path in missing)
        raise SystemExit(f"Notebook path not found: {missing_paths}")

    return notebooks


def run(command: list[str], env: dict[str, str]) -> None:
    subprocess.run(command, cwd=ROOT, env=env, check=True)


def prepare_env(home_dir: Path) -> dict[str, str]:
    home_dir.mkdir(parents=True, exist_ok=True)

    env = os.environ.copy()
    env["HOME"] = str(home_dir)
    env["JUPYTER_CONFIG_DIR"] = str(home_dir / ".jupyter")
    env["IPYTHONDIR"] = str(home_dir / ".ipython")
    env["PYTHONDONTWRITEBYTECODE"] = "1"

    run(["git", "config", "--global", "user.name", "Notebook Tests"], env)
    run(["git", "config", "--global", "user.email", "notebook-tests@example.com"], env)
    run(["git", "config", "--global", "init.defaultBranch", "main"], env)
    run(
        [
            sys.executable,
            "-m",
            "ipykernel",
            "install",
            "--user",
            "--name",
            "python3",
            "--display-name",
            "Python 3",
        ],
        env,
    )
    run([sys.executable, "-m", "bash_kernel.install"], env)

    return env


def run_notebook(path: Path, env: dict[str, str]) -> int:
    command = [
        sys.executable,
        "-m",
        "pytest",
        "--nbmake",
        "--nbmake-timeout=300",
    ]

    kernel_override = KERNEL_OVERRIDES.get(path.name)
    if kernel_override:
        command.extend(["--nbmake-kernel", kernel_override])

    command.append(str(path.relative_to(ROOT)))
    return subprocess.run(command, cwd=ROOT, env=env).returncode


def main(argv: list[str]) -> int:
    notebooks = discover_notebooks(argv)

    with tempfile.TemporaryDirectory(prefix="notebook-tests-") as tmp_dir:
        env = prepare_env(Path(tmp_dir) / "home")
        exit_code = 0

        for notebook in notebooks:
            print(f"\n=== Testing {notebook.relative_to(ROOT)} ===", flush=True)
            notebook_rc = run_notebook(notebook, env)
            if notebook_rc != 0:
                exit_code = notebook_rc

        return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))