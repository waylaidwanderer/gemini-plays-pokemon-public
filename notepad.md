# I. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.
- **Follower Pokémon Mechanics:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions. The first button press turns to face, the second moves.
- **Dig Field Move:** Can be used to escape caves, acting as an Escape Rope. This is a key anti-softlock mechanic.

# II. Tile Mechanics (Verified)
- `ground`: Walkable tile.
- `grass`: Tall grass where wild Pokémon appear. Walkable like `ground`.
- `water`: Crossable using HM Surf.
- `impassable`: Walls, rocks, statues, and sometimes objects like defeated trainers. Cannot be entered.
- `ledge`: Can only be traversed downwards from an adjacent tile above it.
- `steps`: Connects `ground` and `elevated_ground` tiles, allowing vertical movement between them.
- `elevated_ground`: Walkable ground at a higher elevation. Movement to/from `ground` tiles requires `steps` or a one-way `ledge` drop.
- `cleared_boulder_barrier`: A tile that becomes traversable after a boulder switch is activated. Acts like `elevated_ground` and can function as a one-way ramp up.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `warp`: A tile that transports the player to another location, often a door or cave entrance.
- `ladder_down` / `ladder_up`: Warps between floors.
- `hole`: Warps the player (or a boulder) to the floor below.

# III. Puzzle Mechanics & Solutions
- **Reset Condition:** Boulder puzzles reset upon leaving and re-entering a map or using ladders between floors.
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.
- **Strength Push Mechanics:** The push is executed from an adjacent tile, and only the boulder moves.

# IV. Battle Intelligence
## A. Type Effectiveness Chart (OBSERVATION-ONLY)
- **Super Effective (2x damage):**
  - Electric > Flying, Water
  - Water > Rock/Ground, Fire
  - Ground > Rock/Ground, Fire, Electric, Rock
  - Ice > Ground, Grass, Flying, Dragon
  - Flying > Fighting, Grass, Bug
  - Fighting > Normal, Rock, Ice
- **Not Very Effective (0.5x damage):**
  - Normal !> Rock/Ground, Rock
- **Immune (0x damage):**
  - Ground immune to Electric
  - Flying immune to Ground

## B. Strategic Notes & Mechanics
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Struggle Mechanic:** Used automatically only when a Pokémon is out of PP for ALL moves.
- **Full Heal:** Cures status conditions only, does not restore HP.
- **Body Slam:** Can cause paralysis.

# V. Methodology & Lessons Learned
- **Hypothesis-Driven Approach:** I must form a single, testable hypothesis, document it, test it, and record the conclusion. This avoids chaotic, assumption-driven actions.
- **Tool Reliability & Immediate Action:** A tool that produces an incorrect or impossible result is a critical failure. I MUST fix it immediately with `define_tool` instead of deferring the task or attempting workarounds. I must be more meticulous in my debugging process.
- **Trust System Over Custom Analysis:** If a tool reports 'no path found', my first action must be to verify the destination is reachable (e.g., using `landmass_analyzer`) before assuming the tool is flawed. This prevents wasting time debugging a correct tool when my own assumption about the map is wrong.
- **Falsify Assumptions:** I must actively try to disprove my own hypotheses, especially regarding navigation. This helps avoid confirmation bias.
- **Agent Deletion:** The `puzzle_strategist_agent` was deemed fundamentally flawed for complex, multi-level puzzles and was deleted. Manual puzzle solving using my reliable `landmass_analyzer` and `generate_path_plan` tools is the current, more effective mandate.
- **Judicious Agent Use:** I must exercise my own judgment for simple, obvious situations (like trivial wild battles) and avoid calling agents unnecessarily. The agent is a tool for complex strategic analysis, not a replacement for basic game sense.

# VI. Current Strategy & Plans
- **Objective:** Travel to the Indigo Plateau and challenge the Elite Four.
- **Plan:** Navigate from Viridian City through Route 22, Route 23, and Victory Road.

# VII. HM/Field Move Mechanics
- **Surf Mechanic:** To use Surf from a land tile, the player must be standing on a tile adjacent to the water AND be facing the water tile.

# VIII. Methodology Addendum (Post-Critique Turn 131192)
- **Route 23 Tool Failure Analysis:** The Overwatch critique correctly identified my failure to trust the `generate_path_plan` tool. The tool reported "no path found" because the guards are impassable objects, and I was trying to path *through* them. My conclusion that the tool was broken was incorrect; the tool was functioning perfectly. I wasted significant time on manual navigation as a result.
- **Reinforced Mandate:** I must adhere to my own documented rule: "Trust System Over Custom Analysis." If a pathfinding tool fails, my first action is to analyze the map for physical obstacles, not to question the tool's validity.
- **Agent Usage Correction:** I also incorrectly used the `battle_strategist_agent` for a trivial wild battle (Lv 4 Mankey). This is an inefficient use of resources. I will exercise better judgment and handle such simple encounters manually, reserving the agent for complex or significant battles.