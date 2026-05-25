# Route 3, Mt. Moon, and Cerulean City Progression Scratchpad
- Started: Turn 4122, Timestamp: Sunday, May 24, 2026 at 6:18 AM PDT

## Current Status:
- Turn 6996: Reflection turn.
  - Progress: Explored western pathways of Mt. Moon 1F, discovered a ladder at (5, 5) and a Bug Catcher at (5, 6).
  - Goal Check: Bypassing Bug Catcher at (5, 6) by moving via column 4 to (5, 5).
  - Custom tool ideas:
    1. A pathfinder tool for Mt. Moon maps.
    2. A Pokemon Stat/EXP tracker.
    3. An inventory restock checklist.
    4. A battle turn analyzer.
    5. A map connectivity visualizer.
  - Tool maintenance: All tools are currently functioning and no custom tools are broken.
  - Goal clarity: Our objective is to reach Route 4. The method of using the western ladder is documented.
  - Error analysis: Verified that cave platform edges are impassable barriers, and ledge jumps are blocked if landing tiles are solid walls.

- Turn 6999: Standing at (3, 9) on Mt. Moon 1F (Map 0_59), facing Up. Discovered a new ladder at (5, 5) and a Bug Catcher at (5, 6). We are going to stealthily bypass the Bug Catcher by walking up column 4 to (4, 5) and stepping Right onto the ladder at (5, 5), completely avoiding his downward line of sight on column 5.

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

- Turn 6963: Standing at (16, 19) on Mt. Moon 1F (Map 0_59), facing Down. Let's perform some cleanups of redundant and obsolete lines in our scratchpad as requested by overwatch.

## B1F Exploration & Mapping Notes:
- None. (Cleaned up as requested by overwatch).

## Unverified 1F Visual Theories:
- Unverified 1F Visual Wall: Row 19 (e.g., Row 19 of Mt. Moon 1F) and Row 21 appear visually solid. We have NOT physically verified these barriers with direct collision testing yet, so we must treat them as unverified visual theories. We plan to explicitly perform collision tests on these boundaries when we return to 1F.
- Turn 6983: Standing at (3, 17) on Mt. Moon 1F (Map 0_59), facing Down.
  - Hypothesis: Ledge jump Down from (3, 17) (TYPE_3fe2) over (3, 18) (TYPE_2770) to (3, 19) is blocked because the landing tile (3, 19) is a solid rock wall (TYPE_2889).
  - Test Methodology: Pressed "Down" on Turn 6980 while standing at (3, 17) facing Down.
  - Result: Did not move from (3, 17) (verified by Turn 6983 Game State position still at (3, 17) and system warning "pressed 2 movement buttons, but visited 1 tiles").
  - Conclusion: Confirmed! Ledge jumps in Gen 1 are completely blocked if the landing tile is impassable (solid rock wall).
  - Next Plan: Explore the northern part of this western platform by walking Up 4 steps to Row 13.