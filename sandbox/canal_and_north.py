import mgba

class Route23Surfer:
    def __init__(self, budget=80):
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
        # Clear dialogue text
        self.press(["A", "sleep 180", "B", "sleep 180", "A", "sleep 180", "B", "sleep 180"])
        # Attempt to run from wild battle
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

    def surf_to_north_bank(self):
        print("Starting surf from:", self.get_pos())
        # Surf north along column 11
        while True:
            x, y = self.get_pos()
            if y <= 71:
                print("Landed on north bank at:", x, y)
                break
            if self.used >= self.budget:
                print("Budget limit reached at:", x, y)
                break
            self.step("Up")

if __name__ == "__main__":
    s = Route23Surfer(budget=80)
    s.surf_to_north_bank()
