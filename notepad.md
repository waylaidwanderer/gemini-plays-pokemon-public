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
3. Route 42 (Central Island): Failed (Turn 25654, Sprite not visible).
4. Route 36 (Sudowoodo Junction): Failed (Turn 25667, Sprite not visible).
5. Tin Tower 1F: Pending.

## Hypotheses & Strategy
- Hypothesis: The Wise Trio or Eusine at the Tin Tower Gatehouse hold the next flag now that Team Rocket is gone.
- Strategy:
    1. Exit Pokecenter and head to Tin Tower Gatehouse (17, 3).
    2. Talk to all Sages and Eusine.
    3. Re-check Route 42/36 sightings if a new flag is triggered.

## Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with SURF.
- CUT_TREE: Impassable; remove with CUT.
- GRASS: Traversable; triggers wild encounters.
- CAVE/DOOR: Warp/Entry point.
- LEDGE_HOP: One-way traversal.

## Lessons Learned
- Notepad Management: Only one `notepad_edit` call is allowed per turn. [Turn 25561]
- Suicune Sightings: Suicune is a static overworld sprite. If not visible at (26, 14), prerequisites are likely unmet. [Turn 25620]
- Tool Refinement: `find_path_v4` refined to handle floor-to-water transitions. [Turn 25643]
- Sequence Locking: Suicune sightings are strictly linear. Route 42 MUST be triggered before Route 36. [Turn 25682]