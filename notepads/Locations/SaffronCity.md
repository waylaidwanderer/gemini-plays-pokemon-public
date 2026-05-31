# Saffron City Location Records (Map 0_10)

## Overview
- **Entrance**: Unlocked the city via the Route 7 Gatehouse (Turn 30198).
- Entered Saffron City from Route 7 (Map 0_18) via the West Gatehouse on Turn 30221. Spawns at (0, 18) and connects to Saffron's streets at (5, 18).

## Points of Interest
- **Pokémon Center**: Doorway at (9, 29). Entered from (9, 30) (Turn 30421).
- **Saffron Gym**: Doorway at (34, 3), blocked by Rocket Grunt at (34, 4) (Discovered Turn 30623).
- **Fighting Dojo**: Doorway at (26, 3). Challenged Dojo Master Kiyo and defeated all Blackbelts. Claimed the prize HITMONLEE (KICKY) at (4, 1) (sent to Box 1) on Turn 30781. The Dojo is now successfully cleared!
- **Silph Co. Head Office**: Doorway at (18, 21) blocked by Rocket Grunt at (18, 22) (Turn 30296/30299).
- **Blocked Doorway 2**: Doorway at (13, 11) blocked by Rocket Grunt (Turn 30261).
- **Blocked Northwest House (Copycat's House?)**: Entrance door at (7, 5) blocked by Rocket Grunt at (7, 6) ("What do you want? Get lost!") (Turn 30245).

## Landmarks & Coordinates
- Route 7 Gatehouse Entrance/Exit: at Map 0_10 (0, 18)? Yes, we came from (0, 18).

## Regional Gatehouse Passability Testing Protocol
To systematically verify the region-wide gate unlock rule:
1. **Verification Hypothesis**: Giving Fresh Water to the West Gatehouse guard (Turn 30198) permanently unlocked all Saffron City gatehouses (Route 5 North, Route 6 South, Route 8 East) without requiring additional drinks.
2. **Systematic Tests**:
   - **Route 8 Gatehouse (East)**: When nearby, enter the Route 8 Gatehouse, walk past the guard to Saffron City, and verify if we pass freely without being stopped or prompted for a drink. Record turn number, coordinates, and guard interaction.
   - **Route 5 Gatehouse (North)**: When nearby, enter the Route 5 Gatehouse, walk past the guard to Saffron City, and verify if we pass freely. Record turn number, coordinates, and guard interaction.
   - **Route 6 Gatehouse (South)**: When nearby, enter the Route 6 Gatehouse, walk past the guard to Saffron City, and verify if we pass freely. Record turn number, coordinates, and guard interaction.
3. **Database Logging**: Update this section with the empirical results of each gatehouse test to establish definitive 'proof of work'.

## Saffron City Quadrant Summary
- **SW Quadrant**: Pokémon Center at (9, 29) (Open/Visited).
- **SE Quadrant**: Mr. Psychic's House at (29, 29) (Open/Visited, obtained TM29).
- **NE Quadrant**: Saffron Poké Mart at (25, 11) (Open/Visited).
- **NW Quadrant**: Copycat's House at (7, 5) (Blocked by Rocket Grunt).

## Saffron Gatehouse Passability Test Results:
- **Route 5 Gatehouse (North) Test (Turn 30593)**:
  - **Methodology**: Walked north from Saffron City (Map 0_10) at (18, 2) on Turn 30592.
  - **Results**: Seamlessly warped through Saffron North Gatehouse (Route 5 Gatehouse) past the guard without any text box, prompts, or drink requests, emerging on Route 5 (Map 0_16) at (8, 35) on Turn 30593.
  - **Conclusion**: Confirmed! Route 5 Gatehouse is permanently open and free to traverse bidirectional without further drink requirements. This empirically proves the region-wide unlock is fully operational!
- **Route 7 Gatehouse (West) Test (Turn 30878)**:
  - **Methodology**: Walked West from Saffron City (Map 0_10) at (0, 18) to spawn on Route 7 (Map 0_18) at (19, 10). From there, entered Saffron West Gatehouse (Map 0_76) via its East door at (17, 10) on Turn 30875. Walked West from (5, 4) to (0, 4).
  - **Results**: Traversing Map 0_76 westward from (5, 4) to (0, 4) was completely unobstructed. The guard at (3, 1) made no attempts to stop us or prompt for a drink. We successfully reached the West warp at (0, 4) on Turn 30878.
  - **Conclusion**: Confirmed! Saffron West Gatehouse is 100% open and passable without any drink prompts.

- **Route 6 Gatehouse (South) Test (PLANNED)**:
  - **Hypothesis**: Giving Fresh Water to the West Gatehouse guard permanently unlocked the South Gatehouse region-wide.
  - **Methodology**: Access Route 6 South gatehouse from Vermilion City or Route 6, walk north past the guard, and verify if we pass freely to Saffron City without being stopped or prompted for a drink.
  - **Status**: Untested.

- **Route 8 Gatehouse (East) Test (Turn 37218 - 37299)**:
  - **Methodology**: Walked East from Saffron City (Map 0_10) at (39, 18) and (39, 19). Warped directly from Saffron City into a 2x3 alcove on Route 8 (Map 0_19) at (0, 10).
  - **Results**: The alcove is physically blocked on the East side by Saffron East Gatehouse building (columns 2-5, rows 8-11). Walked LEFT from Route 8 (0, 8), (0, 9), or (0, 10) to warp back to Saffron City at (39, 16), (39, 17), or (39, 18).
  - **Systematic Row-by-Row Scan of Column 39**:
    - Conducted a complete, empirical boundary scan on column 39 in Saffron City for rows 20 to 30:
      - Row 20: Blocked by wooden post (TYPE_2889)
      - Row 21: Blocked by wooden post (TYPE_2889)
      - Row 22: Blocked by wooden post (TYPE_2889)
      - Row 23: Blocked by grey statue wall (TYPE_2889, verified Turn 37282)
      - Row 24: Blocked by grey statue wall (TYPE_2889, verified Turn 37285)
      - Row 25: Blocked by grey statue wall (TYPE_2889, verified Turn 37291)
      - Row 26: Blocked by grey statue wall (TYPE_2889, verified Turn 37293)
      - Row 27: Blocked by grey statue wall (TYPE_2889, verified Turn 37295)
      - Row 28: Blocked by grey statue wall (TYPE_2889, verified Turn 37296)
      - Row 29: Blocked by grey statue wall (TYPE_2889, verified Turn 37297)
      - Row 30: Blocked by grey statue wall (TYPE_2889, verified Turn 37298)
  - **Conclusion**: Confirmed! The entire eastern boundary of Saffron City from row 20 to 30 is completely blocked by solid fences/walls, and any direct map connections on rows 16 to 18 only place us in a trapped 2x3 alcove. There is NO direct open bypass on these rows. Saffron East Gatehouse interior Map 0_79 is bypassed, and the alcove on Route 8 is a physical dead end. We must seek an alternative route or find a functional door.

## Inventory Management Plan (Turn 37104) - COMPLETED
- Spaced cleared on Turn 37199.
- Successfully deposited: TM19, MOON STONE, TM07, TM10, TM02, and LIFT KEY.
- Current inventory count: 11/20 items. This leaves 9 open slots, allowing us to safely obtain the Silph Scope rewards and navigate Lavender Town's Pokémon Tower.
## Turn 50 Reflection & Saffron-Route 8 Direct Map Alignment Discovery (Turns 37218-37252)
- **Problem**: Walking east from Saffron City (39, 18) warps the player directly to Route 8 (0, 10). However, the player is trapped in a 2x3 alcove (columns 0-1, rows 8-10) by the Saffron East Gatehouse building (columns 2-5, rows 8-11) and fences (row 7 and row 11).
- **Hypothesis**: The entire eastern edge of Saffron City is connected directly to Route 8 via a direct 1-to-1 map connection offset by 8 rows: `Route 8 Row = Saffron City Row - 8`.
- **Systematic Test Results**:
  - Walked Left from Route 8 (0, 10) -> Saffron City (39, 18) (Turn 37232).
  - Walked Left from Route 8 (0, 8) -> Saffron City (39, 16) (Turn 37238).
  - Walked Left from Route 8 (0, 9) -> Saffron City (39, 17) (Turn 37246).
- **Passability Analysis**:
  - The gatehouse building on Route 8 spans rows 8 to 11.
  - To bypass the building, we need to enter Route 8 above the building (rows 0-7) or below the building (rows 12-15).
  - According to the -8 row offset, Route 8 rows 12-15 correspond to Saffron City rows 20-23.
  - Saffron City row 20 has (39, 20) which is a solid fence. We need to check if Saffron City rows 21, 22, or 23 on column 39 are open.
  - If we walk down to Saffron City row 21-23 and find an open tile on column 39, walking Right will place us on Route 8 row 13-15, completely bypassing the gatehouse building!
- **Notepad/Map Marker Hygiene**:
  - Placed map marker at (39, 18) for Saffron East Gatehouse Exit.
  - Updated current objectives.