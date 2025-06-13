# Gem's Pokémon Yellow Legacy Hard Mode Playthrough Notes

## Game Information
*   **Player Name:** Gem
*   **Rival Name:** Pixel
*   **Current Badges:** 0
*   **Current Level Cap:** 12
*   **Pokédex:** 11/151
*   **Money:** ¥198

## Core Game Rules (Hard Mode)
*   Battle Style: Set
*   No items in battle.
*   Level caps: 0 badges (12), 1 (21), 2 (24), 3 (35), 4 (43), 5 (50), 6 (53), 7 (55), 8 (65).

## Current Objectives & Strategy
*   **Primary Goal:** Earn the Boulder Badge from Brock.
*   **Secondary Goal:** Exit Viridian Forest and heal the party in Pewter City.
*   **Tertiary Goal:** Train the party to the level cap (12).
*   **Current Strategy:** The party is critically injured (two fainted, one at critical HP). The absolute priority is to navigate north out of Viridian Forest to reach the Pewter City Pokémon Center. I will **run from all wild encounters** to conserve HP. After healing, I will assess my team's readiness for Brock, potentially using the `team_composition_advisor_agent` for strategy.

## Key Lessons & Mechanics
*   **Risk Management:** I must prioritize party survival over minor exploration or item collection when resources are low. Reckless risks led to fainted Pokémon.
*   **Navigation:** I must analyze map data more carefully to avoid getting stuck on impassable terrain. Failed pathing in the forest maze has wasted significant time.
*   **Agent Usage:** Agent recommendations are advice, not commands. I need to use my own judgment based on the overall strategic situation. I will start using the `progression_advisor_agent` and `team_composition_advisor_agent` for high-level planning.
*   **Type Anomaly (Poison vs. Bug/Poison):** Observed POISON STING as "super effective" against METAPOD/KAKUNA multiple times. This is a ROM hack change to monitor.
*   **Poison Damage:** Outside battle, poisoned Pokémon lose 1 HP every 4 steps.

## Recent Battle Log (Condensed)
*   (T2820) Wild METAPOD Lv6: NADEL +30 EXP, GOTTSAMER +30 EXP.
*   (T2849) Wild WEEDLE Lv4: NADEL +14 EXP, GOTTSAMER +14 EXP.
*   (T2871) Wild KAKUNA Lv7: SPARKY +71 EXP, **GOTTSAMER fainted** (poisoned).
*   (T2877) Wild WEEDLE Lv4: NADEL +14 EXP, GOTTSAMER +14 EXP.

## Defeated Trainers Log
*   OAK'S LAB - Rival Pixel
*   Viridian Forest - Lass (3,42)
*   Viridian Forest - Youngster (28,20)
*   Viridian Forest - Youngster (28,34)
*   Viridian Forest - Bug Catcher (14,18)
*   Viridian Forest - Bug Catcher (3,19)

## Agent Management
*   My previous agent usage has been suboptimal. I will now integrate agents more effectively into my strategic planning.
*   **`wild_encounter_evaluator_agent`**: Use its advice cautiously, weighing it against the current party status and strategic needs.
*   **`progression_advisor_agent`**: Will use this after escaping the forest to help plan the next major steps.
*   **`team_composition_advisor_agent`**: Will use this to prepare for the Brock fight after healing the party.