# B3F Stairs Warp Trigger Testing Log

We are systematically testing candidates for the staircase warp trigger to B4F on Rocket Hideout B3F.

## Candidate Coordinates to Test:
1. **(19, 13)** - Near the Rocket Grunt at (20, 12).
2. **(20, 13)** - Directly in front of the Rocket Grunt.
3. **(19, 15)** - Traditional ROM coordinate (assembly Y=19, X=15, which translates to X=15, Y=19 on map grid, but let's also test (19, 15)).
4. **(24, 15)** - Far right row 15.

## Testing Log:
- **(28, 15)** to **(19, 15)**: Traversed. Did NOT warp. Status: **Unsuccessful**.
- **(19, 12)**: Traversed on Turn 14343. Did NOT warp. Status: **Unsuccessful**.
- **(19, 13)**: Traversed. Did NOT warp. Status: **Unsuccessful**.
- **(19, 14)**: Traversed on Turn 14360. Did NOT warp. Status: **Unsuccessful**.
- **(19, 15)**: Traversed on Turn 14363. Did NOT warp. Status: **Unsuccessful**.
- **(20, 15)**: Traversed on Turn 14358. Did NOT warp. Status: **Unsuccessful**.
- **(24, 15)** to **(28, 15)**: Traversed on Turn 14365. Did NOT warp. Status: **Unsuccessful**.
- **(18, 14)**: Blocked from North (Turn 14333) and East (Turn 14361). Status: **Impassable**.
- **(15, 19)**: This is our current primary candidate! (Since Y=19, X=15 in ROM assembly is actually X=15, Y=19 on the map grid). We are heading to test it.
- **(15, 19)**: Tested on Turn 14385. Blocked by solid wall. Status: **Unsuccessful**.
- **(18, 19)**: This is the real staircase coordinates (ROM `warp 19, 18` which is Y=19, X=18)! It is entered from the South at `(18, 20)` by walking Up.
- **Row 20 blocked**: Row 20 is blocked at Column 15 by a solid wall `(15, 20)`. So we cannot walk to `(18, 20)` from the west.
- **Super Potion**: Obtained on Turn 14439 from the Poké Ball at `(3, 21)` in the bottom-left corner room.