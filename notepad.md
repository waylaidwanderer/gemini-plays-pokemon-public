# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Reach East side.
- **Hypothesis:** NPC 5's Position determines the Box State.
    - **Theory:**
        - NPC 5 at Y=11 -> Bottom Open / Top Closed (Current State).
        - NPC 5 at Y=10 -> Bottom Closed / Top Open (Target State).
- **Plan:**
    1. **Observe:** Wait for NPC 5 to move to (9, 10).
    2. **Verify:** Check if boxes at (10, 8)/(10, 9) open.
    3. **Lock:** If Open, STUN NPC 5 immediately.
    4. **Execute:** Run through the open path.
- **Status:**
    - Player at (8, 7).
    - NPC 5 at (9, 11) (Bottom).
    - Boxes at Top (8/9) are Closed.
    - Action: Waiting/Pacing to let NPC 5 move.

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