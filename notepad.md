# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Reach East side via Top Passage (Row 8/9).
- **Situation:** Player in Middle Pocket (10,10 - Safe, Always Open). Top Pocket (Row 8/9) is CLOSED. Bottom Pocket (Row 12/13) is CLOSED.
- **Hypothesis:** NPC 5 movement triggers the gates.
    - Currently NPC 5 is looping at Bottom (9, 10/11).
    - Top Gates are Closed.
    - Expectation: When NPC 5 moves to Top (9, 8), Top Gates will OPEN.
- **Plan:**
    1. **Wait** in Middle Pocket for NPC to patrol North.
    2. **Monitor** NPC position.
    3. **Dash** North when (10, 9) opens.
- **Logic Check:** "Work behind scenes" might mean he opens gates only when he is there? Or when he DOESN'T see me? Currently he doesn't see me (he faces Down), but gates are closed. So likely position-based.

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