# Route 3, Mt. Moon, and Cerulean City Progression Scratchpad
- Started: Turn 4122, Timestamp: Sunday, May 24, 2026 at 6:18 AM PDT

## Current Status:
- Turn 10871: Standing at (12, 9) on Map 0_61 (B2F). Battle switch prompt on Miguel's KOFFING. Selecting NO.
- Mt. Moon Progression Start: Turn 5170.

## Southern Bypass Corridor & Far-West Platform Layout (Turn 10809):
- **Bypass Corridor**: Rows 31 & 32 represent a fully passable, continuous horizontal bypass corridor of TYPE_2770 that spans from the Eastern Elevated Platform (Columns 32-34) all the way to the Far-Western Platform (Columns 7-11).
- **Western Platform (Columns 7-11)**:
  - Accessible on Rows 22-32 via the bypass.
  - Bound on the left by solid blue rock wall at Column 6.
  - Bound on the right by solid obstacles (TYPE_de37) at Columns 12 and 13 (from Row 19 down to Row 27).
  - On Turn 10807, we met and defeated a Team Rocket Grunt at (11, 17).
  - Standing at (11, 18) on Turn 10809, we observe:
    - Columns 7-11 are blocked north of Row 16 by a solid rock wall (TYPE_2889) at Row 15.
    - Columns 12-13 on Rows 14-18 are open cavern floor (TYPE_2770), forming a clear corridor going north.
  - **Plan**: Walk Right to Column 12, then proceed North along Columns 12-13 to see where this path leads.
  - **Test Hypothesis**: Columns 12-13 on Rows 10-13 are passable and connect the western cavern to the northern exit of Mt. Moon B2F.
  - **Exploration Path**: From (11, 18), move Right -> Up -> Up -> Up -> Up.

## TM01 Alcove Northern Boundary Testing Protocol (Completed Turn 10534):
- **Goal**: Physically test if Row 4 on Columns 28-30 is passable, to rule out any unverified assumptions about the northern boundary of the TM01 alcove and see if it connects to the elevated eastern platform.
- **Hypothesis**: Row 4 on Column 29 is a passable tile (e.g., an invisible passage or incorrect system wall classification).
- **Methodology & Empirical Verification**:
  1. Navigate from (32, 8) to (28, 8) on B2F using the lower corridor.
  2. Walk north up the stairs at (28, 7) or (29, 7) to enter the alcove.
  3. Stand at (29, 5) facing UP.
  4. Press 'Up' 1 time to attempt to step onto (29, 4).
- **Physical Test Log & Final Results**:
  - **Test 1 (Turn 10516)**: Stood at (29, 5) facing UP. Pressed 'Up' to step onto (29, 4) (labeled TYPE_2889). Result: Collided with solid rock wall (visited 0 tiles). Empirical Proof that (29, 4) is 100% solid and impassable.
  - **Test 2 (Turn 10528)**: Stood at (28, 5) facing UP. Pressed 'Up' to step onto (28, 4) (labeled TYPE_2889). Result: Collided with solid rock wall (visited 0 tiles). Empirical Proof that (28, 4) is 100% solid and impassable.
  - **Test 3 (Turn 10530)**: Stood at (30, 5) facing UP. Pressed 'Up' to step onto (30, 4) (labeled TYPE_2889). Result: Collided with solid rock wall (visited 0 tiles). Empirical Proof that (30, 4) is 100% solid and impassable.
- **Conclusion**: The entire northern boundary of the TM01 alcove (Columns 28-30, Row 4) is physically confirmed solid rock. This alcove is definitively a dead end. We have exhausted all apparent paths in B2F Columns 24-35.

## B1F Eastern Exploration Strategy (Turn 10534):
- **Objective**: Return to B1F at (25, 9) and explore the eastern side of B1F (Columns 26-39) to find the correct route to the elevated eastern chamber on B2F.
- **Hypothesis**: B1F does not terminate at Column 25. There is an unexplored eastern passage on Columns 26-39 on Rows 8-11 that leads to a new ladder going down to the B2F elevated eastern platform.
- **Routing Plan**:
  1. From (30, 5), walk Down 2 steps to (30, 7) (TYPE_2889/stairs? No, wait: walk Left to (28, 5) then Down 3 steps to (28, 8)).
  2. From (28, 8), walk Left 3 steps to (25, 8) then Down 1 step to (25, 9).
  3. Climb up the ladder at (25, 9) to B1F (25, 9).
  4. From B1F (25, 9), physically test walking Right into Column 26.
  5. Systematically map Columns 26-39 on B1F. Log every step and discovery to ensure high-value information retention.

