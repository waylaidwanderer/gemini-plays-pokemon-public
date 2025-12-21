# Tile Mechanics
- FLOOR: Walkable surface. Verified.
- WALL: Impassable barrier. Verified.
- COUNTER: Impassable barrier. Interactable from the front tile. Verified.
- STAIRCASE: Triggers map transition. Verified.
- WARP_CARPET: Triggers map transition. Verified.
- ELEVATOR_DOOR: Warp to Elevator Interior (11_17). Verified.
- LADDER: Triggers map transition. Verified.
- WARP_CARPET_DOWN: Triggers map transition. Verified.

# Global Knowledge
## Lessons Learned
- **Elevators:** Elevator doors are warps. If a button doesn't work, try walking into the door.
- **Counters:** To talk to someone behind a counter, stand in front of the counter tile and face it.
- **Input Hygiene:** NEVER mix directional buttons with A/B/Start/Select in a single turn when precision is required (e.g., interacting with objects).
- **Vending Machines:** Lemonade (350) is the best value for HP restoration (80 HP).
- **Shutter Baseline:** Always re-verify shutter states visually after every switch flip, even if you think you know the baseline. Earlier assumption about (10, 6) being WALL at baseline was incorrect.

## Pokemon Type Effectiveness
- Rock/Ground -> Poison: Super Effective (GNEISS vs Koffing)
- Fire -> Grass: Super Effective (Calcifer vs Gloom)
- Water -> Fire: Super Effective (vs Growlithe)
- Flying -> Bug: Super Effective (Icarus vs Spinarak)

# Strategy: Switch Room Puzzle (Map 3_54)
- Goal: Clear path to ladder at (21, 25).
- Puzzle Start (Reset): Turn 9462.
- Method: Systematic mapping of switch-shutter relationships.
- Switch Logic Table:
    - Switch 1: Toggles Right-side shutters {16, 6; 17, 6; 12, 8; 12, 9}.
    - Switch 2: Toggles Left and Middle shutters {10, 6; 6, 8; 6, 9}.
    - Switch 3: Toggles Middle shutters {12, 8; 12, 9}.
- Experiment Log (Attempt 3): 3-2-1 sequence (All ON) failed. Path blocked.
- Strategy: Following Strategist's 3-2-1 sequence (Started Turn 9605).
    - Step 1: Switch 3 ON (Completed).
    - Step 2: Switch 2 ON (Target).
    - Step 3: Switch 1 ON.

# Area Notes
## Underground Warehouse Switch Room (3_54)
- Switches: 1 (16, 1), 2 (10, 1), 3 (2, 1).
- Items: Item Ball at (14, 9), Item Ball at (1, 12).
- Trainers: Rocket Grunt (17, 2), Burglar Eddie (4, 8), Rocket Grunt (Puzzle) 2 (11, 3), Rocket Grunt (Puzzle) 3 (3, 2).
- Exit: Ladder at (23, 3) leads to the Director's location.
- Rival: Rival Malice encountered at (20, 4) upon entry.