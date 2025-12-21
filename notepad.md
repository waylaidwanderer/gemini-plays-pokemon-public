# Tile Mechanics
- FLOOR: Walkable surface. Verified.
- WALL: Impassable barrier. Verified.
- COUNTER: Impassable barrier. Interactable from the front tile. Verified.
- STAIRCASE: Triggers map transition. Verified.
- WARP_CARPET: Triggers map transition. Verified.
- ELEVATOR_DOOR: Warp to Elevator Interior (11_17). Verified.

# Global Knowledge
## Lessons Learned
- **Elevators:** Elevator doors are warps. If a button doesn't work, try walking into the door.
- **Counters:** To talk to someone behind a counter, stand in front of the counter tile and face it.
- **Input Hygiene:** NEVER mix directional buttons with A/B/Start/Select in a single turn when precision is required (e.g., interacting with objects).
- **Vending Machines:** Lemonade (350) is the best value for HP restoration (80 HP).

## Pokemon Type Effectiveness
- Rock/Ground -> Poison: Super Effective (GNEISS vs Koffing)
- Fire -> Grass: Super Effective (Calcifer vs Gloom)
- Water -> Fire: Super Effective (vs Growlithe)
- Flying -> Bug: Super Effective (Icarus vs Spinarak)

# Strategy: Switch Room Puzzle (Map 3_54)
- Goal: Clear path to ladder at (23, 3).
- Puzzle Start (Reset): Turn 9462.
- Method: Testing sequences from clean state (all OFF).
- Experiment Log (Attempt 2):
    1. Baseline (All OFF): All shutters CLOSED.
    2. Switch 3 (2, 1) ON: (12, 8) OPEN, (12, 9) CLOSED, (6, 9) CLOSED.
    3. Switch 2 (10, 1) ON: (12, 9) OPEN.
    4. Switch 1 (16, 1): Target sequence 3-2-1. Flipping now.
- Current Status: Switch 3 ON, Switch 2 ON, Switch 1 OFF.
- Sequence Attempts: 2 (3-2-1 in progress). Investigating sequence logic.

# Area Notes
## Underground Warehouse Switch Room (3_54)
- Switches: 1 (16, 1), 2 (10, 1), 3 (2, 1).
- Items: Item Ball at (14, 9), Item Ball at (1, 12).
- Trainers: Rocket Grunt (17, 2), Burglar Eddie (4, 8), Rocket Grunt (Puzzle) 2 (11, 3), Rocket Grunt (Puzzle) 3 (3, 2).
- Exit: Ladder at (23, 3) leads to the Director's location.
- Rival: Rival Malice encountered at (20, 4) upon entry.