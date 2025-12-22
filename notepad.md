# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Reach East side (Items/Ladder).
- **Situation:** NPC 5 is at (9, 10) facing Down, blocking the path. The gate at (10, 10) is OPEN (FLOOR) but might close if I'm seen.
- **Plan:**
    1. **Reset:** Unstun NPC 5. Move to (8, 9).
    2. **Trap:** Wait for NPC 5 to move to (9, 9).
    3. **Blind:** Talk to him from (8, 9) to make him face LEFT.
    4. **Lock:** Stun him facing LEFT.
    5. **Execute:** Walk around him: (8, 9) -> (8, 10) -> (9, 10) -> (10, 10).
- **Note:** Do NOT step into (9, 10) while he is at (9, 11) facing Up, as he might see me and close the gate.

## Status
- Player at (8, 9).
- NPC 5 at (9, 11) (Moving).
- Action: Turning RIGHT to face (9, 9). Waiting for NPC to arrive.