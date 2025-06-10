# Pokédex & Badges
*   Badges: Boulder Badge
*   Pokedex: 9/151 (Target: Complete)

# Current Team & Training Focus (Strategic Notes)
*   BELLA (GLOOM Lv21): Core attacker, currently healthy.
*   ZAPPY (PIKACHU Lv16): Healthy (37/47 HP).
*   NINA (NIDORAN♀ Lv12): Keep for Ground/Poison typing. Double Kick is useful.
*   WIGGLES (CATERPIE Lv4): Long-term Butterfree potential.
*   ECHO (ZUBAT Lv11): Flying type coverage, currently healthy.
*   LUNA (CLEFAIRY Lv11): Healthy (37/37 HP).

# Key Items & TMs (Strategic Notes)
*   OLD ROD x1
*   POKé BALL x8
*   TM34 (BIDE) x1 - Evaluate for team.
*   HP UP x1 - Used on ZAPPY.
*   RARE CANDY x1 - Save for strategic use.
*   MOON STONE x1 - Potential use on LUNA (Clefairy) or NINA (Nidoran♀) after evolution to Nidorina for Nidoqueen.
*   TOWN MAP x1

# Current Location
* Route 4 (Before Mt. Moon) (ID: 15) at (19,7)

# Current Goals
*   **Primary Goal:** Reach Cerulean City and prepare to challenge Gym Leader Misty.
*   **Secondary Goal:** Navigate Route 4 (Before Mt. Moon) eastward to reach the path to Cerulean City.
*   **Tertiary Goal:** Find a Fossil in Mt. Moon (deferred).

# Gameplay Notes & Strategy
## Navigation & Exploration
*   **CRITICAL:** Trust the **annotated screen** for immediate obstacles over map memory if there's a conflict.
*   The North map connection from Route 3 (e.g., (58,1)) leads to the *lowest tier* of 'Route 4 (Before Mt. Moon)' at (8,18), not into Mt. Moon 1F (Western side). This route is a loop if trying to access upper Route 4 tiers or the western Mt. Moon entrance for traversal.
*   When on Route 4 (Before Mt. Moon) upper tiers, navigate eastward by descending ledges.
*   The Super Nerd at Mt. Moon B2F (30,12) requests a fossil; he does not provide one.

## Battle Strategy
*   Improve precision in battle menu navigation.
*   Be mindful of type matchups and PP conservation.
*   **Risk Assessment:** Avoid switching in Pokémon with critically low HP against opponents that can KO them.

## ROM Hack Specifics
*   **General Changes:** Old Rod (Viridian Mart), HMs forgettable/menu use, TMs repurchasable, Trade evos by level.
*   **Type Matchup Changes:** Ghost (Special) SE vs Psychic. Bug no longer SE vs Poison.
*   **Stat Boosts:** Pikachu, Farfetch’d, Venomoth, Onix.
*   **Level Caps:** Misty (Starmie Lv21 -> Cap 21), Lt. Surge (Raichu Lv28 -> Player Cap 24).

# Agent Development Plan
*   **`map_analyzer_agent` (Medium Priority - Define/Discard):**
    *   **Purpose:** Parses map XML to identify key features (unseen areas, unvisited warps, dead ends) to aid exploration strategy.
    *   **Action:** Define soon or explicitly discard this idea.
*   **`fossil_chooser_agent` (Low Priority - Test):**
    *   **Status:** Defined. Untested.
    *   **Purpose:** Advises on Dome/Helix fossil choice. Test when fossil choice is presented.
*   **`item_finder_reminder_agent` (USE AS NEEDED):**
    *   **Status:** Defined. Works well.
*   **`rom_hack_mechanics_lookup_agent` (Low Priority - Test):**
    *   **Status:** Defined.
*   **`team_composition_advisor_agent` (Low Priority - Test):**
    *   **Status:** Defined. Untested.
*   **Agent Usage Review (`battle_strategy_agent`, `encounter_optimizer_agent`, `level_up_move_advisor_agent`, `next_battle_action_advisor_agent`, `tm_learning_advisor_agent`):**
    *   **Status:** Defined.
    *   **Action:** Evaluate necessity of less-used agents. Consolidate or delete if not providing consistent value. Reduce reliance on `next_battle_action_advisor_agent`.
*   **`dungeon_navigator_agent` (USE WITH CAUTION):**
    *   **Status:** Defined. High usage noted. Attempt more manual navigation. Review paths or use 'avoid_coordinates' when using.

# Completed Objectives & Discoveries
*   Defeated Brock, obtained Boulder Badge.
*   Explored parts of Route 3 and Mt. Moon 1F, B1F, B2F.
*   Exited Mt. Moon (eastern exit) onto Route 4 (Before Mt. Moon).
*   Confirmed Route 3 (North) to Route 4 (Before Mt. Moon) (South) map connection forms a loop for Mt. Moon traversal purposes.

# Trainer Battle Intel
## Route 3 Trainers
*   All defeated.
## Mt. Moon 1F Trainers
*   All encountered trainers defeated.
## Mt. Moon B2F Trainers
*   Rocket Grunt (ID 3) at (16,23) - Defeated.
*   Super Nerd (Rocket ID 4) at (30,12) - Not a battle. Requests a Fossil.
*   Rocket Grunt (ID 5) at (30,18) - Undefeated (was unreachable).
## Route 4 (Before Mt. Moon) Trainers
*   Cool Trainer F (ID 1) - **UNENGAGEABLE / NOT DEFEATED.** Abandoned attempts to battle.

# ARCHIVED LOGS (Summarized)
*   **Mt. Moon Exploration:** Successfully navigated Mt. Moon and found eastern exit to Route 4. Noted complexity and segmented nature of B1F/B2F. Super Nerd wants a fossil.
*   **Route 4 (Before Mt. Moon) Navigation:** Initial attempts to navigate Route 4 were inefficient, involving looping back to Route 3 and failed attempts to battle Cool Trainer F. Current focus is eastward progression via ledges from the upper tier.