## Progression Roadmap & Checklist:
- [x] Defeat Pewter Gym Leader Brock (Boulder Badge & TM34 secured!).
- [x] Healed team at Pewter City Pokémon Center at (13, 25).
- [x] Stock up on useful items at Pewter Poké Mart at (23, 17) (Secured 4 Potions, 3 Poké Balls, 3 Antidotes, 1 Paralyze Heal; ¥601 remaining).
- [x] Navigate east through Route 3 to Mt. Moon entrance.

## Completed B2F Western Path Exploration Plan (Turns 9356 - 9670 Archive):
- Verified B2F Central Platform is a cul-de-sac at the north end.
- Backtracked to NE cavern and verified the cliff barrier (Row 11/12 cliff) on B2F is impassable.
- Completed systematic test of B2F western corridor (Columns 12-13, Rows 22-27), confirming it is fully isolated and impassable.

## Exploration of New Northern/Eastern Cavern (Turn 9575):
- Started: Turn 9575, Timestamp: Monday, May 25, 2026 at 11:11 AM PDT
- Goals:
  - Walk past Grunt (29, 11) using Row 10 bypass.
  - Traverse east into the unknown cavern.
  - Locate Super Nerd Miguel and the fossils.
- **Socratic Resolution of Cognitive Dissonance (Turn 9724)**:
  - We physically tested Column 32 Row 12 (Down from (32,11)) and directly collided, proving that Column 32 Row 12 is a solid, impassable wall (despite the TYPE_2770 label).
  - However, the eastern corridor path in Mt. Moon B2F is historically known to run along the far-right columns (Column 34 or Column 35). Thus, Row 12 on Column 34 or Column 35 is highly likely to be the open vertical passage north to Miguel!
  - Therefore, we will proceed with the Central Platform route down to the Eastern Floor Area, head east, and explore Columns 34 and 35 going north to resolve the layout.
- **Western Corridor Connection Hypothesis & Test (Turn 10012)**:
  - **Hypothesis**: The pillar tile at (13, 22) on B2F (Map 0_61) is solid and impassable (TYPE_de37).
  - **Testing Method**: Standing at (14, 22) facing UP, press 'Left' once on Turn 10013 to attempt to step onto (13, 22).
  - **Result**: Visited 0 tiles, remaining at (14, 22). This empirically and definitively proves that (13, 22) is a solid, impassable rock pillar wall.

## B2F Central Platform Western Boundary Systematic Testing Protocol (Turn 10087):
- **Objective**: Determine if there is a jumpable ledge or passage on the west side of the B2F Central Platform (Columns 20-22, Rows 14-18) connecting directly to the western corridor (Columns 10-11).
- **Hypothesis**: The west edge of the B2F Central Platform around Column 20 (Rows 14-18) features a one-way jumpable ledge (or passage) leading west.
- **Methodology & Systematic Testing Plan**:
  - Starting Turn: [To be filled when we arrive on B2F Central Platform]
  - Starting Timestamp: [To be filled when we arrive on B2F Central Platform]
  - **Verification Steps**:
    1. Stand at (20, 14) facing Left -> press 'Left' 1 time. Verify if position becomes (19, 14) or (20, 14).
    2. Stand at (20, 15) facing Left -> press 'Left' 1 time. Verify if position becomes (19, 15) or (20, 15).
    3. Stand at (20, 16) facing Left -> press 'Left' 1 time. Verify if position becomes (19, 16) or (20, 16).
    4. Stand at (20, 17) facing Left -> press 'Left' 1 time. Verify if position becomes (19, 17) or (20, 17).
    5. Stand at (20, 18) facing Left -> press 'Left' 1 time. Verify if position becomes (19, 18) or (20, 18).
  - **Rigorous Proof of Work**: Record the exact turn number, action, and resulting position for each of the 5 tests above.
  - **Contingency Plan & Eastern Passage Testing Protocol**:
    - *If a ledge is found*: We will jump west to Column 19, verify we landed on the western cavern floor, and explore the newly accessible area. We will document it as a permanent new overworld bypass.
    - *If no ledge is found*: We will confirm that the Central Platform is a dead end to the west. We will backtrack via the stairs at (26, 15)/(27, 15), walk east past the Rocket Grunt at (29, 17) to (34, 13) or (35, 13), and systematically test the vertical passability of Row 12 on Columns 34 and 35:
      1. Stand at (34, 13) facing UP and press 'Up'. Verify if position becomes (34, 12).
      2. If blocked, stand at (35, 13) facing UP and press 'Up'. Verify if position becomes (35, 12).
      3. If either is successful, attempt to walk further UP into (34, 11) or (35, 11) to reach the northern area.
      4. Record the exact turn numbers and results to empirically prove if Column 34/35 is our true open vertical corridor.
