import os

def update_safari_run_2c():
    path = "complete_safari_run.py"
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    old_path_str = """# Stage 2c from (20, 6) to Area 2 (North) transition (26 steps)
path_stage2c = [
    "Up", "Up", "Up", # (20, 6) -> (20, 3) (3 steps)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", # (20, 3) -> (7, 3) (13 steps)
    "Down", "Down", # (7, 3) -> (7, 5) (2 steps)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left" # (7, 5) -> warp (8 steps)
]"""

    new_path_str = """# Stage 2c from (10, 3) to Area 2 (North) transition (13 steps)
path_stage2c = [
    "Left", "Left", "Left", # (10, 3) -> (7, 3) (3 steps)
    "Down", "Down", # (7, 3) -> (7, 5) (2 steps)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left" # (7, 5) -> warp (8 steps)
]"""

    code = code.replace(old_path_str, new_path_str)

    with open(path, "w", encoding="utf-8") as f:
        f.write(code)

    print("Successfully updated complete_safari_run.py with Stage 2c from (10, 3).")

if __name__ == "__main__":
    update_safari_run_2c()
