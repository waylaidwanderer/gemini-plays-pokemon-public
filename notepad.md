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
  - Switch 3 (2, 1): Status Unknown (Likely OFF/Reset needed).
  - Switch 2 (10, 1): OFF. Wall (12, 8) is OPEN.
  - Switch 1 (16, 1): Toggling to OFF. (Expect Wall 16, 7 to CLOSE).
- Plan:
  1. Toggle Switch 1 OFF.
  2. Confirm Wall (16, 7) is CLOSED.
  3. Go to Switch 3 (2, 1).
  4. Execute Sequence: Switch 3 -> Switch 2 -> Switch 1 (if needed).
- Clue Interpretation:
  - "End is the one to press first" -> Start with Switch 3.
  - "Change the order" -> Order matters.
- Reflection (Turn 41747):
  - 50-turn review: Lots of running, need systematic testing.
  - Risk: Locking myself in North area. Acceptable, as all switches are there.
  - Goal: Open path to Director (9, 12). likely via (6, 8) or (12, 8).
- Reflection (Turn 41696):
  - Current Status: Heading to Middle Area (11, 3).
  - Hypothesis: Switch 2 is in Row 1, between x=6 and x=12.
  - Clue Interpretation: "End is the one to press first" -> Could mean Switch 3 (Left End) or Switch 1 (Right End).
  - Plan: Find Switch 2. Then try sequence: Reset All OFF -> Press 3 -> Press 2 -> Press 1.
- Turn 41725: Defeated Burglar Eddie at (3, 2). Resuming plan to toggle Switch 3 (2, 1).
- Note: Burglars might not move when spotting you? Or he was blocked. Either way, pathing around him.
- Turn 41725: Defeated Burglar Eddie (detected at 3, 2). Proceeding to toggle Switch 3 at (2, 1).