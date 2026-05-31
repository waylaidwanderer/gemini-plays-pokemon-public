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

## Systematic Exploration Protocol & Log (Starts Turn 30465)
We divide Saffron City (Map 0_10) into 4 quadrants to systematically check all buildings:
1. **Southwest (SW) Quadrant (Y: 15-29, X: 0-14)**:
   - Pokémon Center: Door at (9, 29). Checked (Open/Visited, Turn 30421).
2. **Southeast (SE) Quadrant (Y: 15-29, X: 15-29)**:
   - **Mr. Psychic's House**: Door at (29, 29). Entered on Turn 30485 (Open/Visited). Received TM29 (Psychic) from Mr. Psychic on Turn 30488.
3. **Northeast (NE) Quadrant (Y: 0-14, X: 15-29)**:
   - **Saffron Poké Mart**: Located in the Northeast Quadrant with its entrance door at (25, 11) (and its sign "MART" at (26, 11)). This building is completely open and not blocked by barrels. (Verified Turn 30806).
     - **Inventory**: Great Ball (¥600), Hyper Potion (¥1500), Max Repel (¥700), Escape Rope (¥550), Full Heal (¥600), Revive (¥1500). (Fully verified on Turn 30830).
4. **Northwest (NW) Quadrant (Y: 0-14, X: 0-14)**:
   - Copycat's House: Door at (7, 5). Checked (Blocked by Grunt at (7, 6), Turn 30245).

### Exploration Log:
- Turn 30465: Restored bag space to 11/20. Initiating systematic SE quadrant search from (9, 30). Goal: Check if Mr. Psychic's house and Poké Mart are open or blocked.
- Turn 30519: Explored Saffron's eastern edge street along column 36. Discovered that the street is open and runs north-south from row 31 up to at least row 22. The SE quadrant has a yellow building at (32, 27)-(35, 29) with no visible southern doors. Currently at (36, 26), heading north towards row 21 to find Saffron Poké Mart.
- Turn 30578: Confirmed Silph Co.'s western wall is at column 16, ending the row 14-15 street at column 15. The alleyway at columns 14-15 runs from row 14 to row 21 (with the Poké Mart sign at (15, 21)), but has no active doors. Returned to (5, 14), preparing to head north along columns 2-3 to explore Saffron's northern streets (Gyms and Magnet Train).

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

- **Route 8 Gatehouse (East) Test (Turn 37218)**:
  - **Methodology**: Walked East from Saffron City (Map 0_10) at (39, 18) to warp into Route 8 (Map 0_19) on Turn 37218.
  - **Results**: Seamlessly warped from Saffron City directly into Route 8 at (0, 10) without any gatehouse interior map or guard stopping us or requiring a drink.
  - **Conclusion**: Confirmed! Route 8 East Gatehouse is permanently open and free to traverse bidirectionally. This is another proof of the region-wide gatehouse unlock.

## Inventory Management Plan (Turn 37104) - COMPLETED
- Spaced cleared on Turn 37199.
- Successfully deposited: TM19, MOON STONE, TM07, TM10, TM02, and LIFT KEY.
- Current inventory count: 11/20 items. This leaves 9 open slots, allowing us to safely obtain the Silph Scope rewards and navigate Lavender Town's Pokémon Tower.