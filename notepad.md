# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Exit Middle Pocket and reach Bottom Passage (Row 13).
- **Situation:** Player is inside Middle Pocket (10, 10). Top and Bottom internal gates are CLOSED. NPC 5 is patrolling (9, 9) to (9, 11).
- **Insight:** Since NPC 5 isn't opening the Top/Bottom gates, I must exit to the hallway (Column 8) to change rows.
- **Plan:**
    1. **Escape:** Move Left to (9, 10) -> (8, 10). (Spam Left until NPC 5 moves out of the way).
    2. **Traverse:** Walk South to (8, 13).
    3. **Enter:** Check if Bottom Gates (10, 13)/(11, 13) are open.
    4. **Exit East:** Walk through (12, 13) to the ladder area.

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