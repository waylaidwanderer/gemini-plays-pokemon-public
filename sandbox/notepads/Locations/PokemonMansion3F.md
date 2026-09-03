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
- **Row 13 East Shutter Gate (Columns 24-25):** Shutter gate at `(24, 13)` and `(25, 13)`. Empirically verified OPEN in State A on Turn 73242. CLOSED in State B.
- **Row 17 Balcony Shutter Gate (Columns 20-21):** Shutter gate at `(20, 17)` and `(21, 17)`. Empirically verified CLOSED in State A on Turn 73256. OPEN in State B!
- **Row 27 Southeast Shutter Gate (Columns 26-27):** Shutter gate on southern boundary at `(26, 27)` and `(27, 27)`. Empirically verified CLOSED in State A on Turn 73269. OPEN in State B!

## Mewtwo Statue Switches on 3F
- **3F West Switch:** Located at `(2, 5)`. Interacted from `(2, 6)` facing UP.
- **3F Central-East Statue:** Located at `(16, 10)` and `(18, 10)`.

## Ground Truth Route to Balcony Drop (B1F West)
The balcony drop tile at `(19, 18)` drops the player directly into B1F West at `(9, 16)`.
In **State B**:
1. At 3F West switch `(2, 5)`, toggle to **State B**.
2. Walk east along Row 6 to Column 16/17 `(16, 6)` or `(17, 6)`.
3. Walk Down through the open shutter gates at `(16, 7)` / `(17, 7)` to Row 16!
4. Walk south along Column 17 past the Burglar at `(17, 17)` to Row 20 `(17, 20)`!
5. Walk East along Row 20 to `(20, 20)`.
6. Walk North along Column 20 to `(20, 18)`.
7. Walk West to `(19, 18)` (balcony railing) and step Down to drop directly into B1F West!
