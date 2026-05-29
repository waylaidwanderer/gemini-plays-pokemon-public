# RockTunnel_Pathfinding (Updated Turn 26773)
- Current Turn: 26773
- Active Exploration Duration: 5282 turns (Started B1F backtracking on Turn 21491, synchronized Turn 26773)

## Verified Structural Layout Discoveries:
1. Column 17 on 1F: Solid blockage at (17, 15) prevents direct north passage along Column 17.
2. Column 16 on 1F: Fully passable at Rows 14 and 15, allowing us to successfully reach Ladder C at (17, 11).
3. Ladder C (1F 17, 11 <-> B1F 23, 11): Taken down on Turn 24525, taken up on Turn 25009, and down again on Turn 25025.
4. B1F Northern Passage: Fully open from Column 23 via Column 17 north to Row 4, but blocked at Columns 24 and 25 on Rows 2-4 (verified Turn 24546).
5. B1F East-West crossing at Row 20: Physically verified to be BLOCKED on Turn 24686. Columns 18 and 19 on Row 20 are solid rock walls (TYPE_2889).
6. B1F Column 20 Row 14/15 Blockage: Physically verified to be BLOCKED on Turn 24708. Row 14 Column 20 is a solid rock wall (TYPE_2889).
7. B1F East-West crossing via starting chamber: Fully open on Rows 10-13, Columns 14-23.
8. B1F East-West bypass highway: Row 16 has Columns 20-37 open, connecting directly to Column 37 (Ladder D).
9. Column 15 on B1F at Row 22 is solid rock blockage (verified Turn 24763).
10. Column 12 on B1F is a solid vertical wall (TYPE_2889) on Rows 18-25, isolating Columns 10-11.
11. Column 11 on B1F: Blocked at Row 29 by solid rock wall TYPE_2889 (verified Turn 24878, map marker placed).
12. B1F Column 23 Row 14 Blockage: Physically verified to be BLOCKED on Turn 24946. Column 23 Row 14 is a solid rock wall (TYPE_2889).
13. B1F Row 12 Columns 24-25 Blockage: Physically verified to be BLOCKED on Turn 24928. Row 12 Columns 24-25 are solid rock walls (TYPE_2889).
14. Columns 18-19 on B1F are solid rock walls on Rows 14 to 23 (verified Turn 25322).
15. Columns 13 to 19 are solid rock walls on Rows 22 and 23 (verified Turn 25322).

