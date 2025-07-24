# Gem's Pokémon Crystal Adventure Log

# I. Game Mechanics & Systems

## A. Tile Traversal Rules

### Confirmed Traversable:
*   **FLOOR:** Fully traversable.
*   **TALL_GRASS:** Traversable. Can trigger wild Pokémon encounters.
*   **DOOR:** Functions as a two-way warp.
*   **CAVE:** Functions as a warp.
*   **LADDER:** Functions as a two-way warp between floors.

### Warp Tiles:
*   **WARP_CARPET_DOWN:** One-way warp. Activated by pressing 'Down'.
*   **WARP_CARPET_LEFT:** One-way warp. Activated by moving onto the tile from the right.
*   **WARP_CARPET_RIGHT:** One-way warp. Activated by moving onto the tile from the left.

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
*   **WATER:** Confirmed impassable. Blocks movement entirely.

### Confirmed One-Way:
*   **LEDGE_HOP_DOWN:** One-way traversal. Can only be entered from above.
*   **FLOOR_UP_WALL:** Confirmed one-way traversal. Can only be entered from below. Impassable from all other directions.

### Under Investigation:
*   **unknown:** Encountered this tile type when interacting with the Kabuto puzzle in the Ruins of Alph. Its properties are currently unknown as I am locked in the puzzle interface. Must investigate after completion.

# II. Battle Information

## A. Verified Type Matchups
*   Ghost-type Pokémon are immune to Normal-type moves.

# III. Badges & TMs
*   **Zephyr Badge:** Acquired from Falkner. Raises Pokémon's attack power and allows the use of HM05 (Flash) outside of battle.
*   **TM31 (Mud-Slap):** Received from Falkner.
*   **TM39:** Found in Union Cave B1F.

# IV. Reflection Log

## A. 50-Turn Reflection Takeaways (Turn 5320)
*   **Immediate Action Mandate:** I have repeatedly deferred critical tasks (tool fixing, data management) to 'later'. A specific example is failing to immediately mark the warp at (4,0) in the Ruins of Alph Kabuto Chamber, despite multiple system warnings. As an LLM, there is no 'later'. All necessary actions, especially data management and tool refinement, MUST be performed in the immediate turn they are identified. This is a core operational principle I must adhere to.
*   **Untested Assumptions (Ruins of Alph):** My primary assumption is that solving the Kabuto puzzle is the only way to progress. An alternative hypothesis is that the puzzle is optional and the true path is via the unexplored warps at (4, 0) or (4, 9). I will test this by exploring those warps immediately after finishing or abandoning this puzzle attempt.

## B. Past Reflection Takeaways
*   **Untested Assumption (Union Cave):** The southern exit of Union Cave is the correct path to Azalea Town. An alternative hypothesis is that the true path is via the currently inaccessible western section or the unexplored ladder. I will test this by continuing south, and if that path is blocked, I will need to find another way into the western part of the cave.

# V. Phone Calls & Side Quests
*   Wade called about the Bug-Catching Contest at the National Park.

# VI. New Discoveries & Lessons
*   **Ruins of Alph is Mandatory:** My previous assumption that this area was a side quest has been proven false, as all known exits are blocked or inactive. This is now considered the main path forward, and I must explore it thoroughly to find the true exit.
*   **SUPER_NERD at (4, 21) in Union Cave is not a trainer.** He is an NPC who gives a hint about Pokémon roars on Fridays. The western path is currently blocked by him.

## C. 50-Turn Reflection Takeaways (Turn 5372)
*   **Immediate Action Mandate (Reaffirmed):** I have again violated my core principle of immediate action. I deferred fixing my `kabuto_puzzle_solver` tool in favor of failed manual attempts and did not immediately mark discovered warps, despite system warnings. This is a critical failure. All data management, tool refinement, and agent work MUST be performed in the turn they are identified, overriding any gameplay objective.