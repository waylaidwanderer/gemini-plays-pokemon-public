# RockTunnel_Pathfinding (Updated Turn 25951)
- Current Turn: 25951
- Active Exploration Duration: 4460 turns (Started B1F backtracking on Turn 21491, synchronized Turn 25951)

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