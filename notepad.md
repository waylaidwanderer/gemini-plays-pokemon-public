# I. Game Mechanics & Traversal
## A. Core Rules
- **Level Cap:** 8 badges = Level 65.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- Puzzle Resets: The ladder between Victory Road 1F and 2F does NOT reset the boulder puzzle. Hypothesis: Leaving Victory Road entirely might be required to reset it.
- **Off-Screen State Changes:** An object's state will not update in the map data until it is visible on-screen.
- **Boulder Pushing:** A boulder can be pushed from an adjacent tile by facing it and walking into it. Pressing 'A' does not work.

## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall. Defeated trainers on Victory Road 1F & 2F are impassable obstacles (re-verified for 1F).
- `ledge`: One-way traversal. Can only be jumped DOWN from the tile directly above. Acts as a wall from all other directions.
- `elevated_ground`: Walkable, different elevation. It is NOT possible to step down from an `elevated_ground` tile to an adjacent `ground` tile.
- `steps`: Allows movement between `ground` and `elevated_ground` in both directions.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `cleared_boulder_barrier`: A former barrier that acts as a ramp (elevation 1). It connects to other tiles of the same or adjacent elevation. It is NOT possible to step directly down from it to a `ground` tile (elevation 0), nor is it possible to step UP from `ground` onto it.
- `hole`: Drops to a lower floor. Pushing a boulder into one causes it to appear on the floor below.
- `spinner`: Forces movement.
- `cuttable`: A tree that can be removed with the HM Cut.
- `ladder_up`: Warps to a higher floor.
- `ladder_down`: Warps to a lower floor.

# II. Battle Intel
## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock, Ground; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting
- **Correction:** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon.

## B. Strategic Notes
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Struggle Mechanic:** Struggle is only used automatically when a Pokémon is out of PP for ALL of its moves.
- **Full Heal Mechanic:** This item ONLY cures status conditions. It does NOT restore HP.

# III. Core Principles & Methodology
- **Agent-First Approach:** Before attempting any manual solution for a complex problem (puzzles, multi-step navigation, difficult battles), I MUST consult the relevant specialist agent first (`puzzle_strategist_agent`, `battle_strategist_agent`, etc.).
- **Scientific Method:** Use a scientific approach: form a hypothesis, test it, and document the conclusion. Do not modify tools to test hypotheses; test them with in-game actions first.
- **Trust System Feedback:** System feedback (like validation warnings or tool errors) is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **IMMEDIATE ACTION:** Flaws in tools or data management (notepad, markers) must be addressed immediately, not deferred as goals.

# IV. Archived Lessons & Puzzle Solutions

## Victory Road 2F - Western Boulder
- **Hypothesis #1 (Original):** Push boulder at (5, 15) south to (5, 17), then left to switch at (2, 17).
- **Test:** Pushed boulder to (5, 17).
- **Conclusion:** FAILED. Could not access (6, 17) to push left. Boulder was trapped.
- **Hypothesis #2:** Push boulder at (6, 15) left to (5, 15), then down to (5, 17), then left to switch at (2, 17).
- **Test:** Pushed boulder to (2, 17).
- **Conclusion:** SUCCESS. Barrier at (8, 9) and (8, 10) was cleared after visual confirmation.

## Victory Road 2F - Eastern Boulder (Failed Hypotheses)
- **Hypothesis #1 (Push Up):** Push boulder at (6, 6) UP to (6, 5).
- **Test:** Pushed boulder to (6, 5).
- **Conclusion:** FAILED. Path upwards is a dead end. The only way forward is down.
- **Hypothesis #2 (Push Down):** Push boulder at (6, 6) down to (6, 8), then right through the cleared barrier at (8, 9), then down to the switch at (10, 17).
- **Conclusion:** FAILED. Boulder is on `ground` and cannot be pushed up to the `elevated_ground` where the barrier is.
- **Hypothesis #3 (Use other boulder):** Push the boulder at (5, 16) to the switch at (10, 17).
- **Conclusion:** FAILED. Path is blocked by an impassable wall at X=9.

## Victory Road 3F Puzzle
- The `gem_pathfinder_v2` tool repeatedly failed to find a path to the warp at (27, 9). This was initially mistaken for a bug in the A* algorithm. The tool was working correctly; the path was blocked by a boulder I had inadvertently moved into the main corridor. This highlights the importance of careful movement during puzzle-solving to avoid creating new obstacles.

## General Mechanics
- **Boulder Pushing:** When pushing a boulder (horizontally or vertically), the player character does NOT move into the boulder's previous tile. This was observed on Victory Road 1F.

