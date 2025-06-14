# Gem's Strategic Plan

## Primary Goal: Defeat Brock (Pewter City Gym)
*   **Current Status:** Not yet in Pewter City.
*   **Path to Pewter:** Must travel through Viridian Forest and then Route 2.
*   **Action Plan:**
    1.  Finish initial training on Route 22 to get key Pokémon to Lv. 12.
    2.  Travel from Viridian City -> Route 2 -> Viridian Forest -> Pewter City.
    3.  Use `pathfinding_agent` for all city/complex route navigation.

## Secondary Goal: Train Party to Level Cap (12)
*   **Priority Pokémon:**
    *   SPROUT (Lv. 11 -> 12) - Key for Brock.
    *   PIP (Lv. 10 -> 12)
    *   THISTLE (Lv. 4 -> 12)
*   **Training Location:** Route 22 (current), then Route 2 / Viridian Forest.

## Tertiary Goal: Fully Explore Route 2
*   **Objective:** Discover all trainers, items, and wild Pokémon on Route 2 to prepare for Pewter City.

## Verified Mechanics & Rules
*   **Pre-Adventure Checklist:** ALWAYS use `pre_adventure_checker_agent` before leaving a town.
*   **Navigation:** Use `pathfinding_agent` for ANY non-trivial navigation to avoid getting lost. It is my responsibility to clear obstacles on the path it provides.
*   **Failed Hypotheses Log:**
    *   Manual navigation in Viridian City is highly inefficient (failed >10 times). Will use `pathfinding_agent` instead.

## Defeated Trainers
*   Bug Catcher (Viridian Forest, (31,34))
*   Cooltrainer F (Viridian Forest, (3,42))
*   Bug Catcher (Viridian Forest, (3,19))
*   Rival BLAZe (Route 22, (30,5))