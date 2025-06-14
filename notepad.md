# Gem's Playbook (Post-Wipe Reflection 2.0)

## Core Strategy & Goals
- My goals are managed by the system. I will focus on achieving the current primary goal by making sound tactical decisions.

## Strategic Learnings & Battle Tactics
- **Recklessness leads to failure.** I must not engage in trainer battles with a weakened or status-afflicted party. Healing is always the top priority after a tough fight.
- **Retreat is a valid strategy.** Blacking out is inefficient and costly.
- **Preparation is key.** Before a battle, I will check my party's health and lead with a Pokémon that has a strategic advantage.
- **Utilize my tools.** I have powerful agents that can prevent catastrophic failures. I will use them.
- **Sacrifices must be calculated.** Losing a Pokémon should be a strategic choice to gain a significant advantage, not the result of a panicked, poorly thought-out switch.

## Defeated Trainers Log
- **OAK'S LAB:** Rival Pixel
- **ROUTE 22:** Rival Pixel
- **VIRIDIAN FOREST:** Lass (3,42), Youngster (28,20), Youngster (28,34), Bug Catcher (14,18), Bug Catcher (3,19)
- **PEWTER GYM:** Jr. Trainer M (4,7), Gym Leader Brock (5,2)
- **ROUTE 3:** Cool Trainer F (17,10), Youngster (15,6), Youngster (20,6), Lass (21,5), Youngster (23,10)

## Non-Battling NPC Log
- **ROUTE 3, Youngster (11, 7):** Non-battling NPC. Just talks about shorts.

## Key NPC Dialogue
- **PEWTER CITY, Cool Trainer F (9,16):** "It's rumored that CLEFAIRYs came from the moon! They appeared after MOON STONE fell on MT.MOON."
- **PEWTER CITY, Super Nerd (26,26):** "I'm spraying REPEL to keep POKéMON out of my garden!"

## Mechanics & Rules Discovered
- Defeated trainers act as solid obstacles and cannot be walked through.

## Failed Navigation Hypotheses (Pewter City)
- **Hypothesis 1 (Failed):** Long-distance manual pathing is reliable. (Attempted ~10 times, repeatedly blocked by unseen obstacles).
- **Hypothesis 2 (Failed):** `exploration_pathfinder_agent` can navigate cities. (Attempted 2 times, produced invalid paths).
- **Hypothesis 3 (Failed):** `npc_aware_pathfinder_agent` is foolproof. (Attempted 2 times, produced invalid paths, needs prompt update).
- **Conclusion:** Must use short, verifiable, manually-planned movements within complex areas.