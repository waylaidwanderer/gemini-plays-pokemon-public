# Scratchpad: Victory Road Route & Puzzle States
- Route Started: Turn 107326 | Timestamp: Friday, June 19, 2026 at 12:25 PM PDT
- Current Position: (13, 11) on Victory Road 3F East (Map 0_198) | Turn: 107881

## Scientific Testing Plan for Victory Road Exit
We must locate the exact exit warp tile by systematically investigating the 2F East northeast corner.

### Hypothesis 1: 3F East Northeast Corner (Completed Testing)
- **Hypothesis**: The true exit of Victory Road is on the 3rd Floor (3F) East in the northeast corner (Columns 20-28, Rows 0-2).
- **Testing Method**: Systematically step on and test Row 0 and Row 1 candidate tiles.
- **Empirical Test Results on 3F East**:
  - (28, 2): Stepped on at Turn 107581. Result: No warp triggered.
  - (28, 1): Stepped on at Turn 107589. Result: No warp triggered.
  - (28, 0): Pressed Up at Turn 107590. Result: BUMPED (solid rock wall).
  - (27, 0): Pressed Up at Turn 107599. Result: BUMPED (solid rock wall).
  - (26, 0): Pressed Up at Turn 107602. Result: BUMPED (solid rock wall).
  - (25, 0): Pressed Up at Turn 107606. Result: BUMPED (solid rock wall).
  - (24, 0): Pressed Up at Turn 107610. Result: BUMPED (solid rock wall).
  - (23, 0): Pressed Up at Turn 107617. Result: BUMPED (solid rock wall).
  - (22, 0): Pressed Up at Turn 107621. Result: BUMPED (solid rock wall).
  - (21, 0): Pressed Up at Turn 107632. Result: BUMPED (solid rock wall).
  - (20, 0): Pressed Up at Turn 107639. Result: BUMPED (solid rock wall).
  - (19, 0): Pressed Up at Turn 107645. Result: BUMPED (solid rock wall).
- **Conclusion**: Hypothesis 1 is completely DISPROVEN. No exit warp exists on 3rd Floor (3F) East Row 0 or Row 1 on Columns 20-28.

