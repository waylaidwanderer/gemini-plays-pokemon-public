# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Open Bottom Gates (10, 13)/(11, 13).
- **Hypothesis:** Gates open when NPC 7 stands on (8, 13).
    - **Logic:** I was previously standing at (8, 13), blocking him from reaching it, so gates stayed closed.
    - **Current:** I am at (8, 12). NPC 7 is at (7, 13) moving Right.
- **Plan:**
    1. **Wait:** Press A to let time pass.
    2. **Observe:** Watch NPC 7 move to (8, 13).
    3. **Check:** See if gates at (10, 13) open.
    4. **Action:** If they open, RUSH in (Move Down then Right).
- **Note:** If this works, the same logic applies to the Top Pocket (Row 8/9). I blocked NPC 5 from reaching the top? No, NPC 5 moves vertically. Maybe similar logic though.

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