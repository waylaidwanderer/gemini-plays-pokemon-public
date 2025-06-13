# Gem's Pokémon Yellow Legacy Hard Mode Playthrough Notes

## Game Information
*   **Player Name:** Gem
*   **Rival Name:** Pixel
*   **Current Badges:** 0 (Game State is Source of Truth)
*   **Current Level Cap:** 12 (0 badges - Game State is Source of Truth)
*   **Pokédex:** 10/151 (HM05 FLASH requirement met!)
*   **Money:** ¥506 (Game State is Source of Truth)

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
    1.  Explore Viridian Forest: collect items (e.g., item at (13,30)), battle trainers, and train party members (especially FURYFIST, NADEL) aiming for levels closer to the cap (12) before Brock. Prioritize type advantages (Fighting vs. Rock). Catch new Pokémon if encountered and not yet in Pokédex. Use `wild_encounter_evaluator_agent` for fight/run/catch decisions.
    2.  Navigate through Viridian Forest North Gate to Route 2 (North).
    3.  Proceed to Pewter City.
    4.  Re-challenge Jr. Trainer M in Pewter Gym.
    5.  Re-challenge Brock. If battle is difficult, consult `team_composition_advisor_agent` and `battle_strategist_agent`.
*   **Travel to Pewter City (Secondary):** Achieved via steps for primary goal.
*   **Train in Viridian Forest (Tertiary):** Focus on FURYFIST and NADEL. Catch new Pokémon if encountered and not yet in Pokédex. Use `wild_encounter_evaluator_agent` for fight/run/catch decisions.
*   **Item Collection (Deferred - (13,30) Viridian Forest):** BFS path (118 steps) deemed tactically unsound for a single item given current training priorities. Will re-evaluate if a shorter path is found or item becomes critical.

## Lessons Learned, Game Mechanics & Insights
*   **Tile Types:** `ground`, `impassable`, `grass`, `ledge` (jump Y+2, impassable from Y+1 below), `cuttable`.
*   **Battle Menu (2x2):** FIGHT (top-left), PKMN (top-right), ITEM (bottom-left), RUN (bottom-right).
*   **Party List Selection:** 'A' on Pokémon opens sub-menu (SWITCH, STATS, CANCEL).
*   **Naming Screen:** 'START' confirms name. Plan inputs for efficiency.
*   **Poison:** Outside battle, -1 HP every 4 steps.
*   **Pikachu Movement:** Can walk through. Adjacent & not facing: 1st press turns, 2nd moves.
*   **Warp Types:** 1x1 instant (move off/on to re-warp). Larger warps (2x1, 1x2) may need 2 steps (onto warp, then into boundary/direction).
*   **Dialogue Clearing:** ALWAYS press 'A' to clear dialogue/text BEFORE other inputs.
*   **Type Matchups:** Ghost super effective vs. Psychic.
*   **Game Data Trust:** Game State Information is truth (badges, level caps, 'reachable'). Visual interpretation can be flawed.
*   **Interaction Loops:** If NPC/object interaction yields no progress after 2-3 attempts, different trigger needed.
*   **Coordinate Checks:** Verify current coordinates before planning movement.
*   **DV Checking:** Hold START while pressing A on STATS screen.
*   **Notepad `replace`:** `old_text` must be *exact*. `overwrite` for major changes.
*   **Pokémon Switching Menu (Battle):**
    1.  **To Switch OUT Active Pokémon:** From main battle menu, select 'PKMN'. The active Pokémon's sub-menu appears (or select active Pokémon if party list shows first). 'SWITCH' is usually the default. Press 'A'. This takes you to the party list to select the Pokémon to switch IN. Select desired Pokémon, press 'A'.
    2.  **To Switch IN a Benched Pokémon (if active Pokémon is *not* being switched out, e.g. after a faint):** From main battle menu, select 'PKMN'. Navigate to desired Pokémon in party list. Press 'A' to open its sub-menu. 'SWITCH' should be highlighted. Press 'A' to confirm.
    (Clarified after RATTATA battle menu confusion T2660-T2690 & T2703 reflection).
*   **Pathing Precision:** Analyze map memory/screen carefully, especially near ledges/complex terrain. Trust map memory for tile types.
*   **Pokédex Evaluation:** Professor Oak or aides evaluate in person (not via PC, corrected from Viridian Forest sign).
*   **Battle Risk Assessment:** Balance "less cautious" guideline with resource conservation.
*   **WKG Tool Usage:** Single `manage_world_knowledge` call per operation. Record transitions IMMEDIATELY.
*   **NPC Stun Usage (T2311, T2341):** When an NPC is excessively mobile and hindering interaction, the `stun_npc` tool should be considered and utilized much sooner.
*   **Agent Path Verification (T2341, T2380):** MUST manually verify `route_planner_agent` paths against map memory/XML *before* execution, especially for complex routes or near known obstacles. Consider using `map_analyzer_agent` for local alternatives if long paths fail.
*   **Battle Strategy vs. Progression (T2341, T2380):** Prioritize progression over marginal EXP gains from wild battles, especially when Pokémon are very low level. Run from battles more readily if not specifically training or catching.
*   **Map Markers (T2341, T2380):** Be consistent in marking ALL significant map features (used warps, key NPCs, obstacles, items obtained, key signs, etc.) that aid future navigation or recall. Example: Mark sign at (19,46) in Viridian Forest.

## Defeated Trainers Log
*   OAK'S LAB (ID 40) - (6,6) - Rival Pixel (initial battle)
*   Viridian Forest (ID 51) - (3,42) - Lass (Cool Trainer F sprite, VIRIDIANFOREST_COOLTRAINER_F)
*   Viridian Forest (ID 51) - (28,20) - Youngster (Bug Catcher sprite, VIRIDIANFOREST_YOUNGSTER3)
*   Viridian Forest (ID 51) - (28,34) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER2)
*   Viridian Forest (ID 51) - (14,18) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER5)

