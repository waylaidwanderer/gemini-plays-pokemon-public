# Scratchpad: Victory Road Route & Puzzle States
- Current Turn: 105488
- Current Position: (23, 7) on Map 0_198 (Victory Road 3F East)

## Goal
Cross to the east side of 3F East via the northern Row 2/3 bypass and navigate to the ladder at (27, 7) (which is located at (26, 8) on 3F East) to descend into the isolated northern pocket of 2F East and reach the exit.

## Current Visual Layout (Turn 105488):
- Player is standing at (23, 7).
- Boulder C3 is reset at (22, 3).
- Row 6 is a solid horizontal wall of TYPE_2889 blocking (24, 6) through (28, 6).
- Row 10 is completely blocked from (24, 10) to (28, 10) by rock walls and Boulder C2 (at (24, 10)).
- Column 23 is blocked vertically at Row 9 by a rock wall (23, 9).
- Column 24 acts as a complete vertical boundary on ground level (Rows 11-15), dividing Column 23 and below from Column 25 and above.

## Verified Routing to (26, 8) on 3F East:
- Since Column 23 Row 9 is blocked, we cannot go South to Row 10 to cross directly.
- We must go North to the Row 2/3 northern corridor, cross Right to Column 27, and go South to Row 8.
- However, Boulder C3 is currently blocking (22, 3) (which is to our Left-Up, but wait, can we walk on Column 23?).
  - Let's check Column 23 from Row 7:
    - (23, 7) -> (23, 6): TYPE_3fe2
    - (23, 6) -> (23, 5): TYPE_3fe2
    - (23, 5) -> (23, 4): TYPE_3fe2
    - (23, 4) -> (23, 3): TYPE_3fe2
    - (23, 3) -> (23, 2): TYPE_3fe2? Wait!
    - Let's look at (23, 3) in the screenshot: it is TYPE_3fe2, but wait!
    - Let's check (22, 3): there is a boulder at (22, 3).
    - Can we walk from (23, 7) straight Up to (23, 2)?
      - Yes! Let's check:
        - (23, 7) is our current spot.
        - (23, 6) is open.
        - (23, 5) is open.
        - (23, 4) is open.
        - (23, 3) is open.
        - (23, 2): wait, let's look at Row 2.
        - On Row 2: (23, 2) is open!
        - Wait, what about Boulder C3 at (22, 3)? It is at Column 22! So it doesn't block Column 23!
        - Wait, is this really true?
        - Let's check:
          - (22, 3) has a boulder.
          - Column 23 is completely empty from Row 7 to Row 2!
          - So we can walk straight Up to (23, 2) without pushing ANY boulders!
          - Oh my god! Is that true? Let's check:
            - Yes! Column 23 has no boulder!
            - Let's check if there is any wall on Column 23:
              - (23, 6) is TYPE_3fe2.
              - (23, 5) is TYPE_3fe2.
              - (23, 4) is TYPE_3fe2.
              - (23, 3) is TYPE_3fe2.
              - (23, 2) is TYPE_3fe2? No, wait! On the screen, Row 2 is not fully visible, but Row 3 is:
                - (23, 3): TYPE_3fe2.
                - (22, 3): TYPE_3fe2 (but has boulder).
                - (24, 3): TYPE_3fe2.
                - (25, 3): TYPE_3fe2.
                - (26, 3): TYPE_2889 (wall).
                - (27, 3): TYPE_3fe2.
                - (28, 3): TYPE_3fe2.
                - (22, 4): TYPE_3fe2.
                - (23, 4): TYPE_3fe2.
                - (24, 4): TYPE_2889 (wall).
                - (25, 4): TYPE_2889 (wall).
                - (26, 4): TYPE_2889 (wall).
                - (27, 4): TYPE_3fe2.
                - (28, 4): TYPE_3fe2.
              - Wait! Look at Column 24:
                - (24, 4), (25, 4), (26, 4) are all TYPE_2889 (solid wall)!
                - So Row 4 is blocked from Column 24 to Column 26.
              - Look at Row 3:
                - (24, 3): TYPE_3fe2 (open!)
                - (25, 3): TYPE_3fe2 (open!)
                - (26, 3): TYPE_2889 (wall).
                - So Row 3 is blocked at Column 26!
              - Wait, what about Row 2?
                - (23, 2) is open.
                - (24, 2) is open.
                - (25, 2) is open.
                - (26, 2) is open.
                - (27, 2) is open.
                - Yes! Row 2 is completely open across Column 26!
                - So the path to cross from Column 23 to Column 27 is on Row 2!
                - Can we reach Row 2 from Column 23?
                  - Yes, we can just walk Up Column 23: (23, 7) -> (23, 6) -> (23, 5) -> (23, 4) -> (23, 3) -> (23, 2).
                  - This is completely open!
                  - Wait, does the boulder at (22, 3) block us from walking Up Column 23?
                  - No! The boulder is at Column 22. We are on Column 23.
                  - So we can walk straight Up Column 23 to Row 2, then walk Right to Column 27 on Row 2, and then walk Down Column 27 to Row 8!
                  - Let's double check if there are any barriers on Column 27:
                    - (27, 2): open.
                    - (27, 3): open (TYPE_3fe2).
                    - (27, 4): open (TYPE_3fe2).
                    - (27, 5): open (TYPE_3fe2).
                    - (27, 6): TYPE_2889 (solid wall!).
                    - Oh!!!
                    - (27, 6) is a solid rock wall!
                    - So we CANNOT walk Down Column 27 past Row 5!
                    - Wait, what about Column 28?
                      - (28, 6) is also TYPE_2889 (solid wall). So no.
                    - What about Column 26?
                      - (26, 6) is also TYPE_2889 (solid wall). So no.
                    - What about Column 25?
                      - (25, 6) is also TYPE_2889 (solid wall). So no.
                    - What about Column 24?
                      - (24, 6) is also TYPE_2889 (solid wall). So no.
                    - What about Column 23?
                      - (23, 6) is TYPE_3fe2 (open).
                    - Yes! Row 6 is completely blocked by solid rock wall `TYPE_2889` from Column 24 to Column 28!
                    - So there is absolutely NO WAY to walk south from Row 2 to Row 8 on the east side of 3F East!
                    - That is why the bypass must be done on 2F East!

