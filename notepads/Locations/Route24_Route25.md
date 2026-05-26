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

- **Route 25 Trainer No. 2**: Youngster at (14, 3) (initially triggered at (14, 2) when stepping onto (14, 4)) facing Down.
  - Sight Range Constraint: Verified to have a sight range of at least 2 tiles on Turn 12651 (triggered when player was at (14, 4), walking down 1 tile to engage us). Since Rows 5 and 6 of Column 14 were not tested prior to the trigger, the exact maximum boundary is unproven but the minimum is 2 tiles.
  - Team: Rattata Lv 15, Spearow Lv 15. Defeated on Turn 12667. Received ¥225. Sparky and Gemmy switch-trained. Marked with map marker (☠️).
- **Route 25 Trainer No. 3**: Green-Vest Trainer at (18, 5) facing Down.
  - Sight Range Constraint: Verified to have exactly 0 tiles of sight range on Turn 12700. Must be spoken to directly from (17, 5) facing Right to interact.
  - Dialogue: "On S.S.ANNE, I saw trainers from around the world."
  - Status: Already defeated previously. Marked with map marker (☠️).
- **Route 25 Trainer No. 4**: Lass at (18, 8) facing Left.
  - Sight Range Constraint: Adjacent to (17, 8). Did not trigger when standing at (17, 8) facing Down (Turn 12704), but her boyfriend at (18, 5) was defeated, and she is adjacent.
  - Team: Nidoran♂ Lv 15, Nidoran♀ Lv 15. Defeated on Turn 12727. Received ¥225. Sparky and Gemmy switch-trained. Sparky leveled up to 16 and learned Quick Attack! Gemmy got poisoned by Poison Sting. Marked with map marker (☠️).

## Nugget Bridge Defeated Trainer Bypass Routes (Going North):
To walk north up Nugget Bridge from the Cerulean City transition at (21, 0) to Route 25 while completely avoiding collisions with the solid, defeated trainer sprites:
1. Transition onto Route 24 at (11, 35).
2. Walk Left 1 step to (10, 35).
3. Walk Up 5 steps along Column 10 to (10, 30) (bypassing Bug Catcher Cale at (11, 31)).
4. Walk Right 1 step to (11, 30).
5. Walk Up 3 steps along Column 11 to (11, 27) (bypassing Lass Ali at (10, 28)).
6. Walk Left 1 step to (10, 27).
7. Walk Up 3 steps along Column 10 to (10, 24) (bypassing Youngster No. 3 at (11, 25)).
8. Walk Right 1 step to (11, 24).
9. Walk Up 3 steps along Column 11 to (11, 21) (bypassing Lass No. 4 at (10, 22)).
10. Walk Left 1 step to (10, 21).
11. Walk Up 13 steps along Column 10 to (10, 8) (bypassing Rocket Grunt at (11, 15) and Bug Catcher No. 5 at (11, 19)).
12. Walk Right 1 step to (11, 8) and walk north into Route 25.