# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC 5's facing direction controls the boxes. Facing LEFT or UP might open the path.
- **Plan:**
    1. **Position:** Move to (8, 9).
    2. **Manipulate:** Wait for NPC 5 to enter (9, 9). Talk to him so he turns LEFT.
    3. **Lock:** Immediately use `stun_npc` on NPC 5 to freeze him facing LEFT.
    4. **Test:** Walk into Column 9 (e.g., at (9, 10)) and move South to check if boxes shift.

## Status
- Player at (8, 9).
- NPC 5 at (9, 11) (Moving).
- Action: Turning RIGHT to face (9, 9). Waiting for NPC to arrive.