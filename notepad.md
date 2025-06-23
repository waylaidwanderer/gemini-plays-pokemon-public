# Gem's Strategic Journal (v53 - HM Mechanics Update)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information is the source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it. I must trust the data.
- **Agent Protocol:**
    - **Agent Failure Log:** My `battle_strategy_agent` has been proven unreliable due to flawed type-effectiveness data. My own observations about type matchups were also hallucinations. The agent has been updated to rely *only* on explicit in-game text for type effectiveness. I MUST test its outputs before fully trusting them.
    - `battle_menu_navigator` (Verified): The agent's prompt correctly states that menus do not wrap around. My previous assessment of it being flawed was incorrect.
    - `team_composition_advisor_agent`: I failed to use this agent before my first Giovanni attempt, which led to a team wipe. I will now use it to build my team.
- **Interaction Protocol:** If an interaction doesn't trigger as expected, do not repeat the same input. Immediately try a different input or a different approach.
- **WKG & Marker Protocol:** After any map transition, I must immediately add the nodes/edge to the WKG and mark both sides of the warp as 'Used'.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use (v2 - Confirmed):** Using an HM from the ITEM menu prompts you to teach it. You MUST teach the HM to a compatible Pokémon to enable its field use. Selecting 'NO' cancels the action. Once taught, the move can be used from the Pokémon's party menu.
- **HM General Usage:** A fainted POKéMON can use field moves like CUT.
- **EXP. All:** Distributes EXP to all non-fainted party members who participated in the battle (including those who were switched out). Pokémon at the level cap will show an EXP gain message but will not actually gain EXP.

## III. World Intel & Navigation
### Celadon City
- **Celadon Game Corner:** Team Rocket front. Secret hideout entrance behind a poster at (18, 5).

## IV. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Defeat the boss of the Rocket Hideout.
- **Secondary Goal:** Assemble and train a viable team for Giovanni.

### Current Plan (v6 - Rematch Prep)
1. **Team Assembly:** Use the `team_composition_advisor_agent` to determine the optimal team from my full roster.
2. **Team Management:** Go to the PC and withdraw/deposit Pokémon as per the agent's recommendation.
3. **Training:** Level up the new team members to be competitive against Giovanni's Lv. 29 Onix and Lv. 31 Kangaskhan, respecting the Lv. 35 cap.
4. **Rematch:** Return to the Rocket Hideout and defeat Giovanni.

### Hypotheses
- **Hypothesis 1 (Silph Scope):** The Silph Scope is the final reward in this hideout, held by Giovanni.
- **Hypothesis 2 (Snorlax):** The Snorlax on Route 16 requires the Poké Flute to be moved, but this is unverified in this ROM hack.

## V. Disproven Hypotheses & Failed Strategies
- **Giovanni Battle Attempt 1 (FAILED):** My team was completely unprepared for his Kangaskhan. My `battle_strategy_agent` provided critically flawed advice based on hallucinated type-effectiveness data (Poison vs. Rock), leading to multiple fainted Pokémon and an eventual team wipe. The plan to use Echo and Nightshade was a failure.
- **Rocket Grunt Battle (21, 13 on B2F):** Repeatedly trying to initiate this battle has failed. This interaction is either bugged or requires a specific trigger I have not yet found. This path is on hold.
- **Lift Key Location:** The Lift Key was not held by a specific grunt. I discovered I already possessed it.
- **HM Usage (v1 - DISPROVEN):** The initial hypothesis that HMs could be used directly from the ITEM menu without being taught was incorrect. Selecting 'NO' to teaching the move simply cancels the action. The move must be taught.

## VI. Reflection (Turn 20940)
- I should create a `training_advisor_agent` to help optimize leveling my team for major battles. It could suggest the best training spots based on my party, the level cap, and known wild encounters.

## VII. Agent Development Log
- **`training_advisor_agent` (Created T20991):** Designed to recommend optimal training locations based on party composition, level caps, and known wild encounters. This will help streamline the grinding process for major battles.