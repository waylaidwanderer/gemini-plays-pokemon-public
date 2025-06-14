# Gem's Strategic Plan & Learnings

## 1. Current Objective
- **Primary Goal:** Defeat Brock and earn the Boulder Badge.
- **Secondary Goal:** Fully heal the party at the Pewter Pokémon Center.

## 2. Party Status & Training Goals
*   **SPARKY (PIKACHU):** Lvl 12 (CAPPED)
*   **SPROUT (ODDISH):** Lvl 12 (CAPPED)
*   **PIP (PIDGEY):** Lvl 10
*   **KITSUNE (VULPIX):** Lvl 7 (Priority Training Target)
*   **THISTLE (NIDORAN♀):** Lvl 4 (Priority Training Target)

## 3. Key Learnings & Strategy
*   **Heal Before Major Fights:** Always fully heal at a Pokémon Center before any major challenge (Gym Leaders, Rivals, etc.). Going in injured is a recipe for disaster.
*   **Tool-First Navigation:** Use the `pathfinding_agent` for all non-trivial movement to avoid getting stuck and improve efficiency.
*   **Test Assumptions Quickly:** Don't waste time on unverified hypotheses. Test them, and if they fail, document and pivot. (e.g., Old Amber search in museum).

## 4. World Clues
*   Team Rocket is at **Mt. Moon** (source: Gentleman in Pewter PC).
*   The eastern route out of Pewter is blocked because of Team Rocket at Mt. Moon (source: Police Notice).
*   Moon Stones come from **Mt. Moon** (source: Museum Exhibit).

## Courtyard Conundrum
*   **Failed Attempts:** 7. Navigating out of the gym courtyard has failed repeatedly.
*   **Failed Hypothesis:** Re-entering the gym is not possible from this position.
*   **New Hypothesis (Attempt 8):** The solution is to walk south, directly through Pikachu, to reach the other side of the courtyard.