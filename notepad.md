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
- **Goal:** Open Gates (Top or Bottom).
- **Clues:** "Work behind the scenes", "Lose passion if watched".
- **Hypothesis:** Gates open only when **Player is NOT facing them** (or the worker).
    - **Test:** "Blind Observation".
    - **Method:** Stand at (8, 8). Face **LEFT** (Away from Guard/Boxes). Wait.
    - **Verification:** Check `AsciiMap` in the *next turn* to see if (10, 8) became FLOOR.
- **Status:**
    - Player at (8, 8).
    - NPC 5 patrolling.
    - Previous visual observation failed (gates stayed closed while watching).
- **Plan:**
    1. Face Left.
    2. Wait (Press B).
    3. CHECK MAP DATA NEXT TURN.
- **Backup:**
    - If this works, I need to navigate blindly (walking backward?) or time my turn.
    - If fails, try interacting with the boxes from a specific angle?

# Tile Mechanics
- **WALL:** Impassable.
- **FLOOR:** Walkable.
- **WARP_CARPET_UP:** Walkable, triggers warp when stepping OFF the map.
- **LADDER:** Interactable/Walkable, triggers warp.
- **BOXES:** Appear as Brown Boxes. Function as WALL tiles (Impassable). Located at (10, 8-9) and (10, 12-13). Also (6, 8-11).
- **Hypothesis:** Boxes might be pushable (Strength) or interactable objects.
    - **Test:** Walk into boxes at (6, 8) or (10, 8). Interact with them (A).
- **Event:** Gate at (10, 8/9) OPENED.
- **Action:** Entering East Zone.
- **Puzzle:** Top Right (Item/Ladder) is blocked by Wall at Row 4.
- **Hypothesis:** Switch/Trigger in Bottom Right opens Row 4 or provides access.
- **Observation:** Tile changes occurring dynamically (e.g. (5, 11) became WALL).
- **Plan:** Navigate to (13, 8), then explore South East corner.
- **Observation:** Reached East Room.
- **Status:** Bottom Gates (10, 12-13) are Closed. Top Gates (10, 8-9) are Open.
- **Path:** Moving North along East Wall (Col 18) to inspect the barrier at Row 4.
- **Hypothesis:** A switch or trigger in this room opens access to the Ladder at (17, 2).