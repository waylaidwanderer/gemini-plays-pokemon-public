# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Mechanics Testing Protocol
*Goal: Build a comprehensive guide to the game's physics. This must be followed for every new tile type.*
1.  **New Tile Encountered:** When a new, undocumented tile type appears on the map, I must immediately begin testing.
2.  **Impassable Test:** Attempt to move onto the tile from all four cardinal directions (Up, Down, Left, Right).
3.  **One-Way Test:** If traversal is possible from one direction, I must immediately test all other directions to confirm if it is a one-way path. Every direction must be individually verified.
4.  **Record Results:** Document all findings in the 'Verified' section below. No assumption is valid until tested.

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, CUT_TREE, WATER, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC), TEACHER (NPC), YOUNGSTER (NPC), OFFICER (NPC), STATUE, TABLE, CHAIR, BED, TWIN (NPC), GYM_GUIDE (NPC), BUG_CATCHER (NPC), VOID
- **Interactable Obstacles:** HEADBUTT_TREE (Impassable to walk on, but can be interacted with using 'A').
- **Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Standard Warps:** DOOR, CAVE
- **Movement-Based Warps:** LADDER (Activated by moving onto the tile).
- **Directional Warps:** WARP_CARPET_RIGHT, WARP_CARPET_LEFT, WARP_CARPET_DOWN (Activated by moving onto the tile in the specified direction).
- **One-Way Ledges:** LEDGE_HOP_DOWN, LEDGE_HOP_LEFT, LEDGE_HOP_RIGHT (One-way traversal in the specified direction).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered by moving UP. Once on it, you can only exit by moving LEFT or RIGHT. You cannot move UP or DOWN off of it).

### Untested Tile Mechanics
*Goal: Test these tiles as soon as they are encountered.*
- **LEDGE:** Test if this is impassable from all directions.
- **FLOOR_ALLOW_HOP_DOWN:** Test if this tile only allows downward movement.

## II. Quest Progression & Puzzles

### Ilex Forest - Farfetch'd Puzzle
- **Objective:** Guide the lost FARFETCH'D to the apprentice at (7, 28) to get HM01 CUT.
- **Verified Mechanics:**
    1. **Proximity (Turning):** Approaching the Farfetch'd from a specific side causes it to turn and face you.
    2. **Teleportation (Twigs):** Stepping on a twig causes the Farfetch'd to *teleport* to a new, seemingly fixed location. It does not simply move one space.
- **Current Hypothesis:** The puzzle involves triggering a specific sequence of twigs to teleport the Farfetch'd along a hidden path towards the apprentice. The direction it faces might be irrelevant.
- **Current Plan:** Systematically test the teleportation mechanic by manipulating the Farfetch'd's facing direction and triggering specific twigs to understand the teleportation pattern.

### Ruins of Alph Puzzle
- **Objective:** Solve the sliding stone panel puzzle.
- **Current Status:** The ladder at (10, 13) is the only path forward. The solution is likely in another chamber.
- **Clue:** Liz mentioned hearing a strange broadcast from the Ruins of Alph. This might be a clue for the puzzle.

## III. Item Effects
- **EVERSTONE:** A Pokémon holding this item will not evolve.
- **BERRY:** Restores 10 HP. Obtained from FRUIT_TREEs.
- **TM49 (Fury Cutter):** A move that gets stronger with each consecutive hit.
- **SLOWPOKETAIL:** A man on Route 32 offered to sell this. Its purpose is unknown.
- **MOOMOO MILK:** Restores 100 HP. Can be purchased at MOOMOO FARM.

### Farfetch'd Puzzle Hypotheses (from Quest Strategist)
1.  **Hypothesis 1 (Top Priority):** At the start location (22, 29), approach the Farfetch'd from the east to make it face west (towards the final goal). Step on the twig at (22, 30) and then search exclusively along the path to the west for its new location.
2.  **Hypothesis 2:** Test if the Farfetch'd moves opposite to its facing direction. From the start (22, 29), approach it from the west to make it face east. Step on the twig at (22, 30), then search to the west for its new location.
3.  **Hypothesis 3:** Test if the Farfetch'd flees from the source of the sound. From its start position (22, 29), ignore the nearby twigs and walk over to the isolated twig at (29, 30). Stepping on this should make a sound from the east, potentially causing the Farfetch'd to flee west.

