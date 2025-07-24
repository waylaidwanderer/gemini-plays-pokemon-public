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
*   **BLACKBOARD:** Impassable. Functions as an object that can be interacted with for text.
*   **MART_SHELF:** Impassable. Functions as a wall.

### Confirmed One-Way:
*   **LEDGE_HOP_DOWN:** One-way traversal. Can only be entered from above.

### Hypotheses to Test:
*   **WATER:** Hypothesis: Impassable without HM Surf.
*   **CAVE:** Hypothesis: Functions as a warp. Needs testing to see if it's one-way or two-way.
*   **LEDGE_HOP_RIGHT:** Hypothesis: One-way traversal. Needs testing.
*   **unknown:** Hypothesis: Impassable. Needs testing.
*   **INCENSE_BURNER:** Hypothesis: Impassable object. Needs testing.
*   **RADIO:** Hypothesis: Impassable object. May be interactable. Needs testing.

# II. Reminders & Housekeeping
*   **Systematic Testing:** Must test all unknown tile mechanics immediately upon entering a new area.
*   **Data Hygiene:** Must mark all defeated trainers, new NPCs, and warps (both sides) immediately. Trust Game State Info over memory.

# III. Badges & TMs
*   **Zephyr Badge:** Acquired from Falkner. Raises Pokémon's attack power and allows the use of HM05 (Flash) outside of battle.
*   **TM31 (Mud-Slap):** Received from Falkner. A Ground-type move that damages the opponent and lowers their accuracy. It can only be used once.

# IV. Goal-Oriented Planning

## A. Primary Goal: Find and defeat the next Gym Leader

*   **Hypothesis:** The path forward is through this gatehouse to Route 31, which should lead to the next town and gym.
*   **Plan:**
    1.  Interact with the NPCs in this gatehouse for any potential clues.
    2.  Exit the gatehouse to the east, onto Route 31.
    3.  Explore Route 31 thoroughly to find the path to the next city.
    4.  Train my Pokémon on Route 31 to prepare for the next Gym Leader. VULCAN and MIASma are my primary fighters.
    5.  Once in the new city, locate the Gym and challenge the leader.
*   **Cleanup Task:** Delete incorrect warp marker on Route 31 (map 26_10) at (4, 6) which was placed due to a hallucination.

# V. Future Plans & Ideas
*   **Agent Idea:** Create an `exploration_strategist` agent that takes the output of `find_reachable_unseen_tiles` and suggests the most optimal tile to explore next based on current goals.
*   **Mechanics to Test on Route 31:**
    1.  Test WATER tiles to confirm if they are impassable without Surf.
    2.  Test the CAVE entrance at (34, 5) to confirm it's a warp.
    3.  Test the LEDGE_HOP_RIGHT tiles at (13, 7) and (13, 8) to confirm they are one-way only.