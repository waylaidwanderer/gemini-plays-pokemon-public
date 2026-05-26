# Cerulean City Gym Location Records (Map 0_65)

## Overview & Transition:
- Entered from (30, 19) in Cerulean City on Turn 11456.
- Spawns us at (4, 13) inside the Gym.
- Leading Pokémon: SPARKY (PIKACHU, Level 11).

## Gym Guide Advice (Turn 11465):
- Standing at (7, 10). Spoke to him on Turn 11462.
- Advice: "The LEADER, MISTY, is a pro who uses water POKéMON! You can drain all their water with plant POKéMON! Or, zap them with electricity!"

## Layout & Exploration:
- Gym Guide is standing at (7, 10).
- Entrance corridor leads from (4, 13) to (4, 11) / (7, 11).
- Floor contains large water pools (TYPE_4e8c) and solid platforms.

## Active Combat & Training Protocol (Obsolete):
- This protocol is now obsolete. Misty has been defeated and our team has been fully leveled up and prepared.

## Trainers Defeated:
- [x] Swimmer ♂ at (6, 7): Defeated on Turn 11502. Team: Level 16 HORSEA, Level 16 SHELLDER. Sparky and Gemmy switch-trained. Received ¥80!
- [x] Jr. Trainer ♀ at (2, 3): Defeated on Turn 14511. Team: Level 19 GOLDEEN. Gemmy switch-trained and leveled up to 27! Received ¥380!
- [x] Gym Leader Misty at (4, 2): Defeated on Turn 14547. Team: Level 18 STARYU, Level 21 STARMIE. Gemmy swept with DIG! Received Cascade Badge and TM11 (Bubblebeam)!

## Active Verification & Damage Scaling Test (Obsolete):
- This verification test has been successfully completed. We measured our move damage scaling against the Gym's trainers, establishing a strong baseline that carried us to a swift victory against Gym Leader Misty.

## Misty Combat Math & Level 27 Stats (Turn 14525 Updates):
We successfully defeated the Gym's Jr. Trainer ♀ and analyzed our physical damage scaling before challenging Misty:
1. **Level 27 WARTORTLE (GEMMY) Status**: Grew to Level 27 during the Jr. Trainer ♀ battle. Current HP: 70/77. Moveset: DIG, TAIL WHIP, BITE, WATER GUN. Full stats to be documented post-battle.
2. **BITE Scaling Empirical Baseline**: BITE (60 power neutral physical) dealt ~60-65% damage (~27-29 HP) to the Jr. Trainer's Level 19 Goldeen (~45 HP).
3. **Misty's Starmie Combat Math**: Misty's Level 21 Starmie (~70 HP) has 61 Defense (which is double Goldeen's Defense). Thus, GEMMY's BITE is expected to deal only ~11-14 HP (~15-20% damage) to Starmie, resulting in a very slow 5-6 HKO.
4. **DIG Fallback Criticality**: DIG (100 power physical Ground) is 1.67x stronger than BITE. It is expected to deal ~18-21 HP (~25-30% damage) per hit to Starmie, guaranteeing a much safer and faster 3-4 HKO.
5. **Conclusion**: If SPARKY's Electric attacks fail, switching to GEMMY (Lv 27, 70/77 HP) to sweep with DIG is mathematically our most critical fallback weapon.