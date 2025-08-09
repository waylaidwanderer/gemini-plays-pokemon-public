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
  - Ground > Fire, Electric (Note: Effectiveness vs Rock-types is complex; neutral against Rock/Ground)
  - Ice > Ground, Grass, Flying, Dragon
  - Flying > Fighting, Grass, Bug
  - Fighting > Normal, Rock, Ice
- **Not Very Effective (0.5x damage):**
  - Normal !> Rock
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
- **Trust System Over Custom Analysis:** If a pathfinding tool reports 'no path found', my first action MUST be to analyze the map for physical obstacles using a tool like `landmass_analyzer`, not to question the tool's validity. This prevents wasting time debugging a correct tool when my own assumption about the map is wrong.
- **Falsify Assumptions:** I must actively try to disprove my own hypotheses, especially regarding navigation. This helps avoid confirmation bias.
- **Judicious Agent Use:** I must exercise my own judgment for simple, obvious situations (like trivial wild battles) and avoid calling agents unnecessarily. The agent is a tool for complex strategic analysis, not a replacement for basic game sense.
- **Victory Road 1F Failure Analysis:** My pathfinding tools and agents were not broken. They correctly reported that no path existed to the boulder puzzle on the other side of the map. My core assumption that the map was a single connected area was wrong. I wasted dozens of turns trying to fix tools that were working perfectly. This is a critical lesson in trusting my tools and questioning my own assumptions first.
- **Reinforced Mandate:** If a pathfinding tool fails, my first action is to use `landmass_analyzer` to verify the path is possible before attempting any debugging.
- **Agent Usage Correction:** I also incorrectly used the `battle_strategist_agent` for a trivial wild battle (Lv 4 Mankey). This is an inefficient use of resources. I will exercise better judgment and handle such simple encounters manually, reserving the agent for complex or significant battles.

# VI. HM/Field Move Mechanics
- **Surf Mechanic:** To use Surf from a land tile, the player must be standing on a tile adjacent to the water AND be facing the water tile.

# VII. Tool Development & Limitations
- **Future Goal: Multi-Modal Pathfinding:** My current `generate_path_plan` tool can only handle a single mode of transit (walking or surfing). For complex maps like Route 23 that require both, I must manually break the journey into segments. A future goal is to develop a more advanced tool that can automatically plan these multi-modal routes.
- **`landmass_analyzer` Limitation:** This tool determines connectivity based on terrain type alone and does not account for impassable NPCs. This can lead to it reporting that two areas are connected when, in practice, an NPC blocks the path, as seen on Route 23.

# VIII. Future Improvements & Data Gathering
- **Type Chart Granularity:** The current type chart sometimes conflates single and dual-type effectiveness (e.g., Ground vs Rock/Ground). I need to be more diligent in observing and recording matchups against single-type Pokémon to build a more precise and reliable chart.

# Victory Road 1F Active Hypothesis
- **Hypothesis:** Pushing the boulder from (6, 16) to (6, 15) has made the puzzle unsolvable by blocking the steps. I must reset the puzzle by leaving and re-entering the map.
  - **Status:** In progress. Planning to navigate to the exit warp.