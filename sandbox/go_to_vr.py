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
        self.press(["B", "sleep 200", "B", "sleep 200", "A", "sleep 200", "B", "sleep 200"])
        self.press(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 400", "B", "sleep 200", "B", "sleep 150"])

    def step(self, d):
        ox, oy = self.get_pos()
        if not self.press([d, "sleep 180"]):
            return ox, oy
        nx, ny = self.get_pos()
        if (nx, ny) == (ox, oy):
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

    def run(self):
        wps = [
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
        cx, cy = self.get_pos()
        if (cx, cy) == (8, 6):
            self.press(["Up", "sleep 350", "Up", "sleep 350"])
        print("End pos:", self.get_pos(), "used:", self.used)

if __name__ == "__main__":
    n = Nav(budget=70)
    n.run()
