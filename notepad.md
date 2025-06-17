# Gem's Gameplay Journal

## I. Strategic Principles
- **Trust The Game State:** The provided game state data (`map_id`, `reachable` flags) is the ultimate source of truth. Always verify location before making a plan.
- **Systematic Navigation:** Use agents for complex paths; use short, verifiable moves for simple repositions. Cross-reference agent output with game state.
- **NPCs are Walls:** Treat all non-player sprites (except Pikachu) as impassable obstacles.
- **Two-Strikes Rule:** If a path or interaction fails twice, re-evaluate assumptions before trying a third time.
- **Mark Everything:** Immediately mark defeated trainers, used warps, dead ends, and important discoveries to build a reliable mental map.

## II. Game Mechanics & Battle Intel
- **Type Matchups (Verified):**
    - Grass is 4x effective vs. Rock/Ground (e.g., Geodude).
    - Electric-type moves are 'not very effective' against Electric-type Pokémon and Paras (Bug/Grass).
    - Ice-type moves (like Aurora Beam) are super-effective against Grass-types.
- **Status Effects:**
    - Confusion wears off after battle.
    - Poison-type Pokémon are immune to being poisoned.
- **EXP Distribution:**
    - Pokémon at the level cap do not gain EXP, even if the message appears.

## III. Active Hypotheses & Exploration Strategy
- **H1: Cerulean Gym Strategy:** Misty's team likely has coverage moves (e.g., Ice-type). A pure type-advantage approach is risky. I must use my `gym_gauntlet_planner_agent` to create a comprehensive plan before re-challenging the gym. (Status: **Active Planning Target**)
- **H2: Bill's Cottage Path:** The western access on Route 24 is a dead end. The correct path is likely east of Cerulean City, which is currently blocked by a police officer. This path will probably open after defeating Misty. (Status: **Blocked, Post-Gym Goal**)
- **H3: Melanie's Bulbasaur:** Melanie won't give me the Bulbasaur yet. This likely requires a different story trigger, possibly post-Misty. (Status: **Blocked, Low Priority**)

## IV. Agent Development Log
- **`unseen_tile_navigator_agent` & `pathfinder_agent`:** Refined multiple times to handle ledges and obstacles more accurately. They seem reliable now but require continued vigilance.
- **`pokedex_gap_analyzer_agent`:** Tested and verified. Correctly identified Water/Psychic/Ghost type gaps.
- **`battle_strategist_agent` & `battle_switch_agent`:** Verified as reliable.
- **`gym_gauntlet_planner_agent`:** Newly created. Must be used to plan the rest of the Cerulean Gym, especially the battle with Misty.