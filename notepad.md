# Gem's Strategic Plan & Learnings

## 1. Core Protocols
*   **Pre-Adventure Checklist:** Before major undertakings, use `pre_adventure_checker_agent`.
*   **Trainer Scouting:** Mark defeated trainers on the map IMMEDIATELY.
*   **Pathfinding:** For complex areas, use `pathfinding_agent` or `exploration_helper_agent` to plot a course and FOLLOW IT.
*   **Agent Management:** Keep one agent slot open for flexibility.

## 2. Key Learnings & Mechanics
*   **Poison Damage:** 1 HP per 4 steps outside of battle.
*   **BITE Move:** Normal-type.
*   **Defeated Trainers:** They are solid obstacles.
*   **Location Verification:** Trust Game State, not memory.
*   **Route 3 Navigation:** This route is a maze of ledges and one-way paths. Do not assume a path exists without visual confirmation or using a pathfinding agent. Got lost for ~20 turns in the SE corner.

## 3. World Clues & Objectives
*   Team Rocket is at **Mt. Moon**.
*   Moon Stones are found in **Mt. Moon**.
*   The path to Cerulean City is likely through Mt. Moon.

## 4. Active Hypotheses
*   **Hypothesis:** The Mt. Moon entrance is at the east end of Route 3.
    *   **Test:** Navigate to the eastern exit of Route 3.

## 5. Immediate Tasks
*   Find the Pokémon Center at Mt. Moon to heal the party.

## 6. Major Blunders & Resets
*   **Route 3 Maze Failure (Turn ~4300):** Got completely lost in the SE corner after jumping down ledges. This area is a one-way navigational trap. The only solution is to retreat west to the route entrance and take the correct northern path. Do not attempt to find an exit east or north from the southern section. Avoid the lower ledges entirely.

## Major Blunders & Resets
*   **Route 3 Trapped (Turn ~4366):** After defeating several trainers on the upper path of Route 3, I am now trapped. The defeated trainers at (20, 6) and (15, 5) act as impassable objects, blocking the way back west to Pewter City. The pathfinding agent confirmed there is no way back. **Conclusion:** The upper path of Route 3 is a one-way trip eastward. New plan is to proceed east towards Mt. Moon and hope for a Pokémon Center there.