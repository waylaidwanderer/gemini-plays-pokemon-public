# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates.
- **Observations:**
    - NPC 5 Facing UP = Row 10/11 Gates CLOSED.
    - NPC 5 Facing DOWN = Row 10/11 Gates CLOSED (Confirmed).
    - "Work behind scenes where no one can see us".
- **Refined Hypothesis:** Gates open when NPC 5 cannot see the Player.
- **Solution:**
    1. **Unstun** NPC 5.
    2. **Position** at (8, 9).
    3. **Trap** NPC 5 at (9, 9) facing LEFT (by talking).
    4. **Freeze** him.
    5. **Walk** on Row 10 (blind spot).

## Status
- Player at (8, 9).
- NPC 5 at (9, 11) (Moving).
- Action: Turning RIGHT to face (9, 9). Waiting for NPC to arrive.