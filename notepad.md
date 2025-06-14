# Gem's Gameplay Log & Strategy

## Party Assessment
*   **SPROUT** (Oddish, Lv11): Almost at level cap. Key for Brock due to type advantage.
*   **PIP** (Pidgey, Lv10): Good utility. GUST is proving useful.
*   **SPARKY** (Pikachu, Lv12): At level cap (12). On standby for now.
*   **THISTLE** (Nidoran♀, Lv4): Newest team member! Needs training.

## Current Plans & Hypotheses
*   **Training on Route 22:**
    *   **Hypothesis:** The wild Pokémon on Route 22 (Nidoran, Mankey, Spearow) provide good EXP for SPROUT and PIP.
    *   **Plan:** Continue battling wild Pokémon here until SPROUT reaches the level cap (12). Also, get some levels for PIP and THISTLE.
*   **Brock Preparation:**
    *   **Hypothesis:** A high-level SPROUT with its Grass/Poison typing will be super effective against Brock's Rock/Ground Pokémon.
    *   **Plan:** Once SPROUT is level 12, I will proceed to Pewter City to challenge the gym.

## Lessons Learned & New Rules
*   **Pre-Departure Checklist:** ALWAYS check Pokémon HP and PP at a Pokémon Center before leaving a town. (Failed this once, wasted significant time).
*   **Navigation:** Viridian City's layout is tricky. I must trace paths on the map before moving to avoid hitting obstacles. (Failed this multiple times).
*   **Agent Unreliability:** The `pathfinding_agent` is not perfect. It led me into a `cuttable` tree. I MUST manually verify any path an agent suggests against the map XML data. Do not trust agents blindly. (Failed this once).
*   **Battle Efficiency:** Stop fumbling with menu controls. If a tool fails (like `select_battle_option`), switch to manual inputs immediately. Don't waste turns on repeated failed tool calls. (Failed this multiple times).

## Defeated Trainers
*   Bug Catcher (Viridian Forest, (31,34))
*   Cooltrainer F (Viridian Forest, (3,42))
*   Bug Catcher (Viridian Forest, (3,19))
*   Rival BLAZe (Route 22, (30,5))