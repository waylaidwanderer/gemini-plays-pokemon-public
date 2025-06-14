# Gem's Strategic Plan & Learnings

## 1. Core Protocols
*   **Pre-Adventure Checklist:** Before major undertakings, use `pre_adventure_checker_agent`.
*   **Trainer Scouting:** Mark defeated trainers on the map IMMEDIATELY.
*   **Pathfinding:** Use `pathfinding_agent` cautiously. Always verify its paths, especially around ledges.
*   **Agent Management:** Keep one agent slot open for flexibility.

## 2. Key Learnings & Mechanics
*   **Poison Damage:** 1 HP per 4 steps outside of battle.
*   **BITE Move:** Normal-type.
*   **Defeated Trainers:** The rule for whether defeated trainers are obstacles is complex. Some can be walked past, while others (like the Cool Trainer F at (17, 10) on Route 3) still block movement. Evaluate each case individually.
*   **Building Entrances:** Standard building entrances are warps triggered by walking INTO the impassable door tile.
*   **Route 3 Navigation:** The northern section is a one-way path of ledges leading west. The southern section must be used to travel east.

## 3. World Clues & Objectives
*   Team Rocket is at **Mt. Moon**.
*   Moon Stones are found in **Mt. Moon**.
*   The path to Cerulean City is likely through Mt. Moon.

## 4. Active Hypotheses
*   **Hypothesis:** The Mt. Moon entrance is at the east end of Route 3. **Test:** Navigate to the eastern exit of Route 3.
*   **Hypothesis:** The Youngster at (23, 10) is reachable from the southern path. **Test:** Attempt to move north to his position.

## 5. Immediate Tasks
*   Fully explore Route 3 to find the entrance to Mt. Moon.

## 6. Strategy Refinements (Post-Critique)
*   **Agent Usage:** The `pathfinding_agent` is unreliable on complex maps with ledges. Do not use it for navigation in these areas. I need to be more self-reliant.
*   **Exploration Method:** When the game state shows `Reachable Unseen Tiles`, a path forward EXISTS. I must explore systematically and not assume I'm trapped.
*   **Tool Utilization:** I have a `type_chart_lookup_agent` that I haven't been using. I should use it to strategize for trainer battles to conserve resources.
*   **Learning Integration:** I need to actively apply the lessons recorded in this notepad to my gameplay, not just document failures.