# I. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.
- **Follower Pokémon Mechanics:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions. The first button press turns to face, the second moves.

# II. Tile Mechanics (Verified)
- `ground`: Walkable tile.
- `grass`: Tall grass where wild Pokémon appear. Walkable like `ground`.
- `elevated_ground`: Walkable ground at a higher elevation. Movement to/from `ground` tiles requires `steps` or a one-way `ledge` drop.
- **One-Way Drop:** It is possible to drop down from an `elevated_ground` tile to an adjacent `ground` tile.
- `cleared_boulder_barrier`: A tile that becomes traversable after a boulder switch is activated. Acts like `elevated_ground` and can function as a one-way ramp up.
- `steps`: Connects `ground` and `elevated_ground` tiles, allowing vertical movement between them.
- `ledge`: Can only be traversed downwards from an adjacent tile above it.
- `water`: Crossable using HM Surf.
- `impassable`: Walls, rocks, statues, and sometimes objects like defeated trainers. Cannot be entered.
- `ladder_down` / `ladder_up`: Warps between floors.
- `hole`: Warps the player (or a boulder) to the floor below.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `warp`: A tile that transports the player to another location, often a door or cave entrance.

# III. Puzzle Mechanics & Solutions
- **Reset Condition:** Boulder puzzles reset upon leaving and re-entering a map or using ladders between floors.
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.
- **Strength Push Mechanics:** The push is executed from an adjacent tile, and only the boulder moves.

# IV. Battle Intelligence
## A. Type Effectiveness Chart (OBSERVATION-ONLY)
- **Super Effective (2x damage):**
  - Electric > Flying, Water, Rock/Ground
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
- **Tool Reliability & Immediate Action:** A tool that produces an incorrect or impossible result is a critical failure. I MUST fix it immediately with `define_tool` instead of deferring the task or attempting workarounds. This is a non-negotiable directive.
- **Trust System Over Custom Analysis:** If the system validation check insists a path is reachable while my own analysis suggests it is not, the system is correct and my analysis is flawed. The immediate priority becomes re-evaluating my understanding of the map.
- **Falsify Assumptions:** I must actively try to disprove my own hypotheses, especially regarding navigation. If a path fails, I should use tools like `landmass_analyzer` to verify connectivity before repeatedly attempting the same path. This helps avoid confirmation bias where I assume my tool is wrong instead of my assumption.

# VI. Current Strategy & Plans
## A. Route 23 Blockage
- **Goal:** Get past the guard at (5, 36) to enter Victory Road.
- **Status:** Stuck. The guard has given dialogue indicating passage is allowed, but remains physically blocking the path.
- **Hypotheses Tested & Failed:**
  1.  **Hypothesis:** The guard will move after the dialogue completes. **Result:** Failed. (Attempted 5+ times)
  2.  **Hypothesis:** Re-interacting with other guards on the route will trigger a flag. **Result:** Failed. (Re-interacted with guard at (11, 57) with no effect).
  3.  **Hypothesis:** My `pathfinder` tool can find a way around. **Result:** Failed. The tool is bugged on this map.
- **Current Hypothesis:** The map's script state is bugged. Forcing a full map reload by using Fly to leave and return may reset the guard's position/script.
- **Plan:**
  1. Use Fly to travel to any other city.
  2. Immediately use Fly to return to Route 23.
  3. Navigate back to the guard at (5, 36) and attempt to pass.

## B. Victory Road Plan
- **Objective:** Navigate Victory Road to reach the Indigo Plateau.
- **Strategy:** The cave is a series of boulder puzzles. I will use my `puzzle_strategist_agent` at the first opportunity to solve them, as per the Overwatch critique. I must document each puzzle's solution in my notepad.