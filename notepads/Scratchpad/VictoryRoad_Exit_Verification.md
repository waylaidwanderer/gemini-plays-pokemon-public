# Scratchpad: Victory Road Exit Verification & Route
- Created: Turn 104187
- Current State: Standing at (27, 0) on Victory Road 3F East (Map 0_198).

## Observations & Analysis:
- On Turn 104162 and 104163, walking UP at (27, 0) on Victory Road 3F East resulted in a collision/bump against solid cave walls (0 tiles visited).
- Visually, the tiles above Row 0 are unmapped solid cave walls.
- Pokered disassembly analysis confirms Victory Road 3F (Map 198) has only 4 warps, none of which lead to Route 23.
- Pokered disassembly analysis confirms Victory Road 2F (Map 194) has a 5th warp at (29, 1) leading to Route 23.
- Thus, the actual exit to Route 23 is on Victory Road 2F East at (29, 1), NOT on Victory Road 3F East.
- We must walk south from (27, 0) to (27, 15) on Victory Road 3F, take the ladder down to 2F East, and walk to (29, 1) on 2F East to exit Victory Road.

## Testing Plan (Turn 104187):
1. Walk DOWN along Column 27 from (27, 0) to (27, 15) on 3F East.
2. Interact with/take the ladder at (27, 15) to transition DOWN to Victory Road 2F East.
3. On 2F East, verify our position and walk to (29, 1).
4. Step onto (29, 1) (or walk through the exit doorway) to transition to Route 23 North.