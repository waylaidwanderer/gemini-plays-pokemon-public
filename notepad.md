# I. Core Directives & Lessons Learned
## A. Core Directives
- **DIRECTIVE 1: IMMEDIATE DATA MANAGEMENT.** All data management (notepad updates, map markers, tool/agent refinement) is the HIGHEST priority and MUST be performed in the same turn a need is identified.
- **DIRECTIVE 2: ACT ON DOCUMENTATION.** A documented lesson that does not result in a behavioral change is a critical failure of the learning loop.
- **DIRECTIVE 3: ABANDON FAILED HYPOTHESES.** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach.
- **DIRECTIVE 4: TRUST, BUT REFINE, AGENTS & TOOLS.** I must trust the outputs of my agents and system data over my own intuition. If an agent or tool is suboptimal, I must prioritize refining it.
- **DIRECTIVE 5: PROACTIVELY AUTOMATE.** Before performing any complex or repetitive task, I must first consider if it can be automated with a new agent or tool.
- **DIRECTIVE 6: PROACTIVE AGENT USE.** I must leverage existing agents when encountering navigational or environmental puzzles, instead of defaulting to manual trial-and-error.

## B. Lessons Learned from Critiques & Self-Assessments
- **Confirmation Bias & Flawed Tools (`find_path` Failures):** Multiple critiques and self-assessments have identified the `find_path` tool's lack of diagnostic feedback as a critical flaw. This repeatedly led to incorrect conclusions about being trapped (e.g., Cerulean Cave, Cerulean City), causing severe confirmation bias and a failure to consider correct solutions like using Surf. This highlights a core failure in prioritizing immediate tool maintenance and abandoning flawed hypotheses.

- **Overwatch Critique (Turn 180201):** Failure to act on documented information and underdeveloped use of map markers.
- **Self-Assessment (Turn 180373):** Correctly identified an automation opportunity (`item_restock_agent`) and acted immediately.
- **Confirmation Bias in Tool Debugging (Turns ~177769-177818):** `fly_menu_navigator` failures highlighted the need to actively disprove my own assumptions during debugging.
- **Procedural Lesson (Notepad Usage):** Large `overwrite` actions on the notepad are prone to failure. I must break down major updates into smaller, targeted `replace` actions to ensure immediate and successful documentation.
- **Procedural Lesson (LLM Reality):** As an LLM, I cannot defer tasks. Any identified need for data management or tool refinement MUST be acted upon in the same turn. Creating a mental 'to-do list' is a critical failure of my core nature.

# II. World & Game Mechanics
## A. Tile Traversal Rules (Verified)
- **ground:** Standard walkable tile.
- **grass:** Tall grass where wild Pokémon appear. Walkable.
- **impassable:** Cannot be entered. Includes walls, rocks, etc.
- **water:** Traversable only with Surf.
- **cuttable:** A tree that can be cut using the Cut HM. Impassable without Cut.
- **ledge:** A one-way drop. Can be jumped down but not climbed up.
- **ladder_down / ladder_up:** Acts as a warp to another floor.
- **elevated_ground:** Walkable ground at a different elevation. Cannot be accessed from `ground` directly.
- **steps:** The only tile type that allows movement between `ground` and `elevated_ground`.

## B. Map Marker System
- **Standardization:**
    - `🚪 Used Warp`: For any warp that has been traversed.
    - `☠️ Defeated Trainer`: For any trainer that has been battled.
    - `✅ Item Picked Up`: For any overworld item that has been collected.
    - `🚫 Dead End`: For paths that have been confirmed to lead nowhere.
    - `🗝️ Puzzle Solved/Obstacle Cleared`: For puzzles or obstacles that have been overcome.
    - `🔄 Trap/Loop`: For tiles or warps that are part of a confusing loop or trap.

## C. Verified NPC Interactions
- **Magikarp Salesman:** Confirmed he is a one-time interaction and will not sell another Magikarp.

# III. Battle Knowledge
## A. Type Effectiveness & Battle Insights
- **Wild Pokémon Speed (Cerulean Cave):** Wild Pokémon are deceptively fast and can out-speed higher-level party members.
- **SELFDESTRUCT vs. Rock/Ground:** Not very effective.
- **SELFDESTRUCT vs. Ground:** Neutrally effective but very powerful.
- **Normal OHKO vs. Normal:** Ineffective against higher-level Normal-types.
- **Opponent Move Diversity:** Do not assume an opponent will only use its most obvious STAB move.

## B. Known Pokemon Locations
- **Cerulean Cave:** Ditto, Wigglytuff, Electrode, Golem, Raichu, Sandslash, Parasect, Lickitung, Magneton, Dodrio, RHYDON, VICTREEBEL.

# IV. Item & Store Data
## A. Celadon Department Store (Reference)
- **5F:** Sells TMs (WATRGUN, PAYDAY, SMCTOSS, TELEPRT) and stat-boosters (HP UP, PROTEIN, etc.).
- **4F:** Sells POKé DOLL and evolution stones (FIRE, THUNDER, WATER).
- **2F:** Sells POKé BALLs, Potions, and TMs (MEGPNCH, RZRWIND, etc.).

# V. Navigation Strategy
## A. Tool Limitation (find_path)
- The `find_path` tool is limited to single-map navigation and cannot plan routes that require using warps to connect otherwise disconnected areas on the same map. For complex, multi-map or multi-section dungeons, I must rely on manual exploration and my `navigation_troubleshooter` agent.

## B. Cerulean City Navigation
- The city is divided by a river. The western section (where you arrive from Route 4) and the eastern section (where the path to Route 9 is) are separated. To cross between them, I must use Surf.

# VI. Puzzles & Obstacles
- **teleport:** An instant warp tile within the same logical location.
- **gate_offscreen:** A gate whose state is unknown. Treated as potentially open for pathfinding.