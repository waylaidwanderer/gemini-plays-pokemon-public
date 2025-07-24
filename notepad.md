# Gem's Pokémon Crystal Adventure Log

# I. Game Mechanics & Systems

## A. Tile Traversal Rules

### Confirmed Traversable:
*   **FLOOR:** Fully traversable.
*   **TALL_GRASS:** Traversable. Can trigger wild Pokémon encounters.
*   **DOOR:** Functions as a two-way warp.
*   **WARP_CARPET_DOWN:** Functions as a warp. Requires pressing 'Down' on the tile to activate.
*   **WARP_CARPET_LEFT:** Functions as a two-way warp.
*   **WARP_CARPET_RIGHT:** Functions as a two-way warp.
*   **CAVE:** Functions as a warp.
*   **LADDER:** Functions as a two-way warp between floors.

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
*   **FLOOR_UP_WALL:** Hypothesis: One-way traversal, only enterable from below. Test: Attempt to enter from sides.
*   **LEDGE_HOP_RIGHT:** Hypothesis: One-way traversal, only enterable from the left. Test: Attempt to move left from it.
*   **LEDGE_HOP_LEFT:** Hypothesis: One-way traversal, only enterable from the right. Test: Attempt to move right from it.
*   **WATER:** Hypothesis: Impassable without HM Surf. Test: Walk up to it and try to move onto it / press A. (Status: Untested)

# II. Battle Information

## A. Verified Type Matchups
*   Ghost-type Pokémon are immune to Normal-type moves.

# III. Badges & TMs
*   **Zephyr Badge:** Acquired from Falkner. Raises Pokémon's attack power and allows the use of HM05 (Flash) outside of battle.
*   **TM31 (Mud-Slap):** Received from Falkner. A Ground-type move that damages the opponent and lowers their accuracy. It can only be used once.

# IV. Future Plans & Ideas
*   **Agent Idea:** Create a `goal_deconstructor` agent to break down high-level goals into smaller, navigable steps.
*   **Agent Idea:** Create a `debugging_assistant` agent that can analyze faulty code and suggest fixes or debugging steps.
*   **Agent Idea:** Create a `pokedex_advisor` agent to suggest catching priorities for better team composition and type coverage.
*   **Team Composition:** Use `team_composition_advisor` before the next major battle.

# V. Reflection Log

## A. Untested Assumptions
*   **Primary Assumption:** The path south on Route 32 leads directly to the next town.
*   **Alternative Hypothesis:** The path could lead to a different area, or be blocked by an item/event requirement. The `CUT_TREE` at (10, 19) could block an alternate path.
*   **Test:** Explore all reachable paths on Route 32. Interact with all NPCs. Attempt to walk past the `CUT_TREE`.

# VI. 50-Turn Reflection Takeaways
*   **Agent Usage:** I must use the `team_composition_advisor` before the next significant trainer battle to test its effectiveness.
*   **Untested Assumption:** The southern exit of Union Cave is the correct path to Azalea Town. An alternative hypothesis is that the true path is via the currently inaccessible western section or the unexplored ladder. I will test this by continuing south, and if that path is blocked, I will need to find another way into the western part of the cave.