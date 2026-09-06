import mgba

class Route23Segment1:
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

    def clear_text_or_run(self):
        # First try clearing dialogue text
        self.press(["A", "sleep 180", "B", "sleep 180", "A", "sleep 180", "B", "sleep 180"])
        # Then try battle run escape just in case
        self.press(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 350", "B", "sleep 150", "B", "sleep 100"])

    def step(self, d):
        ox, oy = self.get_pos()
        if not self.press([d, "sleep 180"]):
            return ox, oy
        nx, ny = self.get_pos()
        if (nx, ny) == (ox, oy):
            self.clear_text_or_run()
            nx, ny = self.get_pos()
        return nx, ny

    def walk_to(self, tx, ty, max_steps=35):
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
        # Clear initial Cascade badge text
        self.clear_text_or_run()
        print("Starting segment 1 at:", self.get_pos())
        
        wps = [
            (8, 134),
            (14, 134),
            (14, 128),
            (14, 124),
            (8, 124),
            (8, 118),
            (10, 118),
            (10, 110),
            (10, 104)
        ]
        for wx, wy in wps:
            self.walk_to(wx, wy)
            if self.used >= self.budget:
                break
        print("End segment 1 pos:", self.get_pos(), "used buttons:", self.used)

if __name__ == "__main__":
    s1 = Route23Segment1(budget=70)
    s1.run()
