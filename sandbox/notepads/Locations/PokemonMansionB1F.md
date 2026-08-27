# Pok�mon Mansion B1F - Map & Navigation Log

## True Landing Coordinates
- **Balcony Drop Landing:** Landing coordinate is `(19, 16)` in B1F East.
  - Verification: Dropping over the 3F balcony at `(19, 18)` or `(20, 18)` lands us in B1F East. (Note: previous notes containing `(9, 16)` were a typo).

## Key Targets
- **SECRET KEY:** Located in the northwest room of B1F at `(1, 4)`.
  - Status: Open and accessible only in State B!
  - Retrieval Method: Stand at `(1, 5)` facing UP and press `A` to retrieve it.
  

## Switch & Shutter Gate Configuration

### B1F West vs B1F East Separation
- B1F is divided into B1F West and B1F East by a solid vertical wall on Column 9 (except at Row 11 in State A, and Row 5/6 in State B).
- B1F South is divided from B1F North on the West side by a solid permanent brick wall on Row 9 (Columns 1-8 are blocked).

### DEFAULT STATE (State A)
- **Row 11 Gate at `(10, 11)`:** **OPEN** (Allows horizontal crossing from B1F West to B1F East!).
- **Column 10 Vertical Path:** **OPEN** (Allows vertical traversal between Row 11 and Row 5 on the East side).
- **Row 5 Shutter Gate at `(9, 5)`:** **CLOSED** (Blocks horizontal crossing on the North side).
- **Secret Key Room:** **CLOSED**.

### TOGGLED STATE (State B)
- **Row 11 Gate at `(10, 11)`:** **CLOSED** (B1F East is cut off from B1F West on the South side).
- **Column 10 Vertical Path:** **CLOSED** (Blocked at Row 8).
- **Row 5 Shutter Gate at `(9, 5)`:** **OPEN** (Allows horizontal crossing on the North side from B1F East to B1F West!).
- **Secret Key Room at `(1, 4)`:** **OPEN**.

---

## Switch Details (Mansion Switch State B is toggled from 3F West)
- B1F West SOUTH statues at `(3, 10)`, `(3, 12)`, `(3, 14)`, `(8, 10)`, `(8, 12)`, and `(8, 14)` are empirically proven on Turn 61288 to be purely decorative. B1F has NO Mewtwo switches at all!
- However, we do not need to toggle any switch on B1F to retrieve the Secret Key! The entire mansion is solved by toggling the Mewtwo statue switch at `(2, 11)` on 3F West to State B, dropping down the 3F East pitfall at `(26, 6)` to 1F East `(25, 6)`, warping down to B1F East `(22, 2)`, and walking straight across Row 5 through the open Column 9 gate directly to the Secret Key room on B1F West.

## Verified Empirical Discoveries & Proof of Work
- **Permanent Column 1 Wall (Turn 57865):** Column 1 Row 9 has been physically verified as a solid, impassable permanent structural wall. The player cannot walk Up Column 1 past Row 9 in any state (A or B).
- **Row 5 Column 20-21 Solid Barrier (Turn 57908):** Row 5 on Columns 20 and 21 contains a solid permanent horizontal wall block. Direct horizontal crossing from East to West on Row 5 is blocked at Columns 20 and 21. Crossing must be done by walking Left on Row 4 to Column 19, then walking Down to Row 5, and then walking Left directly through the open Column 9 gate at `(9, 5)`.
- **B1F East Mewtwo Statues (Turn 57381):** Statues at `(16, 10)` and `(18, 10)` have been physically interacted with and verified to have no switches. They are purely decorative.
- **Column 9 Row 5 Gate (Turn 57908):** Gate at `(9, 5)` is OPEN in State B and CLOSED in State A. Allows horizontal crossing between B1F East and B1F West North.

## Switch Coordinates & Verified B1F Info (Turn 61084)
- The entire mansion is solved by toggling the Mewtwo switch at `(2, 10)` or `(1, 12)` on 3F West to State B!
- Once in State B, the B1F East NORTH gate at `(9, 5)` is OPEN, allowing us to walk directly across Row 5 from B1F East `(22, 2)` to the Secret Key room at `(1, 4)`.

## 🧪 B1F West SOUTH Empirical Verification (Turn 61288)
- Systematic testing of the Mewtwo statues on B1F West SOUTH has proven that they are **purely decorative and do NOT contain switches**:
  - Statue at `(8, 10)`: Tested and verified decorative (Turn 61259).
  - Statue at `(3, 10)`: Tested and verified decorative (Turn 61262).
  - Statue at `(3, 12)`: Tested and verified decorative (Turn 61279, false positive on Turn 61264 cleared as wild battle desync).
  - Statues at `(3, 14)`, `(8, 12)`, `(8, 14)`: Tested and verified decorative (Turn 61280, false positive on `(3, 14)` cleared as battle desync).
- **Conclusion:** B1F has NO Mewtwo switches at all! The entire mansion puzzle must be toggled from 3F West.
