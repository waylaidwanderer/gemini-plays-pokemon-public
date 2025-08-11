# I. Game World Rules
## A. Traversal & Tile Mechanics
- `ground` / `grass`: Standard walkable tiles.
- `impassable` / `unknown`: Cannot be entered.
- `ledge`: A one-way drop. Can be jumped down from an adjacent higher tile, but not climbed up.
- `steps`: Allows vertical movement between `ground` and `elevated_ground`.
- `elevated_ground`: Walkable ground at a different elevation. Movement to/from `ground` is ONLY possible via `steps` tiles or by a one-way drop from `elevated_ground` down to `ground`.
- `ladder_up` / `ladder_down` / `warp`: Warps between maps or floors.

## B. Puzzle Mechanics
- **Boulder Pushing:**
  - **Vertical Push:** Pushing a boulder vertically (Up/Down) moves the boulder but does NOT move the player.
  - **Horizontal Push:** Pushing a boulder horizontally (Left/Right), whether adjacent or from one tile away, moves the boulder but does NOT move the player.
- **Remote Push:** It is possible to push a boulder when standing one tile away from it. The player's position does not change.
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.
- **Reset Condition:** Boulder puzzles reset upon leaving and re-entering a map or using ladders between floors.
- **`boulder_switch`:** A floor switch that must have a boulder pushed onto it.
- **`boulder_barrier`:** An impassable wall that is removed when a corresponding `boulder_switch` is activated. State does not update until visible on-screen.
- **`cleared_boulder_barrier`:** Acts as ground. Can sometimes function as a one-way ramp up from `ground` to `elevated_ground`.

## C. General Mechanics
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** A fainted Pokémon can be selected to use a field move like Strength.
- **Pikachu Interaction:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions. The first button press turns to face, the second moves.
- **Dig Field Move:** Can be used to escape caves, acting as an Escape Rope.
- **Surf Mechanic:** To use Surf, the player must be standing on a tile adjacent to the water AND be facing the water tile.

# II. Battle Intelligence
## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x damage):**
  - Water > Rock, Ground, Fire
  - Ground > Fire, Electric, Rock, Ground
  - Ice > Ground, Grass, Flying, Dragon
  - Flying > Fighting, Grass, Bug
  - Fighting > Normal, Rock, Ice
  - Electric > Water, Flying
- **Not Very Effective (0.5x damage):**
  - Normal !> Rock
- **Immune (0x damage):**
  - Ground immune to Electric
  - Flying immune to Ground

## B. Strategic Notes
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Body Slam:** Can cause paralysis.

# III. My Methodology
## A. Core Principles
- **IMMEDIATE ACTION IS PARAMOUNT:** My thinking only occurs when processing a turn. A broken tool, a flawed strategy, or a needed agent is a critical failure that must be addressed in the *current* turn. I am forbidden from deferring tasks to a "later" that will never come. Fixing my own capabilities is always the highest priority, above any gameplay objective.
- **Hypothesis-Driven Approach:** I must form a single, testable hypothesis, document it, test it, and record the conclusion. I must actively try to disprove my own conclusions to avoid confirmation bias.

## B. System Interaction Notes
- **TRUST THE SYSTEM OVER MY TOOLS:** System warnings (like 'Dead End Area Mismatch') are the ultimate source of truth. If a system warning contradicts the output of my tools, I MUST assume my tools are bugged and prioritize fixing them over any other action. My own observations can also be flawed by hallucination; the system is the final arbiter.
- **Validation Check Discrepancy:** The system's validation for reachable warps appears to ignore movable obstacles like boulders. This can create a false positive, indicating a path is clear when it is actually blocked. My own tools (`landmass_analyzer`, `generate_path_plan`) provide a more accurate ground truth in these situations, but ONLY if they are not bugged.

## C. Tool Trust Protocol
- If a pathfinding tool reports "no path found," my first assumption must be that the map is physically impassable, not that the tool is broken. I must use `landmass_analyzer` to verify connectivity before attempting to debug the pathfinder. This protocol is superseded by the rule to trust system warnings.

# IV. Active Strategy: Road to the Indigo Plateau
- **Current Objective:** Navigate through Victory Road to reach the Indigo Plateau and challenge the Elite Four.
- **Immediate Plan:** After getting trapped in Victory Road 1F, I used Dig to reset the puzzle. I am now back in Viridian City and will return to Victory Road 1F to re-attempt the boulder puzzles with my newly fixed tools and a fresh perspective.

# V. Identified Development Needs
- **Agent Opportunity:** `puzzle_strategist_agent`. Input: `boulder_puzzle_assistant` output, current map state, goal coordinates. Action: Devises a step-by-step sequence of boulder pushes to achieve the goal. This would automate the complex reasoning I'm currently doing manually.
- **Tool Capability Need:** My pathfinding tools now have an `assume_barriers_open` parameter to handle off-screen state changes. This was a critical fix identified during self-assessment.

# VI. Methodological Corrections & Lessons Learned
- **Tool Failure (Victory Road 1F):** My `generate_path_plan` and `landmass_analyzer` tools failed to correctly identify a valid path on Victory Road 1F, leading me to hallucinate that I was soft-locked. The system's `Dead End Area Mismatch` warning confirmed that reachable exits existed. **Conclusion:** My tools had a critical bug in how they handle elevation changes and off-screen state. I have now fixed them. This was a major failure in trusting my tools over the system's ground truth.
- **Confirmation Bias (Victory Road 1F):** I incorrectly assumed the western boulder puzzle solution in my notepad was the *complete* solution. I wasted dozens of turns trying to force a path that didn't exist instead of re-evaluating the entire puzzle. **Conclusion:** I must treat my own notes as hypotheses to be tested, not infallible law. I need to be more willing to abandon a flawed plan.
- **Deferred Action (Tool Fixing):** I repeatedly deferred fixing my `generate_path_plan` tool, opting for inefficient manual navigation instead of addressing the root problem. This violates the 'IMMEDIATE ACTION IS PARAMOUNT' directive. Broken tools must be fixed immediately.
- **Tool Unreliability (Off-Screen State):** The Overwatch critique correctly identified that my tools are failing because they cannot account for off-screen state changes (e.g., a barrier opening). Trusting them over system warnings led to a repetitive loop. **Conclusion:** For complex puzzles, I must manually test hypotheses when my tools contradict the system. The `assume_barriers_open` parameter is the first step in addressing this.