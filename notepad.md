# Gem's Pokémon Crystal Adventure Log

# I. Game Mechanics & Systems

## A. Tile Traversal Rules (Systematic Testing)
*Method: To confirm a tile's properties, I must attempt to move onto it from all four adjacent, traversable tiles (Up, Down, Left, Right). A conclusion is only valid after all directions are tested.*

### Confirmed Traversable:
*   **FLOOR:** Fully traversable.
*   **TALL_GRASS:** Traversable. Can trigger wild Pokémon encounters.
*   **DOOR:** Functions as a two-way warp.
*   **WARP_CARPET_DOWN/LEFT/RIGHT:** Functions as a two-way warp. (RIGHT and DOWN confirmed by use).

### Confirmed Impassable:
*   **WALL:** Impassable.
*   **COUNTER:** Impassable. Interact with NPCs from the front.
*   **PC:** Impassable. Functions as an object.
*   **VOID:** Impassable. Appears as a black abyss.
*   **CUT_TREE:** Impassable. (Test at Route 31 (13, 5) confirmed). Likely requires HM Cut.
*   **HEADBUTT_TREE:** Impassable and non-interactive. (Test at Route 31 (13, 4) confirmed). Likely requires HM Headbutt.
*   **SIGN:** Impassable. Functions as an object that can be interacted with for text.

### Confirmed One-Way:
*   **LEDGE_HOP_DOWN:** One-way traversal. Can only be entered from above. (Test at Route 31 (7, 9) confirmed).

### Hypotheses to Test:
*   **WATER:** Hypothesis: Impassable without HM Surf. *Plan: Attempt to walk into it from an adjacent tile at the earliest opportunity.*
*   **CAVE:** Functions as a warp. *Plan: Verify if it's two-way.*
*   **LEDGE_HOP_RIGHT:** Hypothesis: One-way traversal. *Plan: Attempt to walk onto it from the opposing direction.*

### Inconsistent Mechanics:
*   **WARP_CARPET_LEFT:** Behavior is inconsistent. Moving left onto the tile worked once but has failed repeatedly since. Interaction by pressing 'A' has also failed. The exact trigger condition is unknown and requires further, systematic testing.

# II. Reminders & Housekeeping
*   **Systematic Testing:** Must test all unknown tile mechanics (`WATER`, `CAVE`, `LEDGE_HOP_RIGHT`) as soon as possible.
*   **Trainer Marking:** Must mark all defeated trainers with '☠️' immediately after battle to avoid confusion.

# III. Badges & TMs
*   **Zephyr Badge:** Acquired from Falkner. Raises Pokémon's attack power and allows the use of HM FLASH outside of battle.
*   **TM31 (Mud-Slap):** Received from Falkner. A Ground-type move that damages the opponent and lowers their accuracy. It can only be used once.

# IV. Future Exploration Plans
*   **Violet City Exits:** If the path south from Violet City leads to a dead end, systematically re-investigate the city's boundaries for other potential exits, possibly requiring HMs like Surf or Cut.