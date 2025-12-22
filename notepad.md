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
- **Hypothesis:** NPC 6 Facing Right triggers the gates.
- **Plan:**
    1. **Turn:** Face Left (towards NPC 6).
    2. **Interact:** Talk to him (He turns Right).
    3. **Lock:** Stun him immediately.
    4. **Check:** Walk to (8, 8) to check gates.
- **Alternative:** If this fails, maybe he needs to face UP (I tried talking from above but didn't check gates? I should check logs).
    - Logs say I talked at (4, 7). He faced Up. I then moved to Machop. I didn't verify gates.
    - If Right fails, I must retry UP and verify.
- **Junk Hint:** Use `Itemfinder` near NPC 7 if NPC 6 strategy fails completely.

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