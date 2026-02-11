# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "THE ULTIMATE PLAN"
**Goal**: P(22, 13), M(22, 15).

## Plan: "Escape & The Jed Ratchet" (Solution Found)
1. **Diagnosis**: Murkrow is trapped in the bottom section (Row 15) behind the Row 14 wall. It needs to be in the Top Section (Row 13) to be next to me at the door.
2. **Escape**:
   - Move Left to (5, 13). M -> (4, 15).
   - Move Down to (5, 16). M -> (4, 12) (Crosses Gap).
   - *State*: P(5, 16), M(4, 12).
3. **The Jed Ratchet**:
   - Target: Use Scientist Jed at (18, 12) to block M's Up movement.
   - Move to Align: P to (19, 16), M to (18, 12).
   - **Action**:
     - Move Right to (19, 16). M -> (18, 12) (Blocked by Jed?).
     - If M is blocked by Jed at 12, it stays at 12.
     - Wait, I need M at (18, 13) first.
     - From P(5, 16), M(4, 12).
     - Move P Up to (5, 13). M moves Down to (4, 15) (Falls back). **BAD.**
     - **Fix**: Use Wall at (13, 13) to block M Down.
     - Move P to (14, 16). M to (13, 12).
     - Move P Up to (14, 13). M Down to (13, 13) (Blocked by Wall). Stays (13, 12).
     - *State*: P(14, 13), M(13, 12).
4. **The Jed Lock**:
   - Move P Right to (19, 13). M -> (18, 12) (Hits Jed?).
     - M moves 13->18 (5 steps).
     - M is at (18, 12). Jed is at (18, 12).
     - So M is blocked from entering (18, 12) from the Left? No, M is at (13, 12).
     - M moves Right 13->14->...->17->18.
     - If Jed is at (18, 12), M stops at (17, 12).
     - *State*: P(19, 13), M(17, 12).
   - This doesn't help sync Y.
   - **Correct Logic**:
     - I need M at (18, 13).
     - From P(14, 13), M(13, 12).
     - Move P Up to (14, 12). M Down to (13, 13) (Blocked). Stays (13, 12).
     - *State*: P(14, 12), M(13, 12). **Y Synced at 12.**
     - Move Right to (19, 12). M -> (18, 12) (Blocked by Jed).
     - M stops at (17, 12).
     - P is at (19, 12).
     - Still separated.
   - **Alternative**: Use Row 11 Wall at Col 23?
     - P(14, 12), M(13, 12).
     - Move Right to (24, 12). M -> (23, 12).
     - Move Down to (24, 13). M -> (23, 11) (Blocked by Wall 23,11). Stays (23, 12).
     - *State*: P(24, 13), M(23, 12).
     - Move Up to (24, 12). M -> (23, 13) (Blocked by Wall 23,13). Stays (23, 12).
     - This traps M at (23, 12).
     - **I need M at Row 13.**
     - P(24, 12), M(23, 12).
     - I need M to go Down (12->13). P must go Up.
     - P(24, 11). M(23, 13) (Blocked).
     - This is impossible with standard moves if Row 13 is walls.
     - **Wait, (21, 13) is Floor.**
     - Target: P(22, 12), M(21, 13).
     - Move P Down. M Up.
     - P(22, 13). M(21, 12).
     - I need to block M Up at Col 21.
     - Wall at (21, 11)? No.
     - **Trap at (21, 11)?** No.
     - **What blocks M Up at Col 21?** Nothing apparent.
     - **Re-read Map**:
       - (18, 12) is Jed.
       - (19, 11) is Switch.
       - (20, 11) is Oath/Table.
       - (21, 11) is Oath/Table (`TYPE_1fdc`).
       - Is `TYPE_1fdc` solid?
       - It's a Table/Sign. Usually solid.
       - If (21, 11) is Solid, then M is blocked Up!
       - **Test**: Assume (21, 11) is Solid.
       - Strategy:
         1. Sync Y at 12 (via (13, 13) block). P(14, 12), M(13, 12).
         2. Move to Col 21/22. P(22, 12), M(21, 12).
         3. Move P Down to (22, 13). M Up to (21, 11) (Blocked). Stays (21, 12).
         4. **State**: P(22, 13), M(21, 12).
         5. Still Row 12.
         6. I need M to move DOWN to 13. P must move UP.
         7. From P(22, 12), M(21, 12).
         8. Move P Up to (22, 11). M Down to (21, 13).
         9. *State*: P(22, 11), M(21, 13).
         10. Now P needs to get to (22, 13) WITHOUT moving M.
         11. Impossible.
         12. **UNLESS** I approach from the top and push M down?
         13. **Wait, Murkrow mimics horizontal, mirrors vertical.**
         14. If I am at (22, 13), M is at (21, 13).
         15. I talk to door.
         16. How to get there?
         17. P at (22, 12). M at (21, 13).
         18. Move P Down. M moves Up.
         19. P(22, 13). M(21, 12).
         20. M is away.
         21. **Maybe (21, 12) is close enough?**
         22. Murkrow radius?
         23. Let's try to get M to (21, 12) first.
         24. Current P: (22, 13).
         25. Go Left to escape.