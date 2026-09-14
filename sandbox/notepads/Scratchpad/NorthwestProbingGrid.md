# Scratchpad: Northwest Sector Local Coordinate Probing Grid (Ladder A)

## Objective & Commitment
Exhaustively map all local tiles and branches in the Northwest sector around Ladder A (1, 3) without leaving the local frontier.

## Probing Grid & Empirical Results
- (3, 1): OPEN FLOOR (visited)
  - Left (2, 1): ROCK WALL (Turn 50156)
  - Up (3, 0): PENDING TEST
  - Down (3, 2): OPEN FLOOR (Turn 50148)
- (3, 2): OPEN FLOOR (visited)
  - Left (2, 2): ROCK WALL (Turn 50148)
  - Down (3, 3): OPEN FLOOR (Turn 50148)
- (3, 3): OPEN FLOOR (visited)
  - Left (2, 3): ROCK WALL (Turn 50154)
  - Down (3, 4): ROCK WALL (Turn 50154)
  - Right (4, 3): OPEN FLOOR (Turn 50147)
- Row 0 Northern Bypass (Row 0 / cols 0..8):
  - (8, 0): OPEN FLOOR (Turn 50157)
  - (7, 0): OPEN FLOOR (Turn 50157)
  - (6, 0): PENDING TEST (Test Left from 7, 0)
  - (5..0, 0): PENDING TEST
- Target Entry into Ladder A (1, 3):
  - Ladder A at (1, 3) descends to B1F (Mewtwo).
  - Approach via (0, 3) -> Right 1 or (1, 2) -> Down 1.