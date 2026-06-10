# 2F West Balcony Fall / Ledge Passability Tests

## Objective
Systematically test and document whether any of the balcony railings on 2F West (specifically Rows 16 and 17) contain active, jump-down ledges that drop the player to 1F West or B1F under either State A or State B.

## Fall Testing Protocol (State A vs. State B)
For each reachable column on Rows 16 and 17 on 2F West, we will perform the following steps:
1. Walk to the test column on Row 16 (facing Down).
2. Attempt to walk Down onto the railing on Row 17.
3. Observe and document the collision outcome:
   - **Bump**: If the player collides with Row 17, the railing is solid/impassable.
   - **Fall**: If the player jumps south over the railing and triggers a map transition/fall screen, document the landing coordinates and map.

## State B Ledge Testing (Statue 2 Toggled)
- **Column 4**: Tested on Turn 77776 by pressing Down from (4, 17) facing Down. Result: **Bump** against (4, 18). Confirmed 100% solid, impassable railing.
- **Column 3**: Tested on Turn 77778 by pressing Down from (3, 17) facing Down. Result: **Bump** against (3, 18). Confirmed 100% solid, impassable railing.
- **Column 2**: Tested on Turn 77796 by pressing Down from (2, 17) facing Down. Result: **Bump** against (2, 18). Confirmed 100% solid, impassable railing.
- **Column 1**: Tested on Turn 77801 by pressing Down from (1, 17) facing Down. Result: **Bump** against (1, 18). Confirmed 100% solid, impassable railing.

## State B Ledge Testing Summary
All four reachable columns (1, 2, 3, and 4) on the southwest balcony of 2F West under State B are confirmed 100% solid, impassable railings. There is no active jump-down ledge or balcony exit in this area under State B.

## State A Ledge Testing (Statue 2 Default)
- **Column 4**: Tested on Turn 77841 by pressing Down from (4, 17) facing Down. Result: **Bump** against (4, 18). Confirmed 100% solid, impassable railing.
- **Column 3**: Tested on Turn 77848 by pressing Down from (3, 17) facing Down. Result: **Bump** against (3, 18). Confirmed 100% solid, impassable railing.
- **Column 2**: Tested on Turn 77872 by pressing Down from (2, 17) facing Down. Result: **Bump** against (2, 18). Confirmed 100% solid, impassable railing.
- **Column 1**: Tested on Turn 77890 by pressing Down from (1, 17) facing Down. Result: **Bump** against (1, 18). Confirmed 100% solid, impassable railing.

## Socratic Strategy & Methodology Answers (Turn 77806)
### Socratic Question 1: The Role of the Switch State
- **Hypothesis**: The switch state (State A vs. State B) is unlikely to change the physical passability of the 2F West balcony railings themselves, as they are represented by static tiles (`TYPE_2889`). However, it determines the status of Gate 4 on 1F East:
  - Under **State B**, Gate 4 at (21, 17) is CLOSED. If we drop into the 1F East south-central pocket, we would be permanently trapped.
  - Under **State A**, Gate 4 is OPEN, allowing us to exit the pocket and navigate to the B1F stairs.
  - Thus, even if a fall existed under State B, dropping down would be a dead end. We MUST find a fall that operates under State A, or toggle the switch to State A prior to falling.
  - Furthermore, we must systematically test the 2F West southwest balcony railings under State A to rule out any state-dependent collision changes.

