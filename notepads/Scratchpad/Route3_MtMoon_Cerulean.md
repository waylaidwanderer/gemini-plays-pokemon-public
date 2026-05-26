# Route 3, Mt. Moon, and Cerulean City Progression Scratchpad
- Started: Turn 4122, Timestamp: Sunday, May 24, 2026 at 6:18 AM PDT

## Current Status:
- Turn 11521: Standing at (3, 7) in Cerulean Pokémon Center (Map 0_64).
- Mt. Moon Progression Start: Turn 5170.

## Progression Roadmap & Checklist:
- [x] Defeat Pewter Gym Leader Brock (Boulder Badge & TM34 secured!).
- [x] Healed team at Pewter City Pokémon Center at (13, 25).
- [x] Stock up on useful items at Pewter Poké Mart at (23, 17) (Secured 4 Potions, 3 Poké Balls, 3 Antidotes, 1 Paralyze Heal; ¥601 remaining).
- [x] Navigate east through Route 3 to Mt. Moon entrance.
- [x] Defeat Super Nerd Miguel and secure the Helix Fossil (Turn 11013).
- [x] Exit Mt. Moon to Route 4 West (Turn 11116).
- [x] Navigate Route 4 East to Cerulean City (Turn 11225).
- [x] Locate Cerulean Pokémon Center (Turn 11248).
- [x] Locate and explore Cerulean Bike Shop (Turn 11368).
- [ ] Explore Cerulean City, locate the Poké Mart and Gym.
- [ ] Challenge Gym Leader Misty.

## Socratic Reflections on Dungeon Exploration & Spatial Assumptions (Turn 10836):
- **The Core Mistake**: Previously, we concluded that the western platform on B2F was completely isolated from the southern area based on partial checks near Row 21, and we spent hundreds of turns backtracking up through B1F and 1F to find another way.
- **The Lesson Discovered**: A continuous horizontal corridor actually existed at the extreme south of B2F (Rows 31 & 32), bypassing all barriers and connecting the far-west platform directly to the eastern stairs.
- **Application to Future Layouts**:
  1. **Systematic Edge Probing**: Never declare an area "isolated" or "dead-ended" without exploring the absolute boundaries (e.g., Rows 31 & 32) of the grid, even if they seem out of the way or directionally unintuitive.
  2. **Avoid Generalizing Collisions**: Just because Column 14 Row 21 was blocked doesn't mean the entire vertical/horizontal traverse is blocked across all columns/rows. We must test every single candidate boundary tile individually before making a conclusion.
  3. **Visual Truncation Alert**: When some areas are off-screen, they must be treated as active exploration targets. We must use our custom pathfinding, systematic walking, and map markers to map the invisible spaces.
- **Refined Reflection (Turn 10926)**:
  - *Tendency Analyzed*: Our tendency to declare dead ends was driven by visual heuristics—assuming a solid block like Column 25 Row 12 or Column 14 Row 21 was part of a larger continuous wall. This led us to initiate massive, unnecessary backtracks across multiple floors.
  - *Cerulean City & Route 4 Strategy*:
    1. **Exhaustive Perimeter Walk**: We will physically walk the boundaries of all newly entered areas (including Route 4 and Cerulean City) to map exits and pathways before drawing conclusions.
    2. **Differential Passability Tests**: When blocked on one tile, we will explicitly test parallel tiles in the column/row.
    3. **Pathfinder Verification**: We will use our restored built-in `find_path_astar` and new `multi_floor_router` agent to verify routing options systematically.

## Route 4 East & Cerulean City Systematic Exploration Strategy (Turn 11425):
- **Perimeter-Walk Verification**:
  We will systematically walk the borders of Cerulean City, test every candidate boundary tile, and document passability.
  - Test boundary gates and ledges systematically to find the entrances/exits.
  - Verify if Column 35 is indeed solid all the way up. We will walk north on Column 34 to check for any bypasses above Row 21.
- **Detailed Trainer Logging**:
  Any trainer encountered in Cerulean City or Routes 24/25 will be logged with:
  - Exact coordinates, class, name, team details, and victory status.
  - Mark defeated trainers with map marker (☠️).
- **Detailed Item Logging**:
  Any item found on the floor will be logged and marked with (🎁).
- **Differential Passability Probing**:
  If blocked on one tile, we will test parallel tiles in the column/row before declaring a dead end.

## SPARKY (PIKACHU) Gym Training Plan (Turn 11425):
- **Objective**: Train SPARKY (PIKACHU, Level 11) to Level 18-20 to lead our battle against Gym Leader Misty. Electric-type moves (Thundershock) are super effective against Misty's Water-type team (Staryu, Starmie), whereas WARTORTLE's water moves are resisted.
- **Grinding Strategy**:
  1. Set SPARKY in the first slot of the party to lead and gain active combat experience.
  2. Grinding Route A: Tall grass on Route 4 East (before entering Cerulean City).
  3. Grinding Route B: Defeat trainers on Route 24/25 (north of Cerulean City) and grind in the tall grass there.
  4. Use GEMMY (WARTORTLE) as a high-level backup if SPARKY is in danger.
- **Execution Log**:
  - Turn 11425: SPARKY is currently Level 11. Moves: THUNDERSHOCK, GROWL, THUNDER WAVE. Max HP: 30.
- Turn 11531: Walking to Cerulean Poké Mart at (25, 25) to restock on supplies.