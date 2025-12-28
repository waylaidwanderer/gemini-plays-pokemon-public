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

## Boulder 2 Sequence (ID 2)
- Boulder currently at (5, 8).
1. Move to (5, 9).
2. Push Up to (5, 6).
3. Move to (6, 6).
4. Push Left to (4, 6).
5. Move to (4, 5).
6. Push Down to (4, 7). [PIT]

# Party Management
- Lead: Calcifer (Lv45) - Fast for escapes, strong for combat.
- Slot 2: KIMCHI (Lv21) - HM Cut.
- Slot 3: ICARUS (Lv16) - HM Fly.
- Slot 4: Ravioli (Lv10) - HM Surf.
- Slot 5: GNEISS (Lv44) - HM Strength.
- Slot 6: XENON (Lv21) - Hypnosis.

## Swap Progress (KIMCHI <-> Calcifer)
- Goal: Put Calcifer in Slot 1.
1. Move to KIMCHI in Slot 1. [DONE - T28468]
2. Press Select on KIMCHI (verify highlight/blinking). [NEXT]
3. Move to Calcifer in Slot 3.
4. Press Select on Calcifer to swap.
5. Exit menu.

# Failed Attempts (Swap)
- Turn 28466: Pressed Select on Calcifer, but swap did not occur. Suspect KIMCHI was not correctly marked. restarting.

# Lessons Learned
- Falling through a PIT on B1F resets the entire floor's boulder puzzle.
- Be extremely cautious when moving near (11, 2), (4, 7), (5, 12), and (12, 13) on B1F.
- Wild battles: Prioritize escaping with Calcifer.
- Leads: ALWAYS lead with Calcifer (Lv45) in wild areas.
- Tool Hygiene: Verify coordinates against Map Markers before tool use.
- Menu Mechanics: Swap = Select (item 1) -> Move -> Select (item 2).