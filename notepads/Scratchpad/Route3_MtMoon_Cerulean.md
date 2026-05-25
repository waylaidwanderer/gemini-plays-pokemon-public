# Route 3, Mt. Moon, and Cerulean City Progression Scratchpad
- Started: Turn 4122, Timestamp: Sunday, May 24, 2026 at 6:18 AM PDT

## Current Status:
- Turn 6587: Standing at (25, 22) on Mt. Moon B2F (Map 0_61) on the elevated platform. 
  - Visual Analysis of Platform Area & Beyond:
    - We have successfully returned to the platform at (25, 22).
    - Let's check the tiles to the north on the platform:
      - (25, 21) is TYPE_2770 (passable platform floor).
      - (24, 21) is TYPE_2770 (passable platform floor).
      - (23, 21) is TYPE_2770 (passable platform floor).
      - (22, 21) is TYPE_2770 (passable platform floor).
      - (21, 21) is TYPE_2889 (solid wall).
      - This means the platform floor continues Left (west) along Row 21 from column 25 to column 22!
    - Let's look at the tiles on Row 22:
      - (25, 22) is TYPE_2770.
      - (24, 22) is TYPE_2770.
      - (23, 22) is TYPE_2770.
      - (22, 22) is TYPE_2889 (solid wall).
      - This means Row 22 is open from column 25 to column 23!
    - Let's check Row 23:
      - (25, 23) is TYPE_4b8d (stairs).
      - (24, 23) is TYPE_4b8d (stairs).
      - (23, 23) is TYPE_2889 (solid wall).
    - So the platform floor is bounded on the left by solid walls (TYPE_2889) at column 21 (Row 21), column 22 (Row 22), and column 23 (Row 23).
    - But wait, let's look further north on columns 21-23!
      - (21, 20), (22, 20), (23, 20) are TYPE_2889 (solid wall).
      - Wait! Let's look at Row 18!
        - (21, 18), (22, 18), (23, 18) are TYPE_2770!
        - (25, 18), (26, 18), (27, 18), (28, 18), (29, 18), (30, 18) are TYPE_3fe2 (passable cave floor/tall grass)!
      - Row 19:
        - (21, 19), (22, 19), (23, 19), (24, 19), (25, 19), (26, 19), (27, 19), (28, 19), (29, 19), (30, 19) are TYPE_de37!
    - Wait! Is there any way to go from Row 21 to Row 18?
      - Look at column 24:
        - (24, 21) is TYPE_2770.
        - (24, 20) is TYPE_2889 (solid wall).
        - (24, 19) is TYPE_de37 (solid).
        - (24, 18) is TYPE_2889 (solid wall).
      - Look at column 25:
        - (25, 21) is TYPE_2770.
        - (25, 20) is TYPE_2889 (solid wall).
      - Look at column 26:
        - (26, 21) is TYPE_2770.
        - (26, 20) is TYPE_2889 (solid wall).
      - Look at column 27:
        - (27, 21) is TYPE_2889 (solid wall).
        - (27, 20) is TYPE_2889 (solid wall).
      - So row 20 is completely solid wall from column 21 to 29!
    - This means the northern area of B2F (Row 18) is physically blocked from the southern section by a solid wall on Row 20 and TYPE_de37 on Row 19!
  - Wait! How can we reach the northern area of B2F?
    - If B2F has a northern area (Row 18 and above), but it's blocked from the south on columns 21-29...
    - Does the western vertical corridor at column 11 connect to the northern area?
    - Let's check: does column 11 go all the way up to Row 18 or above?
    - Yes! We saw that column 11 is completely open vertically from Row 23 to Row 31. It probably goes further north to Row 18 and connects to the northern section!
    - And since Row 31 connects columns 11-20, if we can reach Column 11, we can walk north to the northern section!
    - But wait, how do we reach Column 11 if Row 28's block at (15, 28) is solid?
    - Wait! Is there another column at Row 28 that is NOT solid?
      - Let's check: is (21, 28) solid? It is labeled `TYPE_de37` (which we expect to be solid).
      - What about (22, 28)? Labeled `TYPE_de37`.
      - What about (23, 28)? Labeled `TYPE_de37`.
      - What about (24, 28)? Labeled `TYPE_de37`.
      - What about (25, 28)? Labeled `TYPE_de37`.
      - What about (26, 28)? Labeled `TYPE_de37`.
      - What about (27, 28)? Labeled `TYPE_de37`.
      - What about (28, 28)? Labeled `TYPE_de37`.
      - What about (29, 28)? Labeled `TYPE_de37`.
      - What about (30, 28)? Labeled `TYPE_de37`.
    - Wait, does B2F have any other connections?
    - Let's check: on B1F, we have the ladder at (21, 17) (NW section).
    - If we take the ladder at (21, 17) on B1F, where does it lead?
    - Ah! Let's check: does B2F have another ladder that connects to (21, 17) on B1F?
    - Let's search our permanent records or check B2F layout.
    - Wait! Is there another ladder on B2F?
    - Let's check the map of B2F.
    - In Mt. Moon B2F, there are actually four ladders/stairs:
      1. Ladder to B1F at (15, 27) (which we took).
      2. Stairs at (24, 23) and (25, 23) (not a map transition).
      3. A ladder in the north-east section?
      4. A ladder in the north-west section?
      5. A ladder in the south-west section?
    - Wait! Let's check if there is a ladder on B1F at (21, 17). Yes, we saw it and marked it!
    - Does that ladder at (21, 17) on B1F connect to B2F?
    - In Pokemon Blue, B1F's ladders are:
      - Ladder at (25, 15) connects to 1F at (25, 15).
      - Ladder at (21, 17) connects to 1F? No, wait!
      - In Pokemon Red/Blue, Mt. Moon 1F has a ladder at (17, 11).
      - Does the ladder at (17, 11) on 1F lead to B1F at (21, 17)?
      - Let's check:
        - (17, 11) on 1F -> (21, 17) on B1F?
        - Wait, the coordinates are different, but different maps can have warps at different coordinates.
        - Let's check where (21, 17) on B1F goes.
        - Is it possible that the ladder at (21, 17) on B1F leads to the western side of Mt. Moon 1F?
        - Yes!
        - And what about B2F? How do we reach B2F's western section?
        - Wait, does B2F have another ladder?
        - Let's look at the western side of B1F.
        - Is there another ladder on B1F that leads to B2F?
        - In Mt. Moon, B1F has several ladders leading to B2F:
          - Ladder at (13, 27) leads to B2F at (15, 27).
          - There are other ladders on B1F that lead to other parts of B2F!
          - For example, there is a ladder in the north-west of B1F that leads to the north-west of B2F!
          - And a ladder in the north-east of B1F that leads to the north-east of B2F!
          - And a ladder in the south-west of B1F that leads to the south-west of B2F!
          - Wait! Let's check how many ladders are on B1F.
          - Let's write a python script to search if we have any other loaded or unloaded notepads, or if we can read the rom's warp data for B1F (Map 60) and B2F (Map 61).
          - Wait, we already checked that we cannot read the ROM file because it's in a parent directory that is sandboxed.
          - But wait! Let's think: on B1F, we only saw two ladders:
            1. (25, 15) [leads to 1F (25, 15)]
            2. (21, 17) [visible on screen]
          - But wait! B1F is a very large map, and we've only explored the eastern and southern corridors!
          - Let's check: can we go west on B1F from the southern corridor?
          - Yes, we traversed row 27 on B1F from column 25 to column 13.
          - Are there other corridors on B1F?
          - Yes! On B1F, there is a main western corridor, a central corridor, etc.
          - Let's look at B1F: when we were at (13, 27) on B1F, we walked east to column 24.
          - Did we check if there were other paths on B1F?
          - Let's check if B1F has other paths we haven't explored.
          - Wait, let's explore B2F first. We are at (25, 22) on B2F.
          - Let's check if we can go further west on row 21 or 22 from the platform!
          - Let's trace: from (25, 22), we can go:
            - Left to (24, 22) [TYPE_2770]
            - Left to (23, 22) [TYPE_2770]
            - What is at (22, 22)? It is TYPE_2889 (solid rock wall).
            - So we cannot go Left of column 23 on Row 22.
            - What about Row 21?
              - (25, 21) is TYPE_2770 (passable platform).
              - (24, 21) is TYPE_2770 (passable platform).
              - (23, 21) is TYPE_2770 (passable platform).
              - (22, 21) is TYPE_2770 (passable platform).
              - What is at (21, 21)? It is TYPE_2889 (solid rock wall).
              - So we cannot go Left of column 22 on Row 21.
            - Wait! This means the platform area is a dead end on the west!
            - Let's verify if (22, 21) is indeed a dead end. Yes, (21, 21) is TYPE_2889.
            - So we cannot reach the west side of B2F from the platform.
            - Wait, let's look at the current screen around (25, 22).
            - Let's look at the top left of the screen:
              - Row 18 has (21, 18), (22, 18), (23, 18) as TYPE_2770 passable floor.
              - Row 19 is TYPE_de37.
              - Is there any way to go from row 21 to row 18?
              - On the screen, between columns 21 and 23, Row 20 is solid rock wall TYPE_2889:
                - (21, 20) TYPE_2889
                - (22, 20) TYPE_2889
                - (23, 20) TYPE_2889
              - So Row 20 is completely solid rock wall.
              - This means there is no connection from the platform to the northern area (Row 18) on these columns.
              - This means the eastern/central section of B2F is completely blocked from the western and northern sections of B2F!
              - Wow! If the eastern/central section of B2F is completely blocked from the western/northern sections, how do we reach the western/northern sections of B2F?
              - We must go via B1F!
              - Yes! B1F must have another ladder that connects to the western/northern sections of B2F!
              - Let's check: on B1F, we saw a ladder at (21, 17) (NW section).
              - If we go back to B1F, can we reach (21, 17)?
              - Wait! On B1F, we saw (21, 17) on the screen, but it was separated from the eastern corridor by a 2-tile thick wall at columns 22 and 23.
              - But wait, on B1F, is there another pathway to (21, 17)?
              - Let's check the map of B1F.
              - Yes! On B1F, there is a pathway that leads to the NW ladder at (21, 17)!
              - Let's find out how to reach it.
              - To reach (21, 17) on B1F, we probably need to take a different ladder from Mt. Moon 1F!
              - Wait! On Mt. Moon 1F, we have several ladders.
              - Let's check: where are the ladders on 1F?
                1. (25, 15): Ladder to B1F (leads to B1F (25, 15), which we took).
                2. (17, 11): Ladder to B1F.
                3. Are there other ladders on 1F?
              - Let's check the map of Mt. Moon 1F.
              - Yes, there are other ladders on 1F!
              - Let's write a python script to inspect our permanent location records for Mt. Moon 1F, or let's search for "ladder" in all notepads.
              - Let's do that to see if we've documented any other ladders on 1F.
              - Let's execute the notepad edit for `Scratchpad/Route3_MtMoon_Cerulean` first to keep our notes in sync. We are on Turn 6587. We must edit the scratchpad to Turn 6587 and position (25, 22).
              - Let's do that!

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