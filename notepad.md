# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Open Bottom Gates (10, 13)/(11, 13).
- **Hypothesis:** Gates open when NPC 7 faces LEFT.
- **Current State:** Player at (8, 13). NPC 7 at (6, 13) facing Right.
- **Plan:**
    1. **Face Right:** Look at the gates (10, 13).
    2. **Wait:** Allow NPC 7 to patrol.
    3. **Trigger:** If he walks to (7, 13) then turns Left to go back, the gates should open.
    4. **Action:** If gates open, dash in.
- **Note:** Facing Right prevents accidental interaction with NPC 7 (which would force him Right).
- **Junk Hint:** "Stuff on ground is junk". Possibly hidden items at (6, 13)/(7, 13)? Check later.

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