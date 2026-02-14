# Warehouse Strategy
- Objective: Find the Director in Underground Warehouse (3_54).
- Locations:
  - Stairs: (23, 3) Silver Room <-> (22, 27) Warehouse.
  - Switch 1 (Silver Room, 16, 1): Toggles Wall at (16, 7).
  - Switch 3 (Silver Room, 2, 1): Toggles Wall at (6, 8).
  - Director: (9, 12) in Silver Room (Behind Wall).
  - Item: (15, 12) in Silver Room (Behind Wall).
- Clues:
  - Grunt (Row 4): "Open one shutter, another closes."
  - Grunt (3, 2): "Change the order of switching."
  - Grunt (11, 3): "End is the one to press first, but..."
  - Grunt (11, 3): "I'm confused too... The switch on the..." (Reading now).
- Puzzle Logic:
  - Need to find "Switch 2" or the correct sequence.
  - Current State: Switch 1 ON, Switch 3 ON.
  - Walls at Row 10 are blocking access to Director/Item.
- Puzzle Status:
  - Switch 3 (2, 1): Turning ON. (Expected: Open Wall 6,8).
  - Switch 2 (10, 1): OFF. Wall (12, 8) is OPEN. (Verified).
  - Switch 1 (16, 1): ON. Wall (16, 7) is OPEN.
- Logic:
  - Switch 3 controls Wall (6, 8). ON = OPEN.
  - Switch 2 controls Wall (12, 8). OFF = OPEN.
  - Switch 1 controls Wall (16, 7). ON = OPEN.
- Plan:
  1. Turn Switch 3 ON.
  2. Verify Wall (6, 8) is OPEN.
  3. Enter through (6, 8) or (12, 8) and find path to Director (9, 12).
- Reflection (Turn 41696):
  - Current Status: Heading to Middle Area (11, 3).
  - Hypothesis: Switch 2 is in Row 1, between x=6 and x=12.
  - Clue Interpretation: "End is the one to press first" -> Could mean Switch 3 (Left End) or Switch 1 (Right End).
  - Plan: Find Switch 2. Then try sequence: Reset All OFF -> Press 3 -> Press 2 -> Press 1.
- Turn 41725: Defeated Burglar Eddie at (3, 2). Resuming plan to toggle Switch 3 (2, 1).
- Note: Burglars might not move when spotting you? Or he was blocked. Either way, pathing around him.
- Turn 41725: Defeated Burglar Eddie (detected at 3, 2). Proceeding to toggle Switch 3 at (2, 1).