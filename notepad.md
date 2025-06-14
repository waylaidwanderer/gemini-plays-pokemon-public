# Gem's Playbook v8

## Current Objective & Plan
- **Primary Goal:** Defeat Misty, get Cascade Badge.
- **Secondary Goal:** Heal party at Pewter City Pokémon Center.
- **Tertiary Goal:** Re-evaluate Route 3 navigation strategy.
- **Current Plan:** Retreat west through Route 3 to Pewter City to heal my critically injured party.

## Strategic Self-Improvement
- **Trust the Data:** I must trust the Game State Information (especially `Reachable` status for connections and tiles) over my own flawed assumptions. My failure to do so on Route 3 led to getting lost and nearly wiping my party.
- **Tactical Retreat:** Prolonged battles against non-essential wild Pokémon are a waste of resources. I need to be more willing to run, especially when my party is weakened or I am level-capped. The `wild_encounter_evaluator_agent` should be used to make these decisions.
- **Map Awareness:** I need to be more careful when exploring areas with one-way paths like ledges to avoid getting trapped in cul-de-sacs.

## Agent Development
- **`npc_aware_pathfinder_agent`:** This agent is buggy and unreliable. I need to update its system prompt with more explicit instructions for obstacle detection, as previously planned.
- **New Agent Idea:** Consider creating a 'crisis assessment' agent to recommend high-level actions (Retreat, Proceed, Explore) based on party status and location.

## Key Learnings & Game Mechanics
- **Poison:** Seems to wear off after a Pokémon's HP drops to a very low threshold outside of battle. This needs more testing to confirm the exact trigger.
- **Type Matchups:** Electric was 'not very effective' against the Grass/Poison Oddish. I must not rely on standard type charts and instead build a new one based on in-game observations.
- **Defeated Trainers:** They remain as impassable obstacles on the map.

## Defeated Trainers Log
- **ROUTE 3:** Lass (17,10), Youngster (15,6), Youngster (20,6), Lass (21,5), Youngster (23,10), Youngster (25,7), Lass (34,10)
- **PEWTER GYM:** Jr. Trainer M (4,7), Gym Leader Brock (5,2)
- **VIRIDIAN FOREST:** All trainers defeated.
- **ROUTE 22:** Rival Pixel
- **OAK'S LAB:** Rival Pixel