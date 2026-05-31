# Rocket Hideout B4F Layout Records (Map 0_202)
- **Staircase UP to B2F (Eastern Room)**: Located at (25, 6) on Map 0_201 (B3F). Connects symmetrically to B2F (Map 0_200) at (21, 8). This grants access to the northeast section of B3F.
  - **Staircase UP to B3F (Western Corridor)**: Located at (19, 10) on Map 0_202. Connects symmetrically to B3F (Map 0_201) at (19, 19) (Verified Turn 35235). This grants access to the western/left section of B4F.
  - **Column 21 Physical Separation**: The left (western) and right (eastern) sections of B4F are completely physically separated. In fact, the northeast room formerly misidentified as B4F eastern section is actually the northeast room of B3F (Map 0_201). Thus, there is no eastern section of B4F. To cross between B3F northeast and B3F/B4F west, one must backtrack through B2F.
- **B3F Northeast Section**: Migrated to Locations/RocketHideout_B3F_Layout on Turn 35674.
- **Defeated Trainers**:
  - Rocket Grunt 1: Standing at (26, 11)/(26, 12) on Map 0_201 (B3F Northeast). Defeated. Speaks about needing the Lift Key to run the elevator.
  - Rocket Grunt 2: Standing at (10, 22) on Map 0_201 (B3F). (Defeated).
  - Rocket Grunt 3: Standing at (11, 22) on Map 0_202 (B4F). (Defeated Turn 33850).
- **Collected Items**:
  - Rare Candy at (20, 14) (Collected Turn 33659).
  - TM10 (Double-Edge) at (26, 17) (Collected Turn 33978).
  - HP UP at (10, 12) (Collected Turn 35246 on B4F Map 0_202).
- **Collision Test at (9, 8)**: Tested on Turn 33693. Stood at (9, 9) facing Up and tried to walk Up onto (9, 8). Result: Collision. (9, 8) is a solid, impassable wall/table (TYPE_2889).
- **Burden of Proof & Northwest Room Openings (Row 8)**: Row 8 is a horizontal divider. Rather than assuming all columns are solid, we must systematically inspect Row 8's columns. On Turn 33944, column 20's Row 8 tile (20, 8) was visually observed to be TYPE_3fe2 (completely walkable floor), allowing direct vertical access from the spinner maze to the northern corridor (rows 5-7). This corridor extends westward to the true northwest section. We will test columns 10-15 on row 6/7/8 to find the true entrance to the northwest room.
- **Collision Test at (9, 25)**: Tested on Turn 33840. Tried to walk Left from (9, 25) but collided. This confirms that Column 8 is a solid, impassable wall boundary (TYPE_2889) in the southwest corner as well.
- **B4F Row 4 Columns 9-24 Systematic Passability and Interaction Testing Plan Results**:
  - We systematically tested the passability of the horizontal table boundary on Row 4 (Columns 9-24) from Row 5 to verify if there was any opening or interactive entity behind the table.
  - **Results**:
    - Columns 9-24 are all 100% solid on row 4. All interaction tests with 'A' on Row 5 facing Up yielded no-ops, proving that there are no interactive NPCs standing directly behind the table.

## B4F Column 21 Passability Testing (Turn 36277 - Turn 36297)
- **Verified Facts**:
  - Row 7: Tried to walk Right from (20, 7) onto (21, 7) on Turn 36277. Result: Collision. (21, 7) is 100% solid.
  - Row 6: Tried to walk Right from (20, 6) onto (21, 6) on Turn 36282. Result: Collision. (21, 6) is 100% solid.
  - Row 5: Tried to walk Right from (20, 5) onto (21, 5) on Turn 36284. Result: Collision. (21, 5) is 100% solid.
  - Row 4: Tried to walk Right from (20, 4) onto (21, 4) on Turn 36290. Result: Collision. (21, 4) is 100% solid.
  - Row 3: Tried to walk Right from (20, 3) onto (21, 3) on Turn 36291. Result: Collision. (21, 3) is 100% solid.
  - Row 2: Tried to walk Right from (20, 2) onto (21, 2) on Turn 36294. Result: Collision. (21, 2) is 100% solid.
  - Row 1: Tried to walk Right from (20, 1) onto (21, 1) on Turn 36296. Result: Collision. (21, 1) is 100% solid.
- **Conclusive Proof**: Column 21 is a completely solid vertical wall across all rows on B4F West, meaning B4F West is completely physically separated from the eastern room where the Lift Key Grunt stands. This confirms we must backtrack through B3F and B2F to access him.

## B4F Eastern Section & Giovanni's Room (Uncovered Turn 36864)
- **Arrival**: Warped from Map 0_203 (Elevator Cabin) at (2, 1) to Map 0_202 (B4F) at (25, 15) facing UP on Turn 36864.
- **Elevator Location**: Elevator doors are located on B4F at (24, 11) and (25, 11).
- **Guards**: Two Rocket Grunts are stationed in the hallway:
  - Grunt A at (23, 12) facing DOWN (guards column 23).
  - Grunt B at (26, 12) facing DOWN (guards column 26).
- **Layout**: Row 15 is blocked on the South by a solid wall on row 16. The corridor leads West via columns 21-22 on rows 14-15.
- **Plan**: Walk UP to row 14, then West to cross column 23, triggering a battle with Grunt A. Once defeated, we will explore the Western/Northern passageways to find Giovanni!