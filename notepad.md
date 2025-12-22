# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Open Bottom Gates (10, 13)/(11, 13).
- **Hypothesis:** "Junk" on the ground (Bottom Left) is a hidden item blocking the puzzle.
- **Evidence:** NPC 7 said "Stuff on ground is junk, take it."
- **Plan:**
    1. **Tool:** Use `ITEMFINDER` from the menu (Key Items Pocket).
    2. **Search:** If positive, check tiles in Row 13 (5-8).
    3. **Result:** Finding the item should unblock NPC 7's patrol.

## Discarded Hypotheses
- **NPC 6 (Top Left):** Facing Right/Up/Left/Down did not open Top Gates.
- **NPC 5 (Middle):** Area leads to dead end at (12, 11).
- **Machop:** Interaction yielded only text.
- **Manual Search:** Pressed A on (7, 13) and (8, 13) - Found nothing.

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