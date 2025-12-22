# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Open Gates/Boxes.
- **Current Hypothesis:** NPC 6 (Static at 4,8) controls the boxes/gates based on Facing Direction.
    - NPC 5 (Moving) reverts facing immediately, making him a poor switch candidate.
    - NPC 6 is static, so his facing should persist.
- **Status:**
    - Player moving to (3, 8) to flank NPC 6.
    - NPC 5 Stunned at (9, 9) (Facing Up).
- **Plan:**
    1.  **Move:** Go to (3, 8) via the bottom corridor (Row 12).
    2.  **Interact:** Talk to NPC 6 from the Left to make him Face Left.
    3.  **Verify:** Check if this opens the boxes at Row 8/9 or Gates at Row 10/11.
- **Discarded:**
    - NPC 5 Manipulation (Unreliable due to auto-revert).
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