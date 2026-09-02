# Victory Road Puzzle Mechanics & Master Log

## Floor 1F Puzzle System

### Verified Solution for 1F Switch (17, 13)
- (15, 13), (17, 14), (18, 13) are solid rock walls.
- The ONLY open approach to Switch Plate (17, 13) is from the North at (17, 12).
- Sequence:
  1. From (16, 14), push Boulder North to (16, 12).
  2. Walk around via (14, 14) -> (14, 12) -> (15, 12).
  3. From (15, 12), push Boulder East to (17, 12).
  4. Walk around via (15, 11) -> (17, 11).
  5. From (17, 11), push Boulder South onto Switch Plate (17, 13)!

### Empirically Verified Observations (Floor 1F)
- Exit Warp Boundary: (8, 17) and (9, 17) immediately exit to Route 23 and reset all boulders.
- Obstacles: (6..7, 14..15) and (10..11, 15..16) are solid 2x2 rock obstacles.
- Switch Plate: Located at (17, 13) in eastern chamber.
- Shutters Observed: (5, 13), (7, 7), and (15, 7) have purple horizontal shutter graphics.
- Upper Plateau: Middle plateau (rows 9-12, cols 5-7) is accessible from (5, 12). Cooltrainer stands at (7, 5).

## Floor 2F Puzzle System

### Baseline Observations (Floor 2F)
- Spawn Ladder from 1F: (0, 8)
- Boulder 1: Located at (5, 5)
- Shutter 1: Located at (5, 10) (3 purple horizontal bars)
- Switch Plate 1: Located at (9, 11) (circular red/yellow plate)
- Juggler / Trainer: Located at (12, 9) facing Left

### Verified Push Mechanics & Trajectories
- Empirical Push Protocol: When Strength is active, pressing the directional button toward a boulder immediately pushes the boulder 1 tile into the adjacent vacant space, while the player remains on the starting tile during that frame. A second step in the same direction moves the player into the vacated tile.
- Verified 2F Boulder 2 Solution:
  1. Position at (5, 14) facing West towards Boulder 2 at (4, 14).
  2. Press Left -> pushes Boulder 2 to (3, 14).
  3. Walk to (3, 13) via (4, 14) -> (4, 13) -> (3, 13).
  4. Press Down -> pushes Boulder 2 to (3, 15).
  5. Step Down to (3, 14), press Down -> pushes Boulder 2 to (3, 16).
  6. Walk to (4, 16) via (3, 15) -> (4, 15) -> (4, 16).
  7. Press Left -> pushes Boulder 2 to (2, 16).
  8. Step Left to (3, 16), press Left -> pushes Boulder 2 onto Switch Plate 1 at (1, 16)!
  9. Shutter 1 at (5, 10) OPENS permanently for the session!
### Floor 2F Boulder Reset State (Default)
- Initial Spawn: Boulder 1 at (5, 5), Boulder 2 at (4, 14).
- Switch Plates: Switch 1 at (1, 16) [controls Shutter 1 at (5, 10)]; Switch 2 at (9, 11).
- Dynamic Session State: Resets whenever entering 2F from ladders/warps. Strength must be re-activated each session.
## Floor 2F Verified Layout & Eastern Sector Findings
- Shutter 1 at (5, 10) is opened when Boulder 2 is placed on Switch 1 at (1, 16).
- (15, 8) is a solid rock wall corner; eastward passage from (14, 8) along row 8 is blocked.
- (18, 9) contains an Item Ball (not a boulder).
- (19, 8) has a trainer facing Down/Left.
- (23, 14) has an elevation boundary / ledge separating the lower highway at row 14 from the platform containing the ladder at (25, 14).
- Access to the upper platform / 3F ladder (25, 14) and Moltres (11, 5) requires traversing the northern upper corridor (rows 1-3) or testing NW ladder (1, 1).