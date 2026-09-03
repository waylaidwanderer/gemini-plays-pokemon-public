# Pokémon Mansion - Multi-Floor Switch & Gate State Matrix

## Verified Empirical Observations
- **State A:**
  - **2F East:** Shutter gate at `(18, 8)` / `(19, 8)` is **CLOSED** (verified Turn 73390).
  - **3F West / Center:** Shutter gates at `(16, 7)` and `(17, 7)` are **CLOSED** (verified Turn 73449).
  - **3F East:** Shutter gate at `(24, 13)` and `(25, 13)` is **OPEN** (verified Turn 73242).
  - **3F Balcony:** Shutter gate at `(20, 17)` / `(21, 17)` is **CLOSED** (verified Turn 73256).

- **State B:**
  - **2F East:** Shutter gate at `(18, 8)` / `(19, 8)` is **OPEN** (verified Turn 73513).
  - **2F West:** Shutter gates at `(9, 4)` and `(9, 5)` are **CLOSED** (verified Turn 73581).
  - **3F West / Center:** Shutter gates at `(16, 7)` and `(17, 7)` are **OPEN** (verified Turn 73468).
  - **3F East:** Shutter gate at `(24, 13)` and `(25, 13)` is **CLOSED** (verified Turn 73484).
  - **3F East Column 26:** Pink checkered floor, NO pitfall trap in State B (verified Turn 73478-73484).

## Hypotheses Requiring In-Person Verification
- **1F East Gate (25, 13):** Hypothesized open in State A and closed in State B, but requires direct visual confirmation in current game session.
- **B1F Connecting Gate (9, 5):** Hypothesized open in State B and closed in State A, but requires direct visual verification upon entering B1F.

## 2F East Layout Conclusions (Verified Ground Truth)
- **Northeast Pocket (Columns 24-28, Rows 1-7):** Dead end! Enclosed to the south by solid wall panels on Row 8 `(24-28, 8)` and rubble on Rows 6-7. No southern exit to Rows 9-16.
- **Southwest Corridor (Columns 18-21, Rows 8-15):** Dead end! Blocked on the east by continuous solid rubble on Column 22 `(22, 11-15)`. Blocked to the south by solid balcony railing on Row 16 `(21, 16)`.
- **Southeastern Chamber (Columns 23-28, Rows 9-16 with stairs at (25, 14)):** Inaccessible via walking on 2F in either State A or State B.
