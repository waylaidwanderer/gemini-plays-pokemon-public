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

## XV. Grinding Log (Route 31)
*   **Battle Log:**
    *   Defeated wild Bellsprout (Lv. 5).
    *   Defeated wild Caterpie (Lv. 4). Miasma grew to Lv. 12.
    *   Defeated wild Bellsprout (Lv. 5).
    *   Defeated wild Ledyba (Lv. 4).
    *   Defeated wild Bellsprout (Lv. 5).
    *   Defeated wild Pidgey (Lv. 5).
    *   Defeated wild Ledyba (Lv. 4).
    *   Defeated wild Bellsprout (Lv. 5).
    *   Defeated wild Weedle (Lv. 4). Miasma grew to Lv. 13 and learned MEAN LOOK.
    *   Defeated wild Bellsprout (Lv. 5).
    *   Defeated wild Ledyba (Lv. 4).

## XV. Post-Reflection Tile Additions
*   **WATER:** Hypothesis: Impassable without HM Surf. *Plan: Attempt to walk into it from an adjacent tile.*
*   **CAVE:** Functions as a warp. *Plan: Verify if it's two-way.*
*   **LEDGE_HOP_RIGHT:** Hypothesis: One-way traversal. *Plan: Attempt to walk onto it from the opposing direction.*