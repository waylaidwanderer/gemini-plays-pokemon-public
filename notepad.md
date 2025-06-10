# Pokédex & Badges
*   Badges: Boulder Badge
*   Pokedex: 10/151 (Target: Complete)

# Current Team & Training Focus (Strategic Notes)
*   BELLA (GLOOM Lv21): Core attacker, currently healthy (66/66 HP).
*   ZAPPY (PIKACHU Lv16): Healthy (47/47 HP).
*   NINA (NIDORAN♀ Lv12): Healthy (36/36 HP). Keep for Ground/Poison typing. Double Kick is useful.
*   ECHO (ZUBAT Lv11): Healthy (30/30 HP). Flying type coverage.
*   LUNA (CLEFAIRY Lv11): Healthy (37/37 HP).
*   SIR (PARAS Lv13): Healthy (34/34 HP).

# Key Items & TMs (Strategic Notes)
*   OLD ROD x1
*   POKé BALL x5
*   TM34 (BIDE) x1 - Evaluate for team.
*   HP UP x1 - Used on ZAPPY.
*   RARE CANDY x1 - Save for strategic use.
*   MOON STONE x1 - Potential use on LUNA (Clefairy) or NINA (Nidoran♀) after evolution to Nidorina for Nidoqueen.
*   TOWN MAP x1

# Current Location
*   **Current Location:** Mt Moon (ID: 59) at (25,18)

# Current Goals
*   **Primary Goal:** Reach Cerulean City and prepare to challenge Gym Leader Misty.
*   **Secondary Goal:** Navigate Mt. Moon 1F to find the eastern exit towards Cerulean City.
*   **Tertiary Goal:** Catch any new interesting Pokémon in Mt. Moon if encountered.

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

## PC Interaction Notes
*   Pewter City PC is on the far right (east side) of the Pokecenter, interact from below (e.g., from (14,5) to use PC at (14,4)).
*   'SOMEONE's PC' is for Pokémon Storage. This is where you withdraw/deposit Pokémon.
*   'Gem's PC' is for Item Storage.
*   **CRITICAL MISTAKE LOG (Summarized):** Significant time lost at Pewter PC due to misidentifying PC, incorrect box assumptions for SIR, menu flow misunderstandings, and unproductive repeated inputs. Lesson: Slow down in menus, verify info, and be methodical.

# Agent Development Plan
*   **`item_finder_reminder_agent` (USE AS NEEDED):**
    *   **Status:** Defined. Works well.
*   **`rom_hack_mechanics_lookup_agent` (Low Priority - Tested):**
    *   **Status:** Defined. Works as expected.
*   **`team_composition_advisor_agent` (Low Priority - Tested):**
    *   **Status:** Defined. Works as expected.
*   **Agent Usage Review (9/10 agents defined):**
    *   `hm_advisor_agent` deleted (0 uses).
    *   **Action:** Reduce reliance on `dungeon_navigator_agent` (65 uses) and `next_battle_action_advisor_agent` (19 uses). Attempt manual navigation/battle decisions first.
    *   Review utility of `battle_strategy_agent` (3 uses) and `encounter_optimizer_agent` (1 use) if not used more consistently soon.
*   **`dungeon_navigator_agent` (USE WITH CAUTION):**
    *   **Status:** Defined. High usage noted (69 uses - per critique). Agent does not account for game physics preventing upward ledge movement. MUST attempt more manual navigation. Review paths or use 'avoid_coordinates' when using. **Strategy Update:** When using `avoid_coordinates_json`, ensure it includes *all* known NPCs on `navigable: false` tiles in the relevant area to improve path viability.

## Future Agent Ideas
*   **Shop Inventory Agent:** To track items/TMs sold in Marts.
*   **Item Use Advisor Agent:** To advise on using consumable stat boosters, Rare Candies, or evolution stones.

