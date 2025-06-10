# Pokédex & Badges
*   Badges: Boulder Badge
*   Pokedex: 10/151 (Target: Complete)

# Current Team & Training Focus (Strategic Notes)
*   BELLA (GLOOM Lv21): (66/66 HP) | Moves: STUN SPORE (30 PP), ACID (22 PP), LEECH SEED (10 PP), ABSORB (17 PP)
*   ZAPPY (PIKACHU Lv17): (25/50 HP) | Moves: THUNDERSHOCK (18 PP), DOUBLE TEAM (15 PP), QUICK ATTACK (30 PP), THUNDER WAVE (20 PP)
*   NINA (NIDORAN♀ Lv12): (36/36 HP) | Moves: GROWL (40 PP), DOUBLE KICK (30 PP), POISON STING (35 PP), BITE (25 PP). Keep for Ground/Poison typing.
*   ECHO (ZUBAT Lv11): (30/30 HP) | Moves: LEECH LIFE (25 PP), SUPERSONIC (20 PP), GUST (35 PP). Flying type coverage.
*   LUNA (CLEFAIRY Lv11): (37/37 HP) | Moves: POUND (35 PP), GROWL (40 PP), WATER GUN (25 PP), MEGA PUNCH (20 PP).
*   SIR (PARAS Lv13): (34/34 HP) | Moves: STUN SPORE (30 PP), ABSORB (25 PP), LEECH LIFE (25 PP), POISONPOWDER (35 PP).

# Key Items & TMs (Strategic Notes)
*   OLD ROD x1
*   POKé BALL x5
*   TM34 (BIDE) x1 - Evaluate for team.
*   HP UP x1 - Used on ZAPPY.
*   RARE CANDY x1 - Save for strategic use. Test `item_use_advisor_agent`.
*   MOON STONE x1 - Potential use on LUNA (Clefairy) or NINA (Nidoran♀) after evolution to Nidorina for Nidoqueen. Test `item_use_advisor_agent`.
*   TOWN MAP x1

# Current Location
*   **Current Location:** Route 4 (Before Mt. Moon) (ID: 15) at (19,8)

# Current Goals
*   **Primary Goal:** Reach Cerulean City and prepare to challenge Gym Leader Misty.
*   **Secondary Goal:** Heal ZAPPY (PIKACHU) at the Mt. Moon Pokecenter.
*   **Tertiary Goal:** After healing, secure one of the two Fossils (Dome or Helix) on Mt. Moon B2F by accessing the area via the warp at B1F (14,28).

# Gameplay Notes & Strategy
## Navigation & Exploration
*   **CRITICAL:** Trust the **annotated screen** for immediate obstacles over map memory if there's a conflict.
*   The North map connection from Route 3 (e.g., (58,1)) leads to the *lowest tier* of 'Route 4 (Before Mt. Moon)' at (8,18), not into Mt. Moon 1F (Western side). This route is a loop if trying to access upper Route 4 tiers or the western Mt. Moon entrance for traversal.
*   When on Route 4 (Before Mt. Moon) upper tiers, navigate eastward by descending ledges.
*   The Super Nerd at Mt. Moon B2F (30,12) requests a fossil; he does not provide one.
*   **Path Validation:** Before committing to long movement sequences in complex/warp-heavy areas, manually verify initial steps against map XML/annotated screen to avoid unintended warps or blockages. Reduce reliance on `dungeon_navigator_agent` for all pathing; use it for initial discovery, then verify/segment or navigate manually.
*   **Multi-Tile Warps:** Be consistently aware of 2-step activation (onto tile, then into boundary/direction).

## Battle Strategy
*   Improve precision in battle menu navigation.
*   Be mindful of type matchups and PP conservation.
*   **Risk Assessment:** Avoid switching in Pokémon with critically low HP against opponents that can KO them.
*   **Healing Priority:** If a key Pokémon is critically injured, prioritize reaching a Pokémon Center quickly, potentially by running from non-essential wild encounters.

## ROM Hack Specifics
*   **General Changes:** Old Rod (Viridian Mart), HMs forgettable/menu use, TMs repurchasable, Trade evos by level.
*   **Type Matchup Changes:** Ghost (Special) SE vs Psychic. Bug no longer SE vs Poison. Grass is 0.25x vs Poison/Flying (e.g., Zubat).
*   **Stat Boosts:** Pikachu, Farfetch’d, Venomoth, Onix.
*   **Level Caps:** Misty (Starmie Lv21 -> Cap 21), Lt. Surge (Raichu Lv28 -> Player Cap 24).

