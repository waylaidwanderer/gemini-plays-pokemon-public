import mgba
import time

class Navigator:
    def __init__(self, max_buttons=90):
        self.button_count = 0
        self.max_buttons = max_buttons

    def press(self, buttons):
        count = sum(1 for b in buttons if not b.startswith("sleep"))
        if self.button_count + count > self.max_buttons:
            print(f"Budget warning: {self.button_count + count}/{self.max_buttons}")
        self.button_count += count
        mgba.press_buttons(buttons)

    def get_pos(self):
        return mgba.get_coordinates()

    def escape_battle_if_any(self):
        # Only if we suspect a battle, try clean escape sequence:
        # In Gen 1 battle: Run is bottom-right (Down -> Right -> A)
        # But in overworld, this would move down/right.
        # To test if in battle without moving if in overworld:
        # In battle, B cancels move select or text.
        # In overworld, B does nothing!
        # If we press Start in overworld, menu opens. In battle, Start does nothing.
        pass

    def step(self, d):
        old = self.get_pos()
        self.press([d, "sleep 200"])
        new = self.get_pos()
        return old, new

    def walk_path(self, directions):
        results = []
        for d in directions:
            old, new = self.step(d)
            results.append((d, old, new))
            print(f"Step {d}: {old} -> {new}")
            if old == new:
                print(f"Movement {d} did not change position from {old}.")
                # Could be wall or battle. Let's check with a B press or stop.
                break
        return results
