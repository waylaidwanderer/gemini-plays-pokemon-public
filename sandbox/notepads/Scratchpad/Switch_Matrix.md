# Pok�mon Mansion - Multi-Floor Switch & Gate State Matrix

## Verified Empirical Observations
- **State A:**
  - **2F East:** Shutter gate at `(18, 8)` / `(19, 8)` is **CLOSED** (verified Turn 73390).
  - **3F West / Center:** Shutter gates at `(16, 7)` and `(17, 7)` are **CLOSED** (verified Turn 73449).
  - **3F Center Gate:** Shutter gate at `(15, 4)` / `(15, 5)` is **OPEN** (verified Turn 73952).
  - **3F Lower Center Gate:** Shutter gate at `(15, 10)` / `(15, 11)` is **CLOSED** (verified Turn 73952).
  - **3F East:** Shutter gate at `(24, 13)` and `(25, 13)` is **OPEN** (verified Turn 73242).
  - **3F Balcony:** Shutter gate at `(20, 17)` / `(21, 17)` is **CLOSED** (verified Turn 73256).

- **State B:**
  - **2F East:** Shutter gate at `(18, 8)` / `(19, 8)` is **OPEN** (verified Turn 73513).
  - **2F West:** Shutter gates at `(9, 4)` and `(9, 5)` are **CLOSED** (verified Turn 73581).
  - **3F West / Center:** Shutter gates at `(16, 7)` and `(17, 7)` are **OPEN** (verified Turn 73468).
  - **3F Center Gate:** Shutter gate at `(15, 4)` / `(15, 5)` is **CLOSED** (verified Turn 73958).
  - **3F Lower Center Gate:** Shutter gate at `(15, 10)` / `(15, 11)` is **OPEN** (verified Turn 73958).
  - **3F East:** Shutter gate at `(24, 13)` and `(25, 13)` is **CLOSED** (verified Turn 73484).
  - **3F East Column 26:** Pink checkered floor, NO pitfall trap in State B (verified Turn 73478-73484).

- **Mewtwo Switches:**
  - **3F East Switch at `(18, 25)`:** Confirmed active secret switch on 3F East (verified Turn 74508). Toggled from (18, 26) facing UP.
  - **3F Switch at `(10, 5)`:** Confirmed active secret switch on 3F (verified Turn 73953-73958). Toggled from (10, 6) facing UP.
  - **2F Switch at `(2, 11)`:** Confirmed active secret switch on 2F West (verified Turn 73065).

## Hypotheses Requiring In-Person Verification
- **1F East Gate (25, 13):** Open in State A (verified Turn 68294), closed in State B.
- **B1F Connecting Gate (9, 5):** Hypothesized open in State B and closed in State A, but requires direct visual verification upon entering B1F.

- **Turn 74337 Switch Toggle:** Toggled 3F Mewtwo switch at `(10, 5)` from State A to State B (confirmed by 'Who wouldn't?' prompt and gate closing at (15, 4-5)). Current Mansion State: **State B**.
  - **3F Balcony Gate:** Shutter gate at `(20, 17)` / `(21, 17)` is **OPEN** (verified Turn 74482).