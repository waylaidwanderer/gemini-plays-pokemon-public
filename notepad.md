# Gem's Strategic Journal (v4.2)

## I. Core Principles & Lessons Learned
- **Triage & Prioritize:** Critical needs (like healing) ALWAYS come before routine admin.
- **Progression over Perfection:** The critical path is key. Don't get bogged down if the main objective is elsewhere.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Consult WKG & Agents for Route Planning:** Before any multi-map journey, use the `multi_map_route_planner_agent` and consult the WKG to verify connectivity. Do not assume 'shortcuts' work as expected.
- **Trust Agent Output:** When an agent (especially `pathfinder_agent`) reports "no path found," trust it. Re-evaluate my understanding of the map instead of repeating the failed request.
- **Mark Everything & Use Your Markers:** Diligently mark key locations and trust the warnings you set for yourself.
- **Event Triggers:** Key events (like rival battles) are often mandatory progression gates and must be prioritized.
- **Battle Strategy (REFINED):**
    - Against wild Pokémon faster than my lead, if the first attempt to run fails, it is more efficient to fight with the most powerful super-effective move.
    - Always identify and prioritize using the most powerful super-effective moves to end battles quickly (e.g., Wing Attack vs. Ground-types).
- **Navigation (REFINED):**
    - **Verify map connectivity with the World Knowledge Graph** before assuming a "shortcut" (like Diglett's Cave) leads to the desired destination. Map segments can be isolated.
- **UI Glitch Troubleshooting:** When a menu or UI element bugs out, do not repeat the failing action. Systematically test every other available option on the screen to escape the loop. This was a hard lesson learned at the Cerulean PC.

## II. Game Mechanics & Battle Intel
- **Level Caps:**
    - 0 badges: 12
    - 1 badge: 21
    - 2 badges: 24
    - 3 badges: 35
- **Type Matchups (Verified):**
    - Flying: Super-effective (2x) vs. Ground.
- **Pokémon Evolutions:**
    - ECHO (Zubat) evolved into Golbat at Lv. 22.
- **New Moves Learned:**
    - ECHO (Golbat) learned Wing Attack, replacing Leech Life.

## III. Agent Log & Action Plan
| Agent Name                     | Status                | Action Item                                                                 |
|--------------------------------|-----------------------|-----------------------------------------------------------------------------|
| `pathfinder_agent`             | ✅ Reliable           | Use for single-map navigation.                                              |
| `unseen_tile_navigator_agent`  | ✅ Reliable           | Use for systematic exploration of unseen tiles.                             |
| `battle_menu_navigator`        | ✅ Reliable           | Use for all complex menu navigation in battles.                             |
| `tm_tutor_agent`               | ✅ Reliable           | Use for TM/HM decisions.                                                    |
| `progression_advisor_agent`    | ✅ Reliable           | **Use proactively** when entering new areas to confirm objectives.          |
| `multi_map_route_planner_agent`| ✅ Reliable           | Logic for non-contiguous maps now refined. Monitor for new edge cases.      |
| `rival_battle_strategist_agent`| ✅ Reliable           | **Use BEFORE next rival battle.** Proactive planning is more effective.      |
| `hm_mule_finder_agent`         | ❓ Untested           | **Test before next HM use** to validate its recommendations.                |
| `evolution_advisor_agent`      | ✅ Reliable           | **Test soon** to help plan long-term party development.                     |
| `pokemon_training_advisor_agent`| ❓ Untested           | **Test before next major battle** to formulate training plans.                |

## IV. Current Actionable Objectives
- **Objective:** Acquire HM05 (Flash). **Plan:** Travel through Diglett's Cave (accessible from Route 11, east of Vermilion City). The cave exits to the southern, previously inaccessible part of Route 2. The aide's house is located there, likely requiring Cut.
- **Objective:** Acquire a drink for the Saffron City guard. **Plan:** Investigate the Celadon Dept. Store for a drink item.
- **Objective:** Investigate the Machop in Vermilion City who is building something. **Plan:** Revisit the Machop after acquiring more badges or completing major story events.

## V. Key Discoveries & Navigational Lessons
- **CRITICAL NAVIGATION LESSON:** Route 2 is segmented. The Diglett's Cave exit at (13, 11) leads to a small, isolated northern section with no exits other than the warp back into the cave house. The main path from Pewter City to Viridian Forest is on a separate, unreachable part of this map. Do not use Diglett's Cave as a shortcut to Viridian Forest.
- **TMs Found:** TM08 (BODYSLAM), TM24 (THUNDERBOLT).
- **Key Items Found:** GOOD ROD, HM01 (CUT).
- **Lt. Surge's Raichu (Lv. 29):** Knows Body Slam and Surf.
- **Recurring Obstacles:** The tree at (16, 19) in Vermilion City respawns.

## VI. Open Questions & Assumptions to Test
- **EXP. All Mechanics:** The EXP distribution seems inconsistent. It might not be a true 'All'. **Hypothesis:** Only the active Pokémon and the Pokémon that started the battle get EXP. **Test:** Need to observe a battle from start to finish and check the EXP of all six party members.
- **Route 11 East Blockage:** I assume a Snorlax blocks the path east, but I haven't confirmed this visually. I need to explore eastward to identify the actual obstacle.

## VII. Future Agent Ideas
- `training_hotspot_agent`: An advanced version of the training advisor that could analyze my party's types and levels against all known wild encounter data to recommend the absolute most efficient grinding location on the world map.