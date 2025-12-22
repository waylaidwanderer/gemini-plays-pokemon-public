# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** 
    1. **Vision:** NPC 5 watching Col 9 closes gates.
    2. **Position:** Walking in Col 9 opens gates (observed previously).
- **Constraint:** NPC 5 currently blocks Col 9 at (9, 10).
- **Plan:**
    1. **Trap NPC 5 at (9, 9).** This clears Col 9 for me to walk in.
    2. **Ensure he faces UP (North).** So he doesn't see me in Col 9.
    3. **Action:** Move to (8, 9). Wait for him to enter (9, 9). Stun him.
    4. **Execution:** Enter Col 9 at (9, 10) and walk South to open gates.

## Status
- Player at (8, 9).
- NPC 5 at (9, 11) (Moving).
- Action: Turning RIGHT to face (9, 9). Waiting for NPC to arrive.