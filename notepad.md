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
* Route 4 (Before Mt. Moon) (ID: 15) at (8,18)

# Current Goals
*   **Primary Goal:** Reach Cerulean City and prepare to challenge Gym Leader Misty.
*   **Secondary Goal:** Navigate Mt. Moon to find the eastern exit to Route 4.
*   **Tertiary Goal:** Find a Fossil in Mt. Moon (deferred).

# Gameplay Notes & Strategy
## Navigation & Exploration
*   **CRITICAL:** Trust the **annotated screen** for immediate obstacles over map memory if there's a conflict. Repeatedly trying to move through impassable tiles shown on screen is inefficient.
*   Cave exits, like the one from Mt. Moon 1F to Route 4, are typically ladders or specific warp tiles, not direct map edge transitions.
*   When pathing is blocked, proactively use warp data from `Map Events` to transition between floors or access isolated sections. Consult map memory for alternative routes.
*   The Super Nerd at Mt. Moon B2F (30,12) requests a fossil; he does not provide one. The fossils are likely guarded by another Rocket or found elsewhere in Mt. Moon.
*   Prioritize reaching the next city over minor exploration within complex dungeons when primary goal is city progression.
*   **Map Connection Anomaly:** The North connection from Route 3 (e.g., (58,1)) appears to lead to Route 4 (Before Mt. Moon) at (8,18) on its lowest tier, not directly into Mt. Moon 1F (Western side) as initially assumed. This creates a loop if trying to access upper Route 4 tiers or the western Mt. Moon entrance this way. This needs re-testing.

## Battle Strategy
*   Improve precision in battle menu navigation.
*   Be mindful of type matchups and PP conservation.
*   **Risk Assessment:** Avoid switching in Pokémon with critically low HP against opponents that can KO them.
*   Stun Spore (Normal-type status move) failed vs Zubat (Poison/Flying). Failure likely due to accuracy (75%) or a specific immunity Zubat might have, not Grass vs. Poison type interaction for the move itself.
*   Acid (Poison) vs Zubat (Poison/Flying) is NVE (0.5x).
*   **Self-Challenge:** Attempt more battles without consulting `next_battle_action_advisor_agent` to improve independent tactical decision-making.

## ROM Hack Specifics
*   **General Changes:** Old Rod (Viridian Mart), HMs forgettable/menu use, TMs repurchasable, Trade evos by level.
*   **Type Matchup Changes:** Ghost (Special) SE vs Psychic. Bug no longer SE vs Poison.
*   **Stat Boosts:** Pikachu, Farfetch’d, Venomoth, Onix.
*   **Level Caps:** Misty (Starmie Lv21 -> Cap 21), Lt. Surge (Raichu Lv28 -> Player Cap 24).

## NPC Interactions
*   Defeated trainers might not always move. Check tile navigability.

# Agent Development Plan
*   **`map_analyzer_agent` (Low Priority - Define):**
    *   **Purpose:** Parses map XML to identify key features (unseen areas, unvisited warps, dead ends) to aid exploration strategy.
*   **`fossil_chooser_agent` (Medium Priority - Test):**
    *   **Status:** Defined. Untested.
    *   **Purpose:** Advises on Dome/Helix fossil choice.
    *   **Notes:** Test when fossil choice is presented.
*   **`item_finder_reminder_agent` (USE AS NEEDED):**
    *   **Status:** Defined. Works well.
    *   **Usage:** Use when entering new map areas if item collection is a priority.
*   **`rom_hack_mechanics_lookup_agent` (Low Priority - Test):**
    *   **Status:** Defined.
    *   **Purpose:** Quick lookup for ROM hack mechanics.
    *   **Notes:** Test its utility.
*   **`team_composition_advisor_agent` (Medium Priority - Test):**
    *   **Status:** Defined. Untested.
    *   **Purpose:** Advises on optimal team composition.
    *   **Notes:** Test before next major battle (e.g., Misty).
*   **Agent Usage Review (`battle_strategy_agent`, `encounter_optimizer_agent`, `level_up_move_advisor_agent`, `next_battle_action_advisor_agent`, `tm_learning_advisor_agent`):**
    *   **Status:** Defined.
    *   **Action:** Evaluate necessity of less-used agents. Consolidate or delete if not providing consistent value.
    *   **Note on `next_battle_action_advisor_agent`:** High usage. Reduce reliance.
*   **`dungeon_navigator_agent` (USE WITH CAUTION):**
    *   **Status:** Defined and heavily used.
    *   **Performance:** Paths can lead through unintended warps. Review paths carefully or use 'avoid_coordinates' feature.

# Completed Objectives & Discoveries
*   Defeated Brock, obtained Boulder Badge.
*   Explored parts of Route 3 and Mt. Moon 1F, B1F, B2F.
*   Exited Mt. Moon (eastern exit) onto Route 4 (Before Mt. Moon).
*   Navigated some ledges on Route 4 (Before Mt. Moon).
*   Used South map connection from Route 4 (Before Mt. Moon) (Y=18) to Route 3 (Y=1).

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
*   Cool Trainer F (ID 1) - **UNENGAGEABLE / NOT DEFEATED.** Attempts to battle failed repeatedly; interaction seems bugged or requires specific conditions not met. Abandoned attempts to proceed.

# ARCHIVED LOGS
## Mt. Moon Exploration Log (ARCHIVED - Route 4 Reached)
*   Exited Mt. Moon 1F (eastern exit at (16,36)) onto Route 4 (Before Mt. Moon) at (19,7).
*   Mt. Moon is complex. Systematic exploration of floors and isolated sections is key.
*   Cave exits are typically ladders or specific warp tiles.
*   Western entrance/exit of Mt. Moon 1F (at (4,6)) leads to Route 3.
*   Super Nerd at Mt. Moon B2F (30,12) requests a fossil.
*   Unintended warps can occur with long movement sequences; be cautious.
*   Mt. Moon B1F and B2F are segmented; accessing different areas often requires returning to 1F and using different ladders.

## Route 4 (Before Mt. Moon) Navigation Log (ARCHIVED - Reached Route 3 via South Connection)
*   Exited Mt. Moon at (19,7) on Route 4 (Before Mt. Moon) [upper tier].
*   Cool Trainer F was unengageable after multiple attempts.
*   Navigated ledges downwards: Y=7/8/9 -> Y=10/11 -> Y=16 -> Y=17 -> Y=18.
*   Path east from Y=18 blocked at (15,18) and (21,15 based on earlier view from higher Y).
*   Path south from Y=18 (e.g., at (8,18) or (13,18)) leads to Route 3 (Y=1).