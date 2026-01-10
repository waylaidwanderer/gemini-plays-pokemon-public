# persistent_knowledge
## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with HM Surf.
- TALL_GRASS: Traversable, triggers wild encounters.
- DOOR/WARP: Step on to enter buildings/areas.
- LEDGE_HOP_DOWN: One-way traversal (North to South).
- FLOOR_UP_WALL: Acts as a WALL from the North (cannot be jumped).
- COUNTER: Impassable Wall. Interact from adjacent tile.

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
- **Strategy:** Follow the Rocket Grunt who fled Cerulean Gym to recover the Machine Part. Suspected to be on Route 24.

## Cerulean City Exploration
- **Start Turn:** 39337
- **Detour Note:** Direct North path is blocked by Row 21 ledges. An open path North exists on the EAST side of the Gym through the gap at (33, 23) and (34, 23).
- **Plan:** Search Route 24 (North) for the Rocket Grunt. Confront and defeat him to reveal the Machine Part's location.
- **Strategy:** Move North to Route 24. After defeating the Grunt, return to Cerulean Gym and search the water for the Machine Part.
- **Current Task:** Finding the exit to Route 24 in Northern Cerulean City. (33, 13) is blocked by walls to the North; heading West to look for a passage.

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