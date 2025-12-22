# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Open Gates/Boxes to reach East side.
- **Hypothesis:** NPC 6 (Static at 4,8) controls gates via Facing Direction.
    - **Note:** NPC 6 cannot face LEFT (Wall at 3,8).
    - **Test 1:** Make NPC 6 Face RIGHT (Look at boxes).
    - **Test 2:** Make NPC 6 Face DOWN (Look away?).
    - **Test 3:** Make NPC 6 Face UP (Look away?).
- **Status:**
    - Player moving to (5, 8).
    - NPC 6 at (4, 8).
    - NPC 5 Stunned at (9, 11) Facing Down.
- **Plan:**
    1. **Move:** Go to (5, 8).
    2. **Interact:** Talk to NPC 6. He will Face RIGHT.
    3. **Verify:** Check if boxes at Row 8/9 open.
    4. **Iterate:** If not, try facing Down (talk from 4,9) or Up (talk from 4,7).
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