import pathlib

root = pathlib.Path(".")

(root / "data").mkdir(parents=True, exist_ok=True)
(root / "notebooks").mkdir(parents=True, exist_ok=True)
(root / "src").mkdir(parents=True, exist_ok=True)
(root / "models").mkdir(parents=True, exist_ok=True)
(root / "configs").mkdir(parents=True, exist_ok=True)
(root / "tests").mkdir(parents=True, exist_ok=True)

# placeholder files
for d in ["data", "notebooks", "models"]:
    (root / d / ".gitkeep").touch()

# remaining files
(root / "main.py").touch()
(root / "src" / "__init__.py").touch()
(root / "src" / "preprocess.py").touch()
(root / "src" / "train.py").touch()
(root / "configs" / "config.yaml").touch()
(root / "tests" / "test_smoke.py").touch()

print("Project structure created (without overwriting README.md or requirements.txt).")
