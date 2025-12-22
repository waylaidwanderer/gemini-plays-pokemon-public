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
- **Zone 2 (Top East):** Dead end.
    - North (Row 4): Blocked by Walls.
    - South (Row 12): Blocked by Walls.
- **Action:** Returning to West Side.
- **Goal:** Open Bottom Gates (10, 12-13) to access South East Zone.
- **Hypothesis:** Trigger for Bottom Gates is in Bottom West area.
- **Observation:** Black Belt at (9, 10) did not respond to interaction (Turn 12557).
- **Hypothesis:** He might be a non-interactive "mover" NPC, or interaction requires a specific angle/condition.
- **Action:** Moving to talk to Machop at (7, 7).
- **Goal:** Determine if Machop triggers box movement or provides clues.
- **Observation:** Top Gates (10, 8-9) are OPEN.
- **Correlation:** NPC 5 is at (9, 11) facing Down. NPC 6 is at (4, 8) facing Up.
- **Hypothesis:** NPC 5's position (9, 11) keeps Top Gates open.
- **Action:** Stunning NPC 5 to lock the gate state, then crossing to East Room.
- **Success:** Entered East Room via Top Gate at (13, 8).
- **Observation:** Row 8/9 in East Room contains a block of Walls/Boxes (14-17, 8-9).
- **Action:** Investigating North East Barrier (Row 4) to see if Ladder (17, 2) is accessible.
- **Plan:** Move to (17, 5), then explore South.
- **Hypothesis:** "The Cage" - Entering East Room and letting the Outer Gate (10, 8-9) close might open the Inner Barrier (14-17, 8-9).
- **Test:** Unstun NPC 5 while inside East Room. Wait for Outer Gate to close. Check Inner Barrier.
- **Action:** Moving to (13, 6) to observe. Unstunning NPC 5.
- **Action:** Inspecting Inner Boxes at (14, 8) to see if they are interactable.
- **Hypothesis:** "Line of Sight" mechanic - I need to be hidden from the workers for the layout to change.
- **Plan:** Inspect boxes. If nothing, move to (17, 6) to "hide" behind the central wall and wait for a state change.
- **Action:** Interacted with Box at (14, 8) - No reaction (Inert Wall).
- **Goal:** Talk to Black Belt at (4, 8).
- **Hypothesis:** Interacting with him or entering the West area might toggle the gates (Open Bottom / Close Top).
- **Plan:** Move to (5, 8), talk to NPC, then check Bottom Gate.
- **Confirmed Dialogue (NPC 5):** "Our policy is to work behind the scenes where no one can see us!"
- **Implication:** Box layout changes might depend on Player Position (being "seen" or "unseen").
- **Timestamp:** Turn 12572
- **Action:** Interacting with Machop (7, 7).
- **Dialogue Log:**
    - NPC 5 (Middle): "Work behind the scenes..."
    - NPC 6 (Top Left): "Lose passion if watched..."
    - NPC 7 (Bottom Left): "Junk on the ground... take it."
- **Hypothesis:** Machop might provide a clue or trigger.
- **Observation:** Machoke (7, 7) interaction yielded only "Maaacho!" (Cry). No immediate effect observed.
- **Puzzle Logic (Hypothesis):** Inverse Relation.
    - NPC 5 at Bottom (9, 11) -> Top Gates Open, Bottom Gates Closed.
    - NPC 5 at Top (9, 9) -> Bottom Gates Open, Top Gates Closed?
- **Plan:**
    1. Move to (8, 12).
    2. Wait for NPC 5 to move Up to (9, 9).
    3. If Bottom Gate (10, 12) opens, STUN NPC 5 immediately.
    4. Enter South East Room.
- **Backup:** Talk to Black Belt at (7, 13).
- **Hypothesis:** NPC Facing Direction controls the gates.
    - NPC 7 is facing **Right** (towards Bottom Gates). Gates are **Closed**.
    - **Test:** Make NPC 7 face **Up** or **Down** (away from gates) to see if they open.
    - **Plan:**
        1. Move to (6, 13). Talk (He faces Right). Check Gates.
        2. Move to (5, 12). Talk (He faces Up). Check Gates.
        3. Move to (5, 14). Talk (He faces Down). Check Gates.
- **Correction:** NPC 7 moves between (5, 13) and (6, 13), blocking access.
- **Action:** Stunning NPC 7 to safely move to (6, 13).
- **Observation:** While moving, NPC 7 faces Right and Left. Gates remained closed. This suggests simple facing during movement doesn't trigger it, or I missed it.
- **Plan:**
    1. Stun NPC 7.
    2. Move to (6, 13).
    3. Unstun and Talk (Force Static Right Face).
    4. Move to (5, 12) (Force Static Up Face).
- **Correction (Turn 12580):** Move to (6, 13) failed because NPC 7 occupied it.
- **Plan Adjustment:**
    1. Move to (6, 12) (Above NPC 7 at 6, 13).
    2. Attempt to Talk (Down) to force NPC 7 to Face Up.
    3. Check Gates at (10, 12).
    4. If no change, Unstun NPC 7 and retry.
- **Observation:** NPC 7 is moving (Stun seemingly failed or reset).
- **Action:** Interacting with NPC 7 from (6, 12).
- **Requirement:** Must face DOWN to talk.
- **Expectation:** NPC 7 turns UP.
- **Observation Target:** Check if Gates at (10, 12) open when he faces UP.
- **Correction:** NPC 7 is NOT moving (no path data), just changed facing to Down.
- **Action:** Pressing A to talk to NPC 7 from (6, 12).
- **Test:** Will making NPC 7 face UP open the Bottom Gates (10, 12-13)?
- **Current State:** Gates are CLOSED. NPC 7 facing DOWN.
- **Correction:** NPC 7 was STUNNED. This prevents him from "working" (moving boxes).
- **Action:** Unstunning NPC 7.
- **Plan:** Move to (9, 12) and face Right (towards gate, away from NPC) to test "Behind the Scenes" hypothesis.
- **Hypothesis:** If I don't watch the NPC, he will open the gate.
- **Observation:** NPC 7 interaction ("Oohah! Oohah!") confirmed as a Pokémon cry (Machoke sound?) or exertion noise. No dialogue.
- **Hypothesis:** "Behind the Scenes" mechanic.
- **Test:** Stand at (9, 12), face RIGHT (East). This faces the gate but puts the NPC (West) out of view behind me.
- **Goal:** See if gate (10, 12) opens.