## B2F Central Platform Western Boundary Systematic Testing Protocol Live Execution (Turn 10288):
- Starting Turn: 10288
- Starting Timestamp: Monday, May 25, 2026 at 2:35 PM PDT
- Test 1 (Turn 10292): Standing at (20, 14) facing LEFT, pressed 'Left'. Result: Visited 0 tiles, player remained at (20, 14). This proves (19, 14) is blocked and impassable.
- Test 2 (Turn 10299): Standing at (20, 15) facing LEFT, pressed 'Left'. Result: Visited 0 tiles, player remained at (20, 15). This proves (19, 15) is blocked and impassable.
- Test 3 (Turn 10302): Standing at (20, 16) facing LEFT, pressed 'Left'. Result: Visited 0 tiles, player remained at (20, 16). This proves (19, 16) is blocked and impassable.
- Test 4 (Turn 10305): Standing at (20, 17) facing LEFT, pressed 'Left'. Result: Visited 0 tiles, player remained at (20, 17). This proves (19, 17) is blocked and impassable.
- Test 5 (Turn 10311): Standing at (20, 18) facing LEFT, pressed 'Left'. Result: Visited 0 tiles, player remained at (20, 18). This proves (19, 18) is blocked and impassable.
- Final Western Boundary Conclusion (Turn 10312): Systematic passability testing of Column 20 (Rows 14-18) facing LEFT has been completed. All five coordinates ((19, 14), (19, 15), (19, 16), (19, 17), (19, 18)) are completely impassable. This definitively disproves the hypothesis of a jumpable ledge or passage on the west edge of the Central Platform. The Central Platform is a dead end to the west.

## B2F Northeastern Section Systematic Exploration Plan (Turn 10383):
- Goal: Systematically explore the northeastern corridor (Columns 31-35, Rows 3-9) of Mt. Moon B2F, locate Super Nerd Miguel, and obtain a fossil.
- Context: On Turn 9670, we reached (33, 10). On Turn 9694, standing at (32, 11), we verified that moving south into (32, 12) is blocked by a solid cliff wall. However, we never walked north (UP) into Rows 3-9 from Column 33 or 34!
- Systematic Exploration Strategy:
  1. Travel to B2F (25, 9) north-central section by using 1F (17, 11) -> B1F (25, 9) -> B1F (17, 11) -> B2F (25, 9).
  2. From (25, 9) on B2F, walk east past the Rocket Grunt at (29, 11) using the Row 10 bypass, reaching (33, 10).
  3. Stand at (33, 10) and face UP (north). Press 'Up' to step into Row 9.
  4. Systematically map every coordinate from Row 9 up to Row 3 within Columns 31 to 35. 
  5. We will record the exact starting turn, timestamp, actions, and resulting positions for this exploration to prevent Time Blindness and rigorously document our proof of work.
