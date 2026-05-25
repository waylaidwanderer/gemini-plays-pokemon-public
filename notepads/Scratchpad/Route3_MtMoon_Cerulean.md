# Route 3, Mt. Moon, and Cerulean City Progression Scratchpad
- Started: Turn 4122, Timestamp: Sunday, May 24, 2026 at 6:18 AM PDT

## Current Status:
- Turn 6558: Standing at (21, 27) on Mt. Moon B1F (Map 0_60), facing Left. Traversed west along Row 27 to (21, 27). Disproved the solid wall assumption on Row 18. Verified columns 24-27 are passable down to row 27. We are currently analyzing the paths on B1F to find a way to the western side of the map.

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
- Ladder to 1F: (25, 15) [Current Position]
- Ladder at (21, 17): We see a ladder of TYPE_3fe2 at (21, 17) on B1F. Let's investigate how to access it and where it connects.
- B1F Eastern Corridor:
  - (24, 15) to (27, 15) is passable.
  - Rows 14, 15, 16, 17, 18, 19 have passable paths around columns 24-27.
- Turn 6532: Visual verification of Mt. Moon B1F around (25, 15). Disproved the previous false assumption that Row 18 is a solid wall. Row 18 contains passable floor (TYPE_2770) across columns 24-27. In fact, rows 14-19 are all completely passable floor (TYPE_2770) for columns 24-27.
- Plan: Walk Down 4 steps to (25, 19) to explore the southern corridor of B1F and see where it leads.
- Turn 6556: We have successfully moved Down to (25, 27) on Mt. Moon B1F. Rows 26 and 27 are confirmed completely passable TYPE_2770 floor from column 21 to column 27. This southern horizontal passage connects the eastern corridor to the south-western area where the B2F ladder is at (13, 27).
- Plan: We will walk Left 4 steps along Row 27 to reach (21, 27). This will pan the screen left to show more of the southern corridor and help us trace the path to the western/south-western section of B1F.
- Turn 6568: Successfully took the ladder from B1F down to B2F at (15, 27). Looking closely at <CurrentScreen turn="6568">, we have discovered a major structural connection: Row 31 is completely open and passable floor (TYPE_2770) from Column 11 to Column 20! This forms a wide-open horizontal path connecting the eastern/central section of B2F directly to the western corridor at Column 11.
- Wait, Row 28 is fully blocked by solid blocks (TYPE_de37) from (12, 28) to (20, 28), and Rows 29 & 30 are blocked by solid rock wall (TYPE_2889). So we cannot walk south from our position at (15, 27) directly to Row 31 on these columns.
- However, Column 11 is completely open vertically from Row 23 down to Row 31.
- Let's check how we can reach the western corridor. If we can reach Row 31, we can walk west to Column 11.
- Where can we go south to reach Row 31? Let's trace east. On our previous exploration of B2F, we verified that the eastern corridor (columns 28 & 29) runs vertically from Row 26 down to Row 22. Does the eastern corridor at Column 28 or 29 continue down to Row 31?
- Let's walk east to the platform stairs at (25, 23) or the eastern corridor to find a passage leading south to Row 31!
- Let's trace the path from our current position (15, 27) to the eastern area. Path:
  - (15, 27) -> Up 1 to (15, 26) [TYPE_2770]
  - (15, 26) -> Right 10 steps to (25, 26) [all TYPE_2770]
  - Let's execute this chunk.