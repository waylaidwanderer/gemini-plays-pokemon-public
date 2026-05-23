# Route 1 Exploration Scratchpad
- Live tracking and active routing on Route 1. Started Turn 121.

## Hypotheses to Verify:
1. Viridian City Connection:
   - Route 1 goes straight north to Viridian City.
2. Wild Encounters:
   - Tall grass on Route 1 contains wild Pidgey and Rattata.
3. Item Delivery:
   - Viridian City Poke Mart clerk will give us Oak's Parcel once we talk to him.

## Empirical Verification Logs:
- Turn 121: Heading north towards Route 1 entrance.
- Turn 123: Verified Column X=9 has an impassable fence at Y=1 (TYPE_2889). Route 1 entrance path is at Column X=10 and X=11. Walking Right to (10,2) and Up to (10,0) to enter Route 1.
- Turn 130: Current position (10,0) on Map 0_0, facing Up. Preparing to take a step Up to enter Route 1.
- Turn 138: Standing at (10, 35) on Map 0_12 (Route 1). Corridor of tall grass (TYPE_fed7) from Y=35 to Y=32, bordered by fences/ledges (TYPE_2889) at X=9 and X=12. Clear path (TYPE_3fe2) at Y=31. Plan: move Up step-by-step to reach the path, watching for wild battles.
- Turn 142: Reached (10, 33) without triggering any wild encounters. Verified visually that row Y=32 is the last row of tall grass in this immediate corridor, and Y=31 is clear path (TYPE_3fe2). Plan: step Up to (10, 32).
- Turn 145: Reached (10, 32) safely. Row Y=31 directly above is clear path (TYPE_3fe2). Plan: step Up to (10, 31) to exit the tall grass corridor.