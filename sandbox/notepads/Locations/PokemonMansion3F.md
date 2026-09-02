# PokÃ©mon Mansion 3F - Map & Navigation Log

## Permanent Physical Barriers (Same in State A and State B)
- **Column 15 Row 3 is a Solid Wall:** Column 15 Row 3 is blocked by a permanent solid vertical wall panel. Horizontal travel across Column 15 on Row 3 is impossible.
- **Row 6 Column 15 is Open:** Completely open and walkable pink checkered floor, allowing horizontal crossing (verified open in State A on Turn 72327).
- **Row 6 Column 22 is a Solid Wall:** Solid vertical partition wall panel (impassable).
- **Row 8 Barrier (Columns 11-28):** Completely blocked horizontally across the entire floor. Columns 13-17 and 20-22 are solid wall panel; Column 11 on Row 8 is completely open and walkable vertically; Columns 18-19 are solid bookcase/drawers; Columns 23 is solid rubble; Columns 24-28 are solid horizontal partition wall. No vertical travel is possible across Row 8 on 3F East!
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
Because Row 8 on 3F East is completely blocked horizontally, and Column 11 Row 16 is blocked, 3F is physically split.

### Path 1: The Pitfall Route (Mansion B1F Unlocked in State B)
1. Set Mansion to **State B** on 3F West.
2. Walk to 3F East via Row 6, go down Column 14/15/17 (open in State B) to Row 12, walk LEFT to Column 12, and go down Column 12 (open in State B) to Row 16.
3. Stand at `(21, 15)` in State B (facing the closed balcony gate at 21, 16).
4. Walk to the 3F East switch at `(12, 11)` (via Column 12, open in State B), stand at `(12, 12)` facing UP, and toggle to **State A**.
5. This closes the gate at `(12, 13)` behind you, but opens the balcony gate at `(21, 16)`!

### State A Limitations
- In **State A**, the pitfall trap at `(26, 3)` on 3F East is closed/covered and cannot be fallen through (empirically disproven on Turn 72338 and Turn 72345). Thus, Path 2 is not viable in State A.