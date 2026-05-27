# Vermilion City Route & Walkway Verification (Turn 17771)

## Current Status:
- Standing at (30, 20) on Map 0_5, facing UP.
- Goal: Walk to the Vermilion Pokémon Center at (11, 3).

## Verified Docks Layout:
- Column 18/19 docks are blocked at Row 25 by water, so they do NOT connect directly north to the land.
- Column 30/31 is the eastern pier that successfully connects the docks to the mainland.
- Main horizontal paved street is at Row 17, which goes west to Column 11.

## Tile-by-Tile Route from Docks to Pokémon Center:
1. Walk North along Column 30 from (30, 20) to (30, 17) (3 steps North).
2. At (30, 17), walk West along Row 17 to (11, 17) (19 steps West).
   - Verify columns 11-29 on Row 17 are clear of building collisions.
3. At (11, 17), walk North along Column 11 to (11, 3) (14 steps North).
   - This passes between the Fan Club (9, 13) and Fishing Guru (15, 13).
   - Confirm Column 11 is clear of obstacles.
4. Step onto (11, 3) facing North, and press 'A' or walk North into the Pokémon Center entrance.

## Visual Verification Protocol:
- If we bump into an unexpected barrier or NPC, immediately pause, check coordinates, stun NPCs if needed, and recalculate.