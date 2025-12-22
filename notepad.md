# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Reach East side (Items/Ladder).
- **Correction:** Row 10/11 Right Gates (10,10 to 11,11) are **FLOOR** (Open) in the XML, despite looking like boxes.
- **Hypothesis:** Gates are open by default. They likely close (turn to WALL) only if NPC 5 **sees** the player.
- **Plan:**
    1. **Wait** for NPC 5 to move off (9, 10).
    2. **Stun** NPC 5 to keep him out of the way and prevent him from turning to see me.
    3. **Walk** through (9, 10) to (10, 10).

## Status
- Player at (8, 9).
- NPC 5 at (9, 11) (Moving).
- Action: Turning RIGHT to face (9, 9). Waiting for NPC to arrive.