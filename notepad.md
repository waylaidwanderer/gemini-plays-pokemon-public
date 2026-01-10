# persistent_knowledge
## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with HM Surf.
- TALL_GRASS: Traversable, triggers wild encounters.
- DOOR/WARP: Step on to enter buildings/areas.
- LEDGE_HOP_DOWN: One-way traversal (North to South).
- FLOOR_UP_WALL: Acts as a WALL from the North (cannot be jumped). Verified at (20, 16), (11, 16), (12, 16).
- COUNTER: Impassable Wall. Interact from adjacent tile.
- CAVE_LEDGE: Rock Tunnel B1F Row 26 FLOOR_UP_WALL tiles act as walls from the North.

## Battle Mechanics (Hypotheses)
- Hypothesis: Haunter (XENON) lacks Levitate in this game (Gen 2) and is vulnerable to Ground moves. (Verification needed).

## Kanto Strategy
- **Primary Goal: Complete Kanto Region Journey.**
- **Current Objective: Resolve Power Plant crisis.**
  - Strategy: Retrieve the stolen Machine Part to restore power.
  - Plan: Find Mr. Fuji (Lavender) -> Route 10 -> Power Plant -> Cerulean City (Find thief) -> Cerulean Gym (Retrieve Machine Part).

## PC Storage (Box 1)
1. GLAIVE (Lv14), 2. SELKIE (Lv24), 3. DELTA (MANTINE) Lv20, 4. RANGOON (KRABBY) Lv22, 5. NOMURA (TENTACOOL) Lv17, 6. Ravioli (Lv10), 7. Ouroboros (DRATINI) Lv15

## Movesets (HM Users)
- KIMCHI (GLOOM): Lv40 | CUT, FLASH
- GNEISS (GRAVELER): Lv53 | STRENGTH
- LAPIS (POLIWAG): Lv12 | SURF, WHIRLPOOL, WATERFALL
- ICARUS (PIDGEOTTO): Lv19 | FLY

## Power Plant Investigation
- **Start Turn:** 39084
- **Status:** Met Rocket Grunt in Cerulean Gym. He fled the building.
- **Next Step:** Chase the Rocket Grunt to Route 24 (North).

## Cerulean City Exploration
- **Start Turn:** 39337
- **Goal:** Find the thief and the Machine Part.
- **Status:** Chasing the Rocket Grunt North.
- **Key Locations:**
  - Entrance from Route 9: (39, 22)
  - Cerulean Gym: (30, 23)
  - Pokemon Center: (19, 21)
  - Poke Mart: (25, 29)
  - Fisher (Misty fan): (29, 26)
  - Cooltrainer F: (21, 24)
  - Slowpoke: (20, 24)
- **Plan:** Search Route 24 (North) for the Rocket Grunt. Confront him to recover the Machine Part.
- **Progress:** Encountered Rocket Grunt in Gym; he fled. Now heading North to Route 24. Path blocked by ledges at Row 21; must go around via X=18 or similar.
- **Note:** Route 24 is North of the city. Need to find the exit.

## Route 9 Exploration (Completed)
- Start Turn: 39167
- End Turn: 39336
- Summary: Navigated ledges and cut a tree at (5, 8) to reach Cerulean City. All trainers defeated.
- Key Gaps: (15, 5) and (16, 9) allow Northward travel.
- Ledges: (9, 7) allows Southward travel.
- Cut Tree: (5, 8).

## Lessons Learned
- NPCs act as walls and must be navigated around.
- "find_path_v3_fixed" is more reliable than manual directional inputs for navigating around obstacles.
- Sand-Attack lowers accuracy; fixed-damage moves like Night Shade are good for consistency.
- FLOOR_UP_WALL is not jumpable from the North.
- Always check for gaps in ledges for passage.
- (15, 5) and (16, 9) are gaps allowing Northward travel.
- (9, 7) is a ledge allowing Southward travel to the lower section.
- (5, 8) is a cuttable tree that must be cleared to reach Cerulean City.