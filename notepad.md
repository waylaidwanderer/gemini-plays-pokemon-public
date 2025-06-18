# Gem's Strategic Journal

## I. Core Principles & Lessons Learned
- **Execution Over Complexity:** Abandon multi-input commands. Break down actions (especially menu navigation) into simple, single-button presses per turn to ensure reliability.
- **Effective Training Protocol:** 'Bait-and-switch' is the correct method for training weaker Pokémon. Lead with the trainee, then immediately switch to a stronger Pokémon. Sending them into a guaranteed faint is inefficient.
- **Trust but Verify Agents:** Trust agent *logic* but adapt the *execution* of their plans into reliable, sequential steps.
- **Systematic Exploration:** Prioritize exploring all reachable unseen tiles before assuming a dead end.
- **Mark Everything:** Continue to diligently mark defeated trainers, used warps, and key locations.

## II. Game Mechanics & Battle Intel
- **Type Matchups (Verified):**
    - Grass is 4x effective vs. Rock/Ground.
    - Electric is not very effective vs. Electric or Bug/Grass (Paras).
    - Ice is super-effective vs. Grass.
- **Status Effects:**
    - Confusion wears off after battle.
    - Poison-types are immune to poison.
- **EXP Distribution:**
    - Pokémon at the level cap do not gain EXP.
    - All non-fainted party members share EXP.

## III. Active Objectives & Hypotheses
- **H1: Find Bill:** The primary path forward is east through the remainder of Route 25. This requires defeating all trainers in the way.
- **H2: Post-Bill Progression:** The police officer blocking the way to the robbed house in Cerulean City likely requires a story trigger related to Bill.

## IV. Agent Development Log
- **`battle_menu_navigator`:** Created and refined. Crucial for efficient and reliable battle menu navigation. Must be used consistently.
- **`unseen_tile_navigator_agent` & `pathfinder_agent`:** Proven reliable for overworld navigation.
- **`move_tutor_advisor`:** Created. Ready for use when a new TM is acquired.

## V. Progression Summary
- **Badges:** Boulder Badge (Brock), Cascade Badge (Misty).
- **Mt. Moon:** Cleared Team Rocket, chose the Dome Fossil.
- **Cerulean City:** Defeated rival Pixel. Discovered the path to Bill's house is north, not east through the police blockade.
- **Nugget Bridge (Route 24):** All trainers defeated. Received a Charmander (IGNIS).
- **Route 25:** Currently clearing trainers to reach Bill's Sea Cottage at the end of the route.

- **Situational Awareness & Flexibility:** Rules are guidelines, not unbreakable laws. Always adapt strategy to the current context. Survival and recovery must take precedence over compulsive completionism when the party is in critical condition.

## VI. Future Agent Ideas
- **Retreat Advisor Agent:** An agent to analyze party health/status and recommend if a retreat to a Pokémon Center is necessary. This will help prevent future reckless decisions.

## VII. Agent Development To-Do
- Create the 'Retreat Advisor Agent' to help with strategic decisions about when to return to a Pokémon Center.