# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Mechanics Testing Protocol
*Goal: Build a comprehensive guide to the game's physics. This must be followed for every new tile type.*
1.  **New Tile Encountered:** When a new, undocumented tile type appears on the map, I must immediately begin testing.
2.  **Impassable Test:** Attempt to move onto the tile from all four cardinal directions (Up, Down, Left, Right).
3.  **One-Way Test:** If traversal is possible from one direction, I must immediately test all other directions to confirm if it is a one-way path. Every direction must be individually verified.
4.  **Record Results:** Document all findings in the 'Verified' section below. No assumption is valid until tested.

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, CUT_TREE, WATER, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC), TEACHER (NPC), YOUNGSTER (NPC), OFFICER (NPC), STATUE, TABLE, CHAIR, TWIN (NPC), GYM_GUIDE (NPC), BUG_CATCHER (NPC), YOUNGSTER (NPC), VOID
- **Interactable Obstacles:** HEADBUTT_TREE (Impassable to walk on, but can be interacted with using 'A').
- **Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Standard Warps:** DOOR, CAVE
- **Movement-Based Warps:** LADDER (Activated by moving onto the tile).
- **Directional Warps (Activation Method Unknown/Blocked):** WARP_CARPET_RIGHT, WARP_CARPET_LEFT, WARP_CARPET_DOWN. Repeated attempts to activate by moving onto the tile or pressing 'A' have failed at the Ilex Forest exit (3, 42). Activation may be conditional.
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
- **Current Hypothesis:** The puzzle involves triggering a specific sequence of twigs to teleport the Farfetch'd along a hidden path towards the apprentice. The direction it faces is critical.

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

## IV. Battle Mechanics & Type Effectiveness
- **Water vs. Bug/Grass:** Verified that Water-type moves are neutral against Bug/Grass types (e.g., Paras). My initial assumption that it was 'not very effective' was based on external knowledge and was incorrect.

## V. Lessons Learned & Self-Correction Archive
- **External Knowledge:** I must stop making assumptions based on other Pokémon games. All mechanical knowledge must be built **exclusively** from verified, in-game observations within Pokémon Crystal.
- **Data Management as Priority:** Data management (WKG, Map Markers, Notepad) is the highest priority action, to be performed in the same turn a discovery is made, overriding any other planned action. Deferring these tasks leads to hallucinations and wasted turns.
- **Tool Reliability:** I must ensure my custom tools are flawless. When a tool fails, I must immediately redefine it with a more robust script.
- **Goal Flexibility:** I must be willing to abandon a failing strategy and explore alternatives when progress stalls, rather than becoming fixated on a single approach. The Farfetch'd puzzle is a key example; my long-distance pathing was a flawed strategy due to random encounters resetting the puzzle state.
- **Tile Documentation:** The 'unknown' tile type represents a placeholder for tiles that have not been fully implemented in the game's code, but are still present on the map. They are **traversable** and function as floor tiles.

### Farfetch'd Puzzle Test Log
- **Test 1:** Stepped on twig at (15, 27) while Farfetch'd was at (15, 25) facing down.
  - **Result:** No effect. Farfetch'd did not move or change orientation.
  - **Conclusion:** Hypothesis that this twig affects the bird in this specific configuration is denied.

- **Test 2:** Farfetch'd at (15, 25) facing down. Stepped on twig at (15, 27).
  - **Result:** Farfetch'd teleported to (20, 24).
  - **Conclusion:** Confirmed that the combination of the bird's facing direction and the specific twig triggered determines its teleportation destination.

- **Test 3:** Walked path from (15, 23) to (20, 23).
  - **Result:** Farfetch'd appeared at (20, 24), facing right.
  - **Conclusion:** A specific movement path can trigger the Farfetch'd to appear at a new location. The puzzle is not just about twigs.

- **Test 4:** Interacted directly with Farfetch'd at (20, 24).
  - **Result:** Farfetch'd said 'Kwaa!' and then disappeared.
  - **Conclusion:** Direct interaction resets the Farfetch'd's position, similar to entering a wild battle.

### Farfetch'd Puzzle Test Log - Critique Notes
- **Marking:** I must mark *every* location the Farfetch'd teleports to and *every* twig I interact with. This is crucial for tracking the puzzle's state.

### Farfetch'd Puzzle - Falsification Test
- **Alternative Hypothesis:** The puzzle may not be a linear path. It could require a specific, non-obvious sequence of interactions (twigs, movement, approach direction) that don't necessarily move the Farfetch'd progressively westward. 
- **Test:** After exhausting more direct hypotheses, I will try seemingly illogical actions, such as deliberately herding the Farfetch'd east or interacting with distant twigs, to see if it triggers an unexpected state change.

### Critical Self-Correction: Hallucination Log
- **Issue:** I have experienced repeated, severe locational hallucinations, believing I was on a different map or at different coordinates. This has led to failed actions and wasted turns (e.g., turns 19825-19830).
- **Root Cause:** Failure to prioritize immediate data management (Notepad, WKG) over in-game actions. Deferring documentation after a map change or significant event leads to a corrupted internal state.
- **Corrective Action:** All documentation and data management tasks are the absolute highest priority. They MUST be performed in the same turn a discovery is made, overriding any other planned action. I must verify my location against the game state before every action if I am unsure.

### Ilex Forest - Maze Navigation Strategy
- **Observation:** Pathfinding tools (`path_master_v13`, `exploration_master`) have confirmed that there is no direct, traversable path to the main puzzle area from the entrance. The forest is a maze.
- **Strategy:** The correct approach is methodical, manual exploration. I must trace each path to its end, documenting dead ends and junctions with map markers. I am currently exploring the westernmost corridor by backtracking south to find an eastward path.

### Farfetch'd Puzzle - Falsification Test
- **Alternative Hypothesis:** The puzzle may not be a linear path. It could require a specific, non-obvious sequence of interactions (twigs, movement, approach direction) that don't necessarily move the Farfetch'd progressively westward. 
- **Test:** After exhausting more direct hypotheses, I will try seemingly illogical actions, such as deliberately herding the Farfetch'd east or interacting with distant twigs, to see if it triggers an unexpected state change.