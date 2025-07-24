# Gem's Pokémon Crystal Adventure Log

# I. Game Mechanics & Systems

## A. Tile Traversal Rules

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
*   **BLACKBOARD:** Impassable. Functions as an object that can be interacted with for text.
*   **MART_SHELF:** Impassable. Functions as a wall.

### Confirmed One-Way:
*   **LEDGE_HOP_DOWN:** One-way traversal. Can only be entered from above.
*   **FLOOR_UP_WALL:** One-way traversal. Can only be entered from below (impassable from above).

### Hypotheses to Test:
*   **WATER:** Hypothesis: Impassable without HM Surf.
*   **CAVE:** Hypothesis: Functions as a warp. Needs testing.
*   **LEDGE_HOP_RIGHT:** Hypothesis: One-way traversal. Needs testing.
*   **LEDGE_HOP_LEFT:** Hypothesis: One-way traversal. Needs testing.
*   **unknown:** Hypothesis: Impassable. Needs testing.
*   **INCENSE_BURNER:** Hypothesis: Impassable object. Needs testing.
*   **RADIO:** Hypothesis: Impassable object. May be interactable. Needs testing.

# II. Reminders & Housekeeping
*   **Data Hygiene:** Must mark all defeated trainers, new NPCs, and warps (both sides) immediately. Trust Game State Info over memory.

# III. Badges & TMs
*   **Zephyr Badge:** Acquired from Falkner. Raises Pokémon's attack power and allows the use of HM05 (Flash) outside of battle.
*   **TM31 (Mud-Slap):** Received from Falkner. A Ground-type move that damages the opponent and lowers their accuracy. It can only be used once.

# IV. Goal-Oriented Planning

## A. Primary Goal: Find the next town and challenge its Gym Leader
*   **Hypothesis:** The path forward is south or west out of Violet City.
*   **Plan:**
    1.  Fully explore Violet City to find the exit.
    2.  Use my newly-fixed `find_reachable_unseen_tiles` tool to guide exploration.
    3.  Once the exit is found, proceed to the next route.

# V. Future Plans & Ideas
*   **Agent Idea:** Create an `exploration_strategist` agent that takes the output of `find_reachable_unseen_tiles` and suggests the most optimal tile to explore next based on current goals.