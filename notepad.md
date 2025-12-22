# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Current Plan
1. **Stun NPC 5** at (9, 10) (Current Pos).
2. **Face Right** (from 8, 10).
3. **Unstun NPC 5**.
4. **Immediately Talk (A)** to force him to turn LEFT.
5. Check if Gate 2 (10, 12) opens.

## Status
- Player at (8, 10).
- NPC 5 at (9, 10).
- Action: Stunning and Facing Right.