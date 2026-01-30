# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026

### Current Status
- **Location**: Glitter Lighthouse 3F (Map 3_44).
- **Goal**: Find the way to 4F (Right Side).

### Lighthouse Navigation Fact Sheet
- **1F (3_42)**: Main Lobby. Stairs at (3,11) lead to 2F.
- **2F (3_43)**:
  - Stairs at (3,11) come from 1F.
  - Stairs at (5,3) go to 3F (Left Side).
  - Right Side: Explored, but NO stairs found yet. Needs re-verification if 3F fails.
- **4F (3_45)**:
  - Arrived via stairs at (13, 3).
  - Layout matches 3F: Central void, connected by bottom corridor.
  - **Action**: Bypassing Sailor Kent (defeated) at (7, 14) via Row 15.
  - **Goal**: Reach Left Side and find stairs to 5F.

### Immediate Plan
1. **Verify Window**: Check window at (4,1) one last time.
2. **Verify South 3F**: Walk past Chad to the south end of the room. Check for stairs or windows.
3. **Fallback**: If 3F is a dead end, scour 2F Right Side again.

### Objectives
- **Primary**: Obtain SecretPotion.
- **Secondary**: Heal Amphy.
- **Correction**: On Map 3_45 (Lighthouse 4F), the floor tiles are `TYPE_3fe2`. Previous navigation failed because I treated them as walls. `(3, 5)` is connected to the rest of the floor.
- **Map Structure**: Lighthouse 4F (3_45) has three vertical columns.
  - **Left (x=2-5)**: Isolated at top, accessible via Row 15? No, blocked at Row 11. 
  - **Center (x=8-9)**: Contains stairs to 5F at (9,7). Accessible via Top Row (Row 2).
  - **Right (x=12-17)**: Main vertical corridor. Connects to Center via Row 2.
- **Path to 5F**: From Bottom (Row 15), go Right to x=14, Up to Row 2, Left to x=8, Down to (9,7). Avoid (9,5) (Potential Hole).
- **Lighthouse 5F (3_46)**: Arrived at `(3, 5)`. This Left Section seems isolated from the Center Column. The Center Column (with stairs to 6F) is likely only accessible from **4F Center**.
- **Plan**: Go back to 4F, navigate to Row 2, then across to `(9, 2)` and down to `(9, 7)` to ascend to 5F Center.
### Reflection (Turn 18521)
- **Status**: Currently on 5F (Left). Confirmed this section is a dead end (no items, just a window).
- **Correction**: The "falling from 5F" strategy was a hallucination. The "void" at (9,4) is a wall.
- **New Hypothesis**: The path to the Center Column is on **4F**, via the **Top Row (Row 2)**.
- **Action Plan**:
  1. Return to 4F via stairs at (3,5).
  2. Navigate from Left Side to Right Side via Bottom Corridor (Row 15), bypassing Sailor Kent.
  3. Go UP the Right Side to Row 2.
  4. Walk LEFT along Row 2 to reach the Center Stairs at (9,7).
  5. Take those stairs to 5F (Center).
- **Correction**: The Center Box on 4F (x=8-9, y=4-7) is FULLY ENCLOSED by walls and holes on this floor. It cannot be entered from 4F.
- **Hypothesis**: The entrance is from **3F**, via a ladder/stairs that leads up to `(9, 5)` (marked "To 3F Sailor Room").
- **Plan**: Descend to 3F via stairs at `(13, 3)`, then find the path to the Center Stairs on 3F.
### Status Update (Turn 18563)
- **Location**: 3F Center Room (3_44).
- **Situation**: Standing at (9, 3). Sailor is at (9, 2). Stairs are at (9, 5).
- **Realization**: The Sailor is NORTH of me. The exit is SOUTH. He is not blocking the way!
- **Plan**: Finish the conversation (which seems to be a hint about Jasmine's Steel type) and walk SOUTH to the stairs.
- **Next Steps**:
  1. Take Stairs at (9, 5) UP to 4F Center.
  2. Take Stairs at 4F (9, 7) UP to 5F Center.
  3. Take Stairs at 5F UP to 6F (Top).
### Status Update (Turn 18567)
- **Success**: Ascended from 3F (9, 5) to **4F Center** at (9, 5).
- **Route Confirmed**: The Center Column of the Lighthouse is a vertical shaft accessible only via the "Sailor Room" on 3F.
- **Next Step**: Take stairs at (9, 7) to reach **5F Center**, then hopefully 6F.