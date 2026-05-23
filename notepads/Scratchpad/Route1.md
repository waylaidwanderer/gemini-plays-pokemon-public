# Route 1 Exploration Scratchpad
- Live tracking and active routing on Route 1. Started Turn 121 (Saturday, May 23, 2026 at 12:45 PM PDT).

## Hypotheses to Verify:
1. Viridian City Connection:
   - Route 1 goes straight north to Viridian City. (VERIFIED - Turn 209)
2. Wild Encounters:
   - Tall grass on Route 1 contains wild Pidgey and Rattata. (VERIFIED - Turn 194)
3. Item Delivery:
   - Viridian City Poke Mart clerk will give us Oak's Parcel once we talk to him. (VERIFIED - Turn 247)

## Verified Overworld Facts:
- Route 1 Entrance from Pallet Town is at X=10, 11 on Map 0_0 (Row Y=0) and Map 0_12 (Row Y=35).
- Between Y=35 and Y=32, there is a narrow corridor of tall grass (TYPE_fed7) flanked by ledges/fences (TYPE_2889) at X=9 and X=12.
- At Y=31, a clear path (TYPE_3fe2) begins. There is a ledge (TYPE_44f6) blocking straight north movement at Y=27 on columns X=10 to X=15.
- To bypass the Y=27 ledge, we must walk left to Column X=8 (which has clear path at (8,31) and (8,30)) and then proceed north through columns X=6, 7, or 8.
- Talked to the Poké Mart clerk at (5, 24) on Turn 182 and received a free POTION.

## Active Routing Log:
- Turn 207: Successfully navigated Route 1 from Pallet Town to Viridian City.
- Turn 258 (Saturday, May 23, 2026 at 1:28 PM PDT): Successfully returned to Route 1 (Map 0_12) at (10, 0) from Viridian City. Our primary goal is to return to Pallet Town to deliver Oak's Parcel. Plan: walk Down 4 steps to (10, 4) on clear path.

## Quest: Returning to Pallet Town (Oak's Parcel Delivery)
- **Start Turn:** 258
- **Start Time:** Saturday, May 23, 2026 at 1:28 PM PDT
- **Hypothesis:** We can jump south over the Y=5 ledge (TYPE_44f6) from (10, 4) to (10, 6). (VERIFIED - Turn 262. Landing coordinates (10, 6), proved standard Southward one-way jump mechanic.)
- **Test Plan & Results:**
  1. From (10, 4), press 'Down' to attempt the ledge jump to (10, 6). (Completed Turn 262 - landed at (10, 6))
  2. Verify coordinates and visual screen to prove ledge jump mechanic. (Verified. System position changed multiple times: (10, 4) -> (10, 5) -> (10, 6).)
- **Route Tracking Down Route 1:**
  - (10, 4) -> Start
  - (10, 6) -> Landed via ledge jump (Turn 262)
  - (10, 10) -> Walked Down 4 steps (Turn 271)
  - (8, 14) -> Arrived on Turn 280 (ledge jump successful!).
  - (5, 18) -> Walked Left 3, Down 4 along Column 5 corridor to avoid tall grass (Turn 283).
  - (5, 22) -> Planned next destination via Column 5 (Turn 288).
  - (10, 22) -> Arrived on Turn 312 (exploring right side of Row 22).
  - (12, 24) -> Successfully arrived on Turn 314 (Right 2, Down 2 bypass route via Column 12 through Row 23 tree line).
  - (5, 24) -> Planned next movement Left 7 steps along Row 24 (Turn 331).
  - (5, 24) -> Arrived on Turn 333 (Left 7 completed). Detected Poké Mart clerk NPC at (5, 25).
  - (4, 28) -> Planned bypass route via Column 4 to avoid the NPC and jump the Y=27 ledge (Turn 335).
  - (4, 28) -> Arrived on Turn 341 (bypass successfully completed, ledge jumped!).
  - (10, 28) -> Planned next move Right 6 steps along Row 28 to reach Column 10 (Turn 342).
  - (6, 28) -> Encountered wild Rattata in the tall grass on Turn 349. SQUIRTLE (GEMMY) at 22/22 HP.
  - Turn 351: GEMMY missed with Tackle. Wild Rattata used Tackle (GEMMY HP 19/22).
  - Turn 353: Back at the fight menu, ready to select Tackle again.
  - Turn 355: GEMMY has 16/22 HP, Rattata HP is still full. Ready to select Tackle again.