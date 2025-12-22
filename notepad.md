# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Open Top Right Gates (10, 8).
- **Hypothesis:** NPC 6 must face UP (Away from his watch post) to open gates.
- **Status:** Executing "Lock" strat. Stunned NPC 6 facing UP.
- **Plan:**
    1. **Execute:** Stunned NPC 6. Cleared text.
    2. **Verify:** Moving to (8, 7) to check gates at (10, 8).
    3. **Action:** If Open -> Enter!
    4. **Fail:** If Closed -> Retest Bottom Left with Itemfinder.
- **Backup:** Itemfinder at Bottom Left.

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