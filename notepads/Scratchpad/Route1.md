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
- Turn 177: Reached (8, 27) successfully. NPC (SPRITE_853c) is at (5, 24). Plan: stun him at (5, 24) and walk to (5, 25) via Up, Left, Left, Left, Up, facing Up to prepare to talk to him.
- Turn 181 (Saturday, May 23, 2026 at 1:00 PM PDT): Standing directly at (5, 25) on Map 0_12 (Route 1) facing Up, in front of the NPC at (5, 24). Plan: Press 'A' to talk and discover their identity/dialogue.
- Turn 185 (Saturday, May 23, 2026 at 1:02 PM PDT): Talked to the NPC (Poké Mart clerk) on Turn 182 and received a free POTION! Verified in inventory. Now moving Right 5 steps to (10, 25) to bypass the tree block at (5, 23).
- Turn 186 (Saturday, May 23, 2026 at 1:03 PM PDT): Arrived at (10, 25) safely. Observed tree block at Y=23 on Columns X=10 and X=11. Plan: move Right 2 steps to (12, 25) (tall grass) and then proceed north.
- Turn 188 (Saturday, May 23, 2026 at 1:03 PM PDT): Arrived at (12, 21) safely after traversing the tall grass without battles! Visually identified a ledge barrier at Y=19 (TYPE_44f6) with a flat opening at X=9. Plan: walk Left 3 and Up 3 to reach (9, 18) past the ledge.
- Turn 189 (Saturday, May 23, 2026 at 1:04 PM PDT): Arrived at (9, 18) past the ledge. No encounters triggered. Plan: move Up 4 steps to (9, 14) to explore the path ahead.
- Turn 191 (Saturday, May 23, 2026 at 1:04 PM PDT): Verified current position is (9, 14). Identified a ledge barrier directly north at Y=13 (TYPE_44f6) spanning columns X=6 to X=9, and tree block (TYPE_2889) spanning columns X=10 to X=13. Column X=14 has a tall grass corridor (TYPE_fed7) which is the only way north. Plan: move Right 5 steps to (14, 14), then Up 3 steps to (14, 11) to clear the ledge.
- Turn 193 (Saturday, May 23, 2026 at 1:05 PM PDT): Reached (14, 11) on clear path. Observed a wide grassy area (rows Y=9 to Y=7) blocking north progress. Plan: walk Up 4 steps to (14, 7) through the grass.
- Turn 194 (Saturday, May 23, 2026 at 1:05 PM PDT): Triggered wild encounter with Rattata at (14, 8) on Route 1. SQUIRTLE (GEMMY) is Level 6 with 22/22 HP. Plan: Press 'A' to send out GEMMY.
- Turn 196 (Saturday, May 23, 2026 at 1:06 PM PDT): Battle round 1 resolved: GEMMY used Tackle, dealing significant damage. Rattata used Tail Whip. GEMMY is at 22/22 HP. Plan: Use battle_fight_tackle to select Tackle again and defeat the Rattata.
- Turn 202 (Saturday, May 23, 2026 at 1:08 PM PDT): Confirmed in overworld at (14, 8) after the wild Rattata fainted. HP is 22/22. Plan: move Up 3 steps to (14, 5) to exit the grass.
- Turn 205 (Saturday, May 23, 2026 at 1:08 PM PDT): Current position is (14, 5), facing Up. The ledge line at Y=5 blocks columns X=10 to X=13, and the tree line at Y=1 blocks columns X=12 to X=18. Plan: move Up 1 to (14, 4), Left 4 to (10, 4), and Up 3 to (10, 1) to proceed north safely on clear path.
- Turn 207 (Saturday, May 23, 2026 at 1:09 PM PDT): Arrived at (10, 1) on Map 0_12 (Route 1), facing Up. The path north to Viridian City is wide open at columns X=10 and X=11. Plan: take 2 steps Up to enter Viridian City.