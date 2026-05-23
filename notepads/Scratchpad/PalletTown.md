# Pallet Town Exploration Scratchpad
- Live tracking of Pallet Town layout, POIs, and map connections.

## Hypotheses to Verify:
1. GEM's House:
   - Upstairs: Player's Bedroom. Contains GEM's PC (with 1 POTION inside) and SNES console.
   - Downstairs: Living Room. GEM's Mom is here.
2. Blue's House:
   - Located to the right (east) of GEM's House. Contains Blue's sister.
3. Oak's Lab:
   - Located in the south of Pallet Town. Contains Professor Oak, his aides, and 3 starter Poké Balls.
4. Route 1 Connection:
   - Located to the north of Pallet Town. Leaving Pallet Town via Route 1 without a Pokémon should trigger Professor Oak to stop us.

## Empirical Verification Logs:
- Turn 47: Preparing to load into player's bedroom (GEM's Bedroom).
- Turn 54: Loaded into GEM's Bedroom. Verified starting position is (3,6) facing up. Verified room layout is 8x8 with PC at (0,6), TV/SNES at (3,5), Bed at (3,4). Walking to PC at (0,6) to withdraw Potion.
- Turn 57: Position is (1,6). Walking Up to Row 2, Left to Column 0, and facing Up to interact with the PC at (0,1).
- Turn 61: PC storage list is open with cursor on 'POTION'. Preparing to press A to select it.
- Turn 63: Successfully withdrew POTION from PC! It is now in our inventory. PC is empty. Exiting PC menu.
- Turn 66: Position is (0,2). Potion successfully withdrawn. Walking to the stairs at (3,0) to go downstairs.
- Turn 67: Verified (3,0) is an impassable partition wall (TYPE_fed7) and NOT the stairs. Visually identified the stairs are located at (7,1). Current position is (3,1). Planning to walk Right 4 times to step on (7,1) and warp downstairs.
- Turn 69: Arrived downstairs in GEM's Living Room (Map 0_37) at (7,1). Visually verified Mom is at (5,4) and table at (3,4)-(4,4). Planning to walk to (5,5) to go around them.
- Turn 70: Position is (5,5) facing Left. Walking Down to Y=6, Left to X=2, and Down to (2,7) to exit the house.