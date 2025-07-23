# Gem's Pokémon Crystal Adventure Log

## I. Current Objectives & Strategy
1.  **Primary Goal:** Become the Pokémon League Champion, starting with the Violet City Gym.
2.  **Path:** Route 29 -> Cherrygrove City -> Route 30 -> Route 31 -> Violet City.
3.  **Exploration Strategy:** I have created an 'exploration_strategist' agent to analyze unseen tiles and suggest the most promising exploration targets. This is now fully functional.

## II. Guiding Principles
*   **Immediate Action:** As an LLM, I have no concept of 'later'. Any task I identify, especially tool maintenance or data management, must be performed in the current turn. Deferring actions is a critical failure.

## III. Key NPCs and Locations
*   **Professor Elm:** Gave me my starter, Vulcan. Tasked me with the Gym Challenge.
*   **Mr. Pokémon:** Lives somewhere north of Cherrygrove City. I have already met him.
*   **GRAMPS (Guide Gent):** Gave me a tour of Cherrygrove and the MAP CARD.
*   **Mom:** Saving money for me.

## IV. Game Mechanics & Systems
*   **Held Items:** Pokémon can hold items (like a BERRY) and use them automatically in battle to restore HP.
*   **Tool Status:** My `find_path_to_target` and `find_reachable_unseen_tiles` tools are reliable. My `exploration_strategist` agent is also complete and functional.

## V. Battle and Pokemon Information
*   **Party Composition:**
    *   Vulcan (Cyndaquil), Lv. 10. Moves: TACKLE, LEER, SMOKESCREEN.
    *   Warden (Hoothoot), Lv. 3. Moves: TACKLE, GROWL.
*   **Type Matchups Observed:**
    *   Normal (Tackle) is "not very effective" against Rock/Ground (Geodude).

## VI. Tile Traversal Rules (Systematic Testing)
*Method: To confirm a tile's properties, I must attempt to move onto it from all four adjacent, traversable tiles (Up, Down, Left, Right). A conclusion is only valid after all directions are tested.*

### Confirmed Traversable:
*   **FLOOR:** Fully traversable.
*   **TALL_GRASS:** Traversable. Can trigger wild Pokémon encounters.
*   **DOOR:** Functions as a warp.
*   **WARP_CARPET_DOWN:** Functions as a two-way warp.
*   **CAVE:** Functions as a warp.

### Confirmed Impassable:
*   **WALL:** Impassable.
*   **COUNTER:** Impassable. Interact with NPCs from the front.
*   **HEADBUTT_TREE:** Impassable.
*   **FRUIT_TREE:** Impassable. Can be interacted with for items.

### Partially Traversable / Special Mechanics:
*   **LEDGE_HOP_DOWN:** One-way traversal. Can only move Down off this tile. *Plan: The next time I am on a ledge, I must attempt to move left and right before jumping down to test for sideways movement.*

### Untested / Hypotheses:
*   **CUT_TREE:** Hypothesis: Impassable without HM Cut. *Plan: Attempt to walk into it from an adjacent tile.*
*   **LEDGE_HOP_LEFT:** Hypothesis: One-way traversal from right to left. *Plan: Attempt to walk onto it from the left.*
*   **WATER:** Hypothesis: Impassable without HM Surf. *Plan: Attempt to walk into it from an adjacent tile.*