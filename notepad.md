# Gem's Pokémon Crystal Adventure!

## Game Plan
- Start my journey and get my first Pokémon.

## Tile Mechanics
*I will document my observations on tile traversal rules here.*
- `TYPE_2889`: Confirmed impassable. Acts as a wall or solid object.
- `TYPE_1dc2`: Unknown, part of the bookshelf.
- `TYPE_17bc`: Unknown, part of the bookshelf.
- `TYPE_3fe2`: Confirmed traversable floor tile.
- `TYPE_a82`: Unknown, appears to be a PC.
- `TYPE_1fdc`: Unknown, appears to be a TV.

## Puzzle Solutions
### Staircase (PlayersHouse2F)
- **Hypothesis 1:** Walk directly left onto stair tiles (`TYPE_2889`) at (0, 4) or (0, 5).
- **Result:** Failed. Movement was blocked from (1, 4) and (1, 5).
- **Conclusion:** Direct horizontal entry is impossible.

- **Hypothesis 2:** Interact with the stairs using the 'A' button.
- **Result:** Failed. No event triggered when facing (0, 4).
- **Conclusion:** Stairs are not activated by interaction.

- **Hypothesis 3:** Entry is from the tile directly above the stairs, at (0, 3).
- **Result:** Failed. Attempting to move down from (0, 3) to (0, 4) was blocked.
- **Conclusion:** This hypothesis was flawed, as it required moving onto `TYPE_2889`, which was already confirmed to be impassable.

- **Hypothesis 4 (Current):** A story trigger is required before the stairs can be used. The PC at (4, 1) is a likely candidate for this trigger.
- **Test 1:** Moved to (4, 2), faced PC, and pressed A.
- **Result:** Interacted with the TV instead. Test failed.
- **Conclusion:** Need to find a way to interact with the PC specifically.
- **Test 2:** Remained at (4, 2) and pressed A again.
- **Result:** Interacted with the TV again. Test failed.
- **Conclusion:** Interacting from (4, 2) while facing up consistently targets the TV, not the PC. The interaction logic is not what I expected.
- **Test 3 Plan:** Move to (3, 2), face right towards (4, 1), and press A. This will test if interaction works from the side.

## Lessons Learned
- Do not re-test a hypothesis that has already been proven false. For example, once a tile type is confirmed to be impassable, do not attempt to move onto it as part of a new hypothesis.