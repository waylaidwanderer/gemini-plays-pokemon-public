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
- Elevator Door at (18, 22): Tested on Turn 31901. Confirmed it is closed, impassable, and yields no interactive dialogue box.
- Elevator Warp at (25, 19): Entering this warp on Turn 32141 placed me in the Elevator Cabin (Map 0_203) at (3, 2).
- Elevator Control Panel at (1, 1) (Map 0_203): Interacted facing Up from (1, 2) on Turn 32176. Discovered it requires a key (the LIFT KEY).
- Elevator Exit: Exited the Elevator Cabin on Turn 32179 by walking into (2, 1), warping back to B2F at (25, 19).
- **Spinner Maze (2, 9) to (15, 18) Bypass Sequence**: Empirically solved via BFS modeling on Turn 32629:
  - From (2, 9), walk: `Right, Down, Down, Down, Down, Right, Down, Right, Right, Right, Right, Down, Down, Right, Right, Right, Right, Right, Down, Right`
  - This sequence successfully exits the spinner maze at stop tile (15, 18) without sliding into the (8, 11) trap.
  - Socratic Insight: The (8, 11) trap was designed to capture players who try to walk directly Down/Right too early. By detouring along the perimeter on rows 13 and 14, we bypass the spinners that feed into the trap. This indicates the designers wanted to force a snake-like perimeter route. We can look for similar "perimeter-safe" channels in other mazes.
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