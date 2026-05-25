# Route 3, Mt. Moon, and Cerulean City Progression Scratchpad
- Started: Turn 4122, Timestamp: Sunday, May 24, 2026 at 6:18 AM PDT

## Current Status:
- Turn 7176: Successfully used ESCAPE ROPE to warp out of Mt. Moon. We have arrived safely on Route 3 at (13, 26), right in front of the Route 3 Pokémon Center door at (13, 25). We will enter and heal our entire team immediately!

## Progression Roadmap & Checklist:
- [x] Defeat Pewter Gym Leader Brock (Boulder Badge & TM34 secured!).
- [x] Healed team at Pewter City Pokémon Center at (13, 25).
- [x] Stock up on useful items at Pewter Poké Mart at (23, 17) (Secured 4 Potions, 3 Poké Balls, 3 Antidotes, 1 Paralyze Heal; ¥601 remaining).
- [ ] Explore the Museum of Science (optional, northern part of town).
- [x] Navigate east through Route 3 to Mt. Moon entrance.
- [ ] Traverse Mt. Moon to reach Route 4.
- [ ] Reach Cerulean City.

## Mt. Moon Team-Training Strategy & Timestamps (Turn 4801):
- Starting Turn for Pewter Restocking: Turn 4801
- Target Level-Ups:
  - **BUGGY (METAPOD)**: Lv 12 achieved! Learned Confusion!
  - **SPARKY (PIKACHU)**: Train to Level 11 to learn Quick Attack.

### SPARKY Training Session Log (Turn 6126):
- Starting Turn for SPARKY training: Turn 6126
- Starting Level: Level 6 (0/117 EXP)
- Target Level: Level 16 (to learn Quick Attack in Red/Blue)
- Timestamp: Sunday, May 24, 2026 at 3:25 PM PDT.
- Grinding Progress:
  - Turn 6149: Reached Level 7 after defeating Rocket Grunt's Level 11 Sandshrew (gained 108 EXP).
  - Turn 6168: Gained 66 EXP after defeating Rocket Grunt's Level 11 Rattata.
  - Turn 6198: Reached Level 8 after defeating Rocket Grunt's Level 11 Zubat (gained 63 EXP).
  - Turn 6263: Gained 69 EXP after defeating wild Level 9 Zubat.
  - Turn 6289: Gained 55 EXP after defeating wild Level 9 Geodude.
  - Turn 6307: Reached Level 9 and learned THUNDER WAVE! (Defeated wild Level 10 Zubat, gained 75 EXP).
  - Turn 6339: Gained 49 EXP after defeating wild Level 8 Geodude. SPARKY is now at Level 9 with 98/148 EXP.
  - Turn 6377: Gained 77 EXP after defeating wild Level 10 Zubat. SPARKY is now at Level 9 with 175/148 EXP.
  - Turn 6430: Gained 46 EXP after defeating wild Level 6 Zubat. SPARKY is now at Level 9 with 221/148 EXP.
  - Turn 6460: Defeated wild Level 8 Zubat. SPARKY gained 61 EXP (now Level 9 with 282/148 EXP).
  - Turn 6613: Defeated wild Level 10 Zubat. SPARKY gained 38 EXP and reached Level 10!
  - Turn 6825: Used RARE CANDY on SPARKY. He grew to Level 11! We discovered Pikachu learns Quick Attack at Level 16 in Red/Blue (unlike Level 11 in Yellow). Updating target to Level 16.
- Poké Ball & Capture Plan: We currently have 7 Poké Balls, which is plenty for any rare wild encounters inside Mt. Moon.

## B1F Exploration & Mapping Notes:
- None. (Cleaned up as requested by overwatch).

## Unverified 1F Visual Theories:
- Unverified 1F Visual Wall: Row 19 (e.g., Row 19 of Mt. Moon 1F) and Row 21 appear visually solid. We have NOT physically verified these barriers with direct collision testing yet, so we must treat them as unverified visual theories. We plan to explicitly perform collision tests on these boundaries when we return to 1F.

## Recovery Log:
- Turn 7165: Recovering from a custom tool error where TM34 was accidentally selected. The screen shows "Teach BIDE to a POKéMON?" with YES/NO. We will press B to cancel and return to the item menu to find our Escape Rope.
- Turn 7168: Verified cursor successfully moved down to ANTIDOTE in the item list. We will press Down again to move to PARLYZ HEAL.
- Turn 7179: Standing at (3, 7) inside the Route 3 Pokémon Center. We will walk straight up to the left counter tile at (3, 3) to heal our team.
- Turn 7181: Verified that Column 3 is completely open on the screen. We will press Up 4 times to move from (3, 7) to (3, 3).
- Turn 7183: Successfully arrived at the left counter tile (3, 3) in Route 3 Pokémon Center, facing UP. We will press A to talk to Nurse Joy and heal our team.
- Turn 7185: Standing at (3, 3) facing DOWN. Our team is still fainted because the previous dialog auto-advanced and canceled the healing prompt. We will press Up once to face UP towards Nurse Joy.
- Turn 7187: We are calling our custom tool 'heal_pokemon_at_counter' to execute the complete healing sequence with Nurse Joy. This bypasses the harness auto-advance so we can select HEAL safely.
- Turn 7191: Successfully verified in GameState that our entire team is 100% healed to full health! We are standing at (3, 3) facing UP inside the Route 3 Pokémon Center. We will now turn around and walk south to exit the building. Our path to the door at (3, 7) / (3, 8) is completely open.
- Turn 7195: Exited the Pokémon Center. We are standing outside on Route 3 at (13, 26) facing DOWN. Our team is fully healed. We will now head east back towards the entrance of Mt. Moon.