# Gem's Pokémon Crystal Adventure Log

## I. Critical Lessons & Errors
*   **CRITICAL HALLUCINATION (Turn 1621):** I hallucinated finding a Poké Ball at (19, 15) on Route 31. The item was actually at (29, 5). I failed to verify the item's existence. **LESSON:** ALWAYS verify game state information against the map memory source of truth. NEVER assume an action was successful without confirmation.
*   **DEFERRED DATA MANAGEMENT (Turn 1621-1683):** I have repeatedly failed to immediately update map markers or my notepad after discoveries. **LESSON:** Data management (markers, notepad) must be performed in the same turn a discovery is made. It is the highest priority.
*   **AGENT DESIGN FLAW (Turn 1735):** My `exploration_strategist` agent recommended an unreachable tile because it cannot analyze map topology. It has since been deleted. **LESSON:** Agents are for reasoning, not spatial/computational analysis. Such tasks require a custom tool that can parse map data.
*   **FAILED INTERACTION HYPOTHESIS (Turns 1676-1833):** My attempts to interact with the Super Nerd (ID 3) on Violet City have failed multiple times as he moves away. I conclude that chasing him is not the correct way to trigger an event. I will stop pursuing him and focus on exploration. **Alternative Hypothesis:** An event elsewhere (like clearing Sprout Tower) might change his behavior. I can re-test after the next major objective.

## II. Key NPCs and Locations
*   **Professor Elm:** Gave me Vulcan. Tasked me with the Gym Challenge.
*   **Mr. Pokémon:** Met him north of Cherrygrove. Task complete.
*   **Mom:** Saving my money.
*   **WADE (Bug Catcher):** Met on Route 31. Gives phone calls.
*   **FALKNER:** Violet City Gym Leader.
*   **SPROUT TOWER:** Currently exploring. A giant Bellsprout is the central pillar.
*   **EARL'S POKéMON ACADEMY:** Located in northern Violet City.

## III. Battle and Pokemon Information
*   **Party Composition:**
    *   Miasma (Gastly), Lv. 5. Moves: HYPNOSIS, LICK.
    *   Warden (Hoothoot), Lv. 3. Moves: TACKLE, GROWL.
    *   Vulcan (Cyndaquil), Lv. 11. Moves: TACKLE, LEER, SMOKESCREEN.
*   **Type Matchups Observed:**
    *   Normal is "not very effective" against Rock/Ground.
    *   Normal has no effect on Ghost.
    *   Ghost (Lick) has no effect on Normal.

## IV. Tile Traversal Rules (Systematic Testing)
*Method: To confirm a tile's properties, I must attempt to move onto it from all four adjacent, traversable tiles (Up, Down, Left, Right). A conclusion is only valid after all directions are tested.*

### Confirmed Traversable:
*   **FLOOR:** Fully traversable.
*   **TALL_GRASS:** Traversable. Can trigger wild Pokémon encounters.
*   **DOOR:** Functions as a two-way warp.
*   **LADDER:** Functions as a two-way warp. Requires pressing 'A' while standing on the tile to use.
*   **WARP_CARPET_DOWN:** Functions as a two-way warp.
*   **WARP_CARPET_RIGHT:** Functions as a two-way warp.

### Confirmed Impassable:
*   **WALL:** Impassable.
*   **COUNTER:** Impassable. Interact with NPCs from the front.
*   **FRUIT_TREE:** Impassable. Can be interacted with for items.
*   **PC:** Impassable. Functions as an object.
*   **VOID:** Impassable. Appears as a black abyss.

### Untested / Hypotheses:
*   **CUT_TREE:** Hypothesis: Impassable without HM Cut. *Plan: Attempt to walk into it from an adjacent tile.*
*   **HEADBUTT_TREE:** Hypothesis: Impassable. *Plan: Attempt to walk into it from an adjacent tile.*
*   **LEDGE_HOP_DOWN/LEFT/RIGHT:** Hypothesis: One-way traversal. *Plan: Attempt to walk onto it from the opposing direction.*
*   **WATER:** Hypothesis: Impassable without HM Surf. *Plan: Attempt to walk into it from an adjacent tile.*
*   **CAVE:** Functions as a warp. *Plan: Verify if it's two-way.*

## V. Future Development Ideas
*   **Tool Idea: `exploration_ranker`:** A tool to replace the flawed `exploration_strategist` agent. It would take the output of `find_reachable_unseen_tiles` and rank the tiles based on heuristics like cluster size, proximity, and potential to open new paths. This is a computational task, perfect for a tool.
*   **Task: `marker_fix`:** The marker for the Sage at (12, 3) on SproutTower2F is not linked to its object ID. Must re-define the marker with the correct `object_id` as soon as the Sage is on-screen again.