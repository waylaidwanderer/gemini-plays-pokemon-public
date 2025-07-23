# Gem's Pokémon Crystal Adventure Log

# I. Game Mechanics & Systems

## A. Tile Traversal Rules (Systematic Testing)
*Method: To confirm a tile's properties, I must attempt to move onto it from all four adjacent, traversable tiles (Up, Down, Left, Right). A conclusion is only valid after all directions are tested.*

### Confirmed Traversable:
*   **FLOOR:** Fully traversable.
*   **TALL_GRASS:** Traversable. Can trigger wild Pokémon encounters.
*   **DOOR:** Functions as a two-way warp.
*   **WARP_CARPET_DOWN/LEFT/RIGHT:** Functions as a two-way warp.

### Confirmed Impassable:
*   **WALL:** Impassable.
*   **COUNTER:** Impassable. Interact with NPCs from the front.
*   **PC:** Impassable. Functions as an object.
*   **VOID:** Impassable. Appears as a black abyss.
*   **CUT_TREE:** Impassable. (Test at Route 31 (13, 5) confirmed). Likely requires HM Cut.
*   **HEADBUTT_TREE:** Impassable and non-interactive. (Test at Route 31 (13, 4) confirmed). Likely requires HM Headbutt.

### Confirmed One-Way:
*   **LEDGE_HOP_DOWN:** One-way traversal. Can only be entered from above. (Test at Route 31 (7, 9) confirmed).

# II. Current Objectives & Strategy

## A. Falkner Gym Battle Plan
*   **Primary Goal:** Defeat Falkner and obtain the Zephyr Badge.
*   **Target Level:** Train Vulcan to at least Lv. 15.
*   **Strategy:**
    *   Lead with Vulcan (Quilava). Its Fire-type move, Ember, will be super-effective against Falkner's Flying-type Pokémon (likely Pidgey and Pidgeotto).
    *   Miasma (Gastly) is a backup. Its Ghost-type gives it immunity to Normal attacks, but Lick has 0 PP and is not super-effective. Hypnosis could be useful if Vulcan is in trouble.
    *   Warden (Hoothoot) is too low-level and will not be used in the battle.
*   **Training Status:** Currently grinding on Route 31.

## B. Future Tile Mechanic Tests
*   **WATER:** Hypothesis: Impassable without HM Surf. *Plan: Attempt to walk into it from an adjacent tile.*
*   **CAVE:** Functions as a warp. *Plan: Verify if it's two-way.*
*   **LEDGE_HOP_RIGHT:** Hypothesis: One-way traversal. *Plan: Attempt to walk onto it from the opposing direction.*

### Inconsistent Mechanics:
*   **WARP_CARPET_LEFT:** Behavior is inconsistent. Moving left onto the tile worked once but has failed repeatedly since. Interaction by pressing 'A' has also failed. The exact trigger condition is unknown and requires further, systematic testing.

# III. Reminders & Housekeeping
*   **Systematic Testing:** Must test all unknown tile mechanics (`WATER`, `CAVE`) as soon as possible.
*   **Trainer Marking:** Must mark all defeated trainers with '☠️' immediately after battle to avoid confusion.
*   **SIGN:** Impassable. Functions as an object that can be interacted with for text.