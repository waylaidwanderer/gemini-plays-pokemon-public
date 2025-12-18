# Johto Journey: Gem's Log

## Global Tile Mechanics
- FLOOR: Traversable. Standard ground. Verified Turn 1891.
- WALL / FLOOR_UP_WALL: Impassable. Verified Turn 1905.
- TALL_GRASS: Traversable. Wild encounters.
- LEDGE_HOP_DOWN: One-way South. Verified Turn 1894.
- LEDGE_HOP_RIGHT: One-way East. Verified Turn 1894.
- COUNTER: Impassable. Stand in front to talk to NPCs behind. Verified Turn 1891.
- HEADBUTT_TREE: Impassable. Requires Headbutt.
- CUT_TREE: Impassable. Requires Cut.
- WARP_CARPET: Map transition at edges. Verified Turn 1891.
- LADDER / DOOR / CAVE: Instant warp upon entry. Verified Turn 1907.
- PC / BOOKSHELF / RADIO: Interactable from below (face Up + A).
- WATER / ROCK / INCENSE_BURNER: Impassable. Verified Turn 1906.

## Gym Progress
- **Zephyr Badge:** Obtained from Falkner (Turn 1864).
- **Hive Badge:** Target. Azalea Town.

## Exploration Log
- **Ruins of Alph Detour:** Started Turn 1888. Currently in RuinsOfAlphKabutoChamber.
- **Officer Hint:** Ruins of Alph is a "Look-and-Touch Tourist Site". Mentions "sliding stone panels". Verified Turn 1896.
- **Youngster Hint:** Confirms drawings on stone panels and that they can be moved. Verified Turn 1899.
- **Mystery Chamber:** Identified as "Kabuto Chamber". Verified Turn 1916.
- **Receptionist Hint:** Sliding panels depict a Pokémon. Scientists in the back are examining patterns. Verified Turn 1921.
- **Description Sign:** "A POKéMON that hid on the sea floor. Eyes on its back scanned the area." (Kabuto). Verified Turn 1923.

## Strategy & Lessons
- **Battle Menus:** Selecting NO for switching is faster if current Pokemon is fine.
- **Gym Strategy:** Rock-types (Geodude) with Rock Throw are extremely effective against Flying-types.
- **HMs:** Use FLASH in Dark Cave for level grinding/shortcuts. Requires a Pokemon that can learn it (e.g. Bellsprout - catch one on Route 32).
- **Input Hygiene:** Do not mix directional and action buttons in `press_buttons`. Use `press_sequence` or separate calls. Mixed inputs are truncated by the system. Verified Turn 1922.
- **Puzzle Strategy:** Form the picture of the Pokémon described by the sign (Kabuto).

## Reflection Turn 1935
- **Immediate Execution:** Placing Piece 9.
- **Notepad Hygiene:** Updated piece locations (8 is at 16) and progress.
- **Goal Clarity:** Solving Kabuto puzzle.
- **Root Hypothesis:** Numerical order 1-16 solves the puzzle.
## Puzzle: Kabuto Chamber
- Description: "A POKéMON that hid on the sea floor. Eyes on its back scanned the area."
- Target: Numerical order 1-16 in center 4x4.
- Progress (Turn 1939): Pieces 1-13 and 16 are in correct slots. Pieces 14 and 15 remain in border.
- Strategy:
  1. Move cursor from (4,4) to (5,0), pick up Piece 14.
  2. Move Piece 14 to (2,4) and place it.
  3. Move cursor to (4,0), pick up Piece 15.
  4. Move Piece 15 to (3,4) and place it.
- Observation: Pieces 14 at (5,0), 15 at (4,0). Target slots (2,4) and (3,4) are empty. Cursor is at (4,4).
- Hypothesis: Pieces 14 and 15 (identical black pieces) are swapped. Test: Swap 14 and 15 using (3,5) as temp slot. Verified Turn 1940.