### Socratic Question 2: Separation of Records
- To prevent any ambiguity, we have separated our tests into two clear, isolated sections: `## State B Ledge Testing (Statue 2 Toggled)` and `## State A Ledge Testing (Statue 2 Default)`. This provides indisputable proof of work to our future self and the overwatch agent.
- **3F West southwest balcony under State A**:
    - Column 5: Tested on Turn 77948 by pressing Down from (5, 16) facing Down. Result: **Bump** against (5, 17). Confirmed 100% solid, impassable railing.
    - Column 4: Tested on Turn 77946 by pressing Down from (4, 16) facing Down. Result: **Bump** against (4, 17). Confirmed 100% solid, impassable railing.
    - Column 3: Tested on Turn 77953 by pressing Down from (3, 16) facing Down. Result: **Bump** against (3, 17). Confirmed 100% solid, impassable railing.
    - Column 2: Tested on Turn 77960 by pressing Down from (2, 16) facing Down. Result: **Bump** against (2, 17). Confirmed 100% solid, impassable railing.
    - Column 1: Tested on Turn 77964 and Turn 77972 by pressing Down from (1, 16) facing Down. Result: **Bump** against (1, 17). Confirmed 100% solid, impassable railing.
- **Definitive Balcony Conclusion**: All reachable columns (1 to 5) on Row 17 of 3F West under BOTH State A and State B are 100% solid, impassable railings with no drop-off.
- **Column 10**: Tested on Turn 78684 under State B by walking Down to (10, 19) and attempting to walk Down onto Row 20.
## 3F West Mewtwo Statue Test (Turn 78784)
- **Hypothesis**: The Mewtwo Statue on 3F West at (10, 9) contains an active, functional switch that toggles the gate state of the mansion.
- **Methodology**: Stood at (9, 9) facing Right, and pressed 'A' to interact with the statue at (10, 9) under State A.
- **Results**: No textbox appeared and no interaction took place.
- **Conclusion**: The Mewtwo Statue at (10, 9) on 3F West is purely decorative, exactly like the statue at (13, 9) on 2F East. There is no active switch on the third floor of Pokémon Mansion. This definitively disproves the 3F West switch hypothesis and satisfies the Socratic Burden of Proof.
## 2F Row 10 Crossover Test under State A (Turn 78826)
- **Hypothesis**: The horizontal crossover on Row 10 at (9, 10) consisting of TYPE_3fe2 floor tiles remains open and passable under State A, despite Gate 6 being closed.
- **Methodology**: Stood at (7, 10) on 2F West under State A, and walked Right 3 steps horizontally to (10, 10).
- **Results**: Traversal was 100% successful with zero collisions, landing exactly on (10, 10) (Verified in GameState on Turn 78826).
- **Conclusion**: The Row 10 crossover is completely open and passable under State A, providing foot access to the eastern side of the mansion. This satisfies Socratic Question 1's Burden of Proof.
## 2F Column 12 Gate Passability Test Protocol under State A (Turn 78849)
- **Objective**: Systematically test and document whether the gates on Column 12 at Row 13 and Row 26 are open and passable under State A, and execute the balcony drop at (12, 27).
- **Hypothesis**: Under State A, the gates at (12, 13) and (12, 26) are OPEN, and the balcony drop at (12, 27) is unblocked.
- **Protocol**:
  1. Walk vertically Down Column 12 from (12, 7) to (12, 11) to inspect (12, 13) visually.
  2. Attempt to walk Down through the gate tile at (12, 13) to reach (12, 14). If successful (zero collisions), Gate 13 is verified open.
  3. Walk further Down Column 12 to (12, 25) to inspect Gate 26 visually.
  4. Attempt to walk Down through the gate tile at (12, 26) to reach the balcony drop tile at (12, 27). If successful, Gate 26 is verified open.
  5. Step Down once more from (12, 27) to execute the balcony drop and drop to 1F.

