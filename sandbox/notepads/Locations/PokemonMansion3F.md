# PokÃ©mon Mansion 3F - Map & Navigation Log

## Permanent Physical Barriers (Same in State A and State B)
- **Column 15 Row 3 is a Solid Wall:** Column 15 Row 3 is blocked by a permanent solid vertical wall panel. Horizontal travel across Column 15 on Row 3 is impossible.
- **Row 6 Column 15 is Open:** Completely open and walkable pink checkered floor, allowing horizontal crossing (verified open in State A on Turn 72327).
- **Row 6 Column 22 is a Solid Wall:** Solid vertical partition wall panel (impassable).
- **Row 8 Barrier (Columns 11-28):** Horizontal barrier running across the floor, but vertical travel across Row 8 is possible via Column 11, Column 12, and Column 26/27. Columns 13-17 and 20-22 are solid wall panels; Columns 18-19 are bookcases; Column 23 is rubble; Columns 24-25 are wall panels. Columns 26-27 are completely open pink checkered floors (verified on Turn 73161 and Turn 73192).
- **Column 11 Row 16 is a Solid Wall:** Solid vertical partition wall panel, preventing horizontal travel along Row 16 between 3F West (Column 10) and 3F East (Column 12).
- **Row 12 Debris (Columns 14-17):** Solid rubble permanently blocks horizontal travel along Row 12 on Columns 14-17.
- **Column 19 Row 17 is a Solid Wall:** Permanent solid cabinet/wall structure in both states, blocking direct vertical passage down Column 19 from Row 16 to the balcony.

## State-Dependent Shutter Gates
- **Row 7 Shutter Gates (Columns 16-17):** Shutter gates at `(16, 7)` and `(17, 7)`. Empirically verified CLOSED in State A on Turn 73279. OPEN in State B!
- **Row 13 East Shutter Gate (Columns 24-25):** Shutter gate at `(24, 13)` and `(25, 13)`. Empirically verified OPEN in State A on Turn 73242. Empirically verified CLOSED in State B on Turn 73340.
- **Row 17 Balcony Shutter Gate (Columns 20-21):** Shutter gate at `(20, 17)` and `(21, 17)`. Empirically verified CLOSED and impassable in State A on Turn 73708 (player at (21, 16) bumped when stepping Down). State B configuration is an unverified hypothesis.
- **Row 27 Southeast Shutter Gate (Columns 26-27):** Shutter gate on southern boundary at `(26, 27)` and `(27, 27)`. Empirically verified CLOSED in State A on Turn 73269. (State B unverified).

## Mewtwo Statue Switches on 3F
- **3F West Switch:** Located at `(2, 5)`. Interacted from `(2, 6)` facing UP.

## Verified Layout & Physical Constraints (Turns 73310-73322)
- **Central Statue Chamber (Columns 14-21, Rows 8-12):** Gated on the north by shutter gates at `(16, 7)` and `(17, 7)` (OPEN in State B, CLOSED in State A). West wall is Column 13. South wall is a solid partition wall along Row 13 from Column 13 to Column 21. East boundary is solid rubble on Column 22. This chamber is an enclosed dead-end with NO southern exit.
- **Mewtwo Statues at `(16, 10)` and `(18, 10)`:** Verified inactive with NO interactable switches (tested turns 73316-73317).
- **Column 17 Dead-End:** Column 17 terminates at a solid horizontal wall panel at `(17, 12)` on Row 13. It does NOT connect south to Row 16.
- **Column 12 Vertical Corridor & Row 13 Wall (Turn 73731):** Open pink checkered floor on Rows 6-12 between Column 11 and Column 13. At `(12, 13)` and `(13, 13)`, the corridor terminates in a solid horizontal wall panel. Column 12 does NOT connect south to Rows 14-16.
- **Column 10 Vertical Corridor (Turns 73732-73738):** Open pink checkered floor on Column 10 from Row 10 down to Row 22 (and Column 9 alongside it), running south west of the solid Column 11 vertical partition wall. Visually extends down to Row 26.
- **Tile `(4, 6)`:** Blocked by permanent structure/obstacle; Row 6 cannot be crossed horizontally through Column 4. Must use Row 1 or Row 8 bypass.
## Empirical State Tracking & Observations
- **Turn 73662-73664 (State A Empirical Ground Truth of 3F East):** In State A, shutter gates at `(24, 13)` and `(25, 13)` are visibly OPEN pink checkered floor, allowing passage into southern 3F East (Rows 14-20). Row 16 is open pink floor across Columns 21-28. Row 17 has an open doorway at `(24, 17)` and `(25, 17)` leading south into Rows 18-20. Shutter gate at `(21, 17)` is CLOSED in State A.
- **Turn 73643 (Switch Toggled to State A):** Interacted with 3F West Mewtwo switch at (2, 5) from (2, 6) facing UP, selected YES ('Who wouldn't?'), toggling the mansion into STATE A.
- **Turn 73478-73484 (State B Empirical Test of 3F East Column 26 & Row 13):** In State B, walked down Column 26 from (26, 3) to (26, 11). All tiles are solid pink checkered floor with NO pitfall trigger. At Row 13, the passage is 100% solid and impassable: (22, 13)-(23, 13) rubble, (24, 13)-(25, 13) closed shutter gates, (26, 13)-(28, 13) solid horizontal wall panels. No southern passage exists on 3F East in State B.

- **Turn 73449 (State A Visual Confirmation):** Standing at (12, 9) looking east, the shutter gates at (16, 7) and (17, 7) were visibly CLOSED with orange/black bars and yellow frames, definitively proving the mansion was in State A.
- **Turn 73459 (Switch Toggled to State B):** Interacted with 3F West Mewtwo switch at (2, 5) from (2, 6) facing UP, selected YES ('Who wouldn't?'), toggling the mansion into STATE B.
- **Turn 73468 (State B Visual Confirmation):** Standing at (12, 3) looking southeast, the shutter gates at (16, 7) and (17, 7) were visibly OPEN as pink checkered floor, definitively confirming the mansion is in State B.

## Staircases & Floor Warps
- **Stairs to 2F West:** Located at `(5, 10)` on 3F West. Stepping on it warps player down to 2F West, landing at `(5, 11)` (empirically verified Turn 73379).

## Southeastern Chamber & Southern Wing Layout (Verified Turns 73680-73708 in State A)
- **Column 24 Vertical Barrier:** Continuous solid vertical wall on Rows 19-23, and continuous rubble on Rows 24-27. This completely isolates Columns 26-28 from Columns 20-23 across all southern rows.
- **Column 25 Rubble:** Solid rubble blocks Column 25 on Rows 24-27.
- **Row 27 Boundary:** Columns 22-23 terminate in a solid wall/counter at Row 27. Columns 24-25 are rubble at Row 27. Columns 26-27 terminate in a closed shutter gate at `(26, 27)` and `(27, 27)` in State A.
- **Row 17 Balcony Shutter Gate:** Closed and impassable in State A at `(20, 17)` and `(21, 17)` (tested Turn 73708, bumped). State B configuration is an unverified hypothesis.
- **Burglar NPC & Inner Balcony Corridor:** Burglar is located at `(17, 17)` with balcony railing at `(17-19, 18)`. Columns 17-23 on Row 20 are open pink floor, but completely unreachable from Columns 24-28 due to the Column 24 wall and Row 17 closed gates.