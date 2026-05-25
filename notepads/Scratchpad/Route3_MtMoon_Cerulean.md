# Route 3, Mt. Moon, and Cerulean City Progression Scratchpad
- Started: Turn 4122, Timestamp: Sunday, May 24, 2026 at 6:18 AM PDT

## Current Status:
- Turn 6962: Standing at (16, 19) on Mt. Moon 1F (Map 0_59), facing Down. Just returned from the northern section of B2F. We are exploring the corridor and testing why we are blocked from going from (16, 19) to (16, 20). Let's make sure our team stays healthy. Our current navigation goal is to test the collision on the 1F southern corridors. Let's clean up our scratchpad as requested.

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
- Turn 6578: Standing at (15, 27) on Mt. Moon B2F (Map 0_61), facing Down on the ladder. Tested collision at (15, 28) (TYPE_de37) by pressing "Down" on Turn 6577. Result: Did not move from (15, 27). This empirically proves that (15, 28) is impassable. 
  - Verified Fact: The block of type TYPE_de37 at (15, 28) is solid and impassable.
  - Note on Row 28: Other columns of Row 28 (such as columns 12-14, 16-20, and 22-27) are visual obstacles of TYPE_de37 and are hypothesized to be impassable, but remain unverified by direct physical collision testing. We must treat them as unverified visual theories until tested.
  - Note on 1F: Unverified visual walls or blockages on Mt. Moon 1F (such as Row 19 and Row 21) are currently unverified by physical collision testing and are treated as unverified visual theories.

- Turn 6933: Switched from B2F back to B1F via the northwest ladder. Standing at (17, 11) on Mt. Moon B1F (Map 0_60), facing Down. We will navigate east to return to Mt. Moon 1F via the ladder at (25, 9).
  - Hypothesis: B1F (17, 11) ladder connects bidirectionally to B2F (25, 9).
  - Test Methodology: Came up the ladder at B2F (25, 9) on Turn 6928, ended up at B1F (17, 11) on Turn 6929.
  - Verification: Confirmed bidirectional connection. We will write this down in Locations/MtMoon_B1F.

## Unverified 1F Visual Theories:
- Unverified 1F Visual Wall: Row 19 (e.g., Row 19 of Mt. Moon 1F) and Row 21 appear visually solid. We have NOT physically verified these barriers with direct collision testing yet, so we must treat them as unverified visual theories. We plan to explicitly perform collision tests on these boundaries when we return to 1F.