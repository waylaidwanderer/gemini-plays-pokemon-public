# Gem's Pokémon Yellow Legacy Hard Mode Playthrough Notes

## Game Information
*   **Player Name:** Gem
*   **Rival Name:** Pixel
*   **Current Badges:** 0 (Game State is Source of Truth)
*   **Current Level Cap:** 12 (0 badges - Game State is Source of Truth)
*   **Pokédex:** 11/151 (HM05 FLASH requirement met!)
*   **Money:** ¥198 (Game State is Source of Truth)

## Core Game Rules & Mechanics (Notepad Quick Reference)
### Hard Mode Rules (Player-Only Restrictions):
*   **Battle Style:** Set mode.
*   **No items in battle.**
*   **Level caps apply.** (See table below)

### Level Cap Table:
*   0 badges: **12**
*   1 badge: **21**
*   2 badges: **24**
*   3 badges: **35**
*   4 badges: **43**
*   5 badges: **50**
*   6 badges: **53**
*   7 badges: **55**
*   8 badges: **65**

### Key Gameplay & Balance Changes (ROM Hack):
*   HMs: forgettable, menu use, no PC storage.
*   All 151 Pokémon obtainable.
*   Trade evolutions by level (e.g., Haunter → Gengar at 42, Machoke → Machamp at 38).
*   Smarter AI, anti-sweep tactics.
*   Tougher Boss fights (custom teams, varied).
*   Dynamic scaling for Gyms 4–6.
*   EXP. All obtainable without special requirements.

## Current Objectives & Tactical Plans (HOW to achieve goals)
*   **Boulder Badge Acquisition (Primary):**
    1.  Explore Viridian Forest: collect item at (13,30) (priority for Poké Balls), battle trainers, and train party members (especially NADEL - HP 6/20, manage carefully; GOTTSAMER fainted), aiming for levels closer to the cap (12) before Brock. Prioritize type advantages (Fighting vs. Rock). Catch new Pokémon if encountered and not yet in Pokédex (conserve Poké Balls).
    2.  Navigate through Viridian Forest North Gate to Route 2 (North).
    3.  Proceed to Pewter City.
    4.  Heal party (especially NADEL) and revive FURYFIST and GOTTSAMER at Pewter Pokémon Center.
    5.  Re-challenge Jr. Trainer M in Pewter Gym.
    6.  Re-challenge Brock. If battle is difficult, consult `team_composition_advisor_agent` and `battle_strategist_agent`.
*   **Travel to Pewter City (Secondary):** Achieved via steps for primary goal.
*   **Resource Acquisition & Fainted Pokémon Revival (Tertiary):** Acquire more Poké Balls (item at (13,30) is top priority). Explore remaining unseen areas in Viridian Forest (current focus: (13,25-28)). Revive FURYFIST and GOTTSAMER at the next opportunity (Pewter City Pokémon Center).

