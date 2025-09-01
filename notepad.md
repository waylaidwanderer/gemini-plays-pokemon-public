# I. Core Directives & Lessons Learned
- **DIRECTIVE 1: IMMEDIATE DATA MANAGEMENT.** All data management (notepad updates, map markers, tool/agent refinement) is the HIGHEST priority and MUST be performed in the same turn a need is identified. Acknowledged lapse in battle, will be more diligent.
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

# IV. Battle Knowledge
## A. Discovered Battle Mechanics (Verified)
- **Earthquake vs. Dig:** Earthquake can hit an opponent that is underground using Dig.
- **Wild Pokémon Speed:** Wild Pokémon in Cerulean Cave are deceptively fast and can out-speed higher-level party members. Do not rely on level alone to determine speed order.
- **SELFDESTRUCT vs. Rock/Ground:** SELFDESTRUCT (a Normal-type move) is not very effective against Rock/Ground dual-types.
- **SELFDESTRUCT vs. Ground:** SELFDESTRUCT (a Normal-type move) was observed to be neutrally effective against a Ground-type Pokémon (Marowak), but powerful enough to knock it out from over half health.
- **Normal vs. Normal (OHKO):** Normal-type OHKO moves (like HORN DRILL) were observed to be ineffective against a higher-level Normal-type Pokémon (Kangaskhan).

## B. Known Pokemon Locations (Verified)
- **Cerulean Cave:** Ditto, Wigglytuff, Electrode, Golem, Raichu, Sandslash, Parasect, Lickitung, Magneton, Dodrio. (Levels ~62-65)

# V. Item & Store Data
## A. Celadon Department Store (Reference)
- **5F:** Sells TMs (WATRGUN, PAYDAY, SMCTOSS, TELEPRT) and stat-boosters (HP UP, PROTEIN, etc.).
- **4F:** Sells POKé DOLL and evolution stones (FIRE, THUNDER, WATER).
- **2F:** Sells POKé BALLs, Potions, and TMs (MEGPNCH, RZRWIND, etc.).

# VI. Agent & Tool Ideas
- **Shopping Automation:** An agent that takes the output of `item_restock_agent` (the shopping list) and generates a sequence of button presses for a tool like `execute_button_sequence` to fully automate buying items.
- **Pokémon Switching Automation:** An agent or tool to automate the multi-step process of switching Pokémon in battle (e.g., takes a target Pokémon name and generates the button sequence for `execute_button_sequence`).
- **Flee-Prep Automation:** An agent to handle the logic of switching to a healthy Pokémon when the lead is incapacitated, specifically for the purpose of running on the next turn.

# VII. Future Development & Testing
## A. Agent & Tool Ideas
- **Systematic Tile Tester:** An agent or process to systematically test the properties of all encountered tile types and document the results.
- **Escape Artist Agent:** An agent that takes the party status during a wild battle and determines the optimal sequence of actions (e.g., switch to a specific Pokémon, then run) to flee successfully.
- **Switch & Run Tool:** A tool that takes a Pokémon's name as input and generates the button sequence to switch to it. This could be used by the Escape Artist Agent.

## B. Lessons & Hypotheses
- **Opponent Move Diversity:** Do not assume an opponent will only use its most obvious STAB move. High-level wild Pokémon in dangerous areas like Cerulean Cave have coverage moves (e.g., Golem with Explosion). Be prepared for unexpected attacks.