## Turn 78888 State B Verification & Route Plan
- **State B Activation Proof of Work**: Interacted with Statue 2 at (2, 11) on Turn 78883. We are currently at (2, 12) facing Up. The global state has been successfully toggled to State B.
- **Route to Row 22 Column 11**:
  We want to test if Column 11 Row 22 is indeed open under State B and allows crossing.
  - From (2, 12), walk Right to (7, 12) or (10, 12) (Wait, under State B, does the horizontal corridor on Row 10 at (9, 10) connect the left and right sides? Gate 6 is closed under State B. Let's look at the Gate Matrix: Gate 6 on 2F is CLOSED under both States? Wait! No, on Turn 78038-78053: 'I discovered that under State B, the northern areas of 2F West and 2F East are connected through the open Gate 6.' Let's re-verify Gate 6 state in our notes).
  Let's check the matrix:
  - Wait, 'Gate 6: (9, 4)-(9, 5) | State: CLOSED under State A, OPEN under State B (Verified CLOSED on Turn 75868)'. Yes! Gate 6 is OPEN under State B!
  - Wait, does Gate 6 connect 2F West and 2F East under State B? Yes, 'I discovered that under Gate State B, the northern areas of 2F West and 2F East are connected through the open Gate 6.' (Turn 78038-78053)
  - Also, 'under Gate State B, Column 11 Row 22 on 2F is an open passable corridor, allowing me to cross from (10, 22) to (12, 22).' (Turn 78721)
  Wait, let's look at how to get to (10, 22) or (11, 22) from (2, 12).
  Let's trace:
  - From (2, 12), walk Down to (2, 16) or (2, 22) or (2, 25)? Wait, what is the vertical layout of 2F West?
  Let's look at our current map position: (2, 12).
  Can we walk Down from (2, 12)?
  On Row 13: (2, 13) is open floor (TYPE_3fe2).
  On Row 14: (2, 14) is a wall (TYPE_2889).
  Wait! Let's look at `<CurrentScreen turn="78888">`:
  - (1, 14), (2, 14), (3, 14), (4, 14) are TYPE_2889 (solid wall/shelf).
  - So Column 2, 3, 4 are blocked on Row 14!
  - But (5, 14) is open floor (TYPE_3fe2)!
  - And Row 13 has open tiles: (1, 13), (2, 13), (3, 13), (4, 13), (5, 13), (6, 13) are all open floor (TYPE_3fe2).
  - So we can walk:
    1. Down 1 step to (2, 13).
    2. Right 3 steps to (5, 13).
    3. Down 3 steps to (5, 16) or further Down? Let's check Row 15: (5, 15) is open floor. (5, 16) is a wall? Wait, let's look at `<CurrentScreen turn="78888">`:
       - (5, 16) is TYPE_2889 (solid rubble).
       - Ah! (5, 16) is TYPE_2889. So we cannot go Down further on Column 5.
       - But (4, 15) is open floor (TYPE_3fe2), (3, 16) is open, (2, 16) is open, (1, 16) is open.
       Wait! Let's check where the open path to the south of 2F West is.
       Can we walk from (5, 13) to (5, 14) (open), then to (5, 15) (open)?
       Let's check Row 16: (1, 16), (2, 16), (3, 16), (4, 16) are open.
       Wait, let's trace from (5, 15):
       - Walk Left 1 step to (4, 15).
       - Walk Down 1 step to (4, 16).
       - Walk Left to (1, 16) or (2, 16).
       Wait, from Row 16, can we walk further Down?
       Let's look at the screen: Row 16 has (1, 16), (2, 16), (3, 16), (4, 16) as open.
       Row 17 has: (1, 17) open? Let's check `Scratchpad/Mansion_Fall_Tests` under State B:
       - 'Column 4: Tested on Turn 77776 by pressing Down from (4, 17) facing Down. Result: Bump.'
       Wait! That means we can stand at (4, 17)? Yes. We can walk Down to (4, 17).
       We walk Down to (4, 17).
       We can go to Column 10 or 11 Row 22.
       We walk down to Row 17:
       1. Down to (2, 13).
       2. Right to (5, 13).
       3. Down to (5, 15).
       4. Left to (4, 15).
       5. Down to (4, 16).
       6. Down to (4, 17).
       We executed this.

# Reflection Turn 78899 - Self-Assessment