## Lessons Learned, Game Mechanics & Insights
*   **Tile Types:** `ground`, `impassable`, `grass`, `ledge` (jump Y+2, impassable from Y+1 below), `cuttable`.
*   **Battle Menu (2x2):** FIGHT (top-left), PKMN (top-right), ITEM (bottom-left), RUN (bottom-right).
*   **Party List Selection:** 'A' on Pokémon opens sub-menu (SWITCH, STATS, CANCEL).
*   **Naming Screen:** 'START' confirms name. Plan inputs for efficiency.
*   **Poison:** Outside battle, -1 HP every 4 steps. GOTTSAMER is currently poisoned (in party, fainted).
*   **Pikachu Movement:** Can walk through. Adjacent & not facing: 1st press turns, 2nd moves.
*   **Warp Types:** 1x1 instant (move off/on to re-warp). Larger warps (2x1, 1x2) may need 2 steps (onto warp, then into boundary/direction).
*   **Dialogue Clearing:** ALWAYS press 'A' to clear dialogue/text BEFORE other inputs.
*   **Type Matchups (Observed ROM Hack Changes/Anomalies):**
    *   Ghost super effective vs. Psychic (Confirmed by Oak's Aide).
    *   POISON STING (Poison) displaying as "super effective" against METAPOD (Bug/Poison) and KAKUNA (Bug/Poison). This has occurred multiple times (e.g., T2816, T2817, T2820 with NADEL vs Metapod; T2866 KAKUNA vs GOTTSAMER). Standard typing is NVE. Continue to observe and document.
*   **Game Data Trust:** Game State Information is truth (badges, level caps, 'reachable'). Visual interpretation can be flawed.
*   **Interaction Loops:** If NPC/object interaction yields no progress after 2-3 attempts, different trigger needed.
*   **Coordinate Checks:** Verify current coordinates before planning movement. Be mindful of turn count mismatches.
*   **DV Checking:** Hold START while pressing A on STATS screen.
*   **Notepad `replace` vs `overwrite`:** `old_text` for `replace` must be *exact*. Use `overwrite` for major changes or multiple small edits to ensure accuracy and avoid tool call limits.
*   **Pokémon Switching Menu (Battle):** Clear understanding of sub-menu navigation for switching.
*   **Pathing Precision & Map Memory:** Analyze map memory/XML carefully, especially near ledges/complex terrain. Trust map memory for tile types. Be aware of impassable blocks (e.g., trees at Y=40 in Viridian Forest between X=10-15). Re-route proactively when obstacles are identified.
*   **Pokédex Evaluation:** Professor Oak or aides evaluate in person (not via PC).
*   **Battle Risk Assessment:** Balance progression with resource conservation. NADEL's low HP (6/20) is a current concern; avoid unnecessary risks with her until healed. GOTTSAMER (0/29 HP) and FURYFIST (0/17 HP) are fainted.
*   **WKG Tool Usage:** Single `manage_world_knowledge` call per operation. Record transitions IMMEDIATELY.
*   **NPC Stun Usage:** Consider using `stun_npc` sooner for mobile NPCs hindering interaction or pathing.
*   **Agent Path Verification:** MUST manually verify `route_planner_agent` paths against map memory/XML *before* execution. Consider `map_analyzer_agent` for local alternatives if long paths fail.
*   **Battle Strategy vs. Progression:** Prioritize progression over marginal EXP gains from wild battles, especially when Pokémon are very low level or resources are scarce. Run from battles more readily if not specifically training or catching.
*   **Map Markers:** Be consistent in marking ALL significant map features (used warps, key NPCs, obstacles, items obtained, key signs, defeated trainers that block paths) that aid future navigation or recall.
*   **EXP Updates (Summarized Recent):
    *   (T2803) NADEL (Lv4 WEEDLE) -> Lv5 (HP: 20/20 -> 17/20). GOTTSAMER (Lv9 METAPOD) gained 14 EXP.
    *   (T2820, Wild Lv6 METAPOD) NADEL (Lv5 WEEDLE) gained 30 EXP (HP: 17/20). GOTTSAMER (Lv9 METAPOD) gained 30 EXP.
    *   (T2849, Wild Lv4 WEEDLE) NADEL (Lv5 WEEDLE) gained 14 EXP (HP: 6/20). GOTTSAMER (Lv9 METAPOD) gained 14 EXP.
    *   (T2871, Wild Lv7 KAKUNA) SPARKY (Lv10 PIKACHU) gained 71 EXP (HP: 25/32). GOTTSAMER fainted.
*   **Battle Anomaly (Turn 2787-2789):** Wild WEEDLE battle with SPARKY active ended inconclusively (no EXP gain after 'Up' input registered post-battle).
*   **System Warnings:** Received reminders about making longer movement sequences and turn count mismatches. Be diligent.

## Defeated Trainers Log
*   OAK'S LAB (ID 40) - (6,6) - Rival Pixel (initial battle)
*   Viridian Forest (ID 51) - (3,42) - Lass (Cool Trainer F sprite, VIRIDIANFOREST_COOLTRAINER_F) - *Note: Blocks path west from (4,42) even after defeat.*
*   Viridian Forest (ID 51) - (28,20) - Youngster (Bug Catcher sprite, VIRIDIANFOREST_YOUNGSTER3)
*   Viridian Forest (ID 51) - (28,34) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER2)
*   Viridian Forest (ID 51) - (14,18) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER5)
*   Viridian Forest (ID 51) - (3,19) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER4)

