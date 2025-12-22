# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Reach East Room (Col 13+) via Top Right (Row 8/9) or Bottom Right (Row 13).
- **Map Analysis:**
    - **Middle Right Pocket (10,10 - 11,11):** OPEN, but leads to WALL at Col 12. **DEAD END.**
    - **Top Right Pocket:** CLOSED. Leads to EXIT at (12, 8).
    - **Bottom Right Pocket:** CLOSED. Leads to EXIT at (12, 13).
    - **Conclusion:** I MUST open Top Right or Bottom Right gates.
- **Hypothesis:**
    - NPC 6 (Top Left) -> Controls Top Gates?
    - NPC 7 (Bottom Left) -> Controls Bottom Gates?
- **Current Action:** Talk to NPC 6 at (4, 8).
- **Plan:**
    1. **Talk:** Interact with NPC 6.
    2. **Observe:** Does he say something useful? Do gates open?
    3. **Search:** Use `Itemfinder` if dialogue fails.
    4. **Machop:** Check Machop at (7, 7).

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