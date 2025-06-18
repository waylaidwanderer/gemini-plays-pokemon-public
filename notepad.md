# Gem's Strategic Journal

## I. Core Principles & Lessons Learned
- **Trust the GameStatus:** My location is defined by the `GameStatus`, not my assumptions. I must verify map changes before documenting them.
- **Strategic Prioritization:** After a major story event unlocks the main path, pursue it immediately. Don't get sidetracked by minor, optional exploration unless truly stuck.
- **Execution Over Complexity:** Abandon multi-input commands. Break down actions into simple, single-button presses per turn.
- **Effective Training Protocol:** 'Bait-and-switch' is the correct method for training weaker Pokémon.
- **Trust but Verify Agents:** Trust agent *logic* but adapt the *execution* of their plans into reliable, sequential steps.
- **Systematic Exploration (Contextual):** Prioritize exploring reachable unseen tiles *when stuck*, not when the main path is clear.
- **Mark Everything:** Diligently mark defeated trainers, used warps, and key locations.

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

## III. Active Objectives
- **Primary Objective:** Get the S.S. Ticket from Bill to access the S.S. Anne in Vermilion City and challenge Lt. Surge for the Thunder Badge.
- **Secondary Objective:** Traverse the Underground Path to reach Route 6.

## IV. Agent Development Log
- **`battle_menu_navigator`:** Created and refined. Crucial for efficient battle menu navigation.
- **`unseen_tile_navigator_agent`:** Proven reliable for overworld navigation. Use strategically when stuck.
- **`pathfinder_agent`:** Refined to ensure output stability. Must be re-verified on next use.
- **`move_tutor_advisor`:** Created. Ready for use when a new TM is acquired.

## V. Progression Summary
- **Badges:** Boulder Badge (Brock), Cascade Badge (Misty).
- **Mt. Moon:** Cleared Team Rocket, chose the Dome Fossil.
- **Cerulean City:** Defeated rival Pixel. Discovered the path to Bill's house is north.
- **Nugget Bridge (Route 24):** All trainers defeated. Received a Charmander (IGNIS).
- **Route 25:** Cleared trainers and helped Bill at his Sea Cottage, obtaining the S.S. TICKET.