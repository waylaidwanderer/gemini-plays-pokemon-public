# Helper for Gen 3 naming screen button generation
GRID = {
    'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3), 'E': (0, 4), 'F': (0, 5), '.': (0, 7),
    'G': (1, 0), 'H': (1, 1), 'I': (1, 2), 'J': (1, 3), 'K': (1, 4), 'L': (1, 5), ',': (1, 7),
    'M': (2, 0), 'N': (2, 1), 'O': (2, 2), 'P': (2, 3), 'Q': (2, 4), 'R': (2, 5), 'S': (2, 6),
    'T': (3, 0), 'U': (3, 1), 'V': (3, 2), 'W': (3, 3), 'X': (3, 4), 'Y': (3, 5), 'Z': (3, 6), ' ': (3, 7),
}

def get_naming_buttons(name: str, confirm: bool = True, start_pos: tuple[int, int] = (0, 0)) -> list[str]:
    """Generates button sequence to type an uppercase name from start_pos (default (0,0))."""
    buttons = []
    cur_r, cur_c = start_pos
    for ch in name.upper():
        if ch not in GRID:
            continue
        target_r, target_c = GRID[ch]
        # Step left to col <= 5 before changing rows so we never hit blank columns
        while cur_c > 5 and target_r != cur_r:
            buttons.append("Left")
            cur_c -= 1
        while cur_c > min(target_c, 5):
            buttons.append("Left")
            cur_c -= 1
        while cur_c < min(target_c, 5):
            buttons.append("Right")
            cur_c += 1
        while cur_r < target_r:
            buttons.append("Down")
            cur_r += 1
        while cur_r > target_r:
            buttons.append("Up")
            cur_r -= 1
        while cur_c < target_c:
            buttons.append("Right")
            cur_c += 1
        buttons.append("A")
    if confirm:
        buttons.extend(["Start", "A"])
    return buttons
