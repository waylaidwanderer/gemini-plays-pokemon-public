# Viridian Gym Location Records
- Map ID: 0_45 (Real Gym Map ID)

## Chronological Progress
- **Turn 95868**: Started the Viridian Gym Campaign.
- **Turn 95997**: Spoke to the old man at (30, 8), who confirmed: "VIRIDIAN GYM's LEADER returned!" The gym door is now unlocked.
- **Turn 96025**: Entered the real Viridian Gym (Map 0_45) at landing coordinates (16, 17) facing Up.

## Gym Internal Layout & Progression
### 1F Entrance Area (Rows 13-17, Columns 12-19)
- Landing / entrance tile is at (16, 17) / (17, 17).
- The Gym Guide (using a Tamer sprite on our screen) is located at (16, 15). Talking to him from (16, 16) facing Up triggers: "Yo! Champ in making! Even I don't know VIRIDIAN LEADER's identity! This will be the toughest of all the GYM LEADERs! I heard that the trainers here like ground-type POKéMON!"
- Two tall columns/statues are located at (15, 14)-(15, 15) and (18, 14)-(18, 15).
- Left-pointing arrow / conveyor tiles are located at (13, 16) and (13, 17) (TYPE_550d).
- Red-and-orange square / conveyor tiles are located at (13, 13) and (13, 14) (TYPE_55d4).
- A desk structure is visible on the far left at (12, 15)-(13, 15).

### NW Area (Rows 0-6, Columns 9-15)
- Toggling the conveyor on Column 19 Row 1 slid us all the way to (11, 1).
- A Blackbelt trainer (Karate King) at (10, 1) was defeated on Turn 96069.
- A Blackbelt trainer at (11, 11) was defeated on Turn 96140.
- A Cooltrainer♂ (Tamer sprite in overworld) at (12, 7) was defeated on Turn 96165. He initiated combat at (12, 9).
- A trainer (Tamer/Cooltrainer sprite) is located at (13, 5) facing Up.
- Solid walls of TYPE_2889 block vertical traversal at (11, 3), (12, 3), (13, 3), (14, 3), (15, 3).
- (11, 2) has a Down-pointing conveyor / arrow tile of TYPE_64a2.
## Spinner/Conveyor Test Campaign (Turn 96085)
- **Objective**: Identify the direction and exact behavior of conveyor tiles near the northeast.
- **Current Layout Observation**:
  - Stand: (18, 1) | Normal floor.
  - Right: (19, 1) | TYPE_55d0. Red tile with red/orange arrows pointing LEFT. (Confirmed in historical logs to slide player LEFT to column 11).
  - Down: (18, 2) | TYPE_55cd. Red tile with red/orange arrows pointing DOWN.
  - Down-Left: (17, 2) | TYPE_55d4. Red tile with orange solid squares.
  - Down-Right: (19, 2) | TYPE_55d4. Red tile with orange solid squares.
  - Below (18, 2): (18, 3) | TYPE_3fe2. Normal floor.
  - Below (19, 2): (19, 3) | TYPE_3fe2. Normal floor.
- **Action Plan**:
  - Test the Down conveyor at (18, 2) by stepping DOWN from (18, 1). This should slide us DOWN to (18, 3) or (18, 4) and grant access to the southern room.
- **Results & Empirical Findings (Turn 96086)**:
  - **Action**: Stepped Down from (18, 1) onto (18, 2).
  - **Result**: The player slid continuously DOWN from (18, 2) all the way to (18, 11).
  - **Conclusion**: The initial hypothesis of landing at (18, 3) or (18, 4) is DISPROVEN. The (18, 2) conveyor tile is a continuous vertical slide that forces traversal through the entire column all the way to (18, 11).