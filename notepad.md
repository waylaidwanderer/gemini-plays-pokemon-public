# Gem's Pokémon Crystal Adventure Log

## Current Plan & Strategy
1.  **Objective:** Professor Elm has tasked me with taking on the Pokémon Gym Challenge to become the Champion. The first Gym is in Violet City.
2.  **Immediate Next Step:** Travel to Violet City.
3.  **Path:** Route 29 -> Cherrygrove City -> Route 30 -> Route 31 -> Violet City.
4.  **Future Improvement:** Consider creating an 'exploration_strategist' agent to suggest optimal exploration targets.

## Guiding Principle: Immediate Action
As an LLM, I have no concept of 'later'. Any task I identify, especially tool maintenance or data management, must be performed in the current turn. Deferring actions is a critical failure.

## Key NPCs and Locations
*   **Professor Elm:** Gave me my starter, Vulcan. Tasked me with the Gym Challenge.
*   **Mr. Pokémon:** Lives somewhere north of Cherrygrove City. I have already met him.
*   **GRAMPS (Guide Gent):** Gave me a tour of Cherrygrove and the MAP CARD.
*   **Mom:** Saving money for me.

## Game Mechanics & Systems
*   **Held Items:** Pokémon can hold items (like a BERRY) and use them automatically in battle to restore HP.
*   **Tool Status:** My `find_path_to_target` tool is a new, reliable pathfinder built with a standard BFS algorithm. The `find_reachable_unseen_tiles` tool is also reliable after a recent bug fix.

## Battle and Pokemon Information
*   **Party Composition:**
    *   Vulcan (Cyndaquil), Lv. 10. Moves: TACKLE, LEER, SMOKESCREEN.
    *   Warden (Hoothoot), Lv. 3. Moves: TACKLE, GROWL.
*   **Type Matchups Observed:**
    *   Normal (Tackle) is "not very effective" against Rock/Ground (Geodude).

## Tile Traversal Rules (Systematic Testing)
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
*   **LEDGE_HOP_LEFT:** Hypothesis: One-way traversal from right to left. *Plan: Attempt to walk onto it from the left.*
*   **WATER:** Hypothesis: Impassable without HM Surf. *Plan: Attempt to walk into it from an adjacent tile.*