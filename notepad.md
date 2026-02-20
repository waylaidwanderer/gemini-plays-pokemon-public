### Objectives
- [ ] Get Card Key from Director (Current Loc: 3_53, (18,30))
- [ ] Return to Radio Tower 3F
- [ ] Open Shutters and Defeat Team Rocket

### Warehouse Puzzle Solution
- **Winning State:** Switch 1 ON, Switch 2 OFF, Switch 3 OFF -> Opens Gate 3 (Far Right).
- Gate 3 leads to the Director's Room stairs.

### Key Locations
- Director: Map 3_53 (18, 29)
- Radio Tower: Goldenrod City
- Realized I was turning away from the Director before pressing A. Corrected approach: Move to (18, 30), Face UP, Press A.
- Realized (17, 29) and (17, 30) are WALLS (TYPE_2889). Cannot approach from left.
- Front interaction at (18, 30) failed.
- Plan: Try interacting with the desk/tiles to the right at (19, 29) and (20, 29).
- Checked inventory: No Card Key yet. Must finish dialogue.
- Trying to go BEHIND the desk. Path: (21, 30) -> (21, 28) -> (19, 28).
- This area is unexplored and might allow interaction with the Director from a different angle.
- Tried interacting from (19, 28) facing Left (18, 28) and Down (19, 29).
- If this fails, will try interacting from (21, 29) facing Left.
- Testing walkability of (18, 28) and (19, 29).
- If blocked, will assume interaction must be from (18, 30) and failed due to missing trigger (e.g. Grunt at 19, 24).
- Director interaction at (18, 30) failed repeatedly.
- Grunt interaction at (19, 25) failed to trigger battle in turn 50432 (moved away too fast?).
- Plan: Return to Grunt at (19, 25). Interact CAREFULLY. Do not move away.
- If Grunt is unresponsive, search for hidden switch or item in the room.
- Attempting `advance_dialogue` on Grunt at (19, 24).
- If this fails, I will assume the Grunt is non-interactive and focus 100% on the Director at (18, 29).
- Possibility: The 'Director' sprite is actually at (19, 29) visually? Checking screen alignment.
- Grunt interaction confirmed failed (no dialogue).
- Returning to Director.
- Strategy: Test interaction on BOTH sides of the desk.
- 1. Stand at (19, 30), Face UP, Press A. (Testing right side of desk).
- 2. Stand at (18, 30), Face UP, Press A. (Testing left side/Director body).