## Agent Management (9 Active Agents)
*   **`battle_strategist_agent`**: Analyzes battle data for optimal moves/switches. (System prompt reviewed T2861, OK).
*   **`route_planner_agent`**: Calculates paths. (Code-enabled) (System prompt reviewed T2861, OK).
*   **`level_cap_compliance_agent`**: Checks party vs. level cap.
*   **`wild_encounter_evaluator_agent`**: Advises on wild encounters (FIGHT, RUN, CATCH). (Review logic for EXP vs. progression).
*   **`optimal_training_spot_agent`**: Suggests training areas. (Code-enabled)
*   **`item_reminder_agent`**: Reminds about nearby uncollected items.
*   **`map_analyzer_agent`**: Identifies strategic points on current map. (Code-enabled)
*   **`team_composition_advisor_agent`**: Recommends teams for major battles. (Code-enabled) (Test before Brock).
*   **`pokedex_completion_strategist_agent`**: Suggests areas for Pokédex completion. (Code-enabled) (System prompt updated T2807, revised T2821. Monitor effectiveness).
    *   **Agent Development Plan (Focus Areas):**
    1.  Monitor effectiveness of `pokedex_completion_strategist_agent` after system prompt updates.
    2.  Test `team_composition_advisor_agent` before challenging Brock.
    3.  Review `wild_encounter_evaluator_agent` logic for balancing EXP gain vs. progression speed.
    4.  Consider using `progression_advisor_agent` soon.
    5.  Note: Max 10 agents. Periodically review if all are providing value.

## Archived Plans & Hypotheses (Summarized)
*   **Route 2 (South) - HM Flash Aide Search (Turns ~1988-2002):** Pathing attempts to warp at (4,44) from southern Route 2 failed due to map layout (trees/ledges). Pivoted to Viridian City exploration.
*   **Viridian City Exploration (Turns ~2004-2324):** Explored southern part. Path to northern unseen tiles blocked by Y=10 ledge. Old Man (Gambler1) at (31,9) became inaccessible after being forced down Y=10 ledge post-Gym interaction (T2325). Gym locked. Exploration of Viridian City deemed complete for now.
*   **Viridian Forest NPC Notes (Turn 2205+, T2806, T2822):** Youngster 6 (VIRIDIANFOREST_YOUNGSTER6) at (28,41) gave Poké Ball tip, no battle.
*   **Viridian Forest North Gate NPC Notes (Turn 2467-2468):** Super Nerd (VIRIDIANFORESTNORTHGATE_SUPER_NERD) at (4,3) gave a tip about Pokémon in forests/caves, no battle. Gramps (VIRIDIANFORESTNORTHGATE_GRAMPS) at (3,6) gave a tip about Cut, no battle.
*   **Battle Flexibility:** When a Pokémon's HP becomes critical, reassess battle plan for survivability.
*   **Pewter City NPC Notes:** Cool Trainer M (PEWTERCITY_COOLTRAINER_M) at (18,26) says Brock is a serious trainer. (Non-battling)

## Current Major Unresolved Issues (as of Turn 2562, some addressed)
*   **No Boulder Badge:** Game State consistently shows 'None' for badges after the battle with Brock. This means the level cap is still 12. Must re-investigate and likely re-challenge Brock. (Still current)
*   **Pewter City Pokémon Center Entry Saga:** Resolved by blacking out and respawning in Viridian.
*   **Potion on Fainted Pokémon:** Confirmed Potions do not revive fainted Pokémon.

## Post-Blackout Update (Turn 2641 - Viridian City)
*   Blacked out after NADEL fainted to Jr. Trainer M's SANDSHREW in Pewter Gym. All 6 Pokémon fainted.
*   Respawned at Viridian City Pokémon Center (24,27).
*   Game state still confirms **NO BADGES HELD**. Level cap remains 12.
*   Money reduced to ¥198.
*   Critical Priority: Heal party, travel back to Pewter City, re-challenge Brock for Boulder Badge.
*   Jr. Trainer M in Pewter Gym (who defeated me, causing blackout) is NOT defeated.

## Non-Battling NPC Interactions Log (Key Ones)
*   Viridian Forest (ID 51) - (17,44) - Youngster (VIRIDIANFOREST_YOUNGSTER1) - Dialogue: "I came here with some friends! They're out for POKéMON fights!" - No battle.
*   Viridian Forest (ID 51) - (28,41) - Youngster (VIRIDIANFOREST_YOUNGSTER6) - Dialogue: "I ran out of POKé BALLs to catch POKéMON with! You should carry extras!" - No battle (Confirmed T2806, T2822).