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

### Hypotheses to Test:
*   **WATER:** Hypothesis: Impassable without HM Surf. Test: Walk up to it and try to move onto it / press A.
*   **FLOOR_UP_WALL:** Hypothesis: One-way traversal, only enterable from below. Test: Attempt to enter from sides.
*   **LEDGE_HOP_RIGHT:** Hypothesis: One-way traversal, only enterable from the left. Test: Attempt to move left from it.
*   **LEDGE_HOP_LEFT:** Hypothesis: One-way traversal, only enterable from the right. Test: Attempt to move right from it.

# II. Battle Information

## A. Verified Type Matchups
*   Ghost-type Pokémon are immune to Normal-type moves.

# III. Badges & TMs
*   **Zephyr Badge:** Acquired from Falkner. Raises Pokémon's attack power and allows the use of HM05 (Flash) outside of battle.
*   **TM31 (Mud-Slap):** Received from Falkner. A Ground-type move that damages the opponent and lowers their accuracy. It can only be used once.

# IV. Future Plans & Ideas
*   **Agent Idea:** Create a `debugging_assistant` agent that can analyze faulty code and suggest fixes or debugging steps.
*   **Agent Refinement Idea:** Refine the `battle_strategist` to provide more detailed switching advice, considering the entire party's composition and the opponent's likely moves.

# V. Reflection Log (Turn 3815)
*   **Untested Assumption:** The next town is directly south. 
*   **Alternative Hypothesis:** The path south could be a dead end, and the true path is elsewhere.
*   **Test:** Follow the agent's recommendation to the southernmost point. If it's a dead end, re-evaluate exploration priorities.