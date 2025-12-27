# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell, All Sightings Completed.
- Start: Turn 24182, Saturday 12:45 AM.
- Current Attempt Duration: ~1450 turns (Turn 24182 to 25638).

## Story Progress
- Clear Bell: Obtained.
- Team Rocket: Disbanded at Radio Tower.
- Tin Tower: Shook after entering gatehouse with Clear Bell. (Note: This confirms Clear Bell recognition, not Suicune's arrival).
- Wise Trio Room: Emptied.

## Sighting Progress
1. Burned Tower: [Verified]
2. Cianwood City (North): [Verified]
3. Route 42 (Central Island): Failed (Turn 25654, Sprite not visible after thorough sweep).
4. Route 36 (Sudowoodo Junction): Pending.
5. Tin Tower 1F: Pending.

## Hypotheses & Strategy
- Hypothesis 1: Suicune is a visible overworld sprite on the Route 42 island. (Status: Not visible at Turn 25571).
- Hypothesis 2: A specific flag from Cianwood is missing. [Action: Re-verify Eusine battle outcome].
- Hypothesis 3: Sighting sequence is non-linear or differs in Crystal. [Action: Check Route 36].

## Strategy & Planning
### Strategy for Route 42 Suicune Sighting
1. Land at (33, 9). [Done]
2. Walk to (21, 11) via y=10 path.
3. Surf on (21, 12) and land at (22, 12).
4. Walk to (24, 12).
5. Face (24, 13) and use CUT on the tree.
6. Walk to (26, 14) to trigger Suicune sighting.
7. If Suicune is still not visible, re-verify all previous sightings and flags. [Turn #25637]

### General Exploration
- Route 36 sighting: Fly to Ecruteak, walk south to Route 36 junction via Route 37, and approach from the south (Route 35 entrance).

## Tile Mechanics
- FLOOR: Traversable. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable with SURF. [Verified]
- CUT_TREE: Impassable; remove with CUT. [Verified]
- GRASS: Traversable; triggers wild encounters. [Verified]
- CAVE/DOOR: Warp/Entry point. [Verified]
- LEDGE_HOP: One-way traversal. [Verified]

## Lessons Learned
- Notepad Management: Only one `notepad_edit` call is allowed per turn. [Turn 25561]
- Suicune Sightings: Suicune is a static overworld sprite. If not visible at (26, 14), prerequisites are likely unmet. [Turn 25620]
- Tool Refinement: `find_path_v4` created to handle complex traversals and player detection. [Turn 25624]
- Note: find_path_v4 refined to handle floor-to-water transitions. [Turn 25643]
- Hypothesis: Route 42 sighting might be skipped or already triggered. Moving to Route 36. [Turn 25654]
- Route 36 (Sudowoodo Junction): Failed (Turn 25667, Sprite not visible).
- Current Hypothesis: Eusine or Wise Trio at Tin Tower Gatehouse hold the next trigger. [Turn 25681]