# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained), All overworld sightings must be triggered in order.
- Quest Start: Turn 24182.
- Session Start: Turn 26246.

## Current Strategy
- Plan:
  1. Travel to Cianwood City.
  2. Locate Eusine in the north (near (10, 14)) and defeat him in battle.
  3. Talk to Eusine in Ecruteak Pokémon Center (Prerequisite for sightings).
  4. Trigger Route 42 sighting (Central Island).
  5. Trigger Route 36 sighting (Sudowoodo Junction).
- Attempt 5 (Sequence Correction): Turn 26344.

## Suicune Quest Diagnostic Log
- Burned Tower: Flee event completed.
- Cianwood City (North): Flee event completed. [STATUS: Eusine BATTLE PENDING]
- Route 42: Attempt 1 (Turn 26164) and Attempt 2 (Turn 26322) failed.
- Ecruteak PC: Eusine MISSING (Confirmed at Turn 26293 and 26333).
- Wise Trio: Room (4_2) was empty at Turn 26233.
- Status: Correcting sequence error - heading to Cianwood for Eusine battle. [START TURN: 26344]

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
- Wise Trio battle might be a separate requirement or a trigger for Eusine's appearance.
- Confirmation bias is real: I thought I beat Eusine, but the Analyst corrected me! Always verify battle outcomes in the notepad.