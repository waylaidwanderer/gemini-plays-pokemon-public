# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Open Top or Bottom Gates.
- **Hypothesis:** NPC 5 (Middle) facing LEFT triggers the mechanism.
- **Status:**
    - NPC 5 is Stunned at (9, 10) facing LEFT.
    - **Action:** Closing text and moving to verify gates.
- **Plan:**
    1. **Verify:** Check Top Gates at (10, 8).
    2. **Verify:** Check Bottom Gates at (10, 13).
    3. **Success:** If OPEN, enter!
    4. **Fail:** If CLOSED, then my hypothesis is wrong or incomplete.
- **Discarded:**
    - Local Control (NPC 6/7) - Failed.
    - Hidden Items - Failed.
    - Blocking Paths - Failed.

## Status
- Player moving to (8, 10).
- NPC 5 patrolling (9, 10) <-> (9, 11).
- Plan: Intercept NPC 5 at (9, 10) from (8, 10).
## Reflection (Turn 12312)
- **Time:** Start of specific trap attempt.
- **Hygiene:** Verified map markers and notepad.
- **Status:** Player at (8, 9) facing Right. NPC 5 at (9, 9).
- **Plan:** Press A to turn NPC 5 Left. Then Stun. Then Move.
- **Root Cause Check:** If this "turn him left" strategy fails to open gates, the "Facing Direction" hypothesis might be incomplete (e.g., maybe purely position based, or there's a switch I missed). But evidence points to vision cones.