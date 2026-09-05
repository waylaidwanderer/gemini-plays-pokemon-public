import mgba

class Route23Nav:
    def __init__(self, max_buttons=85):
        self.button_count = 0
        self.max_buttons = max_buttons

    def get_pos(self):
        p = mgba.get_coordinates()
        return p['x'], p['y']

    def press(self, buttons):
        btn_only = [b for b in buttons if not b.startswith("sleep")]
        if self.button_count + len(btn_only) > self.max_buttons:
            print(f"Button limit reached ({self.button_count}/{self.max_buttons}).")
            return False
        self.button_count += len(btn_only)
        mgba.press_buttons(buttons)
        return True

    def escape_battle_or_dialogue(self):
        # A/B to advance text
        self.press(["A", "sleep 120", "B", "sleep 120", "B", "sleep 120"])
        # Attempt to run from battle (Down -> Right -> A)
        self.press(["Down", "sleep 80", "Right", "sleep 80", "A", "sleep 350", "B", "sleep 150", "B", "sleep 100"])

    def step(self, d):
        old_x, old_y = self.get_pos()
        if not self.press([d, "sleep 180"]):
            return old_x, old_y
        new_x, new_y = self.get_pos()
        if (new_x, new_y) == (old_x, old_y):
            self.escape_battle_or_dialogue()
            new_x, new_y = self.get_pos()
        return new_x, new_y

    def walk_to(self, target_x, target_y, max_steps=40):
        steps = 0
        while steps < max_steps:
            x, y = self.get_pos()
            if x == target_x and y == target_y:
                print(f"Reached ({target_x}, {target_y})")
                return True
            if self.button_count >= self.max_buttons:
                print(f"Budget reached at ({x}, {y})")
                return False

            if x < target_x:
                d = "Right"
            elif x > target_x:
                d = "Left"
            elif y < target_y:
                d = "Down"
            elif y > target_y:
                d = "Up"

            self.step(d)
            steps += 1
        return False

    def walk_waypoints(self, waypoints):
        for wx, wy in waypoints:
            ok = self.walk_to(wx, wy, max_steps=abs(wx - self.get_pos()[0]) + abs(wy - self.get_pos()[1]) + 5)
            if not ok and self.button_count >= self.max_buttons:
                break
