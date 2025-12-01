# Gem's Pokémon Crystal Adventure!

## Game Plan
- Start my journey and get my first Pokémon.

## Tile Mechanics
*I will document my observations on tile traversal rules here.*
- `TYPE_2889`: Confirmed impassable. Acts as a wall or solid object.
- `TYPE_1dc2`: Hypothesized impassable (bookshelf).
- `TYPE_17bc`: Hypothesized impassable (bookshelf).
- `TYPE_3fe2`: Confirmed traversable floor tile.
- `TYPE_a82`: Hypothesized impassable (PC).
- `TYPE_1fdc`: Hypothesized impassable (TV).

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
- Test 3: Attempt to move to (3, 2) to interact with the PC from the side.
- Result: Failed. Movement to (3, 2) is blocked.
- Conclusion: An object (a chair) on a normally traversable tile type (`TYPE_3fe2`) can make it impassable. This is a new mechanic. Interacting with the PC from the side is not possible.

## New Plan
- Since interacting with the PC has failed from all possible angles, I will now attempt to interact with other objects in the room.
- Next Target: Bookshelves at (6, 0) and (7, 0). I will move to (6, 1) to interact with them.

## Lessons Learned
- Do not re-test a hypothesis that has already been proven false. For example, once a tile type is confirmed to be impassable, do not attempt to move onto it as part of a new hypothesis.