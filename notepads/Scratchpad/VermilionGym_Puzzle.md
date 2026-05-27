# Vermilion Gym Trash Can Lock Puzzle Strategy

## Puzzle Mechanics:
- There are 15 trash cans inside the Vermilion Gym.
- A lock blocks the path to Lt. Surge.
- To open the lock:
  1. We must search the trash cans to find the 1st switch.
  2. Once the 1st switch is found, the 2nd switch is ALWAYS located in a trash can directly adjacent (North, South, East, or West) to the 1st switch.
  3. If we search any non-adjacent can, or an adjacent can that does not contain the 2nd switch, the lock resets and we must find the 1st switch again!
  4. Once both switches are found in succession, the laser gate opens, allowing us to battle Lt. Surge.

## Systematic Search Strategy:
- We will label and map the trash cans by their coordinates (X, Y) on the Gym map.
- We will search the trash cans in a systematic serpentine pattern (e.g. left-to-right, top-to-bottom) to find the 1st switch.
- Once the 1st switch is found at (X, Y), we will systematically test adjacent tiles:
  - North: (X, Y-1) (if passable/trash can)
  - South: (X, Y+1) (if passable/trash can)
  - East: (X+1, Y) (if passable/trash can)
  - West: (X-1, Y) (if passable/trash can)
- We will log every single test with turn numbers, coordinates, and outcomes to maintain perfect mathematical traceability.

## Lock Reset Recovery Protocol:
- If the lock resets, we will resume our systematic serpentine search from the next unchecked trash can to minimize random guesswork.