# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell, All Sightings Completed.
- Start: Turn 24182, Saturday 12:45 AM.
- Current Attempt Duration: ~1600 turns.

## Story Progress
- Clear Bell: Obtained.
- Team Rocket: Disbanded at Radio Tower.
- Tin Tower: Shook after entering gatehouse with Clear Bell.
- Sages (Gatehouse & 1F): All talked to after tower shook. [Turn 25726]

## Sighting Progress
1. Burned Tower: [Verified]
2. Cianwood City (North): [Verified]
3. Route 42 (Central Island): [In Progress]
4. Route 36 (Sudowoodo Junction): [Pending]
5. Tin Tower 1F: Pending.

## Tile Mechanics
- FLOOR: Traversable. Standard ground collision. [Verified]
- WALL: Impassable. Structural/boundary collision. [Verified]
- WATER: Traversable with SURF. Triggers wild encounters (e.g., Goldeen). [Verified]
- CUT_TREE: Impassable. Can be removed with HM01 CUT. Regrows on map reload. [Verified]
- GRASS / TALL_GRASS: Traversable. Triggers wild encounters. [Verified]
- CAVE / DOOR / WARP: Transitions between maps. [Verified]
- LADDER: Vertical transition between map levels. [Verified]
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt. [Verified]
- FLOOR_UP_WALL: Traversable (ledges/stairs). Typically one-way down for ledges. [Verified]

## Failed Hypotheses & Attempts
- Attempt 1 (Route 42): Swept southern island clearing (Turns 25639-25771). No trigger.
- Attempt 2 (Route 36): Swept Sudowoodo junction (Turns 25787-25794). No trigger.
- Hypothesis: Talking to all Sages was the final trigger for Route 42. [Denied - Swept island, no trigger].

## Strategy
- Current: Perform a granular sweep of the northern part of the Route 42 island floor (22, 12) to (28, 12).
- Next: If no trigger, perform a full granular sweep of the entire island floor again.
- Final: Check Route 36 junction one more time.