# Pokémon Mansion - Multi-Floor Switch & Gate State Truth Matrix

## Global Switch States
A single global flag in RAM controls all Mewtwo statue shutter gates across all floors:
- **State A (Default / Non-toggled):**
  - **1F East:** Shutter gate at `(25, 13)` is **OPEN**.
  - **2F East:** Shutter gate at `(18, 8)` / `(19, 8)` is **CLOSED**.
  - **3F West / Center:** Shutter gates at `(16, 7)` and `(17, 7)` are **CLOSED**.
  - **3F East:** Shutter gate at `(24, 13)` and `(25, 13)` is **OPEN**.
  - **3F Balcony:** Shutter gate at `(20, 17)` / `(21, 17)` is **CLOSED** (in State A).
  - **B1F:** Shutter gate at `(9, 5)` is **CLOSED**.

- **State B (Toggled):**
  - **1F East:** Shutter gate at `(25, 13)` is **CLOSED**.
  - **2F East:** Shutter gate at `(18, 8)` / `(19, 8)` is **OPEN**.
  - **3F West / Center:** Shutter gates at `(16, 7)` and `(17, 7)` are **OPEN**.
  - **3F East:** Shutter gate at `(24, 13)` and `(25, 13)` is **CLOSED**.
  - **B1F:** Shutter gate at `(9, 5)` is **OPEN** (connecting B1F East to B1F West).

## 2F East Layout Conclusions (Verified Turn 73402, 73547, 73559, 73566)
- **Northeast Pocket (Columns 24-28, Rows 1-7):** Dead end! Enclosed to the south by solid wall panels on Row 8 `(24-28, 8)` and rubble on Rows 6-7. No southern exit to Rows 9-16.
- **Southwest Corridor (Columns 18-21, Rows 8-15):** Dead end! Blocked on the east by continuous solid rubble on Column 22 `(22, 11-15)`. Blocked to the south by solid balcony railing on Row 16 `(21, 16)`.
- **Southeast Chamber (Columns 23-28, Rows 9-16 with stairs at (25, 14)):** INACCESSIBLE via walking on 2F in either State A or State B. Must be entered via falling from 3F or accessed from 1F.
