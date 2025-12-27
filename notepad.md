# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell, All Sightings Completed.
- Start: Turn 24182, Saturday 12:45 AM.
- Current Attempt Duration: ~1550 turns.

## Story Progress
- Clear Bell: Obtained.
- Team Rocket: Disbanded at Radio Tower.
- Tin Tower: Shook after entering gatehouse with Clear Bell.
- Wise Trio Room: Emptied.
- Sages (Gatehouse & 1F): All talked to after tower shook. [Turn 25726]

## Sighting Progress
1. Burned Tower: [Verified]
2. Cianwood City (North): [Verified]
3. Route 42 (Central Island): Failed (Turn 25654). Re-attempting after Sage dialogue.
4. Route 36 (Sudowoodo Junction): Pending.
5. Tin Tower 1F: Pending.

## Hypotheses & Strategy
- Hypothesis: Talking to all Sages in Ecruteak while the Clear Bell is active is the final trigger for the Route 42 sighting.
- Strategy:
    1. Travel to Route 42 central island.
    2. Use CUT on tree at (24, 13).
    3. Sweep the southern part of the island to trigger Suicune.
    4. If unsuccessful, return to Cianwood City to re-verify Eusine battle outcome and talk to the Seer.
    5. If still stuck, re-explore Mt. Mortar for any missed triggers.

## Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with SURF.
- CUT_TREE: Impassable; remove with CUT.
- GRASS / TALL_GRASS: Traversable; triggers encounters.
- CAVE / DOOR / WARP: Warp points.
- LADDER: Warp point.
- HEADBUTT_TREE: Impassable.
- FLOOR_UP_WALL: Traversable (ledges/stairs).

## Lessons Learned
- Notepad Management: Only one `notepad_edit` call is allowed per turn.
- Suicune Sightings: Strictly linear. Route 42 MUST be triggered before Route 36.
- Tool Refinement: `find_path_v4` refined for complex types. [Turn 25707]
- Proximity Triggers: Suicune sightings may be zone-based, not just single-tile. [Turn 25741]