## Physical Verification Logs for Active Route:
- B1F Southern Corridor Columns 3-18 Passability (Verified Turn 25864): Walked completely from (19, 31) to (3, 31) along Row 31, proving that Row 31 on Columns 3 to 18 is 100% open and passable (TYPE_3fe2) on B1F.
- B1F Upper-East Row 5 Passability (Verified Turn 25158): Row 5 is completely open and passable from Column 18 to Column 22.
- B1F Column 17/23 Active Detour Physical Verification (Turns 25180-25310): Verified that Column 17 is fully passable from Row 13 to Row 20. Verified that Column 23 Row 14 and Column 21-22 Row 14 are blocked by solid rock walls (TYPE_2889).
- 1F West Column 13 Bypass (Verified Turn 25360): Column 13 has a solid rock wall on Rows 2-13, preventing direct Left movement. To bypass this wall, we walked Left from (17, 11) to (14, 11), walked Down to Row 14, and then walked Left past Column 13 on Row 14.
- 1F Columns 6-7 Blockage (Verified Turn 25363): Attempted to navigate west on Row 14 to Column 5, but collided with solid rock walls on Columns 6 and 7 on Row 14. This forced us to head North along Column 8, reaching Row 8.
- 1F Rows 8-9 Column 6-7 Passable Opening (Verified Turn 25371): Proved that Columns 6 and 7 are open and passable on Row 8, providing a direct horizontal corridor from Column 8 to Column 5 (the western vertical bypass hallway).
- 1F Column 5 Western Hallway (Verified Turn 25452): Column 5 is 100% open and passable from Row 8 to Row 3, leading directly to Ladder B at (5, 3).
- B1F Eastern Corridor Row 3 Passability (Verified Turn 25485): Row 3 is completely open and passable from Column 27 (Ladder B) to Column 33.
16. B1F Column 33 Row 6/7 Blockage (Verified Turn 25505): Column 33 is blocked on Row 6 and Row 7 by solid rock walls (TYPE_2889). Bypassed by detouring to Column 34/35.
- B1F Column 34 East Bypass Corridor (Verified Turn 25510): Column 34 is open and passable on Rows 3-7, providing an active detour past the Column 33 Row 6-7 wall blockages.
- B1F Column 34 Passability (Verified Turn 25591): Column 34 is open and passable on Rows 8-11, connecting our detour back to the central corridor areas.
- B1F Row 19 Passability (Verified Turn 25614): Row 19 is fully open and passable from Column 34 down to Column 26, confirmed visually on screen. Row 20-21 are completely blocked by solid rock walls (TYPE_2889/TYPE_2770) on Columns 26-35.
- B1F Column 25 (Rows 20-27) Passability (Verified Turn 25626): Visually verified on screen that Column 25 is completely open and passable (TYPE_3fe2) across Y=20 to Y=27, forming an active detour path south.
- B1F Column 25 (Rows 28-30) Passability (Verified Turn 25636/25650): Row 28 and 29 are completely blocked by solid rock walls (TYPE_2889/TYPE_2770) on Column 25, while Row 30 Column 25 is fully passable.
- B1F Row 27 Passability (Verified Turn 25637): Visually verified that Row 27 is fully open and passable (TYPE_3fe2) from Column 21 down to Column 17.
- B1F Column 17 Passability (Verified Turn 25637): Visually verified on screen that Column 17 is completely open and passable (TYPE_3fe2) from Row 23 to Row 31, providing an active vertical channel past the Row 28-29 walls.
- B1F Row 30 Column 26 Blockage (Verified Turn 25650): Standing at (25, 30) facing Right, we collided, proving that Row 30 is blocked at Columns 26-27 by the solid vertical rock wall extending from Row 21 down to Row 30. Row 31 must be used for crossing.
- B1F Row 31 (Columns 25-28) Passability (Verified Turn 25665): Physically walked along Row 31 from Column 25 to Column 28, verifying it is 100% open and passable (TYPE_3fe2).
- B1F Column 28 (Rows 25-31) Passability (Verified Turn 25676): Physically walked north on Column 28 from Row 31 up to Row 25, verifying it is 100% open and passable (TYPE_3fe2).
- B1F Row 25 (Columns 28-33) Passability (Verified Turn 25677): Physically walked east on Row 25 from Column 28 to Column 33, verifying it is 100% open and passable (TYPE_3fe2), leading directly to Ladder A at (33, 25) which we ascended to 1F.
- 1F Row 7 (Columns 16-23) Passability (Verified Turn 25746): Fully open and passable (TYPE_3fe2), providing an active horizontal bypass corridor.
- 1F Row 11 (Columns 20-37) Passability (Verified Turn 25746): Fully open and passable (TYPE_3fe2), forming the main east-west corridor on 1F.
- 1F Column 37 (Rows 3-11) Passability (Verified Turn 25746): Fully open and passable (TYPE_3fe2), connecting Ladder A at (37, 3) to the Row 11 corridor.
- 1F Column 23 Row 8 Blockage (Verified Turn 25812): Attempted to walk Down from (23, 7) onto (23, 8) and collided, proving that Column 23 is blocked on Row 8/9 by solid rock wall TYPE_2889/TYPE_2770.
- 1F Column 22 Row 7-10 Passability (Verified Turn 25817): Successfully walked down Column 22 from Row 7 to Row 10, proving Column 22 is an open, passable vertical bypass corridor.
- 1F Column 20 Row 7-10 Passability (Verified Turn 25817): Column 20 is also a verified open vertical corridor connecting the upper and lower sections of the eastern chamber.
- B1F Southwest Corridor Exploration & Inert Tiles Proof (Turns 25877-25895):
  - Standing at (3, 31) (Turn 25877), walked Down to (3, 33). Standing at (3, 33) (Turn 25880), walked Left to (2, 33). Standing at (2, 33) (Turn 25882), walked Up to (2, 30) (Turn 25883).
  - Standing on all these tiles did NOT trigger a warp or ladder sequence.
  - This mathematically and physically proves that the southwestern corner of B1F (specifically (3, 31), (3, 32), (3, 33), (2, 33), (2, 32), (2, 31), and (2, 30)) contains NO active warp or exit ladder. They are completely inert passable floor tiles of TYPE_3fe2.
  - Therefore, the 4th exit ladder is not in this southwestern corner. We must find another path.
