# Pokémon Mansion 3F - Map & Navigation Log

## Permanent Physical Barriers (Same in State A and State B)
- **Column 15 Row 3 is a Solid Wall:** Column 15 Row 3 is blocked by a permanent solid vertical wall panel. Horizontal travel across Column 15 on Row 3 is impossible.
- **Column 15 Crossing (Rows 4-5):** Column 15 has solid vertical wall panels on Row 2, Row 3, and Rows 6-9. Horizontal crossing between 3F West and 3F East is open pink checkered floor on Row 4 and Row 5.
- **Row 6 Column 22 is a Solid Wall:** Solid vertical partition wall panel (impassable).
- **Row 8 Barrier (Columns 11-28):** Horizontal barrier running across the floor. Vertical travel across Row 8 is possible via Column 11 and Column 12 in the west.
- **Column 11 Row 16 is a Solid Wall:** Solid vertical partition wall panel, preventing horizontal travel along Row 16 between 3F West (Column 10) and 3F East (Column 12).
- **Row 12 Debris (Columns 14-17):** Solid rubble permanently blocks horizontal travel along Row 12 on Columns 14-17.
- **Column 19 Row 17 is a Solid Wall:** Permanent solid cabinet/wall structure in both states, blocking direct vertical passage down Column 19 from Row 16 to the balcony.

- **Row 16 Railing (Columns 21-28):** Empirically verified solid and impassable at `(25, 16)` on Turn 74017 (player bumped). Tile `(25, 14)` is a staircase warping between 3F and 2F Southeastern Chamber (verified Turn 74020).

- **Column 22 Rubble Barrier (Rows 8-15):** Empirically verified solid impassable rubble across all rows from Row 8 to Row 15 (tested Turns 74113-74125). There is no horizontal passage across Column 22 on Rows 8-16.

## State-Dependent Shutter Gates

- **Central Corridor Gates (15, 4-5) and (15, 10-11):**
  - Gate at `(15, 4)` and `(15, 5)`: OPEN in State A, CLOSED in State B (verified Turn 73958).
  - Gate at `(15, 10)` and `(15, 11)`: CLOSED in State A, OPEN in State B (verified Turn 73958).
- **Row 7 Shutter Gates (Columns 16-17):** Shutter gates at `(16, 7)` and `(17, 7)`. Empirically verified CLOSED in State A on Turn 73279. OPEN in State B!
- **Row 13 East Shutter Gate (Columns 24-25):** Shutter gate at `(24, 13)` and `(25, 13)`. Empirically verified OPEN in State A on Turn 73242. Empirically verified CLOSED in State B on Turn 73340.
- **Row 17 Balcony Shutter Gate (Columns 20-21):** Shutter gate at `(20, 17)` and `(21, 17)`. Empirically verified CLOSED and impassable in State A on Turn 73708 (player at (21, 16) bumped when stepping Down). State B configuration is an unverified hypothesis.
- **Row 27 Southeast Shutter Gate (Columns 26-27):** Shutter gate on southern boundary at `(26, 27)` and `(27, 27)`. Empirically verified CLOSED in State A on Turn 73269. (State B unverified).

## Verified Layout & Physical Constraints (Turns 73310-73322)
- **Central Statue Chamber (Columns 14-21, Rows 8-12):** Gated on the north by shutter gates at `(16, 7)` and `(17, 7)` (OPEN in State B, CLOSED in State A). West wall is Column 13. South wall is a solid partition wall along Row 13 from Column 13 to Column 21. East boundary is solid rubble on Column 22. This chamber is an enclosed dead-end with NO southern exit.
- **Mewtwo Statues at `(16, 10)` and `(18, 10)`:** Verified inactive with NO interactable switches (tested turns 73316-73317).
- **Column 17 Dead-End:** Column 17 terminates at a solid horizontal wall panel at `(17, 12)` on Row 13. It does NOT connect south to Row 16.
- **Column 12 Vertical Corridor & Row 13 Wall (Turn 73731):** Open pink checkered floor on Rows 6-12 between Column 11 and Column 13. At `(12, 13)` and `(13, 13)`, the corridor terminates in a solid horizontal wall panel. Column 12 does NOT connect south to Rows 14-16.
- **Column 10 Vertical Corridor (Turns 73732-73738):** Open pink checkered floor on Column 10 from Row 10 down to Row 22 (and Column 9 alongside it), running south west of the solid Column 11 vertical partition wall. Visually extends down to Row 26.
- **Tile `(4, 6)`:** Blocked by permanent structure/obstacle; Row 6 cannot be crossed horizontally through Column 4. Must use Row 1 or Row 8 bypass.

