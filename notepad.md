# Pokédex & Badges
*   Badges: Boulder Badge
*   Pokedex: 8/151 (Target: Complete)

# Current Team & Training Focus (Strategic Notes)
*   **Healing Priority:** ZAPPY (PIKACHU Lv16) & LUNA (CLEFAIRY Lv11) are critically low. Must reach Route 4 Pokecenter ASAP.
*   BELLA (GLOOM Lv21): Core attacker, currently healthy.
*   NINA (NIDORAN♀ Lv12): Keep for Ground/Poison typing. Double Kick is useful.
*   WIGGLES (CATERPIE Lv4): Long-term Butterfree potential.
*   ECHO (ZUBAT Lv11): Flying type coverage, currently healthy.
*   **Immediate Healing Priority:** ZAPPY & LUNA at Route 4 Pokecenter.

# Key Items & TMs (Strategic Notes)
*   OLD ROD x1
*   POKé BALL x9
*   TM34 (BIDE) x1 - Evaluate for team.
*   HP UP x1 - Used on ZAPPY.
*   RARE CANDY x1 - Save for strategic use.
*   MOON STONE x1 - Potential use on LUNA (Clefairy) or NINA (Nidoran♀) after evolution to Nidorina for Nidoqueen.
*   TOWN MAP x1

# Current Goals
*   **Primary Goal:** Reach Cerulean City and prepare to challenge Gym Leader Misty.
*   **Secondary Goal:** Exit Mt. Moon to heal Zappy and Luna at a Pokémon Center.
*   **Tertiary Goal:** After healing, resume exploration of Mt. Moon to find a Fossil.

# Gameplay Notes & Strategy
## Navigation & Exploration
*   Mt. Moon is complex. Systematic exploration of floors and isolated sections is key.
*   **CRITICAL:** Trust the **annotated screen** for immediate obstacles over map memory if there's a conflict. Repeatedly trying to move through impassable tiles shown on screen is inefficient.
*   Cave exits, like the one from Mt. Moon 1F to Route 4, are typically ladders or specific warp tiles, not direct map edge transitions.
*   Western entrance/exit of Mt. Moon 1F leads to Route 3.
*   When pathing is blocked, proactively use warp data from `Map Events` to transition between floors or access isolated sections. Consult map memory for alternative routes.
*   The Super Nerd at Mt. Moon B2F (30,12) requests a fossil; he does not provide one. The fossils are likely guarded by another Rocket or found elsewhere in Mt. Moon.

## Battle Strategy
*   Improve precision in battle menu navigation.
*   Be mindful of type matchups and PP conservation.
*   **Risk Assessment:** Avoid switching in Pokémon with critically low HP against opponents that can KO them. Luna fainting was a result of poor risk assessment.
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
*   **`Team Composition Advisor` (Low Priority - Define/Discard):**
    *   **Status:** Idea phase.
    *   **Action:** Decide whether to define this agent or discard the idea to focus development efforts.
*   **Agent Usage Review (`level_cap_check_agent`, `type_matchup_quick_reference_agent`, `encounter_optimizer_agent`, `next_battle_action_advisor_agent`, `tm_learning_advisor_agent`):**
    *   **Status:** Defined.
    *   **Action:** Evaluate necessity of less-used agents. Consolidate or delete if not providing consistent value.
    *   **Note on `next_battle_action_advisor_agent`:** High usage. Reduce reliance.

# Completed Objectives & Discoveries
*   Defeated Brock, obtained Boulder Badge.
*   Explored parts of Route 3 and Mt. Moon 1F, B1F, B2F.
*   Collected various items in Mt. Moon 1F.

# Trainer Battle Intel
## Route 3 Trainers
*   All defeated.
## Mt. Moon 1F Trainers
*   Super Nerd (ID 4) at (25,32) - Defeated.
*   Lass (Cool Trainer F, ID 3) at (31,5) - Defeated.
*   Youngster (ID 7) at (31,28) - Defeated.
*   Youngster (ID 2) at (13,17) - Defeated.
*   Hiker (ID 1) at (6,8) - Defeated.
*   Bug Catcher (ID 6) at (8,25) - Defeated.
*   Lass (Cool Trainer F, ID 5) at (17,24) - Defeated.
*   Bug Catcher (ID 8) at (32,29) - Defeated.
## Mt. Moon B2F Trainers
*   Rocket Grunt (ID 3) at (16,23) - **Defeated**.
*   Super Nerd (Rocket ID 4) at (30,12) - Not a battle. Requests a Fossil.
*   Rocket Grunt (ID 5) at (30,18) - Undefeated (currently unreachable from player's B2F access point).

# Mt. Moon Exploration Log
## Overall Objective
*   Navigate Mt. Moon to reach Route 4 and eventually Cerulean City. Secondary objective: find a Fossil.

## 1F Navigation
*   **Warp at (6,6):** Leads to an isolated 4x4 elevated platform on Mt. Moon B1F. This is not the main B1F area accessible via other ladders like (18,12) or (26,16).
*   **Warp at (18,12):** Leads to Mt. Moon B1F at (26,10).
*   **Warp at (26,16):** Leads to Mt. Moon B1F at (26,16).
*   **Exit to Route 4:** Located at (16,36) on Mt. Moon 1F.

## B1F Navigation
*   **Warp at (26,10) (from 1F (18,12)):** Leads back to Mt. Moon 1F (18,12).
*   **Warp at (18,12):** Leads to Mt. Moon B2F (26,10).
*   **Warp at (26,16) (from 1F (26,16)):** Leads back to Mt. Moon 1F (26,16).
*   **Warp at (22,18):** Leads to Mt. Moon B2F (22,18).
*   **Warp at (14,28):** Leads to Mt. Moon B2F (16,28).

## B2F Navigation
*   **Warp at (26,10) (from B1F (18,12)):** Leads back to Mt. Moon B1F (18,12).
*   **Super Nerd (Rocket ID 4) at (30,12):** Requests a Fossil.
*   **Warp at (16,28) (from B1F (14,28)):** Leads back to Mt. Moon B1F (14,28).
*   **Warp at (22,18) (from B1F (22,18)):** Leads back to Mt. Moon B1F (22,18).

## Navigation Issues & Learnings
*   **Unintended Warps:** Multiple instances of unintentionally taking warps due to long movement sequences crossing warp tiles. (e.g., Turn 5915, Turn 6162). Be more cautious and verify paths.
*   **Pathing Inefficiency:** Some exploration paths were inefficient (e.g., Mt. Moon 1F towards exit; B2F west from (25,x) column). Break down movements into smaller, verifiable segments.
*   **Prioritization:** Prioritize reaching the next city over minor exploration within complex dungeons when primary goal is city progression. This is especially true when party members are critically injured.
*   **Zappy's Status:** Zappy is no longer confused after the battle with the wild Zubat (Turn 6146). Confusion wore off after wild Zubat battle (Turn 6174).

## Agent Performance & Notes
### dungeon_navigator_agent
- **Status:** Defined and in use.
- **Performance:** Failed once (Turn 6273, script produced no output), but worked correctly on subsequent uses (Turn 6274, Turn 6275). Needs monitoring. System prompt to be updated on Turn 6278 to emphasize correct JSON output from its Python script.

## Post-Healing Exploration Strategy for Mt. Moon
*   Prioritize finding undiscovered warps on Mt. Moon B1F, as indicated by game state, to access new areas of B2F for fossil hunting, *after* the party is healed.