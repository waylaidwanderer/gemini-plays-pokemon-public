# Rocket Hideout Exploration & Layout Records
- Started: Turn 31025
- Primary Goal: Locate and clear Celadon Game Corner / Rocket Hideout to secure the SILPH SCOPE.

## Multi-Floor Navigation & Key Landmarks Directory
| Floor | Feature Type | Coordinates | Connects To / Notes | Status / Turn Verified |
|-------|--------------|-------------|---------------------|------------------------|
| B1F   | Stairs UP    | (21, 1)     | Game Corner (17, 4) | Verified (Turn 31019)  |
| B1F   | Stairs DOWN  | (23, 2)     | Floor B2F (27, 8)   | Verified (Turn 31574)  |
| B1F   | Elevator     | TBD         | Elevator Shaft      | Unexplored             |
| B2F   | Stairs UP    | (27, 8)     | Floor B1F (23, 2)   | Verified (Turn 31574)  |
| B2F   | Stairs DOWN  | TBD         | Floor B3F           | Unexplored             |
| B2F   | Elevator     | TBD         | Elevator Shaft      | Unexplored             |
| B3F   | Stairs UP    | TBD         | Floor B2F           | Unexplored             |
| B3F   | Stairs DOWN  | TBD         | Floor B4F           | Unexplored             |
| B3F   | Elevator     | TBD         | Elevator Shaft      | Unexplored             |
| B4F   | Stairs UP    | TBD         | Floor B3F           | Unexplored             |
| B4F   | Elevator     | TBD         | Elevator Shaft      | Unexplored             |

## Key Dungeon Items & Quest Progression
- **Lift Key**: Needed to operate the elevator.
  - [ ] Location: TBD (Usually dropped by a specific Grunt or found on floor)
- **Silph Scope**: Awarded after defeating Boss Giovanni.
  - [ ] Location: B4F (Giovanni's Office)

## Detailed Dungeon Battle Log
- **Floor B1F**:
  - [x] Grunt 1 at (26, 8) (Defeated Turn 31059, Gained ¥630)
  - [x] Grunt 2 at (12, 6) (Defeated Turn 31154)
  - [ ] Grunt 3 at (28, 18) (In SE-South corridor behind Row 16 table)
- **Floor B3F**:

## Floor B2F (Map 0_200)
- B2F Exploration Started: Turn 31575
- Spawn Point/Stairs UP to B1F: (27, 8) inside a small northeast room.
- Exit from northeast room: bottom-left via (23, 14) / (23, 15).
- Defeated Rocket Grunt at (20, 13) on Turn 31597.
- Spinner Maze Entry: Stepped Left from (18, 11) onto (17, 11) on Turn 31625, sliding all the way to stop tile (2, 9).
- Discovered and Collected Poké Ball 1 (Moon Stone) at (1, 11) on Turn 31637. Poké Ball 2 at (6, 12).
## Floor B3F (Map 0_199 - Shared with B1F)
- **Shared Map ID Warning**: Floor B1F and Floor B3F share the exact same emulator Map ID '0_199'.
  - B1F occupies the Northern partition: Y-coordinates 0 to 15.
  - B3F occupies the Southern partition: Y-coordinates 17 to 27.
  - Row 16 serves as a solid horizontal wall divider.
- **Map Marker Protocol**: Since the Map ID is shared, all markers for both B1F and B3F are active on Map 0_199.
  - B1F markers: Y-coordinate <= 15 (e.g. Stairs UP at (21,1), Stairs DOWN at (23,2)).
  - B3F markers: Y-coordinate >= 17 (e.g. Defeated Grunt at (17,25), Defeated Grunt at (18,17)).
  - DO NOT delete B1F markers when cleaning up or editing B3F markers.
- B3F Exploration Started: Turn 31811
- Spawn Point/Stairs UP to B2F: (21, 24) on B3F.
- Visible layout around starting room:
  - There are stairs up at (21, 24).
  - Walkable floor (TYPE_3fe2) extends:
    - West to column 17 (rows 21-26).
    - East to column 22 (rows 21-26).
    - South is blocked by walls (row 27).
    - North is bounded by walls (row 20 is not visible, but row 21 is walkable).
- Defeated Rocket Grunt 1 at (17, 25) on Turn 31831. Added map marker.
- Defeated Rocket Grunt 2 at (18, 17) on Turn 31867. Added map marker.