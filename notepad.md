# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Open Bottom Gates (10, 13)/(11, 13).
- **Hypothesis:** 
    1. **Patrol:** NPC 7 needs to reach `(8, 13)` to trigger gates.
    2. **Item:** A hidden item at `(8, 13)` might be blocking him.
- **Correction:** I was at `(7, 13)` last turn, not `(8, 13)`. My previous checks were invalid.
- **Plan:**
    1. **Position:** Move to `(8, 12)` (Hiding spot / Observation point).
    2. **Search:** Face Down and check `(8, 13)` for hidden item.
    3. **Observe:** Wait for NPC 7 (currently at `5, 13`) to return.
    4. **Verify:** If he steps on `(8, 13)`, gates should open. If he turns early, check `(7, 13)`.
- **Note:** "Stuff on ground is junk" is the key clue. I must find it.

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