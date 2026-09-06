import mgba
import time

class Route23Navigator:
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

    def run_battle_or_dialogue(self):
        # A/B to clear text
        self.press(["A", "sleep 200", "B", "sleep 200", "B", "sleep 200", "A", "sleep 200", "B", "sleep 200"])
        # Attempt to run from battle (Down -> Right -> A)
        self.press(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 400", "B", "sleep 200", "B", "sleep 150"])

    def step(self, d):
        ox, oy = self.get_pos()
        if not self.press([d, "sleep 180"]):
            return ox, oy
        nx, ny = self.get_pos()
        if (nx, ny) == (ox, oy):
            self.run_battle_or_dialogue()
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

    def exit_gate_to_route23(self):
        # From Route 22 Gate (4, 7) -> (4, 0)
        print("Starting in gatehouse:", self.get_pos())
        while True:
            x, y = self.get_pos()
            if y == 0 or y > 50: # Exited to Route 23 (y is ~139)
                break
            self.step("Up")
            if self.used >= self.budget:
                break
        print("Exited gatehouse, current pos:", self.get_pos())

    def traverse_south_route23(self):
        # On Route 23 (y=139 down to canal y=104)
        # Waypoints:
        # Cascade guard approach: (8, 137) -> (8, 134)
        # Corridor 1: (14, 134) -> (14, 128)
        # Corridor 2 / Thunder guard: (14, 124) -> (8, 124) -> (8, 118)
        # Corridor 3 / Rainbow guard: (10, 118) -> (10, 110)
        # Canal approach: (10, 104)
        wps = [
            (8, 137),
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
        print("Route 23 progress pos:", self.get_pos(), "used:", self.used)

if __name__ == "__main__":
    nav = Route23Navigator(budget=75)
    nav.exit_gate_to_route23()
    nav.traverse_south_route23()
