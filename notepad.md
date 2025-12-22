# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Reach East side (Items/Ladder).
- **Situation:** NPC 5 is at (9, 10) facing Up. I am at (8, 9) facing Right.
- **Timing Issue:** Last turn I tried to interact at (9, 9) but he moved to (9, 10). He is fast.
- **Plan:**
    1. **Camp:** Stay at (8, 9) facing Right.
    2. **Spam Interact:** Repeatedly press `A`. When he steps into (9, 9), it will trigger dialogue.
    3. **Manipulate:** Dialogue will force him to face Left (towards me).
    4. **Lock:** Stun him immediately after dialogue closes.
    5. **Execute:** Walk around him.
- **Hypothesis:** If he faces Left at (9, 9), he cannot see the gates at (10, 10), so they should open.

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