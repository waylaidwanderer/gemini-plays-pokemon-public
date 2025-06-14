# Gem's Strategic Plan & Learnings

## 1. Tactical Protocols
*   **Switch-Training:** For low-level Pokémon, lead with them, then immediately switch to a stronger Pokémon to secure the KO. This guarantees safe EXP.
*   **Pre-Adventure Checklist:** Before entering a new route or dungeon, use `pre_adventure_checker_agent` to assess party HP, PP, and status. Heal at a Pokémon Center if recommended.
*   **Risk Management:** A long, guaranteed route is better than a failed shortcut. Be decisive and commit to a clear path.

## 2. Key Learnings
*   **Game Mechanics Correction:**
    *   Poison damage outside of battle is 1 HP per 4 steps.
    *   BITE is a **Normal-type** move in this generation, not Dark-type.
*   **Navigation Failure (Pewter City):** My attempt to find a shortcut through the central plaza was a catastrophic failure. I must trace a full, clear path on the map before committing. Do not repeat failed paths. Use `map_layout_analyzer_agent` for new complex areas.
*   **Recognize Scripted Events:** If a path is illogically blocked, it's likely a story gate. Don't brute-force it; explore other options.

## 3. World Clues
*   Team Rocket is at **Mt. Moon**.
*   Moon Stones come from **Mt. Moon**.
*   The eastern route out of Pewter was blocked. I need to check if my Boulder Badge changes this.