## Correct Verified Progression via 2F East (Step-by-Step):
1. Stand at (23, 7) on 3F East.
2. Go DOWN the ladder to 2F East (lands at (23, 7)).
3. Walk to the plateau stairs:
   - Walk Down to (23, 11) (4 steps: (23, 8), (23, 9), (23, 10), (23, 11)).
   - Walk Left 4 steps to (19, 11).
   - Walk Down 4 steps to (19, 15).
   - Walk Right 2 steps to (21, 15) (Plateau Stairs East).
   - Step Up onto the stairs to climb onto the plateau (21, 15).
4. Walk east on the plateau:
   - Walk Right 5 steps to (26, 15).
   - Walk Up 1 step to (26, 14) (ladder).
5. Take the ladder at (26, 14) UP to 3F East (lands at (27, 15)).
6. Walk to (26, 8) on 3F East (this is on the east side, completely open):
   - From (27, 15), walk Up 7 steps to (27, 8).
   - Walk Left 1 step to (26, 8) (ladder).
7. Take the ladder at (26, 8) DOWN to 2F East (lands at (27, 7) inside the isolated pocket).
8. Walk north to the exit at (28, 1)!
- Turn 105515: Verified that on 3F East, Row 6 is completely blocked by a solid rock wall of TYPE_2889 from Column 24 to Column 28, preventing any southern traversal on the east side from Row 2. Therefore, the northern bypass on 3F East is impassable for crossing to the southeastern exit.
- Strategy: We must use the 2F East plateau route instead.
  1. Step off the ladder at (23, 7) to (23, 8) (Down), then step back on to (23, 7) (Up) to transition back to 2F East.
  2. Walk to the plateau stairs on 2F East.
- Turn 105584: Standing on the ladder at (27, 7) on 2F East. Since Row 6 is completely blocked by solid wall TYPE_2889 (Columns 24-29) and Row 10 is completely blocked by solid wall TYPE_2889 (Columns 24-28), this northeast section is a closed, isolated ground-level pocket on 2F East on the right side of Column 24.
  - To exit this pocket and return to 3F East, we must step off the ladder to the south to (27, 8) (Down) and step back UP onto the ladder at (27, 7) (Up) to trigger the map transition.
  - On 3F East, we can walk north to Row 2/3, cross left to Column 23, walk south to (23, 7), and take the ladder at (23, 7) down to the other side of 2F East, where we can access the plateau stairs to cross over to the actual exit pocket.
  - Wait, let's verify if the northern part of 2F East is blocked. In our notes: "the northern ground floor of 2F East (Columns 19-27, Rows 7-11) is a completely closed, isolated pocket on ground level (z=0)."
  - But wait! Let's check how to reach the exit at (28, 1).
  - Let's look at the exit: is it on 3F East or 2F East?
  - Actually, in vanilla, the exit to Route 23 is on 3F East!
  - Wait, let's test if there is an exit on 3F East or 2F East.
  - Let's first return to 3F East by stepping off the ladder and back onto it.
  - Path: Down to (27, 8), Up to (27, 7) to transition back to 3F East.
- Turn 105731: Verified that the exit of Victory Road is indeed on 3F East in the northeast corner at (28, 1).
- Because Row 6 is blocked on the east side of both 2F and 3F, and Column 23 Row 4 is blocked on 2F East, the ONLY open path to the northern area (Rows 1-5) is to walk UP Column 23 on 3F East from (23, 7) to Row 2, then walk Right on Row 2 to Column 28, and walk Up to (28, 1) to exit.
- Since we are currently at (21, 16) on ground level of 2F East, we can walk around Koga's plateau entirely on ground level via the eastern ground corridors (Row 17 and Column 28) with ZERO boulder pushes and ZERO Strength activations!
- Step-by-Step Route to Victory Road Exit:
  1. From (21, 16) on ground level, walk Down 1 step to (21, 17) (Down).
  2. Walk Right 7 steps along Row 17 to (28, 17) (Right 7).
  3. Walk Up 6 steps along Column 28 to (28, 11) (Up 6).
  4. Walk Left 5 steps along Row 11 to (23, 11) (Left 5).
  5. Walk Up 4 steps along Column 23 to (23, 7) (Up 4).
  6. Take the ladder at (23, 7) UP to 3F East (lands at (23, 7)).
  7. Walk Up 5 steps to Row 2 at (23, 2).
  8. Walk Right 5 steps to Column 28 at (28, 2).
  9. Walk Up 1 step to (28, 1) to exit Victory Road!
- Let's begin executing step 1, 2, and 3: Walk Down 1, Right 7, Up 6.
  - Path: Down, Right, Right, Right, Right, Right, Right, Right, Up, Up, Up, Up, Up, Up.
  - Let's chunk this into: Down, Right, Right, Right, Right, Right, Right, Right.
  - Let's execute this chunk!