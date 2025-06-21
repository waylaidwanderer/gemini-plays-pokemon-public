# Gem's Strategic Journal (v9.0)

## I. Core Principles & Lessons Learned
- **Progression Over Perfection:** The critical path is key. Do not get bogged down in tool refinement if it halts game progress. A working-but-imperfect tool is better than no progress.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Trust but Verify:** Trust agent outputs, but verify their performance with simple, non-critical tests before relying on them for major tasks.

## II. Game Mechanics & Battle Intel
- **Level Caps:**
    - 0 badges: 12
    - 1 badge: 21
    - 2 badges: 24
    - 3 badges: 35
- **HM Usage:** A fainted POKéMON can still use field moves like CUT.
- **Type Matchups (Verified):**
    - Flying: Super-effective (2x) vs. Ground.
- **Move Compatibility (CRITICAL DISCOVERY):** Pokémon move compatibility in this ROM hack differs from standard games. **SUBTERRA (Diglett) cannot learn HM05 Flash**. PULSAR (Magnemite) was able to learn it. I must always trust the in-game 'ABLE'/'NOT ABLE' feedback.
- **Pokémon Evolutions:**
    - ECHO (Zubat) evolved into Golbat at Lv. 22.
- **New Moves Learned:**
    - ECHO (Golbat) learned Wing Attack, replacing Leech Life.
    - PULSAR (Magnemite) learned Flash, replacing Tackle.
- **Trainer Battle Initiation:** Some trainers require manual interaction.
- **Navigation Obstacle:** Defeated trainers act as impassable objects.
- **EXP. All Mechanics (Verified):** EXP is distributed to all non-fainted party Pokémon.

## III. World Intel & Navigation
- **CRITICAL NAVIGATION LESSON:** Route 2 is segmented. The Diglett's Cave exit at (13, 11) leads to a small, isolated northern section. Do not use Diglett's Cave as a shortcut to Viridian Forest.
- **Lt. Surge's Raichu (Lv. 29):** Knows Body Slam and Surf.
- **Recurring Obstacles:** The tree at (16, 19) in Vermilion City and the tree at (16, 23) on Route 2 respawn.
- **Route 11 Gatehouse Split:** The gatehouse east of Route 11 is divided. The west entrance leads to a small room with no access to the eastern section where a guard blocks the path.
- **Item Discovery:** Found a MOON STONE on Route 2 (south section). Can be used to evolve LUNA (Clefairy) or SPIKE (Nidoran♂).
- **Underground Path Item Hint (DEBUNKED):** A girl in the Route 6 gatehouse mentioned a lost item. This has been fully investigated and was a dead end.
- **Route 11 East Blockage (Assumption):** I assume a Snorlax blocks the path east of the Route 11 gatehouse, but I haven't confirmed this visually.

## IV. Agent & Tool Strategy
- **Consolidated Navigation:** Deleted `pathfinder_agent` and `cluster_explorer_agent`. Replaced with a single `route_navigator_agent` to be the sole source of truth for pathfinding.
- **Battle Advisor (FIXED):** The `battle_move_advisor_agent`'s prompt has been updated to correctly calculate multiplicative damage for dual-type Pokémon (e.g., 4x weakness).
- **Evolution Advisor (Defined):** Created `pokemon_evolution_advisor` to analyze the roster and suggest optimal evolution timings based on level caps and move learning. Untested.
- **Healing Advisor (Defined):** Created `healing_advisor_agent` to provide data-driven healing recommendations. Untested.
- **Proactive Testing Mandate:** After defining or significantly refining an agent, I MUST devise a simple, non-critical test case to validate its functionality before relying on it for progression-critical tasks.

## V. Future Agent Development
- **Trainer Hunter Agent (Rebuild):** The original was unreliable. Plan to build a new one with a robust prompt that forces it to correctly parse sprite types and cross-reference with '☠️' markers from the map XML.
- **TM Usage Advisor:** To recommend the best TM allocations across my party and PC, considering current movesets and type coverage.

- **Route Navigator (Rebuild):** The current agent's pathfinding is flawed; it generated a route leading into an impassable tile (25, 13) on Route 9. Needs to be rebuilt with better obstacle validation.