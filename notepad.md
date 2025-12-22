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
    - NPC 5 Facing DOWN = Row 10/11 Right Gates OPEN (Confirmed).
    - "Work behind scenes where no one can see us".
- **Solution:**
    1. **Wait** for NPC 5 to face DOWN.
    2. **Freeze** him with `stun_npc` to keep gates open.
    3. **Cross** to the East side.

## Status
- Player at (8, 9).
- NPC 5 at (9, 11) (Moving).
- Action: Turning RIGHT to face (9, 9). Waiting for NPC to arrive.