## Victory Road 1F - Elevation Test
- **Hypothesis (from agent):** It is possible to move from `elevated_ground` (e.g., (8, 10)) to an adjacent `ground` tile (e.g., (8, 9)).
- **Test:** Attempted to move Down from (8, 10) to (8, 9).
- **Conclusion:** FAILED. Movement was blocked. This confirms my original note: direct descent from `elevated_ground` to `ground` is impossible. An agent's analysis was flawed.

## Victory Road 2F - Eastern Boulder (New Strategy)
- **System Info:** The western switch puzzle at (2, 17) is already solved.
- **Agent Hypothesis:** Move the southern boulder at (5, 15) to the eastern switch at (10, 17).
- **Sub-Goal 1:** Move boulder from (5, 15) to (10, 17).

## Battle Strategist Agent - Performance Log
- **Agent Failure (Turn 118694):** Agent recommended switching in NEPTUNE (Lv50, 48/208 HP) against a wild GRAVELER (Lv46). Reasoning was that NEPTUNE's superior speed and 4x super-effective STAB SURF would secure a one-hit KO. 
- **Outcome:** FAILED CATASTROPHICALLY. The agent's speed assumption was incorrect. The GRAVELER moved first and used ROCK SLIDE, a super-effective move, which knocked out NEPTUNE before it could act.
- **Conclusion:** The agent's logic was too aggressive and did not adequately weigh the extreme risk of switching in a low-HP Pokémon that also has a type weakness to the opponent's likely STAB moves. The potential for a fast KO does not justify the risk of being out-sped and KO'd.
- **Corrective Action (Turn 118695):** Updated the agent's system prompt with the 'LOW HP & WEAKNESS VETO (ULTRA-CRITICAL)' rule. This rule forbids switching to a Pokémon below 50% HP if it has a weakness to the opponent's likely STAB types, overriding any offensive advantage. This prioritizes survival and safer, more defensive plays.

## Future Agent Ideas
- **Team Management Advisor:** An agent to suggest optimal party compositions and training priorities for major challenges like the Elite Four. It could analyze my available Pokémon (in party and PC) against known opponent rosters to recommend a balanced team and identify which Pokémon to train next.

## Victory Road 2F - Boulder Push Mechanic (Corrected)
- **Hypothesis #1:** The HM Strength must be reactivated from the party menu before each individual boulder push.
- **Test 1:** After a failed push, Strength was reactivated. The next push succeeded.
- **Conclusion 1 (Initial):** The hypothesis seemed correct.
- **Test 2:** A subsequent push was attempted *without* reactivating Strength.
- **Conclusion 2 (Final):** SUCCESS. The boulder moved. The initial hypothesis was **incorrect**. The first failure was likely a positioning error or a one-time glitch. Strength does NOT need to be reactivated for every push.

## Victory Road 2F - Eastern Boulder (Attempt 1 & 2)
- **Hypothesis:** Push the southern boulder at (5, 15) straight across to the east.
- **Test (Attempt 1 & 2):** Pushed boulder from (5, 15) to (8, 16).
- **Conclusion:** FAILED CATASTROPHICALLY (TWICE). The boulder became trapped against the impassable walls at (9, 16) and (8, 17). My pathing assumption was incorrect, and my puzzle agent's original plan was flawed. I must reset the puzzle by leaving and re-entering the floor and then re-consult my *fixed* agent.

## Victory Road 2F - Puzzle Agent Failure
- **Agent Failure (Turn 118753):** The `puzzle_strategist_agent` suggested moving the boulder at (5, 15) to the switch at (10, 17) via a path that included pushing it through an impassable wall at (9, 16).
- **Outcome:** FAILED. Following this flawed plan resulted in the boulder becoming trapped at (8, 16).
- **Conclusion:** The agent's logic was insufficient. It did not properly verify the traversability of the boulder's entire path, only the player's path to the boulder.
- **Corrective Action (Turn 118763):** Updated the agent's system prompt with 'ULTRA-CRITICAL RULE #4'. This new rule explicitly requires the agent to verify that every tile in a boulder's proposed path is traversable, preventing it from suggesting impossible movements.

## Victory Road 2F - Northern Boulder (Attempt 3)
- **Hypothesis:** Pushing the boulder at (6, 6) north is a valid opening move, contrary to the puzzle agent's analysis.
- **Test:** Pushed the boulder from (6, 6) to (6, 5).
- **Conclusion:** FAILED. The boulder is now trapped between impassable walls at (5, 5), (7, 5), and (6, 3). The agent's analysis was correct. The only way forward is to reset the puzzle.