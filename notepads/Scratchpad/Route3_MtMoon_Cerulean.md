# Route 3, Mt. Moon, and Cerulean City Progression Scratchpad
- Started: Turn 4122, Timestamp: Sunday, May 24, 2026 at 6:18 AM PDT

## Current Status:
- Turn 7538: Standing at (18, 6) on Map 0_14 facing UP. We are prepared to walk UP into (18, 5) to trigger the Mt. Moon 1F warp. Our team is fully healthy.

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
## Eastern Path Routing Theory (Row 18/19):
- **Verification of Eastern dead end**: Tested (47, 3) and (48, 3) and confirmed they are solid mountain walls. Column 50 is a solid wall, making this entire eastern pocket of the northern corridor a dead end.

## Unified Grounding & Warp Testing:
- On Turn 7502, we realized that we had a massive map-ID hallucination: Route 3 is Map 0_14, and there is no separate "Mt. Moon Exterior" map. Pewter City is Map 0_2. The Escape Rope returned us to Pewter City's Pokémon Center, not a Route 3 one.
- We has backtracked all the way west because of a massive coordinate hallucination thinking the Mt. Moon entrance was at (18, 5).
- However, looking closely at our logs, the Mt. Moon entrance is actually located at the far EAST end of Route 3 (Map 0_14), around column 47/48, which we previously explored before backtracking.
- On Turn 7406/7413, we tested (47, 3) and (48, 3) but those were solid. The actual cave entrance is on the eastern end, likely at (47, 4) or similar, which we must approach from below (such as from Row 5) or by walking UP. Let's head back east across the route to reach the eastern end and find the true Mt. Moon warp.
- Routing east from (18, 5):
  - We have successfully navigated to the far east end of Route 3.
  - Verification: We previously reached (47, 5) but walked horizontally onto it, which failed to trigger the directional warp. The actual Mt. Moon overworld cave entrance is indeed at (47, 5), but must be approached vertically by walking UP from (47, 6).
  - Backtracking Plan: From (49, 8) on Turn 7600, walk Left 12 steps to (37, 8), Up 2 steps through the (37, 7) bidirectional ledge gap to (37, 6), Up 1 step to (37, 5), Right 9 steps to (46, 5), Down 1 step to (46, 6), Right 1 step to (47, 6), and then walk UP into (47, 5) to trigger the Mt. Moon warp. We are beginning this sequence on Turn 7600 by walking Left 5 steps to (44, 8).