# Completed Objectives & Discoveries
*   Defeated Brock, obtained Boulder Badge.
*   Explored parts of Route 3 and Mt. Moon 1F, B1F, B2F.
*   Exited Mt. Moon (western exit) onto Route 4 (Before Mt. Moon).
*   Confirmed Route 3 (North) to Route 4 (Before Mt. Moon) (South) map connection forms a loop for Mt. Moon traversal purposes.
*   Tested `rom_hack_mechanics_lookup_agent` and `team_composition_advisor_agent`.
*   Deleted `hm_advisor_agent`.
*   Deposited WIGGLES (Caterpie Lv4) into PC Box 3. Withdrew SIR (Paras Lv13) from PC Box 1.
*   Healed party at Mt. Moon Pokecenter.

# Trainer Battle Intel
## Route 3 Trainers
*   Youngster (ID 2) at (11,7) - Defeated.
*   Youngster (ID 3) at (15,5) - Defeated.
*   Cool Trainer F (ID 4) at (17,10) - Defeated. Tile (17,10) is `navigable: false`, acting as a physical block, preventing eastward movement on row 10 from (16,10).
*   Youngster (ID 5) at (20,6) - Defeated (Blocks path from east on row 6).
*   Youngster (ID 7) at (23,10) - Non-battling (repeated dialogue). His tile (23,10) is `navigable: false`, acting as a physical block, preventing eastward movement on row 10 from (22,10).
*   Youngster (ID 8) at (25,7) - Defeated.
*   Cool Trainer F (ID 9) at (34,11) - Defeated.
## Mt. Moon 1F Trainers
*   Bug Catcher (ID 6) at (8,25) - Defeated.
*   Lass (Cool Trainer F, ID 5) at (17,24) - Defeated.
*   Super Nerd (ID 4) at (25,32) - Defeated.
*   Bug Catcher (ID 8) at (32,29) - Defeated.
*   Lass (Cool Trainer F, ID 3) at (31,5) - Defeated.
*   Youngster (ID 2) at (14,17) - Defeated.
*   Hiker (ID 1) at (6,8) - Defeated.
*   Youngster (ID 7) at (31,28) - Non-battling (gives dialogue: "This cave leads to CERULEAN CITY!"). His tile (31,28) is `navigable: false` due to NPC presence. The exit to Cerulean City is likely adjacent to him, e.g., (32,28).
## Mt. Moon B2F Trainers
*   Rocket Grunt (ID 3) at (16,23) - Defeated.
*   Super Nerd (Rocket ID 4) at (30,12) - Not a battle. Requests a Fossil.
*   Rocket Grunt (ID 5) at (30,18) - Undefeated (was unreachable).
## Route 4 (Before Mt. Moon) Trainers
*   Cool Trainer F (ID 1) at (10,9) - **UNENGAGEABLE / NOT DEFEATED.** Abandoned attempts to battle. (Player choice to avoid unnecessary battle and prevent looping on lower ledges).

# ARCHIVED LOGS (Summarized)
*   **Mt. Moon Exploration:** Successfully navigated Mt. Moon and found western exit to Route 4. Noted complexity and segmented nature of B1F/B2F. Super Nerd wants a fossil.
*   **Route 4 (Before Mt. Moon) Navigation:** Initial attempts to navigate Route 4 eastward from Mt. Moon's exit were inefficient due to prematurely jumping down ledges, forcing a loop back via Route 3. The correct path requires staying on the upper tier after exiting Mt. Moon (eastern exit) and heading east.

## Navigation Rules & Insights
*   NPCs on `navigable: false` tiles are impassable physical obstacles, even if defeated or non-battling.
*   Ledge tiles marked `navigable="true"` can be occupied (e.g., by jumping down onto them), but upward movement onto a ledge from below is prevented by game physics, even if the tile's `navigable` attribute is true. The game's movement denial takes precedence over the XML's `navigable` flag for directional traversal of ledges from below.

# Agent Review TODO
*   Review utility of `battle_strategy_agent` (3 uses) and `encounter_optimizer_agent` (1 use). Consider revision or deletion if not meeting needs.

**Battle Mechanics Update (Mt. Moon):** Confirmed Acid (Poison-type move) is 'not very effective' (0.5x) against wild Zubat (Poison/Flying). This indicates a ROM hack change where Poison attacks are resisted by either Poison-type or Flying-type Pokémon (or both, though less likely for 0.5x). Standard Gen 1: Poison vs Poison = 1x, Poison vs Flying = 1x.