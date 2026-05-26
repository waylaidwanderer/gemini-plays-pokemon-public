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
- **Nugget Bridge No. 5**: Bug Catcher at (11, 19) facing Down. (Active/Unchallenged).