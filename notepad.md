# Gem's Strategic Journal (v5.0)

## I. Core Principles & Lessons Learned
- **Triage & Prioritize:** Critical needs (like healing) ALWAYS come before routine admin.
- **Progression over Perfection:** The critical path is key. Don't get bogged down if the main objective is elsewhere.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions. My failure on the Eevee puzzle (wasting dozens of turns) is a key example. If 2-3 distinct hypotheses fail, abandon the objective.
- **Consult WKG & Agents for Route Planning:** Before any multi-map journey, use the `multi_map_route_planner_agent` and consult the WKG to verify connectivity. Do not assume 'shortcuts' work as expected.
- **Trust Agent Output:** When an agent (especially `pathfinder_agent`) reports "no path found," trust it. Re-evaluate my understanding of the map instead of repeating the failed request.
- **Mark Everything & Use Your Markers:** Diligently mark key locations and trust the warnings you set for yourself.
- **Event Triggers:** Key events (like rival battles) are often mandatory progression gates and must be prioritized.
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
- **Trainer Battle Initiation:** Some trainers (e.g., Cool Trainer F on Route 6) do not automatically initiate a battle when you enter their line of sight. Manual interaction by facing them and pressing 'A' is required.
- **Navigation Obstacle:** Defeated trainers act as impassable objects and must be navigated around.

## III. AI Observer Critiques & Action Plan
- **Critique (Turn 15571):** Inefficient menu navigation (one button per turn) and illogical goal hierarchy (Rock Tunnel before Flash).
- **Action Plan:**
    1. **IMMEDIATE:** Start chaining button presses in menus for efficiency. Use the `battle_menu_navigator` agent for complex sequences.
    2. **IMMEDIATE:** Correct goal order to: 1. Get Flash, 2. Reach Vermilion, 3. Go through Diglett's Cave.
    3. **SOON:** Test unused agents (`evolution_advisor_agent`, `training_hotspot_agent`).

## IV. Current Actionable Objectives (REVISED)
- **Primary Goal:** Obtain HM05 (Flash). **Plan:** Travel south through Route 6 to Vermilion City. Go east to Route 11 and enter Diglett's Cave. Traverse the cave to reach the isolated southern part of Route 2 where the aide with Flash is located.
- **Secondary Goal:** Acquire a drink for the Saffron City guard. **Plan:** Investigate the Celadon Dept. Store for a drink item (long-term objective).
- **Tertiary Goal:** Investigate the Machop in Vermilion City. **Plan:** Revisit the Machop after acquiring more badges or completing major story events.

## V. Key Discoveries & Navigational Lessons
- **CRITICAL NAVIGATION LESSON:** Route 2 is segmented. The Diglett's Cave exit at (13, 11) leads to a small, isolated northern section with no exits other than the warp back into the cave house. Do not use Diglett's Cave as a shortcut to Viridian Forest.
- **TMs Found:** TM08 (BODYSLAM), TM24 (THUNDERBOLT).
- **Key Items Found:** GOOD ROD, HM01 (CUT).
- **Lt. Surge's Raichu (Lv. 29):** Knows Body Slam and Surf.
- **Recurring Obstacles:** The tree at (16, 19) in Vermilion City respawns.

## VI. Open Questions & Assumptions to Test
- **EXP. All Mechanics:** The EXP distribution seems inconsistent. It might not be a true 'All'. **Hypothesis:** Only the active Pokémon and the Pokémon that started the battle get EXP. **Test:** Need to observe a battle from start to finish and check the EXP of all six party members.
- **Route 11 East Blockage:** I assume a Snorlax blocks the path east, but I haven't confirmed this visually. I need to explore eastward to identify the actual obstacle.
- **Underground Path Item:** The girl in the Route 6 gatehouse mentioned people lose things in the tunnel. This could be a hint for a hidden item. I need to re-explore the Underground Path N-S map (ID 119) and check for hidden items.