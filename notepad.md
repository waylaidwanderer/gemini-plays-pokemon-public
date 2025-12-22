# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Open Top or Bottom Gates.
- **Hypothesis:** NPC 5 (Middle) must face **LEFT** to open gates (looking away from them).
    - *Previous Attempt:* Facing RIGHT failed to open (10, 12).
- **Status:**
    - Player at (10, 11).
    - NPC 5 at (9, 10) (Unstunned).
    - **Action:** Moving to (8, 10) to make him face LEFT.
- **Plan:**
    1. **Position:** Move to (8, 10) (Left side of NPC).
    2. **Interact:** Face Right + A. He turns LEFT.
    3. **Lock:** Stun him.
    4. **Verify:** Check Top/Bottom gates.
- **Discarded:**
    - Local Control (NPC 6/7) - Failed.
    - Hidden Items - Failed.
    - NPC 5 Facing Right - Failed.
- **Discarded:**
    - Local Control (NPC 6/7) - Failed.
    - Hidden Items - Failed.
    - NPC 5 Facing Left - Failed.

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