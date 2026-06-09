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

## Live Testing Progress
- Active Testing.

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
- **Column 2**: Tested on Turn 77858 by pressing Down from (2, 17) facing Down. Result: TBD.
- **Column 1**: Testing planned...

## Socratic Strategy & Methodology Answers (Turn 77806)
### Socratic Question 1: The Role of the Switch State
- **Hypothesis**: The switch state (State A vs. State B) is unlikely to change the physical passability of the 2F West balcony railings themselves, as they are represented by static tiles (`TYPE_2889`). However, it determines the status of Gate 4 on 1F East:
  - Under **State B**, Gate 4 at (21, 17) is CLOSED. If we drop into the 1F East south-central pocket, we would be permanently trapped.
  - Under **State A**, Gate 4 is OPEN, allowing us to exit the pocket and navigate to the B1F stairs.
  - Thus, even if a fall existed under State B, dropping down would be a dead end. We MUST find a fall that operates under State A, or toggle the switch to State A prior to falling.
  - Furthermore, we must systematically test the 2F West southwest balcony railings under State A to rule out any state-dependent collision changes.

### Socratic Question 2: Separation of Records
- To prevent any ambiguity, we have separated our tests into two clear, isolated sections: `## State B Ledge Testing (Statue 2 Toggled)` and `## State A Ledge Testing (Statue 2 Default)`. This provides indisputable proof of work to our future self and the overwatch agent.