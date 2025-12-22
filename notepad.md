# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Reach East side.
- **Layout Insight (The Cage):**
    - The "Box Area" (Cols 10-11) is a cage.
    - **Entry:** Open at Rows 10-11 (West side).
    - **Exit:** BLOCKED East by Wall (Col 12) at Rows 10-11.
    - **Solution:** Must open North Boxes (Row 8-9) OR South Boxes (Row 12-13) to bypass the Wall.
- **Hypothesis:** NPC 5's Position triggers the boxes.
    - NPC 5 at (9, 11) -> All Closed.
    - Test: Wait for NPC 5 to move to (9, 10).
- **Plan:**
    1. **Position:** (8, 9) Facing Right.
    2. **Wait:** Watch NPC 5 move to (9, 10).
    3. **Observe:** Check if boxes at (10, 8/9) open.
    4. **Action:** If open, Stun NPC 5 immediately.
- **Status:**
    - Player at (8, 6).
    - NPC 5 is off-screen (likely at 9, 11).
    - Boxes at Top (8/9) are Closed.
    - Action: Moving back to (8, 7) to observe.

## Status
- Player moving to (8, 10).
- NPC 5 patrolling (9, 10) <-> (9, 11).
- Plan: Intercept NPC 5 at (9, 10) from (8, 10).
## Reflection (Turn 12467)
- **Time:** Start of interaction with NPC 7.
- **Hygiene:** Verified. Notepad clean.
- **Hypothesis Check:**
    - NPC 5 (Top) did NOT trigger gates by facing or position (so far).
    - NPC 6 (Top Left) did NOT trigger gates.
    - **Current:** NPC 7 (Bottom) might control the bottom gates.
- **Root Cause:** If this fails, I might need to re-evaluate if the boxes are controlled by these NPCs at all, or if there's a different trigger (e.g. key item, switch, or sequence).
- **Plan:** Interact with NPC 7. If he turns/moves, check gates.

## Basement Puzzle Strategy
- **Goal:** Open Gates/Boxes.
- **Hypothesis:** Picking up the "Junk" (Item at 6, 3) triggers a state change.
    - **Clue:** NPC 7 says "The stuff on the ground's junk. Take it if you want it!"
    - **Logic:** Maybe clearing the junk satisfies the worker or is the "Switch".
- **Plan:**
    1. Navigate to (6, 3) via the left corridor (Cols 1-2).
    2. Pick up the Item.
    3. Return to NPC 7 or Check Gates.
- **Status:**
    - Player at (5, 12).
    - NPC 7 interaction completed (No gate change).
    - Action: Moving to (6, 3).
- **Discarded:**
    - NPC Facing/Position triggers (so far).
    - "Don't Look" (so far).

# Tile Mechanics
- **WALL:** Impassable.
- **FLOOR:** Walkable.
- **WARP_CARPET_UP:** Walkable, triggers warp when stepping OFF the map.
- **LADDER:** Interactable/Walkable, triggers warp.