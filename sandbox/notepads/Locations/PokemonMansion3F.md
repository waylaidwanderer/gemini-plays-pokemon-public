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
  - Balcony shutter gate at `(21, 16)` is **CLOSED**.
- **State A:**
  - Shutter gate at `(12, 13)` is **CLOSED**, blocking Column 12 at Row 13.
  - Shutter gates on Columns 14, 15, 17 on Row 7/8 are **CLOSED**.
  - Shutter gate at `(25, 13)` is **OPEN**.
  - Shutter gates at `(19, 2)`, `(21, 2)` are **OPEN**.
  - Balcony shutter gate at `(21, 16)` is **OPEN**.

## Mewtwo Statue Switches on 3F
- **3F West Switch:** Located at `(2, 5)`. Interacted from `(2, 6)` facing UP.
- **3F East Switch:** Located at `(12, 10)`. Interacted from `(12, 11)` facing UP.

## The Two Paths to B1F West (Secret Key)
Row 8 is partially blocked, but 3F East and West are horizontally connected via Row 11 and Row 6.

### Path 1: The Pitfall Route (Mansion B1F Unlocked in State B)
1. Set Mansion to **State B** on 3F West.
2. Walk to 3F East via Row 6, go down Column 14/15/17 (open in State B) to Row 12, walk LEFT to Column 12, and go down Column 12 (open in State B) to Row 16.
3. Stand at `(21, 15)` in State B (facing the closed balcony gate at 21, 16).
4. Walk to the 3F East switch at `(12, 11)` (via Column 12, open in State B), stand at `(12, 12)` facing UP, and toggle to **State A**.
5. This closes the gate at `(12, 13)` behind you, but opens the balcony gate at `(21, 16)`!

### Pitfall Trap Status
- In **State A**, the pitfall trap at `(26, 3)` is covered/walkable pink checkered floor (allows safe traversal down Column 26).
- In **State B**, the pitfall trap at `(26, 3)` is active (stepping on it drops the player down to 1F East).