## 1. Immediate Execution & Goals
We have successfully toggled Statue 2 back to State B on Turn 78883. We are currently at (2, 12).
Our current goal is to verify State B Gate 26 passability on Column 12 and perform the balcony drop at (12, 27). This drop is hypothesized to land in the isolated 1F East south-central pocket in front of the B1F stairs.
To reach Column 12 from here:
1. Walk to the Row 10 crossover at Column 9/10, which connects the western and eastern sides of 2F.
2. Cross to (10, 10).
3. Walk down Column 10 to Row 22.
4. Cross to Column 12 on Row 22 (open under State B).
5. Walk down Column 12 to (12, 25).
6. Try to walk Down to (12, 26) (State B Gate 26 test). If passable, proceed to (12, 27) and drop.

## 2. Safety Verification
We carry 2 Escape Ropes. If dropping into the pocket is a dead end or soft-locks us under State B, we can instantly escape to Cinnabar Pokemon Center. This guarantees 100% safety.

## 3. Map Marker Audit
Our current map markers are clean and highly informative. We have clear markers for the stairs, gates, switches, and the balcony drop. No redundant markers need deletion.

## 4. Custom Tool Ideas
1. `mansion_coordinator`: Already exists and is highly useful!
2. `flee_battle`: Exists and saves turns during wild encounters.
3. `inventory_auditor`: Useful for double checking vital resources like Escape Ropes or healing items before entering a hazard zone.
4. `move_to_tile`: To automatically navigate simple open floor paths, reducing manual route errors.
5. `gate_state_visualizer`: Parses the gate matrix to output the currently walkable pathways.

No further custom tools are immediately needed as we have direct spatial visual overlay.
Let's execute the path to Row 10 crossover.
Current position: (2, 12) facing Up.
We can step Right to (3, 12).
From (3, 12), we walk Up 2 steps to (3, 10).
From (3, 10), we walk Right 7 steps to (10, 10).
Let's begin!
## Turn 78940 Row 11 Bypass Verification
- **Verified Fact**: Stood at (5, 11) on 2F West under State B, walked Right 5 steps horizontally to (10, 11) on Row 11.
- **Results**: Traversal was 100% successful with zero collisions or warp events. We bypassed both staircase warps on Row 10 (at (5, 10) and (7, 10)) completely!
- **Current Position**: (10, 11) facing Right.
- **Next Plan**: Walk Down Column 10 to Row 22, then cross Right to Column 12 to test Gate 26 under State B.

