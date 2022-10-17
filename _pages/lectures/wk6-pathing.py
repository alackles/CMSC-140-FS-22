from pathlib import Path

home_dir = "/home/acacia"
home_path = Path(home_dir)
home_path = home_path / "Documents"
print(home_path)
print(Path.cwd())