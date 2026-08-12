import os

def update_safari_run_2c():
    path = "complete_safari_run.py"
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    old_path_str = """# Stage 2c: Area 1 (East) to Area 2 (North) transition (31 steps)
path_stage2c = [
    "Right", "Right", "Right", # (17, 8) -> (20, 8) (3 steps)
    "Up", "Up", "Up", "Up", "Up", # (20, 8) -> (20, 3) (5 steps)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", # (20, 3) -> (7, 3) (13 steps)
    "Down", "Down", # (7, 3) -> (7, 5) (2 steps)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left" # (7, 5) -> warp (8 steps)
]"""

    new_path_str = """# Stage 2c from (20, 6) to Area 2 (North) transition (26 steps)
path_stage2c = [
    "Up", "Up", "Up", # (20, 6) -> (20, 3) (3 steps)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", # (20, 3) -> (7, 3) (13 steps)
    "Down", "Down", # (7, 3) -> (7, 5) (2 steps)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left" # (7, 5) -> warp (8 steps)
]"""

    code = code.replace(old_path_str, new_path_str)

    with open(path, "w", encoding="utf-8") as f:
        f.write(code)

    print("Successfully updated complete_safari_run.py with Stage 2c from (20, 6).")

if __name__ == "__main__":
    update_safari_run_2c()