### Hypothesis 2: 2F East Northeast Corner (Active)
- **Hypothesis**: The exit is at (28, 1) on 2F East, reached by taking the ladder at (26, 8) on 3F East down to (27, 7) on 2F East.
- **Routing Strategy Audit**:
  - Note: (27, 7) on 2F East is inside a completely closed, isolated ground-level pocket on 2F East (bounded by Koga's plateau to the south and the Row 6 rock wall to the north). 
  - If we land at (27, 7) on 2F East, we cannot walk north to Row 1/Row 2 due to the Row 6 solid rock wall across Columns 24-28.
  - Therefore, to access the true northern part of 2F East on ground level, we must utilize the southern ground corridor at Row 16 to cross from 2F East to 2F West, and bypass the plateau.
  - Let's construct a complete unblocked pathing hypothesis via 2F West to reach the northern half of 2F East on ground level.
- **Unblocked 2F West Ground-Bypass Hypothesis**:
  1. We are currently at (9, 2) on 3F East. We must walk to (27, 15) on 3F East and take the ladder DOWN to 2F East (lands at (26, 14) on 2F East plateau level).
  2. From (26, 14), we walk West along the 2F plateau corridor to 2F West (around Column 13/14, Row 12/13).
  3. We descend from the 2F plateau to the southern ground floor at Row 16.
  4. On Row 16, we walk West to Column 9 (near Switch B2 at (9, 16)).
  5. We walk North along Column 9 (which serves as our unblocked vertical passage on the West side) to bypass Koga's plateau and reach the northern ground area at Row 3.
  6. We walk East along Row 3 from Column 9 all the way to Column 27/28 on 2F East.
  7. From Column 27/28, we walk North to Row 1 to reach and test the exit warp at (28, 1) on 2F East!
- **Status**: Active. Navigating back to (27, 15) ladder on 3F East.

### Hypothesis 3: 1F East Northeast Corner (On Hold)
- **Hypothesis**: The true exit is on 1F East.
- **Status**: On hold pending results of Hypothesis 2.

## Current Pathing Instructions:
- Turn 107883: We are standing at (13, 11) directly north of the boulder at (13, 12) with overworld STRENGTH active.
- Step 1: Press Down to push the boulder at (13, 12) Down 1 tile onto (13, 13).
- Step 2: Press Down to step forward onto (13, 12).
- Step 3: From (13, 12), walk East 1 step to (14, 12)? No, (14, 12) is solid rock wall. Wait! We walk Down onto (13, 13)? No, (13, 13) is occupied by the boulder we just pushed.
- Wait! Since the boulder is at (13, 13), we can walk:
  - From (13, 12), walk Right to (14, 12)? Blocked.
  - From (13, 11), we can walk:
    - We must trace how to bypass the boulder at (13, 13).
    - Wait! If we push the boulder at (13, 12) Down to (13, 13), can we walk Left or Right from (13, 13)?
    - Yes, (14, 13) is open!
    - So once we stand on (13, 12), can we walk to (14, 13)? No, we would have to walk through (13, 13) which is blocked, or through (14, 12) which is a solid wall!
    - Wait! Let's check: can we walk:
      - Standing at (13, 11), we push the boulder Down to (13, 13).
      - Then we walk Left to (12, 11) -> (12, 12) is solid wall.
      - Wait! Is there an open path?
      - Let's check if (14, 11) is open. Yes, (14, 11) is open!
      - From (14, 11), can we walk Down to (14, 12)? No, (14, 12) is solid wall.
      - Can we walk from (14, 11) to (15, 11) -> (15, 12) is solid.
      - Wait! If Row 12 is completely solid across Columns 14 to 21, and Column 13 Row 12 has the boulder (which we push to 13, 13)...
      - Then if we push the boulder to (13, 13), the only way to get to the south side of Row 12 is through Column 13!
      - But Column 13 Row 13 is occupied by the boulder!
      - Since the boulder is at (13, 13), we must be able to stand on (13, 12) and walk onto (13, 13)? No, the boulder blocks it!
      - Wait! If the boulder is at (13, 13), can we push it Down again?
        - To push it Down again from (13, 12) facing Down, we would push it onto (13, 14).
        - But (13, 14) is solid TYPE_2889 wall! So we cannot push it Down again!
      - Wait, can we push it Left or Right?
        - To push it Right onto (14, 13) (which is open), we must stand at (12, 13) facing Right.
        - But (12, 13) is a solid wall (TYPE_2889)! So we cannot stand at (12, 13)!
        - To push it Left onto (12, 13) (which is solid wall), we cannot push it Left.
      - Wait! How do we cross Row 12 then?
      - Let's think: is (13, 14) really solid wall?
        - Looking at `<CurrentScreen turn="107883">`:
          - (13, 14) is labeled TYPE_2889 (solid rock wall).
          - (13, 15) is labeled TYPE_2889 (solid rock wall).
          - Wait! What about Column 14 Row 14?
          - (14, 14) is labeled TYPE_3fe2 (open ground)!
          - And (14, 13) is labeled TYPE_3fe2 (open ground)!
          - And (13, 13) is labeled TYPE_3fe2 (open ground)!
      - Wait! What if we do NOT push the boulder Down, but we push it... wait, we can only push it Down from (13, 11) facing Down.
      - Once it is pushed Down to (13, 13):
        - Can we walk Down to (13, 12) (which is now empty)?
        - Yes!
        - And from (13, 12), can we walk Left or Right?
        - (12, 12) and (14, 12) are solid walls, so we cannot walk Left or Right on Row 12!
      - Wait, then is there a way to push the boulder Right from (13, 12)?
        - To push it Right from (13, 12), we would need to stand at (12, 12) (which is solid wall). We cannot.
      - Wait! How is the puzzle solved in vanilla Pokémon Red/Blue?
        - In vanilla, on 3F East, there is a boulder at (13, 12).
        - The player pushes it Down once.
        - Then, wait! In vanilla, does the player push it Down and then can they walk past it?
        - Let's check!
        - In vanilla, the layout of 3F is:
          - There is a boulder on 3F in the center-left.
          - You push it Down into the pocket.
          - But wait! You don't walk past it!
          - The boulder is pushed onto a switch!
          - Ah! Is there a switch at (13, 14) or (13, 13)?
          - No, there is no switch there.
          - Wait! Let's think: does pushing the boulder at (13, 12) Down clear a path, or does it do something else?
          - Let's check our notes on 3F West Boulder C1:
            - Boulder C1 at (22, 3) is pushed all the way to (3, 5) switch.
          - Is there another boulder on 3F?
            - Yes! "Boulder C4 at (13, 12)"!
            - Wait, what is the purpose of Boulder C4 at (13, 12)?
            - Let's check if there is another switch!
            - No, there is no switch.
            - Wait, let's search our notepads or think if there's any other route.
            - Let's search for "Boulder C4" in our notepads.
            - Ah! Let's do that in a code snippet or search. But first, let's write down the active 3F East routing in our notepad.