# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Open Bottom Gates (10, 12)/(10, 13).
- **Hypothesis:** "Work behind scenes where no one can see us."
    - I need to be out of NPC 7's sight (Row 13).
    - I need to be out of NPC 5's sight (Row 9-11).
- **Plan:**
    1. **Hide:** Move to (8, 12). This tile is safe from NPC 7 (Row 13) and mostly safe from NPC 5 (unless he is at (9, 12)).
    2. **Observe:** Check if gates open.
    3. **Action:** If gates open, move Right into the pocket.
- **Junk Hint:** If hiding fails, I will investigate the "junk" at (6, 13)/(7, 13) using the Itemfinder or interaction.

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