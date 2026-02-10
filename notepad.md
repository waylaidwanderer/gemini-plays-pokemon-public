# Team Rocket HQ - Murkrow Puzzle

## RECOVERY: "West Wall Sync"
**Goal**: Reset state to P(1, 13), M(1, 12).

## Current Status (Turn 36485)
- **Player**: (15, 13).
- **Murkrow**: (15, 12).

## Execution Path
1. **Sync X (West)**:
   - Move Left 14 -> P(1, 13). M(1, 12).
   - **State**: P(1, 13), M(1, 12).

2. **Invert Y (Col 1)**:
   - Up 11 -> P(1, 2).
   - M(1, 12) -> Down 11 -> Blocked at 16 (Wall 17). M(1, 16).
   - **State**: P(1, 2), M(1, 16).

3. **Move to Col 22**:
   - Right 21 -> P(22, 2). M(22, 16).
   - **State**: P(22, 2), M(22, 16).

4. **Ratchet to Door**:
   - Down 2 -> P(22, 4). M(22, 16) -> Up 2 -> M(22, 14).
   - **State**: P(22, 4), M(22, 14).

5. **The Final Pin**:
   - Move Down 9 -> P(22, 13).
   - M(22, 14) -> Up 9 -> Blocked at 10. M(22, 11).
   - **State**: P(22, 13), M(22, 11).
   - **PROBLEM**: M is at 11, P is at 13.
   - P Up 1 -> P(22, 12). M Down 1 -> M(22, 12). Collision.

   **Alternate Step 5**:
   - From P(22, 4), M(22, 14).
   - Move Right 4 -> P(26, 4). M stays (22, 14) (Blocked East).
   - Move Down 9 -> P(26, 13). M moves Up 9 -> Blocked at 10 -> M(22, 11).
   - Move Left 4 -> P(22, 13). M stays (22, 11) (Blocked West).
   - **State**: P(22, 13), M(22, 11).
   - P Up 1 -> P(22, 12). M Down 1 -> M(22, 12). Collision.

   **Alternate Step 5 (Bonk Method)**:
   - From P(22, 13), M(22, 11).
   - Move Up 1 (Bonk P at 12? No 12 is clear).
   - Move Up 2 -> P(22, 11). M Down 2 -> M(22, 13).
   - **State**: P(22, 11), M(22, 13).
   - Move Up 1 (Bonk P at 10). P stays (22, 11). M Down 1 -> M(22, 14).
   - **State**: P(22, 11), M(22, 14).
   - Move Right 4 -> P(26, 11). M Stays (22, 14).
   - Move Down 2 -> P(26, 13). M Up 2 -> M(22, 12).
   - Move Left 4 -> P(22, 13). M Left 4 -> M(18, 12) (ESCAPES!).

   **Wait**: Is (21, 12) blocked?
   (21, 12) is TYPE_3fe2. Clear.
   So M escapes West at Row 12.

   **Solution**: Don't let M go to Row 12.
   Keep M at Row 13 or 14.
   
   From P(26, 11), M(22, 14).
   Move Down 1 -> P(26, 12). M Up 1 -> M(22, 13).
   Move Left 4 -> P(22, 12). M Left 4 -> M(18, 13).
   (Check (21, 13): TYPE_3fe2. Clear).
   
   M escapes West on Row 12 and 13.
   M is pinned West on Row 14.
   
   So M MUST be at Row 14 when we approach from the East.
   
   To approach from East (Col 26 -> 22), we need P at Row 13 (to land at 22, 13).
   If P is at (26, 13), M must be at (22, 14) AND NOT MOVE UP.
   But P Down -> M Up.
   
   We need P to be at (26, 13) and M at (22, 14).
   If P moves Left, M moves Left -> Blocked. M stays (22, 14).
   P arrives at (22, 13).
   Interact.
   
   So the Goal State before Final Approach is P(26, 13), M(22, 14).
   
   How to reach P(26, 13), M(22, 14)?
   
   From P(22, 4), M(22, 14). (Derived earlier).
   Move Right 4 -> P(26, 4). M Stays (22, 14).
   Move Down 9 -> P(26, 13).
   M moves Up 9.
   M(22, 14) -> Up -> (22, 5).
   M is at (22, 5).
   
   This doesn't work. M moves too far Up.
   
   I need to move P Down 9, but M moves Up 0.
   I need M to be blocked North.
   M is blocked North at (22, 10).
   So M stops at (22, 11).
   So M ends at (22, 11).
   
   So P(26, 13) results in M(22, 11).
   P Left -> P(22, 13). M Left -> M(22, 11) (Blocked? No, (21, 11) is Oath/Wall).
   (21, 11) is TYPE_1fdc (Oath). Is it solid? Usually yes.
   If (21, 11) is solid, M stays at (22, 11).
   State: P(22, 13), M(22, 11).
   
   Then P Up 1 -> P(22, 12). M Down 1 -> M(22, 12). Collision.
   
   I need M to be at (22, 14).
   
   If M is at (22, 11).
   P (at 22, 13) moves Up 1 -> P(22, 12).
   M moves Down 1 -> M(22, 12).
   
   I need to be ABOVE M to push him down?
   If P is at (22, 12) and M is at (22, 13).
   Interact Down.
   
   How to get P(22, 12), M(22, 13)?
   
   From P(26, 13), M(22, 11).
   P Up 1 -> P(26, 12). M Down 1 -> M(22, 12).
   P Left 4 -> P(22, 12). M Left 4 -> Escape to (18, 12).
   
   Okay, what if we use the "Bonk P Up" trick at Col 26?
   P(26, 13), M(22, 11).
   P Up 3 -> Bonk?
   (26, 11) is Solid Obstacle. (26, 10) is Fake Crate/Solid.
   So P blocked at 12?
   If P moves Up from 13.
   13 -> 12.
   12 -> 11 (Blocked).
   So P stops at 12.
   
   If P moves Up 3.
   P moves 13 -> 12. (1 step).
   M moves Down 3 -> 11 -> 14. (3 steps).
   State: P(26, 12), M(22, 14).
   
   Now P(26, 12), M(22, 14).
   P Left 4 -> P(22, 12).
   M Left 4 -> Blocked at (21, 14). M stays (22, 14).
   State: P(22, 12), M(22, 14).
   
   Close! P is at 12, M at 14. Gap at 13.
   P Down 1 -> P(22, 13).
   M Up 1 -> M(22, 13).
   Collision/Swap.
   
   If I can get M to (22, 13) while P is at (22, 12).
   
   From P(26, 12), M(22, 14).
   Move P Up 1 (Bonk against 11).
   P stays (26, 12).
   M moves Down 1 (Bonk against 15? Statue at 22, 15).
   M stays (22, 14).
   
   Move P Down 1 -> P(26, 13).
   M Up 1 -> M(22, 13).
   State: P(26, 13), M(22, 13).
   
   Move P Left 4 -> P(22, 13).
   M Left 4 -> Escape to (18, 13).
   
   This is tricky.
   
   Wait, if P is at (22, 12) and M is at (22, 14).
   Interact Down?
   Distance is 2. (12 -> 13 -> 14).
   Interact range is 1.
   
   I need M at 13.
   
   If P(22, 12), M(22, 14).
   I want P(22, 12), M(22, 13).
   M needs to move Up 1.
   P needs to move Down 1.
   But P moving Down puts P at (22, 13). Collision.
   
   What if I interact from (22, 13) facing Down to M(22, 14)?
   I need P at (22, 13).
   
   Go back to P(26, 12), M(22, 14).
   Move Down 1 -> P(26, 13).
   M moves Up 1 -> M(22, 13).
   State: P(26, 13), M(22, 13).
   
   Move Left 4 -> P(22, 13).
   M moves Left 4 -> Escape to (18, 13).
   
   UNLESS (21, 13) is a Wall.
   Map check: (21, 13) is TYPE_3fe2 (Clear).
   
   So M escapes.
   
   Is there any way to block M West?
   No.
   
   So I CANNOT approach from East if M is at Row 12 or 13.
   I MUST approach when M is at Row 14 (Pinned West).
   
   So P(26, 13), M(22, 14).
   Left 4 -> P(22, 13).
   M Blocked West -> M(22, 14).
   State: P(22, 13), M(22, 14).
   
   This works!
   
   So the target setup is P(26, 13), M(22, 14).
   
   How to achieve P(26, 13), M(22, 14)?
   
   We tried from P(26, 4), M(22, 14).
   P Down 9 -> P(26, 13).
   M Up 9 -> M(22, 5). (Fails).
   
   We tried from P(26, 11), M(22, 14).
   P Down 2 -> P(26, 13).
   M Up 2 -> M(22, 12). (Fails).
   
   We need P to move Down, but M to NOT move Up.
   M needs to be blocked North.
   M is blocked North at (22, 10).
   So M is at (22, 11) max North.
   
   If M is at (22, 11).
   We want M at (22, 14).
   M needs to move Down 3.
   P needs to move Up 3.
   
   So P needs to be at (26, 16) to end at (26, 13).
   P(26, 16) -> Up 3 -> P(26, 13).
   M(22, 11) -> Down 3 -> M(22, 14).
   State: P(26, 13), M(22, 14).
   
   YES!
   
   So the Target Setup is P(26, 16), M(22, 11).
   
   How to get P(26, 16), M(22, 11)?
   
   From P(22, 4), M(22, 14).
   Move Right 4 -> P(26, 4). M(22, 14).
   Move Down 12 -> P(26, 16).
   M Up 12 -> Blocked at 10 -> M(22, 11).
   State: P(26, 16), M(22, 11).
   
   This works!
   
   Full Chain:
   1. Sync X West: P(1, 13), M(1, 12).
   2. Invert Y: P(1, 2), M(1, 16).
   3. Move to Col 22: P(22, 2), M(22, 16).
   4. Ratchet M to Door: P(22, 4), M(22, 14).
   5. Shift to Col 26: P(26, 4), M(22, 14).
   6. Ratchet M to Top: P(26, 16), M(22, 11).
   7. Position Y: P(26, 13), M(22, 14).
   8. Position X: P(22, 13), M(22, 14).
   9. Interact.
   
   Step 1 requires P(1, 13), M(1, 12).
   I am currently at P(15, 13), M(15, 12).
   Moving Left 14 works perfectly.
   
   Let's DO THIS.