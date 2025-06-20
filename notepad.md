# Gem's Strategic Journal (v8.3)

## I. Core Principles & Lessons Learned
- **Triage & Prioritize:** Critical needs (like healing) ALWAYS come before routine admin.
- **Progression over Perfection:** The critical path is key. Don't get bogged down if the main objective is elsewhere.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Consult WKG & Agents for Route Planning:** Before any multi-map journey, use the `multi_map_route_planner_agent` and consult the WKG to verify connectivity.
- **Trust & Refine Your Tools:** My custom agents are extensions of my own capabilities. If an agent's output seems wrong or it struggles with a task, it's a signal to refine its prompt or my understanding of its output, NOT to abandon it. Reverting to manual methods is inefficient.
- **Mark Everything & Use Your Markers:** Diligently mark key locations and trust the warnings you set for yourself.
- **Event Triggers:** Key events (like rival battles) are often mandatory progression gates and must be prioritized.
- **UI Glitch Troubleshooting:** When a menu or UI element bugs out, do not repeat the failing action. Systematically test every other available option.
- **Avoid Hallucinations:** I must be more diligent in exploring every tile of a map, even small rooms, to avoid miscounting unseen tiles. Trust game data over visual intuition.
- **WKG Management:** To improve efficiency, I will add all related nodes and edges for a new map connection in a single turn whenever possible. The system requires adding nodes and getting their IDs before creating an edge, so this may still take multiple turns. I will add nodes first, then the edge on the next available turn.

## II. Game Mechanics & Battle Intel
- **Level Caps:**
    - 0 badges: 12
    - 1 badge: 21
    - 2 badges: 24
    - 3 badges: 35
- **HM Usage:** A fainted POKéMON can still use field moves like CUT.
- **Type Matchups (Verified):**
    - Flying: Super-effective (2x) vs. Ground.
- **Pokémon Evolutions:**
    - ECHO (Zubat) evolved into Golbat at Lv. 22. ECHO grew to Lv. 23.
- **New Moves Learned:**
    - ECHO (Golbat) learned Wing Attack, replacing Leech Life.
- **Trainer Battle Initiation:** Some trainers require manual interaction; they do not auto-trigger on sight.
- **Navigation Obstacle:** Defeated trainers act as impassable objects.
- **EXP. All Mechanics (Verified):** EXP is distributed to all non-fainted Pokémon in the party, regardless of whether they participated in the battle.

## III. AI Observer Critiques & Action Plan
- **Critique (Turn 15661):** Wasted time trying to fix navigation agents on Route 6 instead of prioritizing the main quest.
- **Critique (Turn 15780):** Repeatedly providing incorrect data to agents, wasting time. Mindset of abandoning tools instead of refining them is a major strategic flaw.
- **Critique (Turn 15930):** Reactive exploration; assuming maps are clear without checking 'Reachable Unseen Tiles'. Unused `battle_move_advisor_agent`. Redundant notepad entries.
- **Critique (Turn 15982):** Reckless battle tactics, refusing to switch a confused SPARKY. Engaging new trainers with a critically wounded party. Poor risk assessment.
- **Critique (Turn 16265):** Over-reliance on `pathfinder_agent`. Failure to verify WKG data before attempting to add duplicates. Making unverified assumptions about NPCs.
- **Action Plan:**
    1. **IMMEDIATE:** Prioritize accurate data entry for all agent calls. Trust the Game State information as the absolute source of truth.
    2. **IMMEDIATE:** Prioritize clearing the current map of all trainers and unseen tiles before leaving for non-critical tasks like healing.
    3. **IMMEDIATE:** Test the `trainer_hunter_agent` at the next suitable opportunity to ensure its utility.

## IV. Current Actionable Objectives (REVISED)
- **Primary Goal:** Obtain HM05 (Flash).
- **Secondary Goal:** Investigate the Underground Path for a potential hidden item.
- **Tertiary Goal:** Acquire a drink for the Saffron City guard.

## V. Key Discoveries & Navigational Lessons
- **CRITICAL NAVIGATION LESSON:** Route 2 is segmented. The Diglett's Cave exit at (13, 11) leads to a small, isolated northern section. Do not use Diglett's Cave as a shortcut to Viridian Forest.
- **Lt. Surge's Raichu (Lv. 29):** Knows Body Slam and Surf.
- **Recurring Obstacles:** The tree at (16, 19) in Vermilion City respawns.
- **Route 11 Gatehouse Split:** The gatehouse east of Route 11 is divided into two sections. The west entrance (from Route 11) leads to a small room with no access to the eastern section where a guard blocks the path.

## VI. Open Questions & Assumptions to Test
- **Underground Path Item Hint (DEBUNKED):** A girl in the Route 6 gatehouse mentioned a lost item. **Hypothesis:** The lost item was HM05 Flash. **Result:** This was incorrect. HM05 Flash was obtained from Prof. Oak's Aide on Route 2. The lost item in the Underground Path is still unknown and a low priority.
- **Route 11 East Blockage:** I assume a Snorlax blocks the path east, but I haven't confirmed this visually. I need to explore eastward to identify the actual obstacle.

## VII. Agent Development Log
- **Healing Advisor Agent (Defined):** Created to combat reckless low-HP play by providing data-driven healing recommendations. It analyzes party health, finds the nearest Pokémon Center via the WKG, and assesses the risk of the travel path.
- **Unseen Tile Navigator Agent (Deleted):** This agent was made redundant by the more efficient `cluster_explorer_agent`. Deleted to make room for the `healing_advisor_agent`.