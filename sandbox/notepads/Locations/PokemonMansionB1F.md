# Pokémon Mansion B1F - Map & Navigation Log

## True Landing Coordinates
- **Balcony Drop Landing:** Landing coordinate is `(19, 16)` in B1F East.
  - Verification: Dropping over the 3F balcony at `(19, 18)` or `(20, 18)` lands us in B1F East. (Note: previous notes containing `(9, 16)` were a typo).

## Key Targets
- **SECRET KEY:** Located in the northwest room of B1F at `(1, 4)`.
  - Status: Open and accessible only in State B!
  - Retrieval Method: Stand at `(1, 5)` facing UP and press `A` to retrieve it.
  - Bag status: Verified on Turn 51636 that we do NOT have the Secret Key, and our Bag has plenty of empty space.

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

## The Ultimate Verified Master Route to B1F East & Secret Key
1. Set the global switch to **State A** (Default). (Completed on Turn 51603/51624).
2. Exit B1F to 1F via the stairs at `(5, 10)` on B1F. (Currently at `(7, 11)` on 1F in State A).
3. On 1F (State A), go to 2F.
4. On 2F (State A), go to 3F.
5. On 3F (State A), cross to the East side:
   - Walk from `(7, 11)` to `(12, 11)` -> Up Column 12 to `(12, 6)` -> Right along Row 6 to `(19, 6)` -> Down Column 19 to `(19, 11)` -> Left along Row 11 to the East Stairs `(15, 11)`.
6. Warp DOWN to 2F East landing at `(16, 11)` on 2F (State A).
7. On 2F East (State A), walk Left to `(12, 11)`. Face Right (towards the Mewtwo statue switch at `(13, 11)`) and press `A` to toggle the switch to **State B**!
8. Now the mansion is in State B!
9. Walk to the East Stairs `(15, 11)` on 2F East and warp UP to 3F East (State B) landing at `(16, 11)`.
10. Walk to the balcony landing `(20, 15)`:
    - Path: `(16, 11) -> (21, 11) -> (21, 15) -> (20, 15)`.
11. Walk Down to `(20, 18)` and step Left to `(19, 18)` to drop to B1F East!
12. Now we land on B1F East at `(19, 16)` in State B!
13. Walk to Column 10 Row 5:
    - Path: `(19, 16) -> (10, 16) -> (10, 5)`.
14. Walk Left along Row 5 to Column 1 through the now-open gate at `(9, 5)`:
    - Path: `(10, 5) -> (1, 5)`.
15. Face UP at `(1, 5)` and press `A` to retrieve the Secret Key!