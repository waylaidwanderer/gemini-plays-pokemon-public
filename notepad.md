# I. Core Directives & Lessons Learned
- **DIRECTIVE 1: IMMEDIATE DATA MANAGEMENT.** All data management (notepad updates, map markers, tool/agent refinement) is the HIGHEST priority and MUST be performed in the same turn a need is identified.
- **DIRECTIVE 2: ACT ON DOCUMENTATION.** A documented lesson that does not result in a behavioral change is a critical failure of the learning loop.
- **DIRECTIVE 3: ABANDON FAILED HYPOTHESES.** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach.
- **DIRECTIVE 4: TRUST, BUT REFINE, AGENTS.** I must trust the outputs of my agents. If an agent's output seems incorrect, my first assumption should be that my understanding of the game state is flawed. If, after verification, the agent is suboptimal, I must refine it immediately.
- **DIRECTIVE 5: PROACTIVELY AUTOMATE.** Before performing any complex or repetitive task, I must first consider if it can be automated with a new agent or tool.
- **DIRECTIVE 6: PROACTIVE AGENT USE.** I must leverage existing agents like `puzzle_solver_agent` and `navigation_troubleshooter` when encountering navigational or environmental puzzles, instead of defaulting to manual trial-and-error.

# II. Lessons Learned from Critiques
- **Overwatch Critique (Turn 180201):** My most significant failure is not acting upon the information documented in my own notepad. My use of map markers is also critically underdeveloped.
- **Self-Assessment (Turn 180373):** I identified an opportunity to automate restocking and created the `item_restock_agent` immediately, which was a good adherence to directives.
- **Confirmation Bias in Tool Debugging (Turns ~177769-177818):** My repeated failures with the `fly_menu_navigator` tool were exacerbated by confirmation bias. **Lesson:** When debugging, I must actively try to *disprove* my own assumptions.
- **Trust in Agents:** My trust in the `master_battle_agent`'s high-risk strategies is correct. The agent's logic is sound, and I must continue to follow it.

# III. Game & World Knowledge
## A. General Game Mechanics (Verified)
- **Porygon's Freezing Move:** Some Pokémon know moves that can inflict Freeze.
- **Segmented Waterways:** Some water routes are segmented and do not connect to all expected areas.
- **HM Deposit Rule:** HMs considered 'important' (like CUT and FLASH) cannot be deposited into the PC.

## B. Tile Mechanics & Traversal Rules (Verified)
- **ground:** Standard walkable tile.
- **grass:** Tall grass where wild Pokémon appear. Walkable.
- **impassable:** Wall or obstacle. Cannot be entered.
- **water:** Requires SURF to cross. Conditions: Must be standing on a tile directly adjacent to a water tile and be facing the water.
- **cuttable:** A tree that can be cut with HM Cut. Becomes `ground` after being cut.
- **elevated_ground:** Walkable, but on a different Z-axis from `ground`. Cannot move directly between `ground` and `elevated_ground`.
- **steps:** The only tile type that allows movement between `ground` and `elevated_ground`.
- **ledge:** Can be jumped down, but not up. A single 'Down' input from above (Y-1) moves the player to the tile below the ledge (Y+2).
- **spinner_up/down/left/right:** Forces movement in the specified direction.
- **ladder_up / ladder_down:** These function as warps, instantly transporting the player between floors.
- **teleport:** An instant warp tile, often used inside buildings like Silph Co.
- **hole:** A warp tile that leads to a lower floor, like in Seafoam Islands.
- **boulder_switch:** A floor switch that is activated by pushing a boulder onto it.
- **boulder_barrier:** An impassable barrier that becomes `cleared_boulder_barrier` when a corresponding switch is activated.
- **unknown:** Tile not visually confirmed. Treat as impassable until seen.

# IV. Battle Knowledge
## A. Type Effectiveness Discoveries (Verified)
- **Poison vs. Bug:** Poison is now super-effective against Bug. Bug is no longer strong against Poison.
- **Poison vs. Ground:** Poison is not very effective against Ground.
- **Poison vs. Poison/Flying:** Poison is not very effective against Poison/Flying dual-types.
- **Water vs. Rock/Water:** Water is not very effective against Rock/Water dual-types.
- **Ground vs. Normal:** Ground was observed to be super-effective against Porygon.
- **Ground vs. Grass/ Psychic:** Ground is not very effective against Grass/Psychic dual-types.
- **Electric vs. Grass/Poison:** Electric is not very effective against Grass/Poison dual-types.
- **Psychic vs. Poison:** Psychic is super-effective against Poison.
- **Electric vs. Flying:** Electric is super-effective against Flying. (Verified against Dodrio).

## B. Discovered Battle Mechanics (Verified)
- **Earthquake vs. Dig:** Earthquake can hit an opponent that is underground using Dig.
- **Wild Pokémon Moves:** Wild GOLEM in Cerulean Cave can use EXPLOSION and SELFDESTRUCT.
- **SELFDESTRUCT vs. Rock/Ground:** SELFDESTRUCT (a Normal-type move) is not very effective against Rock/Ground dual-types.
- **Normal vs. Normal (OHKO):** Normal-type OHKO moves (like HORN DRILL) were observed to be ineffective against a higher-level Normal-type Pokémon (Kangaskhan). The message displayed was "is unaffected!", which typically indicates type immunity.

## C. Known Pokemon Locations (Verified)
- **Cerulean Cave:** Ditto, Wigglytuff, Electrode, Golem, Raichu, Sandslash, Parasect, Lickitung, Magneton, Dodrio. (Levels ~62-65)

# V. Item & Store Data
## A. Celadon Department Store (Reference)
- **5F:** Sells TMs (WATRGUN, PAYDAY, SMCTOSS, TELEPRT) and stat-boosters (HP UP, PROTEIN, etc.).
- **4F:** Sells POKé DOLL and evolution stones (FIRE, THUNDER, WATER).
- **2F:** Sells POKé BALLs, Potions, and TMs (MEGPNCH, RZRWIND, etc.).

# VI. Agent & Tool Ideas
- **Shopping Automation:** An agent that takes the output of `item_restock_agent` (the shopping list) and generates a sequence of button presses for a tool like `execute_button_sequence` to fully automate buying items.

# VII. Untested Hypotheses
- **Electric vs. Electric:** Not very effective. (Verified against a transformed Ditto).