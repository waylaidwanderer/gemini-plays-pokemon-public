# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026

### Current Status
- **Location**: Glitter Lighthouse 6F (Map 3_47).
- **Goal**: Exit Lighthouse and Fly to Cianwood to get SecretPotion.

### Lighthouse Navigation Fact Sheet
- **Route to Top**:
  1. **1F -> 2F**: Stairs at (3,11).
  2. **2F -> 3F**: Stairs at (5,3).
  3. **3F -> 4F**: Stairs at (13,3) (Right Side).
  4. **4F -> 3F (Center)**: Drop down hole at (9,3) or (10,3)? Wait, I took stairs UP from 3F Center. How did I get TO 3F Center?
     - **Correction**: On 4F (Map 3_45), go to Row 2, then to (9,2) and down to (9,7)? No, I dropped from 4F to 3F Center?
     - Let's re-read the log. "Solves navigation puzzle by jumping down a hole at (9, 3) on Lighthouse 4F".
     - YES. **The Drop**: On 4F, go to (9,3) area and fall to reach 3F Center.
  5. **3F (Center) -> 4F (Center)**: Stairs at (9,5).
  6. **4F (Center) -> 5F (Center)**: Stairs at (9,7).
  7. **5F (Center) -> 6F**: Stairs at (9,15).

### Immediate Plan
1. **Exit Lighthouse**: Retrace steps down or find holes to fall through.
   - 6F -> 5F -> 4F -> 3F -> 2F -> 1F.
2. **Fly to Cianwood**: Use HM02.
3. **Get SecretPotion**: Pharmacy at (2,7) in Cianwood.
4. **Return**: Fly back to Olivine, climb Lighthouse again.

### Objectives
- **Primary**: Obtain SecretPotion.
- **Secondary**: Heal Amphy.
### Investigation: The Central Column Trap
- **Problem**: I am currently on 6F. To leave, I must go down. The stairs at (9,15) lead to 5F Center. 5F Center leads to 4F Center. 4F Center leads to 3F Center.
- **Concern**: I previously identified 3F Center, 4F Center, and 5F Center as "dead ends" or "traps" with no connection to the main floors.
- **Hypothesis 1**: There is an exit in 3F Center I missed (maybe a walk-through wall or hidden door).
- **Hypothesis 2**: There is a hole or exit on 6F I missed.
- **Hypothesis 3**: There is a ledge or bridge on 4F or 5F Center I missed.
- **Plan**:
    1. Check 6F for exits using `find_reachable_exits`.
    2. If none, descend to 5F, 4F, 3F and scan specifically for connections to the outer areas.
- **Escape Plan**: Found potential holes at (16,5) and (17,5) on 6F. Attempting to fall down them to bypass the "Trap Column" and reach the lower floors' outer areas.
- **Progress**: Fell from 6F (16,5) to 5F (16,5).
- **Next Step**: Falling from 5F (16,7) to 4F. Expecting to land in the Right Section of 4F.
- **Progress**: Fell from 5F (16,7) to 4F (16,7).
- **Next Step**: Falling from 4F (16,9) to 3F. This should land me in the Right Section of 3F.