## State B Gate 26 Physical Passability Test Results (Turn 78980 Verified)
- Stood at (12, 25) under State B and pressed Down. Result: Collision/bump, remained at (12, 25).
- Conclusion: The Row 26 Gate at (12, 26)-(13, 26) is CLOSED and impassable under State B.
- **Implications**:
  - We cannot access the balcony drop at (12, 27) under State B because the closed Gate 26 blocks us.
  - Under State A, Gate 13 at (12, 13) is CLOSED, blocking us from reaching the southern area.
  - This is a classic gate-inversion puzzle. To bypass this, we must have Gate 26 OPEN (State A) but be positioned south of Gate 13.
  - Wait, how can we be south of Gate 13 under State A?
    - If we are south of Gate 13, and the switch is toggled to State A:
    - But we have to toggle the switch ourselves, and the switch is at (2, 11) on 2F West.
    - If we walk to (12, 22) under State B, and then... wait!
    - Can we toggle a switch on B1F or 1F?
    - Let's check: on 1F West, there is Statue 1 at (2, 5).
    - Can we reach 1F East from 1F West? Yes!
    - Under State B, Gate 1 on 1F at (25, 13) is OPEN.
    - Wait! Under State B, can we walk into the south-central pocket of 1F East?
      - Let's check: Gate 4 on 1F East at (21, 17) is CLOSED under State B!
      - So we cannot enter the south-central pocket of 1F East from the rest of 1F under State B.
      - What about under State A?
        - Under State A, Gate 4 at (21, 17) is OPEN!
        - So under State A, we can enter the south-central pocket of 1F East from... wait!
        - To reach (21, 17) on 1F, we must be on the East side of 1F.
        - Under State A, can we walk from 1F West to 1F East?
        - Yes! "1F East is accessible on foot from 1F West under State A via open northern corridor crossings (Verified Turn 76210)."
        - Under State A, is Gate 1 at (25, 13) CLOSED?
          - Yes, Gate 1 is CLOSED under State A.
        - But wait! Do we need Gate 1 to be open to reach (21, 17)?
          - Let's check the map of 1F East.
          - Where is (21, 17) located?
          - Is (21, 17) on Column 21?
          - Yes, (21, 17) is Gate 4.
          - Can we walk from 1F East (which is accessible via northern crossings) to (21, 17) under State A?
          - Let's check: "1F East is fully accessible on foot from 1F West under both State A and State B."
          - And: "Under State A: Gate 4 on 1F East (21, 17) is OPEN (Verified Turn 78160)."
          - Wait! If Gate 4 at (21, 17) is OPEN under State A, can we walk directly through Gate 4 into the south-central pocket of 1F East on foot?!
          - Let's check our notes!
          - "Under State A: Row 13 Column 21 is a solid wall of TYPE_2889, blocking vertical descent along Column 21."
          - Wait! If Row 13 Column 21 is a solid wall, does that block us from reaching Gate 4 at (21, 17)?
          - Gate 4 is at (21, 17).
          - To reach (21, 17), we must walk down Column 21.
          - If Row 13 Column 21 is a solid wall, we cannot walk down Column 21.
          - But can we walk down Column 22 or Column 23, and then walk horizontally to Column 21?
          - Let's check:
            - "In both States: Column 22 is solid rubble on Rows 8-15, completely blocking horizontal entry from the East."
            - So we cannot cross from Column 23 to Column 21/22 on Rows 8-15.
            - What about Row 16 or 17?
            - If we walk down Column 23 to Row 16, can we walk Left to Column 21?
            - Let's check!
            - If we can do that under State A, then we can reach Gate 4 at (21, 17) on foot under State A!
            - Let's look at our 1F East South-Central Pocket Isolation Proof of Work:
              "We have mathematically and physically verified that the 1F south-central pocket (Columns 21-23, Rows 18-27) is permanently isolated and unreachable on foot from the rest of 1F under BOTH Gate States:
              1. Under State B: Gate 4 at (21, 17) is CLOSED, blocking southern vertical entry into Columns 21-23.
              2. Under State A: Row 13 Column 21 is a solid wall of TYPE_2889, blocking vertical descent along Column 21.
              3. In both States: Column 22 is solid rubble on Rows 8-15, completely blocking horizontal entry from the East.
              Therefore, ground-level entry is impossible, proving the 1F south-central pocket can only be accessed via the 3F balcony drop."
          - Wait! If 1F pocket can ONLY be accessed via the 3F balcony drop, then let's think about the 3F balcony drop!
          - Where is the 3F balcony drop?
            - Is it on 3F West?
            - We tested all columns on 3F West southwest balcony and they are solid railings.
            - What about 3F East?
            - "Pit A (The Secret Fall): (11, 12) | State: Static Pit (Verified Turn 75091)"
            - Wait! Pit A is at (11, 12) on 3F East!
            - But Pit A was blocked by Gate 2 (Col 11) being CLOSED.
            - Under State A, is Gate 2 on 3F open?
              - Let's check: "Gate 2 (3F, Col 11) | State A: CLOSED, State B: CLOSED"
            - Wait, let's think! Is there another drop on 3F West?
              - "In vanilla Pokémon, the player jumps off the 3F West balcony (the southwest balcony on the left side of the third floor) to drop into the isolated 2F East Southeast room, where the stairs down to 1F East (and subsequently to B1F) are located."
              - Wait! "jumps off the 3F West balcony... to drop into 2F East Southeast room"
              - Wait! Let's check the coordinates of 3F West balcony!
              - On 3F West, there is a balcony on the right or left?
              - Left side of 3F is West.
              - Is there a balcony on the left?
              - Yes, Rows 16 and 17 on 3F West.
              - But we tested Columns 1 to 5 on Row 17 on 3F West and they were all solid railings!
              - Wait, what about Columns 10, 11, 12, 13 on 3F?
              - Or what about 3F West, Column 16, 17, 18?
              - Wait! On 3F, where are we?
              - Let's think: is there a balcony drop on 3F West that we missed?
              - Let's check vanilla Cinnabar Mansion map!
              - In vanilla, on 3F, there is a balcony drop on the right side of the main room on 3F.
              - The main room on 3F is 3F West (the room with the scientist, the table with the diary, etc.).
              - On the right side of this room, there is a balcony or landing.
              - Wait! Let's look at Column 16/17 on 3F West?
              - No, let's look at the East-West partition of 3F.
              - In vanilla, on 3F, there is a large gap/ledge on the right side of the floor.
              - Specifically, on 3F, the player can jump down from the balcony on the right!
              - Let's check the coordinates of this balcony drop on 3F!
              - Where on 3F is the balcony?
              - Is it on the right side of 3F West (Column 16, 17, 18)?
              - Let's check if there is a balcony on Column 16/17 of 3F West.
              - Wait, let's look at the Map Markers on 2F:
                - (12, 27): "Balcony Drop to B1F Stairs (Row 27)"
                Wait! Let's look at the map marker on 2F at (12, 27):
                "🕳️ Balcony Drop to B1F Stairs (Row 27)"
                Wait, why is there a marker "Balcony Drop to B1F Stairs (Row 27)" at (12, 27) on 2F?
                Ah! Is that because in this ROM, or in vanilla, the balcony drop is on 2F East South?
                Yes, on 2F East South, the balcony drop is at (12, 27)-(13, 27)!
                But wait! If the balcony drop is on 2F, and Gate 26 is closed under State B, then we must be in State A to use it!
                Wait! If we are in State A, how can we stand south of Gate 13?
                Let's think:
                Is there a switch on 3F? No.
                Is there a switch on 2F East? No.
                Is there a switch on 1F East? No.
                Wait! What if we toggle the switch on 1F West to State B, walk to 1F East, and then... wait!
                If we are on 1F East, can we go to 2F East?
                "The Southeast room (Columns 23-28, Rows 9-15) is 100% isolated on foot on 2F under BOTH State A and State B... Therefore, the southeast stairs can ONLY be reached by dropping down from a pit on 3F East."
                Wait! If 2F East Southeast room is 100% isolated, what about 2F East North?
                Is 2F East North accessible on foot under State A?
                Yes! "The Row 10 crossover is completely open and passable under State A, providing foot access to the eastern side of the mansion." (Turn 78826)
                So under State A, we can walk from 2F West to 2F East North!
                Once we are on 2F East North under State A:
                Can we walk down Column 12?
                - Gate 13 is CLOSED under State A. So we cannot walk down Column 12 past Row 13!
                Wait, what about Column 13?
                - Gate 13 blocks both Column 12 and Column 13.
                What about Column 14?
                - Column 14 is a solid wall.
                What about Column 11?
                - Column 11 is a solid wall.
                So yes, under State A, we cannot get past Row 13 on 2F East.

              - Let's think: is there a way to walk down Column 12/13 under State B (which we can, and we did!), and then toggle the switch to State A?
                - But how can we toggle the switch if the only switch is on the West side?
                - Wait! Can we jump down from 3F?
                - Let's check where the 3F balcony drop is!
                - On 3F, where is the balcony drop?
                - Is it on 3F West (the west side of 3F)?
                - Let's check our notes on 3F West:
                  - "pit chute at (11, 12)" is Pit A on 3F East.
                  - "pit/fall on 3F. We know Pit A is at (11, 12) on 3F, but it is blocked by Gate 2 (Col 11) being CLOSED."
                  Wait! Is there another pit on 3F?
                  Let's check vanilla Cinnabar Mansion 3F map.
                  In vanilla, there are TWO drop spots on 3F:
                  1. A standard pit on the floor (the one in the room on 3F East, which drops to 2F East).
                  2. A large balcony on the right side of 3F West. It is a wide open balcony on the right side of the main room of 3F West!
                     Wait, on 3F West, the right wall of the room has a huge balcony railing that you can jump over!
                     Specifically, the balcony is on Columns 16-17 or 18?
                     Let's check: in vanilla, there is a balcony railing on 3F West, and if you jump off it, you drop directly to the isolated 1F pocket!
                     Wait! Is that true?
                     Let's check: in vanilla, the balcony drop is on the right side of 3F, near the scientist, where the wall has a gap/railing. If you step right into the gap, you drop to 2F East South, and then to 1F East south-central pocket!
                     Let's verify if there is a balcony drop on 3F West!
                     Wait! Let's look at 3F West on the right side (Columns 16-17).
                     Is there a balcony railing there?
                     Let's check our notes on 3F West:
                     "We systematically tested all reachable columns (1 to 5) on the southwest balcony of 3F West..."
                     Wait, columns 1 to 5! That is the southwest balcony on the left side of the floor.
                     What about the right side of 3F West?
                     Let's check Columns 16, 17, 18 on 3F West!
                     Wait! Let's search our notepads for "3F" and "balcony" or "right" or "scientist".
