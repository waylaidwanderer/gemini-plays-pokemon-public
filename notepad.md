# Gem's Strategic Journal (v9.0)

## I. Core Principles & Lessons Learned
- **Progression Over Perfection:** The critical path is key. Do not get bogged down in tool refinement if it halts game progress. A working-but-imperfect tool is better than no progress.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Trust but Verify:** Trust agent outputs, but verify their performance with simple, non-critical tests before relying on them for major tasks.

## II. Game Mechanics & Battle Intel
- **Level Caps:**
    - 0 badges: 12
    - 1 badge: 21
    - 2 badges: 24
    - 3 badges: 35
- **HM Usage:** A fainted POKéMON can still use field moves like CUT.
- **Type Matchups (Verified):**
    - Flying: Super-effective (2x) vs. Ground.
- **Move Compatibility (CRITICAL DISCOVERY):** Pokémon move compatibility in this ROM hack differs from standard games. **SUBTERRA (Diglett) cannot learn HM05 Flash**. PULSAR (Magnemite) was able to learn it. I must always trust the in-game 'ABLE'/'NOT ABLE' feedback.
- **Pokémon Evolutions:**
    - ECHO (Zubat) evolved into Golbat at Lv. 22.
- **New Moves Learned:**
    - ECHO (Golbat) learned Wing Attack, replacing Leech Life.
    - PULSAR (Magnemite) learned Flash, replacing Tackle.
    - NIGHTSHADE (Gloom) learned Mega Drain at Lv. 25, replacing Absorb.
- **Trainer Battle Initiation:** Some trainers require manual interaction.
- **Navigation Obstacle:** Defeated trainers act as impassable objects.
- **EXP. All Mechanics (Verified):** EXP is distributed to all non-fainted party Pokémon.

## III. World Intel & Navigation
- **CRITICAL NAVIGATION LESSON:** Route 2 is segmented. The Diglett's Cave exit at (13, 11) leads to a small, isolated northern section. Do not use Diglett's Cave as a shortcut to Viridian Forest.
- **Lt. Surge's Raichu (Lv. 29):** Knows Body Slam and Surf.
- **Recurring Obstacles:** The tree at (16, 19) in Vermilion City and the tree at (16, 23) on Route 2 respawn.
- **Route 11 Gatehouse Split:** The gatehouse east of Route 11 is divided. The west entrance leads to a small room with no access to the eastern section where a guard blocks the path.
- **Item Discovery:** Found a MOON STONE on Route 2 (south section). Can be used to evolve LUNA (Clefairy) or SPIKE (Nidoran♂).
- **Underground Path Item Hint (DEBUNKED):** A girl in the Route 6 gatehouse mentioned a lost item. This has been fully investigated and was a dead end.
- **Route 11 East Blockage (Assumption):** I assume a Snorlax blocks the path east of the Route 11 gatehouse, but I haven't confirmed this visually.

## IV. Agent & Tool Strategy
- **Navigation Agent (Rebuilt):** The `route_navigator_agent` has been rebuilt to be the sole source of truth for pathfinding. It now requires testing on a simple, non-critical task.
- **Battle Advisor (FIXED):** The `battle_move_advisor_agent`'s prompt has been updated to correctly calculate multiplicative damage for dual-type Pokémon (e.g., 4x weakness).
- **Trainer Hunter Agent (Rebuilt):** The unreliable `trainer_hunter_agent` has been deleted and rebuilt with a more robust prompt. Requires testing.
- **New Agents (Defined & Untested):**
    - `pokemon_evolution_advisor`: To suggest optimal evolution timings.
    - `healing_advisor_agent`: To provide data-driven healing recommendations.
    - `tm_usage_advisor_agent`: To recommend optimal TM allocations.
- **Proactive Testing Mandate:** After defining or significantly refining an agent, I MUST devise a simple, non-critical test case to validate its functionality before relying on it for progression-critical tasks.

## V. Strategic Lessons & Course Corrections
- **Risk Management Failure (Route 9):** Pushing forward with a critically injured party resulted in being trapped by one-way ledges. This was entirely avoidable. I must prioritize healing and use my `healing_advisor_agent` before committing to paths with no return. Attrition is a real threat.

## VI. Agent Testing To-Do (Mandate)
- **Test Case 1 (`pokemon_evolution_advisor`): COMPLETE**
  - **Result:** Agent provided solid advice.
  - **Key Takeaways:**
    - SPARKY: Wait for Lv. 26 (Thunderbolt) before evolving.
    - NIGHTSHADE: Evolve now (needs Leaf Stone).
    - SUBTERRA: Wait for Lv. 31 (Slash).
    - PULSAR: Wait for Lv. 35 (Swift).
    - CRAG: Evolve at Lv. 25.
- **Test Case 2 (`trainer_hunter_agent`): COMPLETE**
  - **Result:** Agent correctly returned `trainer_found: false` when no trainers were present. The fix to prevent hallucinations was successful.
  - **Key Takeaways:** The agent is now reliable for identifying the presence or absence of trainers.
- **Test Case 3 (`tm_usage_advisor_agent`): ON HOLD**
  - **Reason:** Agent requires Pokémon stats (Attack, Defense, etc.) which are not available in the current game state information. Cannot be tested until this data is accessible.