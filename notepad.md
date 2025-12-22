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
    - **Observation:** NPC 6 is currently at (4, 8) Facing **RIGHT**. The boxes at (6,8) are **WALLS (Closed)**.
    - **Conclusion:** Facing RIGHT does NOT open the boxes (or requires a trigger).
    - **Next Tests:**
        - **Test 2:** Make NPC 6 Face **DOWN** (stand at 4,9).
        - **Test 3:** Make NPC 6 Face **UP** (stand at 4,7).
- **Status:**
    - Player at (5, 8).
    - NPC 6 at (4, 8) Facing Right.
- **Plan:**
    1. **Interact:** Talk to NPC 6 from current position (Face Left) just to check dialogue.
    2. **Move:** Go to (4, 9).
    3. **Interact:** Talk to NPC 6 from Below (Face Up).
    4. **Verify:** Check boxes.
    5. **Iterate:** If failing, try (4, 7).
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