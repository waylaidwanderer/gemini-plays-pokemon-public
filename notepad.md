# Tile Mechanics (Global Reference)
- FLOOR: Walkable.
- WALL: Impassable.
- WATER: Requires Surf.
- WATERFALL: Requires HM07 Waterfall. Facing Up/North at the base of the waterfall (e.g., (10, 30)) and pressing A triggers the climb. (Note: Menu usage may fail; interaction requires being directly adjacent and facing the waterfall tile).
- TALL_GRASS: Wild encounters.
- DOOR/WARP: Map transitions.
- FLOOR_UP_WALL: Blocks North/South movement. (Verified Turn #43532, #43576).
- LEDGE_HOP: One-way movement.

# Area Records: Silver Cave Room 2 (3_75)
- Warp to Room 1: (17, 31).
- Warp to Item Room: (13, 21).
- Warp to Next Area: (11, 5).
- Waterfall Logic: Facing Up/North at the base of the waterfall (e.g., (10, 30)) and pressing A triggers the climb. (Note: Menu usage may fail; interaction requires being directly adjacent and facing the waterfall tile). (Verified Turn #43564).
- Water: (13, 30)-(13, 31), (12, 14)-(21, 14), (4, 22)-(7, 27).
- FLOOR_UP_WALL: Row 16 (Hypothesis), Row 32.

# Team Goals & Battle Prep
- Grind team to Lv 75+ (currently Lv 12-64).
- Lead with KIMCHI (Gloom) or GNEISS (Graveler) for efficient XP.
- Replace ICARUS (Lv19) with LAPIS for Waterfall.
- Evolve KIMCHI (Gloom) using Sun Stone or Leaf Stone.
- Lead GNEISS (Graveler) with Hard Stone vs Pikachu (uses Earthquake). (Prepared Turn #43638).
- Teach GORP (Snorlax) Shadow Ball (TM02) vs Red's Espeon.
- Use XENON (Haunter) for Curse vs Red's Snorlax.

# Time Tracking
- Primary Goal (Defeat Red): Started Turn #43156.
- Exploration of Room 2: Started Turn #43268.

# Mt. Silver Grinding Strategy
- Wild Pokemon: Lv 40-50 (Goldeen, Machoke, etc.).
- Observed Wild Pokemon: Goldeen, Machoke (Lv48: Cross Chop, Vital Throw, Foresight), Larvitar (Lv20 - Caught: DAPXWW).
- KIMCHI (Grass STAB) vs Blastoise/Lapras.
- Calcifer vs Venusaur/Charizard.
- Target Level for Red: 75+.

# Area Records: Silver Cave Room 3 (3_76)
- Warp to Room 2: (9, 33).
- Layout: Large room, exploration required.
- Goal: Defeat Red (located at (9, 10)).

# Red Battle Log
- Pikachu (Lv81): Defeated by GNEISS (Earthquake) - Turn #43644.
- Espeon (Lv73): Encountered Turn #43644. Strategy: Switch to GORP (Snorlax) to tank Psychic moves.

# Reflection Turn #43645
- Immediate Execution: No deferred tasks.
- Notepad Hygiene: Battle log added. Reorganized in Turn #43622.
- Map Hygiene: Red marked. Redundant waterfall marker removed.
- Automation Strategy: Using battle_strategist. find_path_v7_robust refined for axial blocking.
- Goal Clarity: Goal is "Defeat Red". Method is switching to tank.
- Error Analysis: Turn count mismatch in #43644 noted. Verification of one-way walls (axial blocking) confirms they block movement on their entire axis.