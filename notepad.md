# I. Core Directives & Lessons Learned
- **DIRECTIVE 1: IMMEDIATE DATA MANAGEMENT.** All data management (notepad updates, map markers, tool/agent refinement) is the HIGHEST priority and MUST be performed in the same turn a need is identified. Acknowledged lapse in battle, will be more diligent.
- **DIRECTIVE 2: ACT ON DOCUMENTATION.** A documented lesson that does not result in a behavioral change is a critical failure of the learning loop.
- **DIRECTIVE 3: ABANDON FAILED HYPOTHESES.** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach.
- **DIRECTIVE 4: TRUST, BUT REFINE, AGENTS & TOOLS.** I must trust the outputs of my agents and system data over my own intuition. If an agent or tool is suboptimal (like `find_path` in Cerulean Cave), I must prioritize refining it.
- **DIRECTIVE 5: PROACTIVELY AUTOMATE.** Before performing any complex or repetitive task, I must first consider if it can be automated with a new agent or tool.
- **DIRECTIVE 6: PROACTIVE AGENT USE.** I must leverage existing agents like `puzzle_solver_agent` and `navigation_troubleshooter` when encountering navigational or environmental puzzles, instead of defaulting to manual trial-and-error.

# II. Lessons Learned from Critiques & Self-Assessments
- **Overwatch Critique (Turn 180201):** Failure to act on documented information and underdeveloped use of map markers.
- **Self-Assessment (Turn 180373):** Correctly identified an automation opportunity (`item_restock_agent`) and acted immediately.
- **Confirmation Bias in Tool Debugging (Turns ~177769-177818):** `fly_menu_navigator` failures highlighted the need to actively disprove my own assumptions during debugging.
- **Self-Assessment (Turn 181193):** `find_path` tool is unreliable in Cerulean Cave. Manual exploration is necessary when automation fails. Tile mechanic documentation needs to be more formal.

# III. World & Tile Mechanics
## A. Tile Traversal Rules (Verified)
- **ground:** Standard walkable tile.
- **impassable:** Cannot be entered. Includes walls, rocks, water (without Surf), etc.
- **ladder_down / ladder_up:** Acts as a warp to another floor.
- **elevated_ground:** Walkable ground at a different elevation. Cannot be accessed from `ground` directly.
- **steps:** The only tile type that allows movement between `ground` and `elevated_ground`.
- **water:** Traversable only with Surf.

# IV. Battle Knowledge
## A. Discovered Battle Mechanics (Verified)
- **Earthquake vs. Dig:** Earthquake can hit an opponent that is underground using Dig.
- **Wild Pokémon Speed (Cerulean Cave):** Wild Pokémon are deceptively fast and can out-speed higher-level party members.
- **SELFDESTRUCT vs. Rock/Ground:** Not very effective.
- **SELFDESTRUCT vs. Ground:** Neutrally effective but very powerful.
- **Normal OHKO vs. Normal:** Ineffective against higher-level Normal-types.

## B. Known Pokemon Locations (Verified)
- **Cerulean Cave:** Ditto, Wigglytuff, Electrode, Golem, Raichu, Sandslash, Parasect, Lickitung, Magneton, Dodrio, RHYDON, VICTREEBEL.

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

# VIII. World & Tile Mechanics
## A. Tile Traversal Rules (Verified)
- **ground:** Standard walkable tile.
- **impassable:** Cannot be entered. Includes walls, rocks, water (without Surf), etc.
- **ladder_down:** Acts as a warp to a lower floor.

## B. Hypotheses Under Investigation
- **Mewtwo's Location:** It is assumed Mewtwo is located deep within Cerulean Cave. This is based on general knowledge and has not been confirmed with in-game evidence.