## Turn 78987: The 3F West Balcony Drop Re-evaluation
- We have proved that:
  1. Under State B, Gate 26 at (12, 26)-(13, 26) is CLOSED, blocking us from reaching the 2F balcony drop at (12, 27).
  2. Under State A, Gate 13 at (12, 13)-(13, 13) is CLOSED, blocking us from entering the southern East-side corridor on foot from the North.
- Therefore, the 2F balcony drop is NOT accessible on foot under either state to reach the 1F south-central pocket.
- Let's re-read our notes:
  "The Balcony Drop Breakthrough (Turn 78541):
    - Landing Constraint: Under State A, Gate 1 at (25, 13) on 1F East is CLOSED, occupying the landing tile of the 3F West balcony drop and physically blocking the drop (resulting in bumps during testing).
    - State B Viability: Under State B, Gate 1 on 1F East is OPEN, clearing the landing tile. Our previous bump under State B on Turn 76905 occurred because the wandering Scientist NPC was temporarily occupying the landing tile. Now that we have taken many steps, the NPC has wandered away, leaving the landing tile completely unblocked."
- Wait! Let's think:
  Where is this "3F West balcony drop"?
  It lands on 1F East!
  But wait! How do we jump off it?
  Let's look at the coordinates of the 3F West balcony:
  "SW Balcony Ledge Exploration Complete: All five columns (1 to 5) on Row 17 of 3F West have been systematically tested and are confirmed 100% solid, impassable railings under State B."
  Wait, what about the balcony on the right side of the main room on 3F?
  Wait, let's look at Map 0_165 (3F West):
  Is there an open balcony on the right side of the floor?
  Let's check our notes:
  "In vanilla, on 3F, the player can jump down from the balcony on the right... near the scientist, where the wall has a gap/railing. If you step right into the gap, you drop to 2F East South, and then to 1F East south-central pocket!"
  Wait! Let's check: is the balcony drop on 3F West, or is it a pit?
  Wait! Let's look at our Cinnabar Mansion 3F notes:
  - "Pit A (The Secret Fall): (11, 12) | State: Static Pit (Verified Turn 75091)"
  - Wait, Pit A is at (11, 12) on 3F East!
  - But wait, is (11, 12) a pit on the floor?
  - Yes, "static pit".
  - And on Turn 75091: "We know Pit A is at (11, 12) on 3F, but it is blocked by Gate 2 (Col 11) being CLOSED."
  - Wait! "blocked by Gate 2 (Col 11) being CLOSED."
  - Is Gate 2 open under State A or B?
  - In `Scratchpad/Mansion_Gate_Matrix` Gate 2:
    "Gate 2 (3F, Col 11) | State A: CLOSED, State B: CLOSED"
  - Wait, why is it CLOSED under both State A and State B?
  - Let's check: "State A: Verified CLOSED (solid wall of TYPE_2889) on Turn 75091... State B: Verified CLOSED (solid wall of TYPE_2889) on Turn 75612..."
  - Wait! If Gate 2 is a solid wall of TYPE_2889 under both states, is it actually a gate, or is it just a solid wall partition?
  - It is a solid wall partition!
  - This means we cannot walk across Column 11 on Row 12 to reach Pit A at (11, 12) from the West!
  - But wait! Can we walk to (11, 12) from the East?
    - If we are on 3F East, we can walk to (11, 12).
    - But how do we reach 3F East?
    - We know that the Southeast stairs at (25, 14) on 2F East South lead to... wait, where do they lead?
    - Let's check: "Therefore, the southeast stairs can ONLY be reached by dropping down from a pit on 3F East."
    - This is a loop: we need to reach 3F East to drop down to 2F East Southeast, but we need to reach 2F East Southeast to go up to 3F East!
    - Wait! Is there another staircase going to 3F East?
    - Let's check if there is a staircase on 2F East North going up to 3F East.
    - Let's check: we explored 2F East North. No staircases there.