## Traversal to Northeast Section (Turn 10418):
- Starting Turn: 10418
- We are at (11, 17) on 1F, facing Down.
- Goal: Get to the north-central ladder at (17, 11) on 1F.
- Pathing Details:
  - There is a Youngster NPC at (12, 16).
  - Column 12 and 13 are solid walls (TYPE_2889) on rows 13-15.
  - Rows 16, 17, 18, 19 of Column 13 are fully passable (TYPE_3fe2).
  - Let's check Row 17:
    - (12, 17) is TYPE_3fe2 (passable)
    - (13, 17) is TYPE_3fe2 (passable)
    - (14, 17) is TYPE_3fe2 (passable)
    - (15, 17) is TYPE_3fe2 (passable)
    - (16, 17) is TYPE_3fe2 (passable)
    - (17, 17) is TYPE_3fe2 (passable)
  - So from (11, 17), we can walk straight Right 6 steps to reach (17, 17):
    - 1. Right to (12, 17)
    - 2. Right to (13, 17)
    - 3. Right to (14, 17)
    - 4. Right to (15, 17)
    - 5. Right to (16, 17)
    - 6. Right to (17, 17)
  - From (17, 17), we can walk straight Up 6 steps to reach (17, 11):
    - 1. Up to (17, 16)
    - 2. Up to (17, 15)
    - 3. Up to (17, 14)
    - 4. Up to (17, 13)
    - 5. Up to (17, 12)
    - 6. Up to (17, 11) (which is the ladder).
  - Total sequence: ['Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Up', 'Up', 'Up', 'Up', 'Up', 'Up']
## Northeastern Section Systematic Exploration Live Log (Turn 10460):
- Starting Turn: 10460
- Starting Timestamp: Monday, May 25, 2026 at 3:15 PM PDT
- Current Position: (32, 9)
- Visual Map Data from `<CurrentScreen turn="10460">`:
  - Columns 32 to 35, Rows 5 to 11 are visible on screen.
  - Let's map out the tiles:
    - Row 9:
      - (32, 9): Player standing here (TYPE_3fe2).
      - (33, 9): TYPE_2889 (solid rock wall).
      - (34, 9): TYPE_3fe2 (cavern floor).
      - (35, 9): TYPE_3fe2 (cavern floor).
    - Row 8:
      - (32, 8): TYPE_3fe2 (cavern floor).
      - (33, 8): TYPE_3fe2 (cavern floor).
      - (34, 8): TYPE_3fe2 (cavern floor).
      - (35, 8): TYPE_3fe2 (cavern floor).
    - Row 7:
      - (32, 7): TYPE_3fe2 (cavern floor).
      - (33, 7): TYPE_3fe2 (cavern floor).
      - (34, 7): TYPE_3fe2 (cavern floor).
      - (35, 7): TYPE_3fe2 (cavern floor).
    - Row 6:
      - (32, 6): TYPE_3fe2 (cavern floor).
      - (33, 6): TYPE_3fe2 (cavern floor).
      - (34, 6): TYPE_3fe2 (cavern floor).
      - (35, 6): TYPE_3fe2 (cavern floor).
    - Row 5:
      - (32, 5): TYPE_2889 (solid rock wall).
      - (33, 5): TYPE_2889 (solid rock wall).
      - (34, 5): TYPE_2889 (solid rock wall).
      - (35, 5): TYPE_2889 (solid rock wall).
  - This is fascinating! Row 5 is a solid rock wall (TYPE_2889) on Columns 32-35.
  - This means the northern wall of this area is at Row 5.
  - Let's look further left on Row 5:
    - (31, 5): TYPE_2889 (solid wall)
    - (30, 5): TYPE_2770 (cavern floor)
    - (29, 5): TYPE_2770 (cavern floor)
    - (28, 5): TYPE_2770 (cavern floor)
  - Wait, columns 28 to 30 on Row 5, 6, 7 are accessible?
    - Yes, (29, 5) is where we collected TM01!
  - Let's check Row 6 and Row 7:
    - (31, 6) is TYPE_2889 (solid rock wall).
    - (30, 6) is TYPE_2770 (cavern floor).
    - (31, 7) is TYPE_2889 (solid rock wall).
    - (30, 7) is TYPE_2889 (solid rock wall).
    - (29, 7) is TYPE_4b8d (stairs).
    - (28, 7) is TYPE_4b8d (stairs).
  - This means Column 31 is a solid wall on Rows 5, 6, 7.
  - Wait, is Column 31 a solid wall on Rows 8, 9, 10, 11?
    - Let's look at the screen for Turn 10460:
      - (31, 8) is TYPE_3fe2.
      - (31, 9) is TYPE_3fe2.
      - (31, 10) is TYPE_3fe2.
      - (31, 11) is TYPE_3fe2.
    - These are cavern floors! This means there is a gap/passage between Column 31 and Column 32 on Rows 8 to 11.
  - Wait, let's look at Columns 36 and 37:
    - Column 36:
      - (36, 5): TYPE_2770
      - (36, 6): TYPE_2770
      - (36, 7): TYPE_2770
      - (36, 8): TYPE_2889 (solid rock)
      - (36, 9): TYPE_2889 (solid rock)
      - (36, 10): TYPE_2889 (solid rock)
      - (36, 11): TYPE_2889 (solid rock)
      - (36, 12): TYPE_2770
    - This means Column 36 is solid from Row 8 to Row 11!
    - So the cavern's eastern boundary on Rows 8-11 is at Column 36.
  - Let's find out what is in this open area (Columns 32-35, Rows 6-8):
    - Wait! Is there an NPC or item here?
    - On the screen, we see some sprite at (33, 9)? Wait, (33, 9) is TYPE_2889 (rock wall).
    - Wait! Is there any NPC in Columns 32-35 on Rows 6-8?
    - On the screen of Turn 10460, there is a giant blue-ish/gray-ish dome-shaped sprite at (33, 9)? No, wait, (33, 9) has a round rock sprite, which is the standard rock wall tile TYPE_2889.
    - Wait, let's look at Rows 6, 7, 8: they are completely empty cavern floor.
    - Wait, is there anything further to the right or left?
    - Let's walk north:
      - From (32, 9), walk Up to (32, 8).
      - From (32, 8), walk Right to (35, 8) to explore Row 8.
      - Let's walk to (35, 8):
        - Up 1 to (32, 8)
        - Right 3 to (35, 8)
