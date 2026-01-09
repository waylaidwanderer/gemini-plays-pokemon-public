# Johto Journey - Final Phase

## Strategy: Navigate Tohjo Falls
- Start Turn: 35972
- Objective: Traverse Tohjo Falls to reach the eastern exit leading to the rest of Route 27.
- Requirements: SURF and WATERFALL (Rising Badge allows use).
- Steps:
  1. Obtain HM07 Waterfall from Ice Path 1F. [Collected Turn 36188]
  2. Teach Waterfall to LAPIS (slot 6) replacing Bubble. [Current]
  3. Use Waterfall to climb the falls in Tohjo Falls.
  4. Locate the eastern exit of Tohjo Falls.

## Strategy: Teach Waterfall and Exit
- Status: Teaching Waterfall to LAPIS (Turn 36190).
- Menu Navigation Offsets:
  - Start Menu -> PACK: 2 'Down' from top.
  - PACK -> TM/HM Pocket: 3 'Right' from Items.
  - HM07 Position: 10 'Down' from TM24.
  - Party Member (LAPIS): 5 'Down' from XENON.
  - Move to Replace (Bubble): Slot 1.
- Plan:
  1. Teach HM07 Waterfall to LAPIS. [Current]
  2. Exit Ice Path via (36, 27) using ice_pathfinder tool.
  3. Fly to New Bark Town and head east to Tohjo Falls.

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
- ICE: Causes sliding in the direction of movement until an obstacle or non-ice tile is reached.

## Lessons Learned
- Rising Badge: Allows use of HM07 Waterfall outside battle.
- Tohjo Falls Ledges: Row 16 ledges are impassable from North.
- Navigation: If a movement fails twice, the tile is impassable from that direction.
- Item Discovery: Moon Stone found in Tohjo Falls at (2, 6).
- Time Tracking: Searched for HM07 in Tohjo Falls for ~90 turns before verifying location.
- Wild Encounters: Trigger battles and block movement on the turn they occur. (Turn 36162)

## Route 44 Navigation Notes
- Ledge Gap: A traversable gap in the east-west ledges exists at x=49 (row 8 to 14 is clear at this x-coordinate).
- NPC Obstacles:
  - Cooltrainer Cybil: (31, 14), Cooltrainer Allen: (37, 15), Bird Keeper Vance: (51, 6), Youngster: (51, 5)
- Ice Path Entrance: (56, 7). Reachable from the north section of Route 44.
- North/South Section Divide: Divided by ledges in row 9 (x=51-57) and row 13 (x=50-53). Use gap at x=49.