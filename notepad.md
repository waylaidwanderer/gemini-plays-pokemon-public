# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Reach Item Ball at (14, 2).
- **Realization:** The "Puzzle" of the boxes might be a distraction or optional. The map shows a clear path around the top (Row 6) and potentially the bottom (Row 13).
- **New Plan:** Bypass the boxes entirely.
    - Path: (4,9) -> (5,9) -> (5,8) -> (5,7) -> Around Machop -> East Side.
- **Hypothesis:** I can walk around the obstacles.
- **Status:**
    - Player moving to (8, 6).
    - NPC 6 at (4, 8).
    - NPC 5 at (9, 11).
- **Discarded:**
    - Trying to open boxes via NPC facing (for now).
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