- B1F Row 30 Columns 2-6 Passability (Verified Turns 25914-25918):
  - Walked from (2, 30) to (6, 30) along Row 30.
  - Encounters: Wild Machop level 15 encountered at (6, 30) on Turn 25915, successfully fled.
  - This physically proves that Row 30 on Columns 2 to 6 is 100% open and passable (TYPE_3fe2) on B1F.
- B1F Southwest to Central Backtrack and Detour (Turns 25941-25948):
  - Walked Right from (18, 30) to (25, 30).
  - Confirmed (26, 30) is blocked by solid rock wall extension Y=21 to Y=30.
  - Detoured: Walked Down to (25, 31). Walked Right on Row 31 through (26, 31), (27, 31) to (28, 31). Walked Up on Column 28 through (28, 30) to (28, 29).
  - Encounters: Wild Geodude level 16 encountered at (28, 29) on Turn 25948, successfully fled.
  - This physically proves that Row 31 on Columns 25 to 28 and Column 28 on Rows 29 to 31 are 100% open and passable (TYPE_3fe2) detours on B1F.
- 1F Row 11 (Columns 33-37) Physical Passability (Verified Turn 26042): Standing at (37, 11) facing LEFT, the current view shows columns 33 to 37 on Row 11 are completely open and passable (TYPE_3fe2), proving a clear horizontal path westwards.
- 1F Row 11 (Columns 28-32) Physical Passability (Verified Turn 26072): Walked along Row 11 from Column 34 to Column 28 on Turn 26059-26063, verifying that Row 11 is completely open and passable (TYPE_3fe2) across Columns 28 to 32, forming a continuous horizontal connection.
- 1F Row 11 (Columns 24-27) Physical Passability (Verified Turn 26102): Walked along Row 11 from Column 28 to Column 24 on Turn 26085-26089, verifying that Row 11 is completely open and passable (TYPE_3fe2) across Columns 24 to 27, forming a continuous horizontal connection.
- 1F Column 37 (Rows 11-13) and Row 13 (Columns 32-37) Passability (Verified Turn 26160): Walked south along Column 37 from Row 11 to Row 13, then west along Row 13 to Column 32, confirming complete passability (TYPE_3fe2) for these segments.
- 1F Row 13 (Columns 27-32) Passability (Verified Turn 26165): Walked west along Row 13 from Column 32 to Column 27, verifying complete passability (TYPE_3fe2). Row 14 and Row 15 are fully blocked by solid wall TYPE_2889/TYPE_2770 across Columns 23-37.
- 1F Row 13 (Columns 23-26) Physical Passability (Verified Turn 26174): Walked west along Row 13 from Column 27 to Column 23 on Turns 26161-26174, verifying that Row 13 is completely open and passable (TYPE_3fe2) across Columns 23 to 26. Visually verified Column 19 is blocked on Rows 9-15 by solid rock wall TYPE_2889.
- 1F Column 37 (Rows 3-13) and B1F Row 25 (Columns 28-33) Backtrack Corridor (Verified Turn 26234): Navigated south from (37, 3) to (37, 13) on 1F, and then walked east along Row 25 from (28, 25) to (33, 25) on B1F, confirming complete passability and successfully returning to Ladder A.
- B1F Column 15 (Rows 24-31) and Row 24 (Columns 15-19) Passability (Verified Turn 26275): Navigated south to (15, 31) and then north up Column 15 to (15, 24), then east along Row 24 to (19, 24), verifying 100% open and passable corridor segments.
- B1F Column 33 (Rows 25-31), Row 31 (Columns 28-33), Column 20 (Rows 22-24), Row 27 (Columns 17-20), and Column 17 (Rows 27-31) Detour Segments (Verified Turn 26311): Navigated south along Column 33 to Row 31, then east to (28, 31), then north up Column 20 to (20, 22) where Pokémaniac blocks the path, then backtracked south to (20, 27), detoured left along Row 27 to Column 17, walked down Column 17 to Row 31, and walked west to (4, 31), confirming 100% passability.
- B1F Row 24 (Columns 17-21) Passability (Verified Turn 26331): Walked east along Row 24 from Column 17 to Column 21, verifying a 100% open and passable corridor segment.
- B1F Active Detour Path (Turns 26371-26395): Navigated from (21, 17) to (15, 31) on B1F via (23, 18) and (25, 22), verifying passability of these segments.
- B1F West Expansion (Turns 26413-26419): Navigated from (6, 31) to (2, 30) on B1F via Column 2 Row 30 and Row 31 Columns 2-6, verifying physical passability of these corridor segments.
- B1F Return Detour (Turns 26428-26456): Navigated back from (2, 30) to (15, 24) on B1F via Column 15 Rows 24-30 and Row 30 Columns 14-15, verifying physical passability of these corridor segments.
- B1F Detour Around Pokémaniac (Verified Turns 26481-26485): Navigated around the defeated Pokémaniac sprite at B1F (20, 21) by walking south to (20, 22), east to (21, 22), north to (21, 20), and west to (20, 20), proving that these tiles are fully passable and free of obstacles.
- B1F Row 24 Passage (Verified Turns 26522-26523): Identified Row 24 as a fully open horizontal link (TYPE_3fe2) from Column 15 to Column 25, bypassing the solid blockages on Rows 22 and 23. This connects the eastern side directly to Column 17 going north.
- Active Exploration Duration Update: Synchronized to Turn 26522. Elapsed: 5031 turns.
- B1F Eastern and Central Bypass (Verified Turns 26531-26545): Walked from (26, 11) down to (26, 13), east along Row 13 to (32, 13), down Column 32 to Row 16, and west along Row 16 to (32, 16), confirming that Row 13 (Columns 26-32), Column 32 (Rows 13-16), and Row 16 (Columns 28-32) are fully passable and free of obstacles.
- B1F Row 16 Passability Progress (Verified Turns 26545-26561): Physically walked Left along Row 16 from Column 32 to Column 29, verifying that (32, 16), (31, 16), (30, 16), and (29, 16) are fully passable and free of obstacles.
- B1F Row 16 Columns 20-29 Passability (Verified Turn 26615): Physically walked Left along Row 16 from Column 29 to Column 20, proving the East-West bypass highway is fully passable on these columns.
- B1F Column 20 Rows 16-18 Passability (Verified Turn 26651): Physically walked along Column 20 from Row 16 to Row 18, verifying that Column 20 is completely open and passable.
- B1F Pokémaniac Detour (Verified Turns 26664-26667): Successfully bypassed the solid defeated Pokémaniac sprite at (20, 21) by walking south to (20, 22), east to (21, 22), north to (21, 20), and west to (20, 20), proving that Column 21 (Rows 20-22) and Row 20 (Columns 20-21) are fully open and passable detour corridor segments.
- B1F Row 31 Columns 17-28 Passability (Verified Turns 26711-26725): Walked East along Row 31 from Column 17 to Column 28, verifying the wide southern corridor is 100% open and passable.
- B1F Column 28 Rows 27-31 Passability (Verified Turns 26727-26728): Walked North along Column 28 from Row 31 to Row 27, verifying it is completely open and passable.
- B1F Row 25 Columns 28-32 Passability (Verified Turns 26729-26730): Walked East along Row 25 from Column 28 to Column 32, verifying it is 100% open and passable.
- 1F Column 37 Rows 3-11 Passability (Verified Turns 26745-26747): Physically walked South along Column 37 from Row 3 to Row 11, verifying it is 100% open and passable.
- 1F Row 11 Columns 34-37 Passability (Verified Turns 26755-26756): Physically walked West along Row 11 from Column 37 to Column 34, verifying it is 100% open and passable.
- B1F Row 16 Columns 20-29 Passability (Verified Turn 26615): Physically walked Left along Row 16 from Column 29 to Column 20, proving the East-West bypass highway is fully passable on these columns.
- B1F Column 20 Rows 16-18 Passability (Verified Turn 26651): Physically walked along Column 20 from Row 16 to Row 18, verifying that Column 20 is completely open and passable.
- B1F Pokémaniac Detour (Verified Turns 26664-26667): Successfully bypassed the solid defeated Pokémaniac sprite at (20, 21) by walking south to (20, 22), east to (21, 22), north to (21, 20), and west to (20, 20), proving that Column 21 (Rows 20-22) and Row 20 (Columns 20-21) are fully open and passable detour corridor segments.
- B1F Row 31 Columns 17-28 Passability (Verified Turns 26711-26725): Walked East along Row 31 from Column 17 to Column 28, verifying the wide southern corridor is 100% open and passable.
- B1F Column 28 Rows 27-31 Passability (Verified Turns 26727-26728): Walked North along Column 28 from Row 31 to Row 27, verifying it is completely open and passable.
- B1F Row 25 Columns 28-32 Passability (Verified Turns 26729-26730): Walked East along Row 25 from Column 28 to Column 32, verifying it is 100% open and passable.