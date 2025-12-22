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
- **Puzzle Structure:**
    - **Top Path (Row 8-9):** Blocked by Boxes (10-11). Open at Col 12.
    - **Middle Path (Row 10-11):** Open at Cols 10-11. Blocked by Wall at Col 12.
    - **Bottom Path (Row 12-13):** Blocked by Boxes (10-11). Open at Col 12.
    - **Objective:** Open Top OR Bottom Boxes.
- **Status:**
    - Pushing Boxes failed.
    - NPC 5 (Guard) patrols (9, 9) <-> (9, 10) <-> (9, 11).
    - Current Observation: At (9, 11), Top Boxes (10, 8) are CLOSED.
- **Hypothesis:** Top Boxes might open when NPC 5 is at (9, 9) (Top of patrol) or (9, 10).
- **Plan:**
    1. Face Right at (8, 8).
    2. Wait for NPC 5 to reach (9, 9).
    3. Check `AsciiMap` for changes at (10, 8) (WALL vs FLOOR).
    4. If Open, STUN NPC 5 and run through.
- **Backup:**
    - Is there a switch I missed in the open area (Rows 10-11, Cols 10-11)?
    - Maybe I need to stun him ON a specific tile?

# Tile Mechanics
- **WALL:** Impassable.
- **FLOOR:** Walkable.
- **WARP_CARPET_UP:** Walkable, triggers warp when stepping OFF the map.
- **LADDER:** Interactable/Walkable, triggers warp.
- **BOXES:** Appear as Brown Boxes. Function as WALL tiles (Impassable). Located at (10, 8-9) and (10, 12-13). Also (6, 8-11).
- **Hypothesis:** Boxes might be pushable (Strength) or interactable objects.
    - **Test:** Walk into boxes at (6, 8) or (10, 8). Interact with them (A).