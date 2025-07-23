# Gem's Pokémon Crystal Adventure Log

## I. Current Objectives & Strategy
1.  **Primary Goal:** Become the Pokémon League Champion, starting with the Violet City Gym.
2.  **Path:** Route 29 -> Cherrygrove City -> Route 30 -> Route 31 -> Violet City.
3.  **Exploration Strategy:** I will use my `find_reachable_unseen_tiles` tool and `exploration_strategist` agent to guide my exploration of new areas.

## II. Guiding Principles
*   **Immediate Action:** As an LLM, I have no concept of 'later'. Any task I identify, especially tool maintenance or data management, must be performed in the current turn. Deferring actions is a critical failure.
*   **Verify, Don't Assume:** My memory is fallible. I must ALWAYS verify my assumptions against the game state information and map memory before acting.

## III. Critical Lessons & Errors
*   **CRITICAL HALLUCINATION (Turn 1621):** I hallucinated finding a Poké Ball at (19, 15) on Route 31. The item was actually at (29, 5). I failed to verify the item's existence. **LESSON:** ALWAYS verify game state information against the map memory source of truth. NEVER assume an action was successful without confirmation.
*   **DEFERRED DATA MANAGEMENT (Turn 1621-1628):** I failed to immediately update map markers after believing I had collected an item, waiting until after a long battle. **LESSON:** Data management (markers, notepad) must be performed in the same turn a discovery is made. It is the highest priority.

## IV. Key NPCs and Locations
*   **Professor Elm:** Gave me my starter, Vulcan. Tasked me with the Gym Challenge.
*   **Mr. Pokémon:** Lives somewhere north of Cherrygrove City. I have already met him.
*   **GRAMPS (Guide Gent):** Gave me a tour of Cherrygrove and the MAP CARD.
*   **Mom:** Saving money for me.
*   **WADE (Bug Catcher):** Met on Route 31. Not a trainer. Gave me his phone number.

## V. Battle and Pokemon Information
*   **Party Composition:**
    *   Miasma (Gastly), Lv. 5. Moves: HYPNOSIS, LICK.
    *   Warden (Hoothoot), Lv. 3. Moves: TACKLE, GROWL. (Asleep)
    *   Vulcan (Cyndaquil), Lv. 11. Moves: TACKLE, LEER, SMOKESCREEN.
*   **Type Matchups Observed:**
    *   Normal (Tackle) is "not very effective" against Rock/Ground (Geodude).
    *   Normal (Tackle) has no effect on Ghost (Gastly).
    *   Ghost (Lick) has no effect on Normal (Hoothoot).

## VI. Tile Traversal Rules (Systematic Testing)
*Method: To confirm a tile's properties, I must attempt to move onto it from all four adjacent, traversable tiles (Up, Down, Left, Right). A conclusion is only valid after all directions are tested.*

### Confirmed Traversable:
*   **FLOOR:** Fully traversable.
*   **TALL_GRASS:** Traversable. Can trigger wild Pokémon encounters.
*   **DOOR:** Functions as a warp.
*   **WARP_CARPET_DOWN:** Functions as a two-way warp.

### Confirmed Impassable:
*   **WALL:** Impassable.
*   **COUNTER:** Impassable. Interact with NPCs from the front.
*   **HEADBUTT_TREE:** Impassable.
*   **FRUIT_TREE:** Impassable. Can be interacted with for items.

### Partially Traversable / Special Mechanics:
*   **LEDGE_HOP_DOWN:** One-way traversal. Can only move Down off this tile. *Plan: The next time I am on a ledge, I must attempt to move left and right before jumping down to test for sideways movement.*

### Untested / Hypotheses:
*   **CUT_TREE:** Hypothesis: Impassable without HM Cut. *Plan: Attempt to walk into it from an adjacent tile.*
*   **LEDGE_HOP_LEFT/RIGHT:** Hypothesis: One-way traversal. *Plan: Attempt to walk onto it from the opposing direction.*
*   **WATER:** Hypothesis: Impassable without HM Surf. *Plan: Attempt to walk into it from an adjacent tile.*
*   **CAVE:** Functions as a warp. *Plan: Verify if it's two-way.*
*   **SPROUT TOWER:** Mentioned by the Officer in the Route 31 Gatehouse. Sounds important.