## Battle Strategy (Blackthorn Gym)
- Leader Clair: Dragonair Lv37 x3, Kingdra Lv40.
- Typhlosion (Lv45) with Thunderpunch is key for Kingdra.
- Graveler (Lv44) with Earthquake for Dragonairs.
- Fodder: Gloom, Pidgey, Krabby, Gastly (Lv10-21) to heal/switch.
- Prep: Catch Swinub/Jynx in Ice Path for Ice-type moves.

# Tile Mechanics
- FLOOR: Walkable. Verified.
- WALL: Impassable. Verified.
- WATER: Needs Surf (HM03). Verified.
- ICE: Sliding mechanic. Verified. You slide until you hit a wall, an object, or a non-ice tile.
- PIT: Warp to B2F. Verified.
- BOULDER: Pushable with Strength (HM04). Verified.

# B1F Boulder Puzzle
- Start Turn: 28207.
- Reset Turn: 28385 (Fell through pit, floor reset).
- Pit 1 (11, 2): Pending Boulder 1 (ID 1).
- Pit 2 (4, 7): Pending Boulder 2 (ID 2).
- Pit 3 (5, 12): COMPLETED.
- Pit 4 (12, 13): COMPLETED.

## Boulder 1 Sequence (ID 1)
- Boulder currently at (10, 1).
1. Move to (9, 1).
2. Push Right to (11, 1).
3. Move to (11, 0).
4. Push Down to (11, 2). [PIT]

# Current Status (B1F)
- Start Turn: 28207.
- Reset Turn: 28385 (Fell through pit, floor reset).
- Boulder 1 (ID 1) is at (10, 1).
- Boulder 2 (ID 2) is at (5, 8).

# Lessons Learned
- Falling through a PIT on B1F resets the entire floor's boulder puzzle.
- Be extremely cautious when moving near (11, 2), (4, 7), (5, 12), and (12, 13) on B1F.
- If a wild battle occurs during a puzzle, prioritize escaping with a fast Pokemon (Calcifer) to avoid distraction and resource drain.
- Time Tracking: Boulder puzzle started Turn 28207.
- Leads: ALWAYS lead with Calcifer (Lv45) in wild areas. Reorder party in overworld menu immediately after this battle.
- Tool Hygiene: Double-check boulder coordinates before calling plan_boulder_push_v2.