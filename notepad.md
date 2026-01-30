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