# Johto Journey - Final Phase

## Strategy: Navigate Tohjo Falls
- Start Turn: 35972
- Objective: Traverse Tohjo Falls to reach the eastern exit leading to the rest of Route 27.
- Requirements: SURF and WATERFALL (Rising Badge allows use).
- Steps:
  1. Obtain HM07 Waterfall from Ice Path 1F. [Current]
  2. Use Waterfall to climb the falls in Tohjo Falls.
  3. Locate the eastern exit of Tohjo Falls.

## Strategy: Obtain HM07 Waterfall
- Verified Location: Ice Path 1F, northeast corner of main floor. [Confirmed by location_analyst Turn 36062]
- New Plan (Started Turn 36063):
  1. Fly to Mahogany Town. [Current]
     - Note: Fly map cursor usually defaults to current location.
     - Fly Map Order (Crystal): New Bark, Cherrygrove, Violet, Azalea, Goldenrod, Ecruteak, Olivine, Cianwood, Mahogany, Blackthorn, Indigo Plateau.
     - Logic: 'Up' moves forward in this list.
  2. Travel east to Route 44 and enter Ice Path.
  3. Locate and pick up HM07 Waterfall.
  4. Return to Tohjo Falls and climb the waterfall.

## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable (requires SURF).
- WATERFALL: Impassable (requires WATERFALL).
- LEDGE (FLOOR_UP_WALL): One-way jump.
- COUNTER: Impassable; interactable from front.
- LADDER: Warp to another floor/map.
- WARP_CARPET_DOWN: Exit/warp to another map.
- PC: Impassable; interactable from front (up).

## Lessons Learned
- Rising Badge: Allows use of HM07 Waterfall outside battle.
- Tohjo Falls Ledges: Row 16 ledges are impassable from North.
- Navigation: If a movement fails twice, the tile is impassable from that direction.
- Item Discovery: Moon Stone found in Tohjo Falls at (2, 6).
- Time Tracking: Searched for HM07 in Tohjo Falls for ~90 turns before verifying location.

## Strategy: Fly Map Navigation
- Main Menu Order: 1. POKéDEX, 2. POKéMON, 3. PACK, 4. POKéGEAR, 5. GEM, 6. SAVE, 7. OPTION, 8. EXIT.
- Logic: 'Up' moves forward through towns on map.
- Current Status: Mahogany Town selected. Confirming flight.
- Note: Always verify the starting location on the FLY map before counting.
## Route 44 Navigation Notes
- Ledge Gap: A traversable gap in the east-west ledges exists at x=49 (row 8 to 14 is clear at this x-coordinate).
- NPC Obstacles:
  - Cooltrainer Cybil: (31, 14)
  - Cooltrainer Allen: (37, 15)
  - Bird Keeper Vance: (51, 6)
  - Youngster: (51, 5)
- Ice Path Entrance: (56, 7). Reachable from the north section of Route 44.
- North/South Section Divide: Route 44 is divided by a line of ledges in row 9 (x=51-57) and row 13 (x=50-53). Use the gap at x=49 to move between them.