# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell, All Sightings Completed.
- Start: Turn 24182, Saturday 12:45 AM.
- Current Attempt Duration: ~1500 turns.

## Story Progress
- Clear Bell: Obtained.
- Team Rocket: Disbanded at Radio Tower.
- Tin Tower: Shook after entering gatehouse with Clear Bell.
- Wise Trio Room: Emptied.

## Sighting Progress
1. Burned Tower: [Verified]
2. Cianwood City (North): [Verified]
3. Route 42 (Central Island): Failed (Turn 25654, Sprite not visible after thorough sweep). Note: Prerequisites might be missing despite completed sightings.
4. Route 36 (Sudowoodo Junction): Failed (Turn 25667, Sprite not visible). Note: Sighting #3 must be completed first.
5. Tin Tower 1F: Pending.

## Hypotheses & Strategy
- Hypothesis: The Wise Trio or Eusine at the Tin Tower Gatehouse hold the next flag now that Team Rocket is gone.
- Strategy:
    1. Talk to all Sages and Gramps in the Gatehouse. [Done - Turn 25706]
    2. Investigate Tin Tower grounds via Section 3 (Left Strip) of map 4_1.
    3. Reach Section 3 via the Wise Trio Room (4_2) ladder at (17, 3) in map 4_1.
    4. If Suicune is not at Tin Tower, return to Cianwood to check for missed Eusine dialogue.

## Tin Tower Gatehouse Investigation (Archived Results)
- Result: Gramps talked about the two towers and the two Pokémon that flew away. Sages mentioned a Pokémon returned to the top. This dialogue confirms the Clear Bell is recognized and the tower is active. [Turn 25706]

## Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with SURF.
- CUT_TREE: Impassable; remove with CUT.
- GRASS: Traversable; triggers wild encounters.
- CAVE/DOOR: Warp/Entry point.
- LEDGE_HOP: One-way traversal.
- LADDER: Warp tile; triggers transition upon entry or movement. [Verified - Turn 25708]

## Lessons Learned
- Notepad Management: Only one `notepad_edit` call is allowed per turn. [Turn 25561]
- Suicune Sightings: Suicune is a static overworld sprite. If not visible at (26, 14), prerequisites are likely unmet. [Turn 25620]
- Tool Refinement: `find_path_v4` refined to handle floor-to-water transitions and ladder/door types. [Turn 25707]
- Sequence Locking: Suicune sightings are strictly linear. Route 42 MUST be triggered before Route 36. [Turn 25682]