import mgba

class ButtonBudgetExceeded(Exception):
    pass

class Navigator:
    def __init__(self, max_buttons=90):
        self.button_count = 0
        self.max_buttons = max_buttons

    def press(self, buttons):
        # Count non-sleep actions
        count = sum(1 for b in buttons if not b.startswith("sleep"))
        if self.button_count + count > self.max_buttons:
            raise ButtonBudgetExceeded(f"Cannot press {count} buttons: budget {self.button_count}/{self.max_buttons}")
        self.button_count += count
        mgba.press_buttons(buttons)

    def get_pos(self):
        return mgba.get_coordinates()

    def handle_battle(self):
        # Escape battle cleanly
        seq = [
            "B", "sleep 200", "B", "sleep 200",
            "Down", "sleep 100", "Right", "sleep 100",
            "A", "sleep 350", "B", "sleep 200", "B", "sleep 200"
        ]
        self.press(seq)

    def step(self, d):
        old = self.get_pos()
        self.press([d, "sleep 220"])
        new = self.get_pos()
        if old == new:
            self.handle_battle()
            self.press([d, "sleep 220"])
            new = self.get_pos()
        return new

    def walk_path(self, directions):
        for d in directions:
            old = self.get_pos()
            new = self.step(d)
            print(f"Step {d}: {old} -> {new}")
            if old == new:
                print(f"Blocked moving {d} at {old}")
                return False
        return True