- Turn 10486: Standing at (35, 7) on Map 0_61 (B2F). We have arrived at (35, 8) on Turn 10461 and moved to (35, 7) on Turn 10475.
- Cliff Boundary Discovery (Turn 10476): We attempted to walk Right from (35, 7) onto (36, 7) and directly collided with an impassable cliff face (visited 0 tiles). This empirically proves that Column 36 (Rows 4-7) is an elevated upper platform (TYPE_2770), and Column 35 is on the lower level (TYPE_3fe2). There is a vertical cliff boundary separating them, making the eastern elevated chamber currently inaccessible from this lower eastern area.
## B1F Column 25 Eastern Boundary Verification (Turn 10549):
- **Objective**: Physically test if Column 25 is a solid, impassable wall blocking any eastern traversal to Column 26 on Rows 8, 10, and 11.
- **Hypothesis**: Column 26 on Rows 8, 10, and 11 is solid rock, meaning Column 25 is the eastern boundary of B1F in this section.
- **Visual Check (Turn 10549)**: Standing at (24, 10), we can see:
  - (25, 9) is indeed a ladder (labeled TYPE_3fe2).
  - (25, 10) is labeled TYPE_2770, which is passable floor.
  - (25, 8) is labeled TYPE_2770, which is passable floor.
  - (25, 11) is labeled TYPE_2770, which is passable floor.
  - Column 26 on Rows 8, 9, 10, and 11 is labeled TYPE_2889 (solid rock).
- **Physical Test Plan**:
  - 1. Standing at (24, 10), walk Right to step onto (25, 10).
  - 2. Facing Right at (25, 10), press 'Right' to attempt to step onto (26, 10) (labeled TYPE_2889).
  - 3. Verify if player collides or is blocked, proving that Column 26 is impassable.
- **Execution of Step 1 (Turn 10550)**: Walk Right 1 step to stand on (25, 10).
- **Execution of Step 2 (Turn 10555)**: From (25, 10), pressed Right to walk into (26, 10) (labeled TYPE_2889).
- **Result (Turn 10556)**: Player collided with the wall (visited 0 tiles) and remained at (25, 10).
- **Final Verification Conclusion**: Column 26 is physically verified as solid rock wall and completely impassable. This definitively disproves the hypothesis of an eastern passage on B1F in this section. The B1F northeast section is indeed a completely isolated pocket. We must seek another way to access the eastern elevated chamber on B2F.
- **Next Action Plan**:
  - We will backtrack by taking the (25, 9) ladder up to 1F (17, 11).
  - From there, we will proceed to 1F (17, 17) -> 1F (11, 17) -> 1F (5, 5) -> B1F (5, 5) -> B1F (21, 17) -> B2F (21, 17) to access the Central Platform.
  - On the Central Platform, we will walk east down the stairs at (26, 15)/(27, 15), walk east past the Rocket Grunt at (29, 17) to (34, 13) or (35, 13), and systematically test the vertical passability of Row 12 on Columns 34 and 35. This is our primary remaining unexplored route on B2F!

