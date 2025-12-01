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
- **Test Plan:** Move to (4, 2) and interact with the PC.