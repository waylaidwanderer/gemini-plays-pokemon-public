# Route 24 & Route 25 Location Records

## Layout & Navigation:
- **Southern Entrance**: Connects to Cerulean City. Transition is at Route 24 (11, 35) to Cerulean City (21, 0).
- **Nugget Bridge Bypass Routes**:
  - Youngster No. 3 at (11, 25) blocks Column 11. Bypass by walking on Column 10 from Row 23 to Row 26.
  - Lass Ali No. 2 at (10, 28) blocks Column 10. Bypass by walking on Column 11 from Row 26 to Row 29.
  - Bug Catcher Cale No. 1 at (11, 31) blocks Column 11. Bypass by walking on Column 10 from Row 29 to Row 35.

## Nugget Bridge Trainers & Sight Range Constraints:
- **Nugget Bridge No. 1**: Bug Catcher Cale at (11, 31) facing Down. Defeated on Turn 12014.
- **Nugget Bridge No. 2**: Lass Ali at (10, 28) facing Down. Defeated on Turn 12050.
- **Nugget Bridge No. 3**: Youngster at (11, 25) facing Down. Defeated on Turn 12211.
- **Nugget Bridge No. 4 Sight Range Constraint**:
  - **Hypothesis**: The Lass trainer at (10, 22) facing Down has a custom sight range.
  - **Testing Methodology**:
    - Turn 12228: Stepped onto Row 26 (4 tiles away). No trigger.
    - Turn 12233: Stepped onto Row 25 (3 tiles away). No trigger.
    - Turn 12234: Stepped onto Row 24 (2 tiles away). No trigger.
    - Turn 12237: Stepped onto Row 23 (1 tile away). No trigger.
  - **Results**: Verified. The Lass at (10, 22) has a sight range of exactly 0 tiles and must be spoken to directly from (10, 23) facing Up. Defeated on Turn 12309.
- **Nugget Bridge No. 5 Sight Range Constraint & Defeat**:
  - **Hypothesis**: Bug Catcher No. 5 at (11, 19) facing Down has a custom sight range.
  - **Testing Methodology (Turn 12417-12429)**: Stood at (11, 23) (4 tiles away), (11, 22) (3 tiles away), (11, 21) (2 tiles away), and (11, 20) (1 tile away). None of these triggered the battle.
  - **Results**: Verified on Turn 12429. Bug Catcher No. 5 has a sight range of exactly 0 tiles and must be spoken to directly from (11, 20) facing Up.
  - **Defeat (Turn 12447)**: Defeated on Turn 12447. Team: Mankey Lv 18. Gemmy swept with BITE. Marked with map marker (☠️).
- **Rocket Grunt (Map 0_35)**:
  - Location: (11, 15) facing Down.
  - Event Trigger: Automatically triggers when the player steps onto Row 15, Column 10 (or Column 11) on Turn 12496, showing a horizontal sight range of at least 1 tile or a full-row event-line trigger at Row 15.
  - Prize: Gives 1 GOLD NUGGET (verified in inventory on Turn 12499).
  - Battle: Initiated on Turn 12499. Defeated on Turn 12536. Team: Ekans Lv 15, Zubat Lv 15. Sparky and Gemmy switch-trained. Received ¥450 and 1 Gold Nugget. Marked with map marker (☠️).

## Route 25 Trainers & Sight Range Constraints:
- **Route 25 Trainer No. 1**: Hiker Franklin (represented by Youngster sprite) at (8, 4) facing Down.
  - Sight Range Constraint: Verified to have exactly 0 tiles of sight range on Turn 12591. Must be spoken to directly from (8, 5) facing Up to start battle.
  - Team: Machop Lv 15, Geodude Lv 15. Defeated on Turn 12638. Received ¥525. Sparky, Buggy, and Gemmy switch-trained. Marked with map marker (☠️).