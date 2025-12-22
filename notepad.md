# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Reach Item Ball at (14, 2).
- **Layout Analysis:**
    - **Zone 1 (West):** Start area.
    - **Zone 2 (Middle):** Where Player is (Col 8, 9).
    - **Zone 3 (East):** Target area.
    - **Barriers:**
        - **Col 10/11:** Blocked by Boxes at Rows 8/9. Open at Rows 10/11.
        - **Col 12:** Blocked by Wall at Rows 10/11. Open at Rows 8/9.
    - **Implication:** I MUST open the boxes at Rows 8/9 (Col 10/11) to pass through the gap in the Col 12 wall.
- **Clue:** "I lose my passion for work if someone's watching."
- **Current Test:** Interact with Machop at (7, 7).
- **Status:**
    - Player at (8, 7).
    - Machop at (7, 7).
    - Action: Turning Left to interact.
- **Discarded:**
    - Walking through Row 10/11 (Blocked by Wall at Col 12).
    - Walking through Row 13 (Blocked by Wall at Col 10/11).
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