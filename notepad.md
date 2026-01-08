# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34501
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 11).
- Floor Reset: Using a ladder or falling into a pit resets all boulder positions on 2F.
- Push Mechanic: Player stays in the same tile after pushing a boulder.

# Verified Obstacles
- (4, 12), (5, 10), (5, 12), (6, 6), (7, 11), (8, 9), (9, 12), (9, 13) are WALLs.
- Fran (4, 11) is an impassable NPC.

# Connectivity Analysis
- Left Section (x=0-3) and Right Section (x=5-9) are separated by a column 4 wall from Row 0 to Row 12.
- Only known gap is at Row 13: (4, 13) is a FLOOR.
- Column 5 is blocked at Row 10 and Row 12.
- Column 6 is clear from Row 13 to Row 7.
- Column 7 connects to column 8/9 at Row 1, 3, 5, 7, 12, 13.

# Strategy: Blackthorn Gym 2F
- Current Task: Reach (5, 1) to test if Cody (4, 1) is passable.
- If Cody is passable, it provides a second gap between Left and Right sections.
- B6 (3, 3) needs to reach P2 (2, 5). B7 (6, 1) and B8 (8, 11) need to reach P1 and P3.

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).