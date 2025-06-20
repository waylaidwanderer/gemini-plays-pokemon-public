# Gem's Strategic Journal (v7.1)

## I. Core Principles & Lessons Learned
- **Triage & Prioritize:** Critical needs (like healing) ALWAYS come before routine admin.
- **Progression over Perfection:** The critical path is key. Don't get bogged down if the main objective is elsewhere.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Consult WKG & Agents for Route Planning:** Before any multi-map journey, use the `multi_map_route_planner_agent` and consult the WKG to verify connectivity.
- **Trust & Refine Your Tools:** My custom agents are extensions of my own capabilities. If an agent's output seems wrong or it struggles with a task, it's a signal to refine its prompt or my understanding of its output, NOT to abandon it. Reverting to manual methods is inefficient.
- **Mark Everything & Use Your Markers:** Diligently mark key locations and trust the warnings you set for yourself.
- **Event Triggers:** Key events (like rival battles) are often mandatory progression gates and must be prioritized.
- **UI Glitch Troubleshooting:** When a menu or UI element bugs out, do not repeat the failing action. Systematically test every other available option.

## II. Game Mechanics & Battle Intel
- **Level Caps:**
    - 0 badges: 12
    - 1 badge: 21
    - 2 badges: 24
    - 3 badges: 35
- **Type Matchups (Verified):**
    - Flying: Super-effective (2x) vs. Ground.
- **Pokémon Evolutions:**
    - ECHO (Zubat) evolved into Golbat at Lv. 22. ECHO grew to Lv. 23.
- **New Moves Learned:**
    - ECHO (Golbat) learned Wing Attack, replacing Leech Life.
- **Trainer Battle Initiation:** Some trainers require manual interaction.
- **Navigation Obstacle:** Defeated trainers act as impassable objects.

## III. AI Observer Critiques & Action Plan
- **Critique (Turn 15661):** Wasted time trying to fix navigation agents on Route 6 instead of prioritizing the main quest.
- **Critique (Turn 15780):** Repeatedly providing incorrect data to agents, wasting time. Mindset of abandoning tools instead of refining them is a major strategic flaw.
- **Critique (Turn 15930):** Reactive exploration; assuming maps are clear without checking 'Reachable Unseen Tiles'. Unused `battle_move_advisor_agent`. Redundant notepad entries.
- **Action Plan:**
    1. **IMMEDIATE:** Prioritize accurate data entry for all agent calls. Trust the Game State information as the absolute source of truth.
    2. **IMMEDIATE:** Complete the full exploration of Route 11, defeating all trainers and identifying the eastern blockage.
    3. **IMMEDIATE:** After Route 11 is clear, proceed with the Primary Goal: Obtain HM05 (Flash).
    4. **NEW:** Test `battle_move_advisor_agent` in the next suitable wild encounter.

## IV. Current Actionable Objectives (REVISED)
- **Primary Goal:** Obtain HM05 (Flash). **Plan:** After clearing Route 11, enter Diglett's Cave. Traverse the cave to reach the isolated southern part of Route 2 where the aide with Flash is located.
- **Secondary Goal:** Acquire a drink for the Saffron City guard. **Plan:** Investigate the Celadon Dept. Store for a drink item (long-term objective).
- **Tertiary Goal:** Fully explore all routes accessible from my current location. **Plan:** Systematically clear each route of trainers, items, and unseen tiles before moving on.

## V. Key Discoveries & Navigational Lessons
- **CRITICAL NAVIGATION LESSON:** Route 2 is segmented. The Diglett's Cave exit at (13, 11) leads to a small, isolated northern section. Do not use Diglett's Cave as a shortcut to Viridian Forest.
- **Lt. Surge's Raichu (Lv. 29):** Knows Body Slam and Surf.
- **Recurring Obstacles:** The tree at (16, 19) in Vermilion City respawns.

## VI. Open Questions & Assumptions to Test
- **EXP. All Mechanics:** The EXP distribution seems inconsistent. **Hypothesis:** Only the active Pokémon and the Pokémon that started the battle get EXP. **Test:** Need to observe a battle from start to finish and check the EXP of all six party members.
- **Route 11 East Blockage:** I assume a Snorlax blocks the path east, but I haven't confirmed this visually. I need to explore eastward to identify the actual obstacle.
- **Underground Path Item:** The girl in the Route 6 gatehouse mentioned people lose things in the tunnel. This could be a hint for a hidden item. I need to re-explore the Underground Path N-S map (ID 119) and check for hidden items.

- **Underground Path Item Hint:** A girl in the Route 6 gatehouse mentioned people lose things in the tunnel. This could be a hint for a hidden item. I need to re-explore the Underground Path N-S map (ID 119) and check for hidden items.