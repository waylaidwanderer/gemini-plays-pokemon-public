# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell, All Sightings Completed.
- Start: Turn 24182, Saturday 12:45 AM.

## Story Progress
- Clear Bell: Obtained.
- Team Rocket: Disbanded at Radio Tower.
- Tin Tower: Shook after entering gatehouse with Clear Bell.
- Wise Trio Room: Emptied.

## Sighting Progress
1. Burned Tower: [Verified]
2. Cianwood City (North): [Verified]
3. Route 42 (Central Island): Pending.
4. Route 36 (Sudowoodo Junction): Pending.
5. Tin Tower 1F: Pending.

## Hypotheses & Strategy
- Hypothesis 1: Suicune is a visible overworld sprite on the Route 42 island.
- Hypothesis 2: A specific flag from Cianwood (e.g., Eusine battle) is required. [Verified: Defeated Eusine]
- Hypothesis 3: Approaching from Route 36 first is required.

## Strategy & Planning
- Route 42 sighting: [Current Target - Started Turn 25547]
  - Goal: Confirm Suicune sprite visibility on the central island.
  - Plan: Surf to the island, use Cut, and check for sprite at (26, 14).
  - Failed Attempts: 3 (Swept island multiple times, sprite not visible).
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
- Suicune Sightings: Sweeping every tile on the Route 42 island may not trigger the event if the sprite is missing. Prerequisites are likely unmet. [Turn 25572]
- Battle State: Navigation tools (like `find_path_v3`) cannot be used while in battle. Use `select_battle_option` instead. [Turn 25560]
- Tool Refinement: `find_path_v3` needs debugging for water-to-land transitions. `find_path_v4` created. [Turn 25620]