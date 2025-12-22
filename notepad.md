# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Open Top or Bottom Gates.
- **Hypothesis:** NPC 5 (Middle) must face RIGHT to open gates.
- **Reasoning:** Haven't tested this direction yet. Requires being inside the pocket.
- **Plan:**
    1. **Unstun** NPC 5.
    2. **Enter** Middle Pocket (10, 10) when he moves off (9, 10).
    3. **Position** at (10, 11).
    4. **Wait** for NPC 5 to reach (9, 11).
    5. **Interact** (Face Left). He turns RIGHT.
    6. **Lock** (Stun) and Verify.
- **Status:** Unstunning and attempting to enter pocket.

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