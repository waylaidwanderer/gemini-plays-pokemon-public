# Route 1 Exploration Scratchpad
- Live tracking and active routing on Route 1. Started Turn 121 (Saturday, May 23, 2026 at 12:45 PM PDT).

## Hypotheses to Verify:
1. Viridian City Connection:
   - Route 1 goes straight north to Viridian City.
2. Wild Encounters:
   - Tall grass on Route 1 contains wild Pidgey and Rattata.
3. Item Delivery:
   - Viridian City Poke Mart clerk will give us Oak's Parcel once we talk to him.

## Verified Overworld Facts:
- Route 1 Entrance from Pallet Town is at X=10, 11 on Map 0_0 (Row Y=0) and Map 0_12 (Row Y=35).
- Between Y=35 and Y=32, there is a narrow corridor of tall grass (TYPE_fed7) flanked by ledges/fences (TYPE_2889) at X=9 and X=12.
- At Y=31, a clear path (TYPE_3fe2) begins. There is a ledge (TYPE_44f6) blocking straight north movement at Y=27 on columns X=10 to X=15.
- To bypass the Y=27 ledge, we must walk left to Column X=8 (which has clear path at (8,31) and (8,30)) and then proceed north through columns X=6, 7, or 8.

## Active Routing Log:
- Turn 151: Currently at (8, 31) on Map 0_12 (Route 1), facing Up. Plan: move Up to (8, 30) (clear path).
- Turn 156: Stepped Up to (8, 30) (clear path with flowers TYPE_3fe2). Screen confirms our position is exactly (8, 30). Plan: step Up to (8, 29) (tall grass TYPE_fed7) to continue heading north.
- Turn 160: Confirmed position at (8, 30) on Map 0_12 (Route 1), facing Up. Plan: step Up to (8, 29) into tall grass.
- Turn 164: Reached (8, 29) successfully on Map 0_12 (Route 1) without triggering a wild encounter. We are standing in tall grass (TYPE_fed7). Directly above is (8, 28) (tall grass TYPE_fed7) and then (8, 27) (clear path TYPE_3fe2). Plan: step Up to (8, 28).
- Turn 167: Verified position at (8, 29) on Map 0_12 (Route 1), facing Up. Still standing in tall grass. Plan: step Up to (8, 28) (tall grass) to reach the clear path directly ahead.
- Turn 169: Reached (8, 28) successfully on Map 0_12 (Route 1) without a wild encounter. Directly above is (8, 27) which is clear path (TYPE_3fe2) and bypasses the ledge (TYPE_44f6) at columns X=10 to X=15. An NPC (SPRITE_853c) is visible to the northwest at (5, 24). Plan: step Up to (8, 27).
- Turn 177: Reached (8, 27) successfully. NPC (SPRITE_853c) is at (5, 24). Plan: stun him at (5, 24) and walk to (5, 25) via Up, Left, Left, Left, Up, facing Up to prepare to talk to him.