## Agent Management (9 Active Agents)
*   **`battle_strategist_agent`**: Analyzes battle data for optimal moves/switches.
*   **`route_planner_agent`**: Calculates paths. (Code-enabled)
*   **`level_cap_compliance_agent`**: Checks party vs. level cap.
*   **`wild_encounter_evaluator_agent`**: Advises on wild encounters (FIGHT, RUN, CATCH). (Review logic for EXP vs. progression).
*   **`optimal_training_spot_agent`**: Suggests training areas. (Code-enabled)
*   **`item_reminder_agent`**: Reminds about nearby uncollected items.
*   **`map_analyzer_agent`**: Identifies strategic points on current map. (Code-enabled)
*   **`team_composition_advisor_agent`**: Recommends teams for major battles. (Code-enabled) (Test before Brock).
*   **`pokedex_completion_strategist_agent`**: Suggests areas for Pokédex completion. (Code-enabled) (Failed T2324, requires review/debugging).
    *   **Agent Development Plan (Updated T2522):**
    1.  **COMPLETED (T2442):** Input schemas for ALL code-enabled agents reviewed.
    2.  **High Priority:** Review `pokedex_completion_strategist_agent` (failed T2324). Decide whether to debug, remove, or update notepad entry based on feasibility.
    3.  **High Priority (Pewter City):** Test `team_composition_advisor_agent` before challenging Brock.
    4.  Review `wild_encounter_evaluator_agent` logic for balancing EXP gain vs. progression speed.
    5.  Review `route_planner_agent` system prompt to emphasize its experimental nature for complex paths.
    6.  Review and potentially update the `battle_strategist_agent`'s system prompt to better consider Pokémon survivability under Hard Mode rules.
    7.  **New Task:** Test `progression_advisor_agent` (created T2510) soon to evaluate its effectiveness.
    8.  Note: Max 10 agents. Periodically review if all are providing value.

## Archived Plans & Hypotheses (Summarized)
*   **Route 2 (South) - HM Flash Aide Search (Turns ~1988-2002):** Pathing attempts to warp at (4,44) from southern Route 2 failed due to map layout (trees/ledges). Pivoted to Viridian City exploration.
*   **Viridian City Exploration (Turns ~2004-2324):** Explored southern part. Path to northern unseen tiles blocked by Y=10 ledge. Old Man (Gambler1) at (31,9) became inaccessible after being forced down Y=10 ledge post-Gym interaction (T2325). Gym locked. Exploration of Viridian City deemed complete for now.
*   **Viridian Forest NPC Notes (Turn 2205+):** Youngster 6 (VIRIDIANFOREST_YOUNGSTER6) at (28,41) gave Poké Ball tip, no battle.

*   Viridian Forest (ID 51) - (3,19) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER4)

*   **Viridian Forest North Gate NPC Notes (Turn 2467-2468):** Super Nerd (VIRIDIANFORESTNORTHGATE_SUPER_NERD) at (4,3) gave a tip about Pokémon in forests/caves, no battle. Gramps (VIRIDIANFORESTNORTHGATE_GRAMPS) at (3,6) gave a tip about Cut, no battle.

*   **Battle Flexibility:** When a Pokémon's HP becomes critical, reassess the current battle plan (even if agent-generated) and consider defensive switches or alternative moves to prioritize survivability, especially under Hard Mode rules.

*   **Pewter City NPC Notes:** Cool Trainer M (PEWTERCITY_COOLTRAINER_M) at (18,26) says Brock is a serious trainer, unlike Bug Catchers. (Non-battling)

## Current Major Unresolved Issues (as of Turn 2562)
*   **No Boulder Badge:** Game State consistently shows 'None' for badges after the battle with Brock. This means the level cap is still 12. Must re-investigate and likely re-challenge Brock.
*   **Pewter City Pokémon Center Entry Saga:** Repeated attempts (at least 12 noted via system warnings and my own count of ~5 distinct failed hypotheses from T2530-T2539, plus multiple attempts T2540-T2545, and then the final attempts before blacking out in T2546-T2548) to enter the Pewter Pokémon Center at (19,23)/(19,24) have failed. The exact warp mechanic for this 2x1 mat is not understood. Should have abandoned this approach much sooner and prioritized other healing methods or objectives.
*   **Potion on Fainted Pokémon:** Confirmed Potions do not revive fainted Pokémon (attempted on NIGHTSHADE in Pewter Mart, T2561). Need Revives or Pokémon Center access.

## Post-Blackout Update (Turn 2641 - Viridian City)
*   Blacked out after NADEL fainted to Jr. Trainer M's SANDSHREW in Pewter Gym. All 6 Pokémon fainted.
*   Respawned at Viridian City Pokémon Center (24,27).
*   Game state still confirms **NO BADGES HELD**. Level cap remains 12.
*   Money reduced to ¥198.
*   Critical Priority: Heal party, travel back to Pewter City, re-challenge Brock for Boulder Badge.
*   Jr. Trainer M in Pewter Gym (who defeated me, causing blackout) is NOT defeated.

## Non-Battling NPC Interactions Log
*   Viridian Forest (ID 51) - (17,44) - Youngster (VIRIDIANFOREST_YOUNGSTER1) - Dialogue: "I came here with some friends! They're out for POKéMON fights!" - No battle.

*   **Encounter Notes (Turn 2787-2789):** Wild WEEDLE battle with SPARKY active (T2787) ended inconclusively without EXP gain when an Up input was registered post-battle. Subsequently encountered another wild Lv4 WEEDLE (T2789) while moving towards Youngster at (28,41). System warning received to make longer movement sequences (T2788).