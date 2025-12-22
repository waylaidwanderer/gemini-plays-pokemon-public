# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Reach East side (Items/Ladder).
- **Situation:** NPC 5 is at (9, 10) facing Up. I am at (9, 9) (blocking him).
- **Plan:**
    1. **Clear Way:** Move Left to (8, 9) to let him enter (9, 9).
    2. **Trap:** Wait for him to move to (9, 9).
    3. **Engage:** Press `Right` (Face Right) + `A` to talk. He turns Left.
    4. **Lock:** Stun him.
    5. **Pass:** Walk (8, 9) -> (8, 10) -> (9, 10) -> (10, 10) (East).
- **Critical Detail:** When at (8, 9), if NPC is at (9, 9), pressing `Right` faces him. If he is NOT there, it moves me back. Must verify position before acting.

## Status
- Player at (8, 9) facing Right.
- NPC 5 at (9, 11).
- Action: Waiting for NPC 5 to reach (9, 9). Pressing A to intercept.