# Route 3, Mt. Moon, and Cerulean City Progression Scratchpad
- Started: Turn 4122, Timestamp: Sunday, May 24, 2026 at 6:18 AM PDT

## Current Status:
- Turn 6585: Standing at (28, 22) on Mt. Moon B2F (Map 0_61), facing Down. 
  - Visual Analysis of Eastern Section:
    - We are in a vertical corridor at Columns 28-29.
    - Northern end: blocked by solid wall TYPE_2889 at (28, 21) and (29, 21).
    - Southern end: blocked by TYPE_de37 at (28, 28) and (29, 28).
    - Left (west) connections: Row 24 is completely open across (27, 24) and (26, 24) [both TYPE_2770], connecting Columns 28-29 to the platform stairs area (Column 24-25).
    - Right (east) connections: Separated from the easternmost corridor (Columns 32-33) by a solid wall of TYPE_de37 at Columns 30-31.
  - Plan: Traverse west back onto the platform area. Path from (28, 22):
    - Down 2 steps to (28, 24) [TYPE_2770]
    - Left 3 steps to (25, 24) [TYPE_2770]
    - Up 2 steps to (25, 22) [TYPE_2770, platform floor]
  - Let's execute this movement.

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
- Target Level: Level 11 (to learn Quick Attack)
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
- Poké Ball & Capture Plan: We currently have 7 Poké Balls, which is plenty for any rare wild encounters inside Mt. Moon.

## B1F Exploration & Mapping Notes:
- Turn 6532: Visual verification of Mt. Moon B1F around (25, 15). Disproved the previous false assumption that Row 18 is a solid wall. Row 18 contains passable floor (TYPE_2770) across columns 24-27. In fact, rows 14-19 are all completely passable floor (TYPE_2770) for columns 24-27.
- Plan: Walk Down 4 steps to (25, 19) to explore the southern corridor of B1F and see where it leads.
- Turn 6556: We have successfully moved Down to (25, 27) on Mt. Moon B1F. Rows 26 and 27 are confirmed completely passable TYPE_2770 floor from column 21 to column 27. This southern horizontal passage connects the eastern corridor to the south-western area where the B2F ladder is at (13, 27).
- Plan: We will walk Left 4 steps along Row 27 to reach (21, 27). This will pan the screen left to show more of the southern corridor and help us trace the path to the western/south-western section of B1F.
- Turn 6572: Standing at (15, 27) on Mt. Moon B2F (Map 0_61), facing Down on the ladder. We are investigating access to the western corridor at Column 11. Row 31 appears visually open from Column 11 to Column 20, but Row 28 appears blocked from Column 12 to Column 20 by TYPE_de37 tiles, and Rows 29 & 30 are blocked by TYPE_2889 tiles. 
  - Hypothesis: Row 28 (between Columns 12 and 20) is solid and impassable, preventing direct southern access to Row 31.
  - Test Plan: Instead of immediately detouring, we will empirically test this hypothesis by attempting to walk Down onto (15, 28) on Turn 6572 to verify if TYPE_de37 on Row 28 is impassable at this coordinate. This provides proper proof of work.