# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Open Bottom Gates (10, 13)/(11, 13).
- **Hypothesis:** NPC 7 needs to step on (8, 13). I was previously blocking him.
- **Current Status:** Player at (8, 12). NPC 7 at (6, 13).
- **Observation:** NPC 7's path has been (5,13) <-> (7,13). He hasn't touched (8,13) yet.
- **Plan:**
    1. **Wait:** Stay at (8, 12) (Do NOT block 8, 13).
    2. **Watch:** See if NPC 7 extends patrol to (8, 13).
    3. **Contingency:** If he turns back at (7, 13) again, then something *else* is blocking him (Hidden Item?).
    4. **Action:** If blocked, use **Itemfinder**.
- **Itemfinder Note:** I have the Itemfinder key item. It's the perfect tool to verify the "junk" hint.

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