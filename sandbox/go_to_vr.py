import mgba

class Nav:
    def __init__(self, budget=70):
        self.budget = budget
        self.used = 0

    def get_pos(self):
        p = mgba.get_coordinates()
        return p['x'], p['y']

    def press(self, seq):
        btn_count = len([b for b in seq if not b.startswith("sleep")])
        if self.used + btn_count > self.budget:
            return False
        self.used += btn_count
        mgba.press_buttons(seq)
        return True

    def run_battle(self):
        # Clear battle text / intro and attempt Run
        self.press(["A", "sleep 250", "B", "sleep 250", "A", "sleep 250", "B", "sleep 250"])
        self.press(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 400", "B", "sleep 200", "B", "sleep 150"])

    def step(self, d):
        ox, oy = self.get_pos()
        if not self.press([d, "sleep 180"]):
            return ox, oy
        nx, ny = self.get_pos()
        if (nx, ny) == (ox, oy):
            # Check if battle or dialogue
            self.run_battle()
            nx, ny = self.get_pos()
        return nx, ny

    def walk_to(self, tx, ty, max_steps=40):
        steps = 0
        while steps < max_steps:
            x, y = self.get_pos()
            if x == tx and y == ty:
                return True
            if self.used >= self.budget:
                return False
            if x < tx:
                d = "Right"
            elif x > tx:
                d = "Left"
            elif y < ty:
                d = "Down"
            elif y > ty:
                d = "Up"
            self.step(d)
            steps += 1
        return False

    def route22(self):
        # We start around (33, 9)
        # First ensure out of battle
        self.run_battle()
        print("After run attempt, pos:", self.get_pos())
        
        # Canonical Route 22 waypoints from (33, 9):
        # 1. Down to (33, 12)
        # 2. Left to (31, 12)
        # 3. North through grass to (31, 8)
        # 4. North through gap at (31, 7) to Upper Highway (31, 5)
        # 5. West along Upper Highway to (16, 5)
        # 6. Hop south at (16, 7) down ledge to (16, 8) -> (16, 12)
        # 7. West to (5, 12)
        # 8. North through carpet to (5, 10)
        # 9. East to (11, 10)
        # 10. North to (11, 6)
        # 11. West to (8, 6)
        # 12. North to (8, 5) (Gatehouse entrance)
        wps = [
            (33, 12),
            (31, 12),
            (31, 8),
            (31, 5),
            (16, 5),
            (16, 7),
            (16, 12),
            (5, 12),
            (5, 10),
            (11, 10),
            (11, 6),
            (8, 6),
        ]
        for wx, wy in wps:
            self.walk_to(wx, wy)
            if self.used >= self.budget:
                break
        
        # If at (8, 6), enter gatehouse
        cx, cy = self.get_pos()
        if (cx, cy) == (8, 6):
            self.press(["Up", "sleep 300", "Up", "sleep 300"])
        print("Finished script at pos:", self.get_pos(), "used buttons:", self.used)

if __name__ == "__main__":
    n = Nav(budget=70)
    n.route22()
