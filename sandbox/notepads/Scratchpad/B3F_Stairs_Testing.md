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