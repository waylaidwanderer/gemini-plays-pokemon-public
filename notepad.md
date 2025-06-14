# Gem's Strategic Plan & Learnings

## 1. Core Protocols
*   **Pre-Adventure Checklist:** Before major undertakings, use `pre_adventure_checker_agent`.
*   **Trainer Scouting:** Mark defeated trainers on the map IMMEDIATELY.
*   **Pathfinding:** For complex areas, use `pathfinding_agent` or `exploration_helper_agent` to plot a course and FOLLOW IT.
*   **Agent Management:** Keep one agent slot open for flexibility.

## 2. Key Learnings & Mechanics
*   **Poison Damage:** 1 HP per 4 steps outside of battle.
*   **BITE Move:** Normal-type.
*   **Defeated Trainers:** They are NOT solid obstacles. They can be walked past. My previous assumption was a major hallucination that cost me over 75 turns.
*   **Location Verification:** Trust Game State Information (e.g., 'Reachable: Yes') over personal assumptions or even agent outputs. If the game says a path exists, it does.
*   **Building Entrances:** Standard building entrances are warps triggered by walking INTO the impassable door tile.

## 3. World Clues & Objectives
*   Team Rocket is at **Mt. Moon**.
*   Moon Stones are found in **Mt. Moon**.
*   The path to Cerulean City is likely through Mt. Moon.

## 4. Active Hypotheses
*   **Hypothesis:** The Mt. Moon entrance is at the east end of Route 3.
    *   **Test:** Navigate to the eastern exit of Route 3.

## 5. Immediate Tasks
*   Heal the party at the Pewter City Pokémon Center.

## 6. Major Blunders & Resets
*   **Route 3 Hallucination (Turns ~4366-4440):** I incorrectly concluded that defeated trainers were impassable obstacles, trapping me on the eastern side of Route 3. This was a complete hallucination, as the Game State consistently indicated the path to Pewter City was reachable. This led to a ~75 turn loop of failed exploration and near party-wipe. **Lesson:** Always trust the game's ground truth data over personal assumptions. Defeated trainers do not block the path.