## PC Interaction Notes
*   Pewter City PC is on the far right (east side) of the Pokecenter, interact from below (e.g., from (14,5) to use PC at (14,4)).
*   'SOMEONE's PC' is for Pokémon Storage. This is where you withdraw/deposit Pokémon.
*   'Gem's PC' is for Item Storage.
*   **CRITICAL MISTAKE LOG (Summarized):** Significant time lost at Pewter PC due to misidentifying PC, incorrect box assumptions for SIR, menu flow misunderstandings, and unproductive repeated inputs. Lesson: Slow down in menus, verify info, and be methodical.

# Mt. Moon Exploration Strategy (Revised Turn 7826)
*   **Immediate Objective:** Heal ZAPPY at the Mt. Moon Pokecenter.
*   **Fossil Hunt Plan (Post-Healing):**
    1.  Return to Mt. Moon B1F.
    2.  The warp at B1F (14,28) leading to the fossil area of B2F is NOW CONFIRMED `reachable: yes` by Game State Info. This is the primary route to the fossils.
    3.  Proceed to B1F (14,28) and take the warp to B2F to find the fossils near the previously defeated Rocket Grunt at B2F (16,23).
    4.  Secure a Fossil on B2F.
    5.  Return the fossil to the Super Nerd at (30,12) on B2F (in the other B2F segment).
*   **Pathfinding Note:** REINFORCED - Be extremely cautious with `dungeon_navigator_agent` paths, especially on maps with warps. Manually verify against map XML or use `local_area_analyzer_agent` to check for unintended warps *before* committing to long movement sequences. Avoid repeating the error of taking an unintended warp.

# Agent Development & Usage
*   **`item_finder_reminder_agent` (USE AS NEEDED):** Status: Defined. Works well.
*   **`rom_hack_mechanics_lookup_agent` (1 use):** Status: Defined. Low usage, evaluate if slot is better used.
*   **`team_composition_advisor_agent` (1 use):** Status: Defined. Low usage, evaluate if slot is better used.
*   **`item_use_advisor_agent` (1 use):** Status: Defined. Prioritize testing further (e.g., Moon Stone, Rare Candy).
*   **`dungeon_navigator_agent` (82 uses):** High usage. Reduce reliance. Prioritize manual navigation or segment/verify agent paths.
*   **`next_battle_action_advisor_agent` (20 uses):** High usage. Continue efforts for more manual battle decisions.
*   **`battle_strategy_agent` (3 uses):** Re-evaluate utility. Consider for Gym Leaders. If usage remains low, consider deletion.
*   **`training_regimen_planner_agent` (IDEA - Low Priority):** Purpose: Suggest optimal training order/locations. Status: Idea only. Would require deleting an existing agent. Re-evaluate utility vs. existing agents after challenging Misty.
*   **Agent Slot Management:** 10/10 agents defined. Be mindful of the limit. Consider deleting less useful agents if new ones are needed.

# Critique Action Items (From Turn 7825 Feedback)
*   Reduce reliance on `dungeon_navigator_agent`; improve manual pathfinding, segment/verify agent paths.
*   Prioritize healing critical Pokémon quickly (e.g., run from battles if needed).
*   Consistently apply knowledge of multi-tile warp activation.
*   Thoroughly test `item_use_advisor_agent`.
*   Action (create/discard) `training_regimen_planner_agent` idea post-Misty.
*   Condense verbose notepad sections (e.g., Mt. Moon strategy).
*   For Trainer Battle Intel, focus on defeat status/location, omit redundant `navigable: false` notes if XML is trusted.

# Completed Objectives & Discoveries
*   Defeated Brock, obtained Boulder Badge.
*   Explored parts of Route 3 and Mt. Moon 1F, B1F, B2F.
*   Exited Mt. Moon (western exit) onto Route 4 (Before Mt. Moon).
*   Confirmed Route 3 (North) to Route 4 (Before Mt. Moon) (South) map connection forms a loop for Mt. Moon traversal purposes.
*   Deposited WIGGLES (Caterpie Lv4) into PC Box 3. Withdrew SIR (Paras Lv13) from PC Box 1.
*   Healed party at Mt. Moon Pokecenter (multiple times).
*   Warp at B1F (14,28) to B2F (fossil area) confirmed `reachable: yes` as of Turn 7800.

