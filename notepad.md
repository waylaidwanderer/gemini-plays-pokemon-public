# Gem's Gameplay Journal

## I. Strategic Principles
- **Trust The Game State:** The provided game state data (`reachable` flags, etc.) is the ultimate source of truth.
- **Systematic Navigation:** Use agents for complex paths; use short, verifiable moves for simple repositions.
- **NPCs are Walls:** Treat all non-player sprites (except Pikachu) as impassable obstacles.
- **Two-Strikes Rule:** If a path or interaction fails twice, re-evaluate assumptions before trying a third time.
- **Mark Everything:** Immediately mark defeated trainers, used warps, dead ends, and important discoveries to build a reliable mental map.

## II. Game Mechanics & Battle Intel
- **Type Matchups (Verified):**
    - Grass is 4x effective vs. Rock/Ground (e.g., Geodude).
    - Electric-type moves are 'not very effective' against Electric-type Pokémon.
    - Electric-type moves are 'not very effective' against Paras (Bug/Grass).
- **Status Effects:**
    - Confusion wears off after battle.
    - Poison-type Pokémon are immune to being poisoned.
- **EXP Distribution:**
    - EXP is shared only with Pokémon in the party when the final opponent faints.
    - Pokémon at the level cap do not gain EXP, even if the message appears.

## III. Active Hypotheses & Exploration Strategy
- **H1: Cerulean Gym Access:** The gym is blocked by a Super Nerd at (5, 13). The intended path is likely through the eastern part of the city, possibly through the burgled house at (28, 12). (Status: **Active Exploration Target**)
- **H2: Bill's Cottage Path:** The eastern part of Route 24 seems to be a separate, dead-end area, making Bill's Cottage inaccessible for now. Must clear Cerulean Gym first. (Status: **Blocked, Progression Paused**)
- **H3: Melanie's Bulbasaur:** Melanie won't give me the Bulbasaur yet. Requires a different story trigger. (Status: **Blocked, Low Priority**)
- **H4: Wild Pokémon Movesets:** Wild Pokémon of the same species may have different movesets. (Status: **Unverified**)

## IV. Agent Development Log
- **`unseen_tile_navigator_agent` & `pathfinder_agent`:** Refined and reliable for navigating around objects and ledges.
- **`pokedex_gap_analyzer_agent`:** Tested and verified. Correctly identified Water/Psychic/Ghost type gaps.
- **`battle_strategist_agent` & `battle_switch_agent`:** Verified as reliable.
- **`gym_gauntlet_planner_agent`:** Newly created. Needs testing for the Cerulean Gym.
- **`building_identifier_agent`:** Untested.