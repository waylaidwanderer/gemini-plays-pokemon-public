# Gem's Pokémon Crystal Adventure Log

# I. Game Mechanics & Systems

## A. Tile Traversal Rules (Systematic Testing)
*Method: To confirm a tile's properties, I must attempt to move onto it from all four adjacent, traversable tiles (Up, Down, Left, Right). A conclusion is only valid after all directions are tested.*

### Confirmed Traversable:
*   **FLOOR:** Fully traversable.
*   **TALL_GRASS:** Traversable. Can trigger wild Pokémon encounters.
*   **DOOR:** Functions as a two-way warp.
*   **WARP_CARPET_DOWN:** Functions as a two-way warp.
*   **WARP_CARPET_LEFT:** Functions as a two-way warp.
*   **WARP_CARPET_RIGHT:** Functions as a two-way warp. 

### Confirmed Impassable:
*   **WALL:** Impassable.
*   **COUNTER:** Impassable. Interact with NPCs from the front.
*   **PC:** Impassable. Functions as an object.
*   **VOID:** Impassable. Appears as a black abyss.
*   **CUT_TREE:** Impassable. Likely requires HM Cut.
*   **HEADBUTT_TREE:** Impassable. Likely requires HM Headbutt.
*   **SIGN:** Impassable. Functions as an object that can be interacted with for text.
*   **BOOKSHELF:** Impassable. Functions as an object that can be interacted with for text.

### Confirmed One-Way:
*   **LEDGE_HOP_DOWN:** One-way traversal. Can only be entered from above.

### Hypotheses to Test:
*   **WATER:** Hypothesis: Impassable without HM Surf.
*   **CAVE:** Hypothesis: Functions as a warp. Needs testing to see if it's one-way or two-way.
*   **LEDGE_HOP_RIGHT:** Hypothesis: One-way traversal. Needs testing.
*   **BLACKBOARD:** Impassable. Functions as an object that can be interacted with for text.

# II. Reminders & Housekeeping
*   **Systematic Testing:** Must test all unknown tile mechanics immediately upon entering a new area.
*   **Trainer Marking:** Must mark all defeated trainers with '☠️' immediately after battle.

# III. Badges & TMs
*   **Zephyr Badge:** Acquired from Falkner. Raises Pokémon's attack power and allows the use of HM05 (Flash) outside of battle.
*   **TM31 (Mud-Slap):** Received from Falkner. A Ground-type move that damages the opponent and lowers their accuracy. It can only be used once.

# IV. Future Exploration Plans
*   **Violet City Exits:** If the path south from Violet City leads to a dead end, systematically re-investigate the city's boundaries for other potential exits, possibly requiring HMs like Surf or Cut.