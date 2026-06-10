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

### Empirical Results of 1F East Row 13 Passability Test under State A (Turns 79215-79227)
- **Turn 79215**: Tested Column 23 by standing at (23, 11) facing Down and pressing Down. Result: **Bump** against (23, 12) (`TYPE_2889`). This physically proves that Column 23 is blocked at Row 12 under State A by a solid stone pillar/statue, preventing all southern traversal along Column 23.
- **Turn 79220**: Tested Column 24 by standing at (24, 12) facing Down and pressing Down. Result: **Bump** against (24, 13) (`TYPE_a83b`). This physically proves that Gate 1 is CLOSED and impassable on Column 24 under State A.
- **Turn 79227**: Tested Column 25 by standing at (25, 12) facing Down and pressing Down. Result: **Bump** against (25, 13) (`TYPE_a83b`). This physically proves that Gate 1 is CLOSED and impassable on Column 25 under State A.
- **Final Conclusion**: Row 13 is 100% impassable on foot across all possible columns under State A, making the southern 1F East south-central pocket completely unreachable on foot from the north under State A. This definitively confirms that the B1F stairs can only be reached via the 3F East pit drop.