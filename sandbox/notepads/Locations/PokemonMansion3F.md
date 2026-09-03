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
- **State B (Default):**
  - Shutter gate at `(12, 13)` is **OPEN**, unblocking Column 12 down to Row 16.
  - Shutter gates on Columns 14, 15, 17 on Row 7/8 are **OPEN**.
  - Shutter gate at `(25, 13)` is **CLOSED**.
  - Shutter gates at `(19, 2)`, `(21, 2)` are **CLOSED**.
  - Balcony shutter gate at `(21, 17)`: Empirically verified CLOSED in State A on Turn 73256.
- **State A:**
  - Shutter gate at `(12, 13)` is **CLOSED**, blocking Column 12 at Row 13.
  - Shutter gates on Columns 14, 15, 17 on Row 7/8 are **CLOSED**.
  - Shutter gate at `(25, 13)` is **OPEN**.
  - Shutter gates at `(19, 2)`, `(21, 2)` are **OPEN**.
  
## Mewtwo Statue Switches on 3F
- **3F West Switch:** Located at `(2, 5)`. Interacted from `(2, 6)` facing UP.

## Verified Route to B1F West (Secret Key)
Row 8 is partially blocked, but 3F East and West are horizontally connected via Row 11 and Row 6.

### Verified Balcony Route (To B1F West)
1. At 3F West switch at `(2, 5)`, stand at `(2, 6)` facing UP, and press A to confirm text 'A secret switch! ... Pressed it!' to toggle to **State A**.
2. Walk to 3F East via Row 6 to `(8, 6)`, Up Column 8 to `(8, 2)`, Right to `(10, 2)`, Up to Row 1 `(10, 1)`, Right along Row 1 to `(26, 1)`.
3. Walk Down Column 26 to `(26, 12)`, Left to `(25, 12)`.
4. In State A, the shutter gate at `(25, 13)` is OPEN! Walk Down Column 25 past Row 13 to Row 16 `(25, 16)`.
7. Step Down over the railing to drop into B1F at `(9, 16)`!

### Column 26 Walkability Status
- Column 26 is completely walkable pink checkered floor from Row 1 down to Row 12 in both states (verified on Turns 73161, 73192, and 73199). There is no active drop trap on (26, 3).