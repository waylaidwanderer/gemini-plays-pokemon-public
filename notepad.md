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

## Reflection Turn 1922
- **Immediate Execution:** Marked unactivated warps (3, 3), (4, 3), (4, 0).
- **Notepad Hygiene:** Removed transient status info and redundant EXP tracking. Added input hygiene lesson.
- **Goal Clarity:** Reading description sign to prepare for puzzle.
- **Root Hypothesis:** Unmarked warps in Kabuto Chamber are likely puzzle rewards.
## Puzzle: Kabuto Chamber
- Description: "A POKéMON that hid on the sea floor. Eyes on its back scanned the area."
- Target: Numerical order 1-16 in center 4x4.
- Center Slots: [7, 8, 9, 10, 13, 14, 15, 16, 19, 20, 21, 22, 25, 26, 27, 28]
- Piece Locations (Turn 1930):
  1:7, 2:8, 3:9, 4:0, 5:3, 6:5, 7:6, 8:35, 9:23, 10:17, 11:1, 12:12, 13:18, 14:30, 15:4, 16:29
- Progress: Placing Piece 4.