# Trainer Battle Intel
## Route 3 Trainers
*   Youngster (ID 2) at (Route 3, 11,7) - Defeated.
*   Youngster (ID 3) at (Route 3, 15,5) - Defeated.
*   Cool Trainer F (ID 4) at (Route 3, 17,10) - Defeated.
*   Youngster (ID 5) at (Route 3, 20,6) - Defeated.
*   Youngster (ID 7) at (Route 3, 23,10) - Non-battling (dialogue only).
*   Youngster (ID 8) at (Route 3, 25,7) - Defeated.
*   Cool Trainer F (ID 9) at (Route 3, 34,11) - Defeated.
## Mt. Moon 1F Trainers
*   Bug Catcher (ID 6) at (Mt Moon 1F, 8,25) - Defeated.
*   Lass (Cool Trainer F, ID 5) at (Mt Moon 1F, 17,24) - Defeated.
*   Super Nerd (ID 4) at (Mt Moon 1F, 25,32) - Defeated.
*   Bug Catcher (ID 8) at (Mt Moon 1F, 32,29) - Defeated.
*   Lass (Cool Trainer F, ID 3) at (Mt Moon 1F, 31,5) - Defeated.
*   Youngster (ID 2) at (Mt Moon 1F, 14,17) - Defeated.
*   Hiker (ID 1) at (Mt Moon 1F, 6,8) - Defeated.
*   Youngster (ID 7) at (Mt Moon 1F, 31,28) - Non-battling (gives dialogue: "This cave leads to CERULEAN CITY!").
## Mt. Moon B2F Trainers
*   Super Nerd (ID 4, sprite MTMOONB2F_ROCKET2) at (Mt Moon B2F, 30,12) - Not a battle. Requests a Fossil.
*   Rocket Grunt (ID 5, sprite MTMOONB2F_ROCKET3) at (Mt Moon B2F, 30,18) - Undefeated (was unreachable, blocked by Super Nerd).
*   Rocket Grunt (ID 3) at (Mt Moon B2F, 16,23) - Defeated.
## Route 4 (Before Mt. Moon) Trainers
*   Cool Trainer F (ID 1) at (Route 4 Before Mt. Moon, 10,9) - **UNENGAGEABLE / NOT DEFEATED.** (Player choice to avoid).

# ARCHIVED LOGS (Summarized)
*   **Mt. Moon Exploration:** Successfully navigated Mt. Moon and found western exit to Route 4. Noted complexity and segmented nature of B1F/B2F. Super Nerd wants a fossil.
*   **Route 4 (Before Mt. Moon) Navigation:** Initial attempts to navigate Route 4 eastward from Mt. Moon's exit were inefficient due to prematurely jumping down ledges, forcing a loop back via Route 3. The correct path requires staying on the upper tier after exiting Mt. Moon (eastern exit) and heading east.

## Navigation Rules & Insights
*   NPCs on `navigable: false` tiles are impassable physical obstacles, even if defeated or non-battling.
*   Ledge tiles marked `navigable="true"` can be occupied (e.g., by jumping down onto them), but upward movement onto a ledge from below is prevented by game physics, even if the tile's `navigable` attribute is true. The game's movement denial takes precedence over the XML's `navigable` flag for directional traversal of ledges from below.
*   Defeated trainers may sometimes remain as physical obstacles on their tile; their tile will remain `navigable: false` in map memory.

# Battle Mechanics Update (Mt. Moon):
*   Confirmed Acid (Poison-type move) is 'not very effective' (0.5x) against wild Zubat (Poison/Flying). This indicates a ROM hack change where Poison attacks are resisted by either Poison-type or Flying-type Pokémon (or both, though less likely for 0.5x). Standard Gen 1: Poison vs Poison = 1x, Poison vs Flying = 1x.
*   Confirmed Absorb (Grass-type move) is 'not very effective' (0.25x or similar, very low damage) against wild Zubat (Poison/Flying). This implies Grass is resisted by both Poison and Flying types in this ROM hack. Standard Gen 1: Grass vs Poison = 0.5x, Grass vs Flying = 0.5x. Combined would be 0.25x.