## IV. Reflections & Self-Correction (Turn 19292)
- **Data Management:** I have repeatedly failed to update my World Knowledge Graph and Map Markers immediately after discovering new information or transitions. This has caused a cascade of hallucinations and wasted turns. **Correction:** I must treat data management as the highest priority action, to be performed in the same turn a discovery is made, overriding any other planned action.
- **Tool Reliability:** My `path_master_v10` and `path_master_v11` tools have proven unreliable in complex, maze-like environments like Ilex Forest. They failed to find valid paths that exist. **Correction:** I have redefined my pathfinding tool as `path_master_v12` with a more robust A* algorithm to ensure it can handle complex navigation. I must trust my tools, which means I must ensure they are flawless.
- **Goal Flexibility:** I became fixated on the idea that the officer in the gatehouse was the only way forward, and on solving the Farfetch'd puzzle immediately. This wasted significant time. **Correction:** I need to be more willing to abandon a failing strategy and explore alternatives, as documented in my notepad. I will pivot to a new primary goal when progress stalls.

## V. Battle Mechanics & Type Effectiveness
- **Water vs. Bug/Grass:** Verified that Water-type moves are neutral against Bug/Grass types (e.g., Paras). My initial assumption that it was 'not very effective' was based on external knowledge and was incorrect.

## VI. Self-Correction (Turn 19321)
- **External Knowledge:** My assumption about Water-type effectiveness was based on knowledge from other games. I must build my understanding of mechanics *only* from verified, in-game observations in Pokémon Crystal.

## VII. Self-Correction (Turn 19337)
- **External Knowledge (Again):** After observing Water Gun being 'not very effective' against Paras, I hypothesized about 'Dry Skin', an ability from later games. This is another instance of relying on external knowledge. I must strictly adhere to forming hypotheses based only on mechanics I can observe and verify within Pokémon Crystal.

## VIII. Self-Correction (Turn 19411)
- **External Knowledge (Recurrence):** I continue to make assumptions based on other Pokémon games (e.g., hypothesizing about 'Dry Skin'). This is a critical failure. I must build my type effectiveness chart and all mechanical knowledge **exclusively** from verified, in-game observations within Pokémon Crystal. All external knowledge must be treated as invalid until proven otherwise through direct testing.

## IX. Self-Correction (Turn 19439)
- **Notepad Management:** The `overwrite` action failed due to excessive character deletion. I must follow the system's guidance and use more precise `replace` or `append` actions for future edits instead of attempting large-scale rewrites. 
- **Farfetch'd Puzzle - New Hypotheses:**
    1. The direction the Farfetch'd faces is irrelevant; the puzzle is purely about the *sequence* of twigs stepped on.
    2. An external event or item interaction elsewhere in the forest is needed to change the puzzle's state or the Farfetch'd's behavior.
## IV. Lessons Learned & Self-Correction Archive
- **External Knowledge:** I must stop making assumptions based on other Pokémon games (e.g., hypothesizing about 'Dry Skin', type effectiveness). All mechanical knowledge must be built **exclusively** from verified, in-game observations within Pokémon Crystal.
- **Data Management:** I must treat data management (WKG, Map Markers, Notepad) as the highest priority action, to be performed in the same turn a discovery is made, overriding any other planned action. Deferring these tasks leads to hallucinations and wasted turns.
- **Tool Reliability:** I must ensure my custom tools are flawless. When a tool fails (like `path_master_v12`), I must immediately redefine it with a more robust script (`path_master_v13`).
- **Goal Flexibility:** I must be willing to abandon a failing strategy and explore alternatives when progress stalls, rather than becoming fixated on a single approach.

## V. Farfetch'd Puzzle - Current Hypothesis
- **Current Hypothesis (High Priority):** The apprentice's dialogue about his boss being angry is the key clue. I must return to Kurt's house in Azalea Town and speak to him to resolve the quest.
- **Failed Hypotheses Log:**
  1. Making the Farfetch'd disappear and then talking to the apprentice.
  2. Leaving the forest and returning to reset the puzzle state.
  3. Repeatedly talking to Kurt in his house after chasing the Farfetch'd away.