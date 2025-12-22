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
    - **Observation:** NPC 6 is currently at (4, 8) Facing **LEFT**. The boxes at (6,8) are **WALLS (Closed)**.
    - **Conclusion:** Facing LEFT does NOT open the boxes.
    - **Next Tests:**
        - **Test 3:** Make NPC 6 Face **DOWN** (stand at 4,9).
- **Status:**
    - Player at (4, 9).
    - NPC 6 at (4, 8) Facing Left.
- **Plan:**
    1. **Face Up:** Turn to face NPC 6 (Done).
    2. **Interact:** Talk to NPC 6 (He turns DOWN).
    3. **Lock:** Stun him immediately after dialogue.
    4. **Verify:** Check boxes.
- **Discarded:**
    - Facing Right (Closed).
    - Facing Up (Closed).
    - Facing Left (Closed).
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