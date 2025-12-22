# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Open Bottom Gates (10, 13)/(11, 13).
- **Hypothesis:** A hidden item at (7, 13) is blocking NPC 7's patrol path. Removing it will allow him to step on the switch at (8, 13).
- **Evidence:**
    - NPC says "Stuff on ground is junk, take it".
    - NPC patrol path is short/looping (5-6), not reaching the end (8).
- **Plan:**
    1. **Search:** Face Left from (8, 13) and press A to check (7, 13).
    2. **Verify:** If I find an item ("Ultra Ball" etc.), picking it up clears the path.
    3. **Wait:** Move out of the way (to 8, 12) and let him walk to (8, 13).
    4. **Execute:** Gates should open.

## Status
- Player at (9, 9).
- NPC 5 at (9, 11).
- Error: Previous attempt to move to (8, 9) failed or I moved back.
- Action: Moving Left to (8, 9) to clear the spot for NPC 5. Then waiting.
## Reflection (Turn 12312)
- **Time:** Start of specific trap attempt.
- **Hygiene:** Verified map markers and notepad.
- **Status:** Player at (8, 9) facing Right. NPC 5 at (9, 9).
- **Plan:** Press A to turn NPC 5 Left. Then Stun. Then Move.
- **Root Cause Check:** If this "turn him left" strategy fails to open gates, the "Facing Direction" hypothesis might be incomplete (e.g., maybe purely position based, or there's a switch I missed). But evidence points to vision cones.