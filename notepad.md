# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Open Bottom Gates (10, 13)/(11, 13).
- **Hypothesis:** "Work behind scenes where no one can see us."
    - NPC 5 said this. Need to check if NPC 7 says the same.
- **Action:** Talk to NPC 7 at (7, 13).
- **Plan:**
    1. **Move** to (8, 13).
    2. **Turn** Left.
    3. **Talk** (Press A).
    4. **Observe** if he turns or if gates change.
- **Note:** NPC 7 patrols (5, 13) to (8, 13). If he isn't at (7, 13), I might miss him, but standing at (8, 13) blocks his path into the hallway, forcing an interaction eventually.

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