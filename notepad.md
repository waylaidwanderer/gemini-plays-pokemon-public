# I. Core Directives & Lessons Learned
## A. Core Directives
- **DIRECTIVE 1: IMMEDIATE DATA MANAGEMENT.** All data management (notepad updates, map markers, tool/agent refinement) is the HIGHEST priority and MUST be performed in the same turn a need is identified.
- **DIRECTIVE 2: ACT ON DOCUMENTATION.** A documented lesson that does not result in a behavioral change is a critical failure of the learning loop.
- **DIRECTIVE 3: ABANDON FAILED HYPOTHESES.** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach.
- **DIRECTIVE 4: TRUST, BUT REFINE, AGENTS & TOOLS.** I must trust the outputs of my agents and system data over my own intuition. If an agent or tool is suboptimal, I must prioritize refining it.
- **DIRECTIVE 5: PROACTIVELY AUTOMATE.** Before performing any complex or repetitive task, I must first consider if it can be automated with a new agent or tool.
- **DIRECTIVE 6: PROACTIVE AGENT USE.** I must leverage existing agents when encountering navigational or environmental puzzles, instead of defaulting to manual trial-and-error.

## B. Lessons Learned from Critiques & Self-Assessments
- **Overwatch Critique (Turn 180201):** Failure to act on documented information and underdeveloped use of map markers.
- **Self-Assessment (Turn 180373):** Correctly identified an automation opportunity (`item_restock_agent`) and acted immediately.
- **Confirmation Bias in Tool Debugging (Turns ~177769-177818):** `fly_menu_navigator` failures highlighted the need to actively disprove my own assumptions during debugging.
- **Self-Assessment (Turn 181193):** `find_path` tool is unreliable in Cerulean Cave. Manual exploration is necessary when automation fails. Tile mechanic documentation needs to be more formal.
- **Overwatch Critique (Turn 181252):** Multi-turn failures to update notes are a critical procedural error. I must break down large `overwrite` or `replace` actions into smaller, targeted chunks to avoid character limit errors and ensure immediate documentation.
- **Overwatch Critique (Turn 181551):** Deferring tool maintenance is a critical failure. The `find_path` tool's lack of diagnostic feedback led to incorrect conclusions about being in a dead end.
- **Overwatch Critique (Turn 181601):** Deferring tool maintenance via the 'Development Pipeline' is a critical failure. Tile traversal documentation is incomplete and map marker usage is inefficient and inconsistent.
- **Overwatch Critique (Turn 181701):** My `find_path` tool is critically flawed and lacks diagnostic feedback. My notepad is disorganized with duplicated and missing information. My map marker discipline is inconsistent.
- **Overwatch Critique (Turn 181951):** My `find_path` tool is a crutch that lacks diagnostic feedback. My notepad is used passively to document flaws instead of actively triggering fixes. My map marker discipline is inconsistent, leading to clutter. I failed to document a critical change in party status (0 PP on attacking moves).
- **Overwatch Critique (Turn 182008):** My reactive approach to tool maintenance, deficient notepad management (especially the multi-turn failure to document critical party status), and inconsistent map markers are major procedural errors.
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
- The `find_path` tool is limited to single-map navigation. For complex, multi-level dungeons like Mt. Moon, it is unreliable. I must rely on methodical manual exploration and my `navigation_troubleshooter` agent instead of using `find_path` to plan routes across different floors.

# VI. Future Development
- **`nickname_generator` Tool:** The manual process of nicknaming is tedious and error-prone. A tool should be developed to take a target name and current cursor position as input, and output the precise sequence of button presses needed to enter it. This would automate the process and eliminate manual errors.

# VII. Puzzles & Obstacles
## A. Route 4 "Geodude" Trainer Puzzle
- **Location:** Route 4, Cool Trainer F at (10, 7).
- **Description:** Trainer blocks the path. Interacting with 'A' triggers the message "Ouch! I tripped over a rocky POKéMON, GEODUDE!" but does not initiate a battle. The trainer is impassable.
- **Failed Hypotheses:**
  1. Interacting normally starts a battle. (Attempted 3 times)
  2. The trainer can be walked through. (Attempted 1 time)
  3. Leading with a Rock/Ground type Pokémon (Golem) allows passage. (Attempted 1 time)
  4. Interacting from the side (left) changes the outcome. (Attempted 1 time)