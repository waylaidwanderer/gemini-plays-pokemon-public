# Gem's Strategic Plan & Learnings

## 1. Tactical Protocols
*   **Pre-Adventure Checklist:** Before major undertakings (new route, dungeon, gym), use `pre_adventure_checker_agent` to assess party status. TRUST THE RESULTS.
*   **Trainer Scouting:** Mark defeated trainers on the map IMMEDIATELY after battle to avoid confusion.
*   **Pathfinding:** For complex areas or when navigating around multiple obstacles, use the `pathfinding_agent` to plot an efficient course. Don't just wing it.

## 2. Key Learnings & Verified Mechanics
*   **Poison Damage:** 1 HP per 4 steps outside of battle.
*   **BITE Move:** Is a Normal-type move.
*   **Defeated Trainers:** They still function as solid, impassable obstacles.
*   **Location Verification:** ALWAYS trust the Game State Information for current location, not memory, to avoid hallucinations.

## 3. World Clues & Objectives
*   Team Rocket is at **Mt. Moon**.
*   Moon Stones are found in **Mt. Moon**.
*   The eastern road from Pewter is blocked. The path to Cerulean City is likely through Mt. Moon.

## 4. Active Hypotheses
*   **Hypothesis:** The path forward to Cerulean City is through Mt. Moon, which is at the end of Route 3.
    *   **Test:** Clear Route 3 and see if it leads to the Mt. Moon entrance.

## 5. Failed Hypotheses & Corrected Assumptions
*   **Unreachable Trainer (Route 3):** The Youngster at (23, 10) is in a separate, inaccessible area. Wasted ~5 turns attempting to reach him. **Correction:** Must analyze map layout more carefully before committing to a path.

## 1. Tactical Protocols (Updated)
*   **Agent Management:** Maintain a maximum of 9 active agents to leave one slot open for creating new, specialized agents as needed. Regularly review and delete less useful agents.