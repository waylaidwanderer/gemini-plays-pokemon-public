import mgba
import time

class Navigator:
    def __init__(self, max_buttons=80):
        self.button_count = 0
        self.max_buttons = max_buttons

    def press(self, buttons):
        btn_only = [b for b in buttons if not b.startswith("sleep")]
        if self.button_count + len(btn_only) > self.max_buttons:
            print(f"Budget limit reached ({self.button_count}/{self.max_buttons}). Aborting further presses.")
            return False
        self.button_count += len(btn_only)
        mgba.press_buttons(buttons)
        return True

    def get_pos(self):
        p = mgba.get_coordinates()
        return p['x'], p['y']

    def run_from_battle(self):
        # Down -> Right -> A (RUN)
        print("Escaping potential battle/dialogue...")
        return self.press(["B", "sleep 100", "Down", "sleep 100", "Right", "sleep 100", "A", "sleep 400", "B", "sleep 200", "B", "sleep 100"])

    def cast_strength(self):
        print("Activating Strength with ATLAS...")
        # Start -> Down -> A -> Down -> Down -> A -> A -> B -> B
        return self.press([
            "Start", "sleep 200",
            "Down", "sleep 200",
            "A", "sleep 300",
            "Down", "sleep 200",
            "Down", "sleep 200",
            "A", "sleep 300",
            "A", "sleep 500",
            "A", "sleep 500",
            "B", "sleep 300",
            "B", "sleep 300"
        ])

    def step(self, d):
        old_x, old_y = self.get_pos()
        if not self.press([d, "sleep 200"]):
            return old_x, old_y
        new_x, new_y = self.get_pos()
        if (new_x, new_y) == (old_x, old_y):
            self.run_from_battle()
            new_x, new_y = self.get_pos()
        return new_x, new_y

    def move_to(self, target_x, target_y, max_steps=30):
        steps = 0
        while steps < max_steps:
            x, y = self.get_pos()
            if x == target_x and y == target_y:
                print(f"Reached ({target_x}, {target_y})")
                return True
            
            if x < target_x:
                d = "Right"
            elif x > target_x:
                d = "Left"
            elif y < target_y:
                d = "Down"
            elif y > target_y:
                d = "Up"
            
            new_x, new_y = self.step(d)
            if self.button_count >= self.max_buttons:
                print(f"Budget reached at ({new_x}, {new_y})")
                return False
            steps += 1
        print(f"Failed to reach ({target_x}, {target_y}) within {max_steps} steps. Pos: {self.get_pos()}")
        return False
