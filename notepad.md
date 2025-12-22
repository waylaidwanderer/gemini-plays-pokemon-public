# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Reach East side (Items/Ladder).
- **Situation:** Player is INSIDE the middle-right box pocket at (10, 10).
- **Observation:** The boxes at (10, 10)/(11, 10) are OPEN (FLOOR). The boxes at (10, 9)/(11, 9) are CLOSED (WALL).
- **Plan:**
    1. **Unstun** NPC 5 to let him move.
    2. **Wait** for him to patrol North to (9, 8).
    3. **Hypothesis:** When he is at the top of his route, the Top-Right boxes (Row 8/9) will open.
    4. **Action:** Spam `Up` to catch the opening and move to (10, 9) -> (10, 8).
    5. **Exit:** Move East through the wall gap at (12, 8) or (12, 9).

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