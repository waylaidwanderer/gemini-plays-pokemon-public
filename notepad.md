# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC), TEACHER (NPC), YOUNGSTER (NPC), OFFICER (NPC)
- **Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Standard Warps:** DOOR, CAVE, LADDER (Acts as a two-way vertical warp)
- **Directional Warps:** WARP_CARPET_LEFT, WARP_CARPET_RIGHT, WARP_CARPET_DOWN (Must walk in the indicated direction to activate).
- **One-Way Ledges:** LEDGE_HOP_DOWN, LEDGE_HOP_LEFT, LEDGE_HOP_RIGHT (One-way traversal in the specified direction).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered by moving UP. Once on it, you can only exit by moving LEFT or RIGHT. You cannot move UP or DOWN off of it).

## II. Quest Progression & Puzzles

### Blocked Path: Ilex Forest West
- **Objective:** Clear the CUT tree at (8, 25) to access the western part of the forest.
- **Prerequisite:** Obtain HM01 (CUT).
- **Plan:** After dealing with the Slowpoke Well situation and getting CUT, I will return to this location.

### Ruins of Alph Puzzle
- **Clues:** 
  - Officer in gatehouse: 'There's a puzzle that involves sliding stone panels.'
  - Teacher in inner chamber: 'This place has a mystical quality to it. It feels sort of ethereal even.' (Flavor text)
- **Failed Attempts (4):** Interacted with all four northern statues in the inner chamber. All were just replicas.
- **Current Hypothesis:** The solution is not in the first chamber. The ladder at (10, 13) is the only other path forward.

## III. Tool Development & Bug Reports

### `stun_npc` Tool Investigation
- **Hypothesis:** The stun effect is temporary and wears off after a certain number of turns or actions.
- **Test Plan:**
  1. Find a stationary NPC that doesn't block a path.
  2. Use `stun_npc` on them and confirm the 'stopped' message.
  3. Take a specific number of steps (e.g., 10) away and back.
  4. Observe if the NPC has started moving again.
  5. Record the number of steps/turns it takes for the effect to wear off.

### `path_master_v5` (New)
- Created to correctly handle directional `LEDGE_HOP_*` tiles.

## IV. Item Effects
- **EVERSTONE:** A Pokémon holding this item will not evolve.
- **FRUIT_TREE:** Gives a 'BERRY' item when interacted with. Seems to be a one-time collection per tree.

## V. Procedural Reminders & Methodologies

### Personal Rules & Reminders
- **Check Map Markers!** Before interacting with an NPC or navigating to a specific spot, always check existing map markers.
- **Use Your Agents!** For complex puzzles like the Ruins of Alph, use the `quest_strategist` agent to generate new hypotheses instead of relying on simple trial and error.
- **Debug Tools Immediately!** If a tool is not behaving as expected, stop and investigate it immediately. Do not continue to use a faulty tool.

## VI. Mechanics to Investigate
- **LEDGE tile:** Test if this is impassable from all directions.
- **FLOOR_ALLOW_HOP_DOWN tile:** Test if this tile only allows downward movement.