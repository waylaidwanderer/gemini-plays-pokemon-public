# Core Directives & Lessons Learned
- **IMMEDIATE DATA MANAGEMENT:** All documentation (notepad, markers) and tool/agent refinement is the HIGHEST priority and must be performed in the same turn a need is identified.
- **ACT ON DOCUMENTATION:** A documented lesson that does not result in a behavioral change is a critical failure.
- **ABANDON FAILED HYPOTHESES:** If a strategy fails repeatedly, document it and pivot.
- **TRUST, BUT REFINE, AUTOMATION:** Trust agent/tool outputs over intuition. If an agent is suboptimal, prioritize refining it.
- **PROACTIVELY AUTOMATE & USE AGENTS:** Before any complex/repetitive task, consider if it can be automated. Leverage existing agents instead of defaulting to manual trial-and-error.

# II. Lessons Learned from Critiques & Self-Assessments
- **Overwatch Critique (Turn 180201):** Failure to act on documented information and underdeveloped use of map markers.
- **Self-Assessment (Turn 180373):** Correctly identified an automation opportunity (`item_restock_agent`) and acted immediately.
- **Confirmation Bias in Tool Debugging (Turns ~177769-177818):** `fly_menu_navigator` failures highlighted the need to actively disprove my own assumptions during debugging.
- **Self-Assessment (Turn 181193):** `find_path` tool is unreliable in Cerulean Cave. Manual exploration is necessary when automation fails. Tile mechanic documentation needs to be more formal.
- **Overwatch Critique (Turn 181252):** Multi-turn failures to update notes are a critical procedural error. I must break down large `overwrite` or `replace` actions into smaller, targeted chunks to avoid character limit errors and ensure immediate documentation.

# III. World & Game Mechanics
## A. Tile Traversal Rules (Verified)
- **ground:** Standard walkable tile.
- **impassable:** Cannot be entered. Includes walls, rocks, water (without Surf), etc.
- **ladder_down / ladder_up:** Acts as a warp to another floor.
- **elevated_ground:** Walkable ground at a different elevation. Cannot be accessed from `ground` directly.
- **steps:** The only tile type that allows movement between `ground` and `elevated_ground`.
- **water:** Traversable only with Surf.

## B. Other Mechanics (Verified)
- **Earthquake vs. Dig:** Earthquake can hit an opponent that is underground using Dig.

# IV. Battle Knowledge
## A. Type Effectiveness & Battle Insights
- **Wild Pokémon Speed (Cerulean Cave):** Wild Pokémon are deceptively fast and can out-speed higher-level party members.
- **SELFDESTRUCT vs. Rock/Ground:** Not very effective.
- **SELFDESTRUCT vs. Ground:** Neutrally effective but very powerful.
- **Normal OHKO vs. Normal:** Ineffective against higher-level Normal-types.
- **Opponent Move Diversity:** Do not assume an opponent will only use its most obvious STAB move. High-level wild Pokémon in dangerous areas like Cerulean Cave have coverage moves (e.g., Golem with Explosion).

## B. Known Pokemon Locations
- **Cerulean Cave:** Ditto, Wigglytuff, Electrode, Golem, Raichu, Sandslash, Parasect, Lickitung, Magneton, Dodrio, RHYDON, VICTREEBEL.

# V. Item & Store Data
## A. Celadon Department Store (Reference)
- **5F:** Sells TMs (WATRGUN, PAYDAY, SMCTOSS, TELEPRT) and stat-boosters (HP UP, PROTEIN, etc.).
- **4F:** Sells POKé DOLL and evolution stones (FIRE, THUNDER, WATER).
- **2F:** Sells POKé BALLs, Potions, and TMs (MEGPNCH, RZRWIND, etc.).

# VI. Development Pipeline
## A. Agent & Tool Ideas
- **Escape Artist Agent:** An agent to manage the loop of running from wild battles and re-pathfinding to safely escape dangerous areas with a critically injured team. This is a top priority after escaping.
- **Shopping Automation:** An agent that takes the output of `item_restock_agent` (the shopping list) and generates a sequence of button presses for a tool like `execute_button_sequence` to fully automate buying items.
- **Pokémon Switching Automation:** An agent or tool to automate the multi-step process of switching Pokémon in battle.
- **Systematic Tile Tester:** An agent or process to systematically test the properties of all encountered tile types and document the results.
- **`navigation_troubleshooter` Refinement:** Add `party_health_summary` as an input to allow it to prioritize escape/healing when the party is weak.
- **`find_path` Refinement:** Investigate and fix the tool's pathing logic, specifically its handling of `steps`, `elevated_ground`, and complex multi-level maps like Cerulean Cave. This is a top priority after escaping.