## Southeastern Chamber & Southern Wing Layout (Verified Turns 73680-73708 in State A)
- **Column 24 Vertical Barrier:** Continuous solid vertical wall on Rows 19-23, and continuous rubble on Rows 24-27. This completely isolates Columns 26-28 from Columns 20-23 across all southern rows.
- **Column 25 Rubble:** Solid rubble blocks Column 25 on Rows 24-27.
- **Row 27 Boundary:** Columns 22-23 terminate in a solid wall/counter at Row 27. Columns 24-25 are rubble at Row 27. Columns 26-27 terminate in a closed shutter gate at `(26, 27)` and `(27, 27)` in State A.
- **Burglar NPC & Inner Balcony Corridor:** Burglar is located at `(17, 17)` with balcony railing at `(17-19, 18)`. Columns 17-23 on Row 20 are open pink floor, but completely unreachable from Columns 24-28 due to the Column 24 wall and Row 17 closed gates.
- **Column 11 Vertical Barrier (Verified Turn 73743):** Solid vertical wall panel extends continuously from Row 13 all the way down to Row 27, where it meets the solid Row 27 south wall. There is NO eastern crossing between Column 10 and Column 12 anywhere on Rows 13-27.
- **Row 27 Southern Boundary (3F West, Verified Turn 73743):** Row 27 is a continuous solid wall/counter across Columns 8-15, terminating the map at Row 27. Rows 28-30 are void.

## 3F Southwest Quadrant Layout (Verified Turns 73746-73764)
- **Columns 1-2 Western Corridor:** Continuous open pink checkered floor running vertically from Row 10 down to Row 26 along the solid Column 0 western outer wall.
- **Columns 4-7 Red Carpet Runner:** 4-tile wide red carpet running uninterrupted from Row 10 down to Row 27.
- **Columns 3 & 8 Pedestals:** Lined with display pedestals on even rows (Rows 14, 16, 18, 20, 22, 24) with open pink floor gaps on odd rows (Rows 15, 17, 19, 21, 23, 25, 26).
- **Row 9 Northern Boundary:** Solid continuous horizontal wall across Columns 1-7.
- **Row 10 Connection & Stairs:** Open corridor at Row 10 connecting Columns 1-7 directly to the hallway leading to descending stairs to 2F West at `(6, 1)`. Row 11 connects Columns 1-12 across.
- **Southwest Dead-End:** No switches, pitfalls, or exits in the southwest quadrant; all paths terminate at Row 27 solid wall.
- **Central Switch Chamber (Columns 11-15, Rows 7-11, Verified Turn 73912):**
  - Row 8 Column 11 is a solid horizontal wall panel. Passage to Column 13 is via Row 7 `(12, 7)` and `(13, 7)`.
  - Mewtwo statues are located at `(12, 9)` and `(12, 11)` with a shrub at `(12, 10)`. Both statues face east toward open pink floor on Column 13 `(13, 9)` and `(13, 11)`.
## Negative Interaction Logs (Verified Ground Truth)
- **Mewtwo Statues at (12, 9) and (12, 11) (Verified Turn 73917 & 73928):** Inactive decorative statues with NO switches. Tested facing UP from (12, 12) on Turn 73917 (negative), and tested facing LEFT from (13, 11) on Turn 73928 (negative). No prompt or dialogue triggered.

- **Active 3F Mewtwo Statue Switch at `(10, 5)` (Verified Turn 73953):** Confirmed active secret switch! Interacted from `(10, 6)` facing UP. Triggers "A secret switch!" prompt.
## Trainers on 3F
- **Scientist Ted at `(19, 11)`:** Defeated on Turn 73998 (awarded ¥1650). No longer blocks or initiates combat.
## Empirical Pitfall & Warp Drops (Verified Ground Truth)
- **3F East Pitfall at `(19, 14)` (Verified Turn 74244):** Stepping into the dark pitfall tile at `(19, 14)` on 3F East drops the player to `(18, 14)` on 2F East Southwest Corridor (`(19, 13) -> (19, 14) -> [New Map|(18, 14)]`).

- **Row 12 Column 22 Open Bridge (Verified Turn 74354):** Tile `(22, 12)` is open pink checkered floor between rubble at `(22, 11)` and wall at `(22, 13)`, providing horizontal passage between Columns 19-21 and Column 23.
- **Rows 14-15 Central Chasm (Verified Turn 74354):** Columns 18-22 on Rows 14 and 15 are a dark grey chasm/void (pitfall). Column 23 is open pink floor bypassing the chasm to the east.