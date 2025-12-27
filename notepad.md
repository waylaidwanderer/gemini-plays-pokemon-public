# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained), All overworld sightings must be triggered in order.
- Quest Start: Turn 24182.
- Session Start: Turn 26246.

## Current Strategy
- Plan:
  1. Finish dialogue with Poke Seer.
  2. Fly to Ecruteak City.
  3. Perform a comprehensive full-island sweep of Route 42 (x=21-32, y=11-18).
  4. If Suicune triggers, follow to Route 36.
  5. If no trigger, check Route 36 junction (35, 9) anyway.
  6. If both fail, re-verify Sage dialogues in Gatehouse and Tin Tower 1F.
- Loop Start: Turn 26164 (Stuck on sightings).

## Suicune Quest Diagnostic Log
- Burned Tower: Flee event completed.
- Cianwood City (North): Flee event completed.
- Eusine Battle: COMPLETED (Verified by summary and marker).
- Ecruteak PC: Eusine MISSING (Checked 1F/2F at Turn 26293 and 26333).
- Wise Trio Room (4_2): EMPTY (Checked at Turn 26233).
- Tin Tower 1F: Explored (Turn 26236). Clear Bell reactivated 'Tower Shake' event (Turn 26110).
- Status: Re-attempting Route 42 sighting with a wider sweep. [START TURN: 26371]

## Global Tile Mechanics (Verified)
- FLOOR: Traversable. Includes visual "Warp Carpets" and "Exit Mats".
- WALL: Impassable.
- WATER: Traversable ONLY with SURF.
- CUT_TREE: Impassable; remove with CUT. Regrows when map is reloaded.
- LADDER: Vertical transition (Warp).
- FLOOR_UP_WALL: Impassable from the NORTH. Functions like a ledge.
- HEADBUTT_TREE: Impassable.
- TALL_GRASS: Walkable.
- CAVE: Entrance/Exit warp.
- DOOR: Interactive warp tile.
- WARP_CARPET_LEFT: Warp tile at map edge.

## Lessons Learned
- Suicune events are strictly linear and mandatory.
- Eusine dialogue in Ecruteak PC is a known prerequisite in Crystal.
- Sages granting passage to Tin Tower doesn't mean sightings are done.
- Tile 'type' in XML is the source of truth for collision.
- Wise Trio battle happens AFTER all overworld sightings (Route 42/36).
- Confirmation bias is real: I thought I beat Eusine, but I need to re-verify the Cianwood battle.

## Suicune Quest Diagnostic Log
- Burned Tower: Flee event completed.
- Cianwood City (North): Flee event completed. [STATUS: PENDING BATTLE CHECK]
- Route 42: Attempt 1 (Turn 26164) and Attempt 2 (Turn 26322) failed.
- Ecruteak PC: Eusine MISSING (Confirmed at Turn 26293 and 26333).
- Wise Trio: Room (4_2) was empty at Turn 26233.
- Status: Verifying northern Cianwood for Eusine battle. [START TURN: 26364]
- Cianwood Sweep Result: Swept (1, 10) to (16, 15) at Turn 26363. No Eusine found. Suicune spot (10, 14) is empty.
- Current Hypothesis: Eusine moves to Ecruteak PC ONLY after being defeated in Cianwood. If he's missing from both, check if the Cianwood flee event actually happened (Summary says yes).