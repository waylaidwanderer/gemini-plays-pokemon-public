# Gem's Pokémon Crystal Adventure Log

## I. Critical Lessons & Errors
*   **CRITICAL HALLUCINATIONS (Turns 1621 & 2043):** I have hallucinated my position and the location of items. **LESSON:** Always trust the game state information over my own memory. Verify everything.
*   **DEFERRED DATA MANAGEMENT (Turns 1621-1683):** I have repeatedly failed to immediately update map markers or my notepad after discoveries. **LESSON:** Data management (markers, notepad) must be performed in the same turn a discovery is made. It is the highest priority.
*   **FAILED INTERACTION HYPOTHESIS (Turns 1676-1833):** My attempts to interact with the Super Nerd (ID 3) on Violet City have failed multiple times as he moves away. I conclude that chasing him is not the correct way to trigger an event. **Alternative Hypothesis:** An event elsewhere (like clearing Sprout Tower) might change his behavior. I can re-test after the next major objective.

## II. Key NPCs and Locations
*   **Professor Elm:** Gave me Vulcan. Tasked me with the Gym Challenge.
*   **Mr. Pokémon:** Met him north of Cherrygrove. Task complete.
*   **Mom:** Saving my money.
*   **WADE (Bug Catcher):** Met on Route 31. Gives phone calls.
*   **FALKNER:** Violet City Gym Leader.
*   **SPROUT TOWER:** Cleared! The Elder gave me an HM.
*   **EARL'S POKéMON ACADEMY:** Located in northern Violet City.

## III. Battle and Pokemon Information
*   **Type Matchups Observed:**
    *   Normal is "not very effective" against Rock/Ground.
    *   Normal has no effect on Ghost.
    *   Ghost (Lick) has no effect on Normal.
    *   Grass (Vine Whip) is "not very effective" against Ghost/Poison.
*   **Moveset Notes:**
    *   Miasma (Gastly) learned SPITE at Lv. 8.

## IV. Tile Traversal Rules (Systematic Testing)
*Method: To confirm a tile's properties, I must attempt to move onto it from all four adjacent, traversable tiles (Up, Down, Left, Right). A conclusion is only valid after all directions are tested.*

### Confirmed Traversable:
*   **FLOOR:** Fully traversable.
*   **TALL_GRASS:** Traversable. Can trigger wild Pokémon encounters.
*   **DOOR:** Functions as a two-way warp.
*   **WARP_CARPET_DOWN:** Functions as a two-way warp.
*   **WARP_CARPET_RIGHT:** Functions as a two-way warp.

### Confirmed Impassable:
*   **WALL:** Impassable.
*   **COUNTER:** Impassable. Interact with NPCs from the front.
*   **FRUIT_TREE:** Impassable. Can be interacted with for items.
*   **PC:** Impassable. Functions as an object.
*   **VOID:** Impassable. Appears as a black abyss.

### Untested / Hypotheses:
*   **LADDER:** Hypothesis: Functions as a two-way warp. *Plan: Attempt to use from both ends.*
*   **CUT_TREE:** Hypothesis: Impassable without HM Cut. *Plan: Attempt to walk into it from an adjacent tile.*
*   **HEADBUTT_TREE:** Hypothesis: Impassable. *Plan: Attempt to walk into it from an adjacent tile.*
*   **LEDGE_HOP_DOWN/LEFT/RIGHT:** Hypothesis: One-way traversal. *Plan: Attempt to walk onto it from the opposing direction.*
*   **WATER:** Hypothesis: Impassable without HM Surf. *Plan: Attempt to walk into it from an adjacent tile.*
*   **CAVE:** Functions as a warp. *Plan: Verify if it's two-way.*
*   **STATUE:** Hypothesis: Non-interactive decoration. *Plan: Interact with a statue to test for any effect.*

## V. Future Development Ideas & Tasks
*   **Task: `marker_fix`:** The marker for the Sage at (12, 3) on SproutTower2F is not linked to its object ID. Must re-define the marker with the correct `object_id` as soon as the Sage is on-screen again.