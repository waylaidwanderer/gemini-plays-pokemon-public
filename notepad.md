# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Open Top Right Gates (10, 8).
- **Current Location:** (5, 8) - Right of NPC 6.
- **Observation:** NPC 6 is facing DOWN. ASCII Map shows Gates at (10, 8) are CLOSED (WALL).
- **Hypothesis:** NPC 6 must face RIGHT to open gates.
- **Plan:**
    1. **Action:** Talk to NPC 6 from (5, 8). He will turn RIGHT.
    2. **Lock:** When dialogue appears, use `stun_npc` to freeze him facing RIGHT.
    3. **Close:** Finish dialogue.
    4. **Verify:** Check gates.
- **Backup:** If this fails, try `Itemfinder` near NPC 7 (Bottom Left).
- **Note:** I must stun him *during* the text to prevent him from turning back.

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