## Super Nerd Miguel Battle Log (Turn 10820):
- Battle started on Turn 10820.
- Miguel's first Pokémon: Level 12 GRIMER.
- GEMMY is leading at Lv 23 (40/66 HP).
- Strategy: Use Water Gun to quickly defeat his Poison-type and other Pokémon.
- Turn 10821: Opened the FIGHT menu in the battle with Super Nerd Miguel's GRIMER.
- Turn 10824: Move menu wrapped successfully to WATER GUN. Initiating WATER GUN attack on GRIMER.
- Turn 10827: Selecting WATER GUN to finish off GRIMER.
- Turn 10829: GRIMER fainted! Miguel is sending in VOLTORB. Opting not to switch Pokémon (selecting NO).

## Socratic Reflections on Dungeon Exploration & Spatial Assumptions (Turn 10836):
- **The Core Mistake**: Previously, we concluded that the western platform on B2F was completely isolated from the southern area based on partial checks near Row 21, and we spent hundreds of turns backtracking up through B1F and 1F to find another way.
- **The Lesson Discovered**: A continuous horizontal corridor actually existed at the extreme south of B2F (Rows 31 & 32), bypassing all barriers and connecting the far-west platform directly to the eastern stairs.
- **Application to Future Layouts**:
  1. **Systematic Edge Probing**: Never declare an area "isolated" or "dead-ended" without exploring the absolute boundaries (e.g., Rows 31 & 32) of the grid, even if they seem out of the way or directionally unintuitive.
  2. **Avoid Generalizing Collisions**: Just because Column 14 Row 21 was blocked doesn't mean the entire vertical/horizontal traverse is blocked across all columns/rows. We must test every single candidate boundary tile individually before making a conclusion.
  3. **Visual Truncation Alert**: When some areas are off-screen, they must be treated as active exploration targets. We must use our custom pathfinding, systematic walking, and map markers to map the invisible spaces.
- Turn 10836: Battle progress - Deciding not to switch Pokémon for VOLTORB. Selecting NO.
- Turn 10838: Cursor is confirmed on NO. Pressing A to confirm and start the battle with VOLTORB.
- Turn 10839: Selecting NO to proceed with WARTORTLE (GEMMY) against VOLTORB.
- Turn 10842: In battle against Level 12 VOLTORB. Opening FIGHT menu to attack.
- Turn 10845: Standing at (12, 9) on B2F, fighting VOLTORB. Selected FIGHT to access moves list.
- Turn 10848: Moves menu confirmed open. Cursor is pointing at WATER GUN. Pressing A to attack VOLTORB.
- Turn 10852: VOLTORB is in the red. Opening FIGHT menu to select a finishing move.
- Turn 10856: Cursor is confirmed on BUBBLE (PP 10/30). Pressing A to attack and defeat VOLTORB.
- Turn 10858: GEMMY grew to Level 24 and is learning BITE. Plan to delete BUBBLE (redundant with WATER GUN) to make room for BITE. Selecting YES.
- Turn 10863: Move forget menu is open. Cursor starts at TACKLE. Pressing Down twice to select BUBBLE for deletion.
- Turn 10867: Verified cursor is pointing directly at BUBBLE on the forget move screen. Pressing A to confirm forgetting BUBBLE.
- Turn 10869: GEMMY successfully forgot BUBBLE and learned BITE! Miguel is sending in KOFFING (Level 12). Select NO on the switch prompt.
- Turn 10875: KOFFING sent out. GEMMY remains in battle. Opening FIGHT menu to select our attack.
- Turn 10877: Battle against Miguel's Level 12 KOFFING continues. Opening FIGHT menu.
- Turn 10878: Confirmed battle menu is back with FIGHT selected. Pressing A to open moves menu.