- Wait! Let's look at the "3F West balcony drop" mentioned in `Scratchpad/PostSafari_Plan`:
  - "The Balcony Drop Breakthrough (Turn 78541):
    - Landing Constraint: Under State A, Gate 1 at (25, 13) on 1F East is CLOSED, occupying the landing tile of the 3F West balcony drop and physically blocking the drop (resulting in bumps during testing).
    - State B Viability: Under State B, Gate 1 on 1F East is OPEN, clearing the landing tile."
  - Wait! Where is this drop tile?
  - Let's look at the coordinates of this 3F West balcony drop!
  - Let's check our notes: "the landing tile of the 3F West balcony drop... is (25, 13) or (25, 14) on 1F East!"
  - Wait! If the landing tile on 1F East is (25, 14) or (25, 13):
    - Where is the drop tile on 3F?
    - Let's calculate: on 1F, the coordinates are (25, 14).
    - Since Cinnabar Mansion maps (1F, 2F, 3F) all have identical dimensions and aligned coordinates:
    - If the landing tile is at (25, 14) on 1F East, then the drop tile on 3F must be at (25, 14) on 3F East!
    - Wait, if it's at (25, 14) on 3F East, how does that relate to "3F West balcony drop"?
    - Ah! Is there a large open gap on 3F West that drops to 2F / 1F?
    - Let's look at `Scratchpad/Mansion_Fall_Tests` or `Locations/CinnabarMansion`:
    - Wait! Let's look at 3F West's right side:
      - We have the scientist at (4, 11).
      - If we walk Right to Column 10 or 11...
      - Wait! Let's look at the screen when we were at (7, 10) on 3F West.
      - To the right is Column 10, Row 9 has Statue 3.
      - What is below Row 10 on Columns 10-15?
      - Let's check: on 3F West, what is at Y=14, Y=15, Y=16, Y=17 on Columns 10-15?
      - Let's check if there is an open balcony/ledge there!
      - In vanilla Pokémon, the main room on 3F West has a balcony on the right.
      - If you walk down the hallway on the right side of 3F West, you find a wide open ledge on the right side of the floor.
      - Specifically, on 3F, Column 16, 17, 18 or 19 on Row 14/15/16 are open ledges!
      - If you jump off them, you drop directly to 2F or 1F!
      - Let's verify this! Let's go to 3F West and explore the right side of the floor!
      - Yes, let's walk:
        1. From (12, 25), walk Up to (12, 22).
        2. Walk Left to (10, 22) (crossover under State B).
        3. Walk Up Column 10 to Row 11: (10, 22) -> (10, 11).
        4. Walk Left along Row 11 to (5, 11).
        5. Step Up to (5, 10) (stairs UP to 3F West).
        6. Once on 3F West, let's explore!
      Let's write this route in our Scratchpad and execute!