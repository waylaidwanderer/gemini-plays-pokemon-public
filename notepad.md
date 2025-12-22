# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Reach Item Ball at (14, 2).
- **Correction:** Row 6 is blocked by a wall at X=12. Must pass through the boxes at Row 8/9.
- **Clue:** "I lose my passion for work if someone's watching."
- **Hypothesis:** 
    1. The Machop (Worker) needs to be interacted with.
    2. Or, I need to make sure no one is "watching" the work area (Boxes).
- **Status:**
    - Player at (8, 7).
    - Machop at (7, 7) Facing Down.
- **Plan:**
    1. **Interact:** Talk to Machop from (8, 7).
    2. **Observe:** Does it move? Does it turn? Do boxes open?
    3. **Iterate:** If it turns, maybe that's the key (make it look away from boxes).
- **Discarded:**
    - Bypass Plan (Wall confirmed).
    - NPC 6 Facing Alone (Didn't work, but might be part of a combo).
- **Discarded:**
    - Local Control (NPC 6/7) - Failed.
    - Hidden Items - Failed.
    - NPC 5 Facing Left - Failed.

## Status
- Player moving to (8, 10).
- NPC 5 patrolling (9, 10) <-> (9, 11).
- Plan: Intercept NPC 5 at (9, 10) from (8, 10).
## Reflection (Turn 12312)
- **Time:** Start of specific trap attempt.
- **Hygiene:** Verified map markers and notepad.
- **Status:** Player at (8, 9) facing Right. NPC 5 at (9, 9).
- **Plan:** Press A to turn NPC 5 Left. Then Stun. Then Move.
- **Root Cause Check:** If this "turn him left" strategy fails to open gates, the "Facing Direction" hypothesis might be incomplete (e.g., maybe purely position based, or there's a switch I missed). But evidence points to vision cones.