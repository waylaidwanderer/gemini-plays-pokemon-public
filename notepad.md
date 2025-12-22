# Dept Store Basement Strategy

## Puzzle Mechanics
- **Goal:** Reach East side (Items/Ladder).
- **Hypothesis:** NPC Facing Direction triggers the gates (Boxes).
    - NPC 5 (Middle) -> Controls Row 11/12 Gates?
    - NPC 6 (Top Left) -> Controls Top Gates?
- **Rule:** Stunned NPCs do NOT change facing direction during dialogue. Must Unstun before talking.

## Basement Puzzle Strategy
- **Goal:** Open Bottom Gates (10, 13)/(11, 13).
- **Hypothesis:** NPC 7 needs to step on (8, 13) to open the gates.
- **Problem:** I was standing on (8, 13), blocking him.
- **Plan:**
    1. **Unblock:** Move to (8, 12).
    2. **Wait:** Stay at (8, 12) and watch NPC 7.
    3. **Observe:** Does he enter (8, 13)? Do gates open?
    4. **Action:** If gates open, rush in.
- **Backup:** If he refuses to enter (8, 13) even when clear, use Itemfinder to find the "junk" blocking him.
- **Note:** `Map Events` shows no background objects (hidden items), so "junk" might be flavor text or a dynamic object not in the static list.

## Status
- Player at (9, 9).
- NPC 5 at (9, 11).
- Error: Previous attempt to move to (8, 9) failed or I moved back.
- Action: Moving Left to (8, 9) to clear the spot for NPC 5. Then waiting.
## Reflection (Turn 12312)
- **Time:** Start of specific trap attempt.
- **Hygiene:** Verified map markers and notepad.
- **Status:** Player at (8, 9) facing Right. NPC 5 at (9, 9).
- **Plan:** Press A to turn NPC 5 Left. Then Stun. Then Move.
- **Root Cause Check:** If this "turn him left" strategy fails to open gates, the "Facing Direction" hypothesis might be incomplete (e.g., maybe purely position based, or there's a switch I missed). But evidence points to vision cones.