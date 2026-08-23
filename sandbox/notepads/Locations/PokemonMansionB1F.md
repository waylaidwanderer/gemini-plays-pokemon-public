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
- B1F East has Mewtwo statues at `(16, 10)` and `(18, 10)`. B1F West has Mewtwo statues at `(3, 10)`, `(3, 12)`, `(3, 14)`, `(8, 10)`, `(8, 12)`, and `(8, 14)`.
- However, we do not need to toggle any switch on B1F to retrieve the Secret Key! The entire mansion is solved by toggling the Mewtwo statue switch at `(2, 11)` on 3F West to State B, dropping down the 3F East pitfall at `(26, 6)` to 1F East `(25, 6)`, warping down to B1F East `(22, 3)`, and walking straight across Row 5 through the open Column 9 gate directly to the Secret Key room on B1F West.