# Gem's Strategic Journal

## I. Core Principles & Lessons Learned
- **The `GameStatus` is the only source of truth.** All actions must be based on confirmed map data, not assumptions or memory. Verify map changes *before* documenting.
- **Trust but Verify Agents:** Trust agent *logic* but adapt the *execution* of their plans into reliable, sequential steps.
- **Systematic Exploration (Contextual):** Prioritize exploring reachable unseen tiles *when stuck*, not when the main path is clear.
- **Mark Everything:** Diligently mark defeated trainers, used warps, and key locations.
- **Strategic Prioritization:** After a major story event unlocks the main path, pursue it immediately.
- **Execution Over Complexity:** Abandon multi-input commands. Break down actions into simple, single-button presses per turn.

## II. Game Mechanics & Battle Intel
- **Type Matchups (Verified):**
    - Grass is 4x effective vs. Rock/Ground.
    - Electric is not very effective vs. Electric or Bug/Grass (Paras).
    - Ice is super-effective vs. Grass.
- **Status Effects:**
    - Confusion wears off after battle.
    - Poison-types are immune to poison.
- **EXP Distribution:**
    - Pokémon at the level cap do not gain EXP.
    - All non-fainted party members share EXP.

## III. Agent Development Log
- **`battle_menu_navigator`:** Created. For efficient battle menu navigation.
- **`unseen_tile_navigator_agent`:** Reliable for overworld navigation when stuck.
- **`pathfinder_agent`:** Refined to ensure output stability. Must be re-verified on next use.
- **`move_tutor_advisor`:** Created. Ready for use when a new TM is acquired.