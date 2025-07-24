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
*   **CAVE:** Functions as a warp.

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
*   **LEDGE_HOP_RIGHT:** One-way traversal. Can only be entered from the left.
*   **LEDGE_HOP_LEFT:** One-way traversal. Can only be entered from the right.

### Hypotheses to Test:
*   **WATER:** Hypothesis: Impassable without HM Surf.

# II. Reminders & Housekeeping
*   **Data Hygiene:** Must mark all defeated trainers, new NPCs, and warps (both sides) immediately. Trust Game State Info over memory.
*   **Marker Hygiene:** All moving NPCs MUST be marked with their `object_id`.
*   **HIGH PRIORITY To-Do:** Revisit Violet City and update all NPC markers (Super Nerd, Gramps, Fisher, Youngster, Lass) to link them with their `object_id`.

# III. Badges & TMs
*   **Zephyr Badge:** Acquired from Falkner. Raises Pokémon's attack power and allows the use of HM05 (Flash) outside of battle.
*   **TM31 (Mud-Slap):** Received from Falkner. A Ground-type move that damages the opponent and lowers their accuracy. It can only be used once.

# IV. Goal-Oriented Planning

## A. Primary Goal: Travel south to find the next town and its Gym Leader
*   **Plan:**
    1.  Exit Violet City to the south.
    2.  Explore the new route.
    3.  Look for signs or NPCs that indicate the way to the next town.

# V. Future Plans & Ideas
*   **Agent Idea:** Create a `debugging_assistant` agent that can analyze faulty code and suggest fixes or debugging steps.

# VI. Battle Information

## A. Verified Type Matchups
*   Ghost-type Pokémon are immune to Normal-type moves.