# Victory Road 1F
- Map ID: 0_108
- Entrance from Route 23 is at (8, 17).
- Puzzle 1: Boulder started at (5, 15). Switch is at (17, 13).
- TRUE SOLUTION FOUND:
  1. Use Strength.
  2. Walk to (5, 14) and push boulder DOWN to (5, 16).
  3. Walk to (4, 16) and push boulder RIGHT to (9, 16).
  4. Walk to (9, 17) and push boulder UP to (9, 14).
  5. Walk to (8, 14) via (8, 15). Push boulder RIGHT to (16, 14).
  6. Walk to (16, 15) via (15, 15). Push boulder UP to (16, 12).
  7. Walk to (15, 12) via (14, 14) -> (14, 12). Push boulder RIGHT to (17, 12).
  8. Walk to (17, 11) via (16, 11). Push boulder DOWN to switch at (17, 13).
- Player is at (5, 16).
- Current puzzle state: Strength needs reactivation, preparing to execute the 8-step solution.
[Turn 50013 Progress]
- The Start menu is open. The cursor is on EXIT.
- The Start menu wraps. Pressing Down twice should wrap to POKéDEX, then move to POKéMON.
- Executing 'Down', 'Down'.
[Turn 50015 Progress]
- Hallucination Correction: In Turn 50013, I manually pressed 'Down' twice, but I expected it to wrap. 
- Looking at the Turn 50014 screen, the cursor is still on EXIT.
- Wait! The overworld Start Menu DOES NOT wrap vertically from EXIT to POKéDEX!
- My `Mechanics/UI` notepad has conflicting info. Line 15 says "The Start Menu WRAPS!", but Line 27 says "Overworld Item Menu Wrap: Pressing Up at the very top... DOES NOT wrap".
- Let me test this right now. If I am at EXIT and press Down twice and it doesn't move, it doesn't wrap downward.
- I will press Up, Up, Up, Up to get to POKéMON instead.
[Turn 50016 Progress]
- The Start menu is open. The cursor is on POKéMON.
- Pressing 'A' to open the Party menu.