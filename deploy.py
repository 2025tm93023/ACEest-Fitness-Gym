
from pathlib import Path
import sys
import subprocess

BASE_DIR = Path(__file__).resolve().parent

VERSIONS = {
    "1.0": "Aceestver-1.0.py",
    "1.1": "Aceestver-1.1.py",
    "1.1.2": "Aceestver1.1.2_fixed.py",
    "2.0.1": "Aceestver2.0.1.py",
    "2.1.2": "Aceestver-2.1.2.py",
    "2.2.1": "Aceestver-2.2.1.py",
    "2.2.4": "Aceestver-2.2.4.py",
    "3.0.1": "Aceestver-3.0.1.py",
    "3.1.2": "Aceestver-3.1.2_fixed.py",
    "3.2.4": "Aceestver-3.2.4.py",
}


def deploy(version):
    print(f"Preparing deployment of ACEest Fitness v{version}")

    filename = VERSIONS.get(version)

    if filename is None:
        print(f"DEPLOYMENT FAILED: Version {version} is not approved.")
        return False

    app_path = BASE_DIR / filename

    if not app_path.is_file():
        print(f"DEPLOYMENT FAILED: Application file not found: {filename}")
        return False

    try:
        with app_path.open("rb") as source:
            compile(source.read(), str(app_path), "exec")
    except (SyntaxError, OSError) as error:
        print(f"DEPLOYMENT FAILED: Validation error: {error}")
        return False

    print(f"Validation passed: {filename}")
    print(f"Launching ACEest Fitness v{version}...")

    subprocess.Popen([sys.executable, str(app_path)], cwd=str(BASE_DIR))
    print(f"Deployment started for version {version}.")
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py deploy.py VERSION")
        sys.exit(1)

    sys.exit(0 if deploy(sys.argv[1]) else 1)
