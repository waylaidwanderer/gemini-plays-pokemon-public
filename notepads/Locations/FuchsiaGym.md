# Fuchsia Gym Verified Location Records (Map 0_157)

- **Entrance Warp Connection**:
  - Entrance door is connected to Fuchsia City (Map 0_7) at (5, 27). Inside warp lands at (4, 17).
- **Physical Landmarks & Obstacles**:
  - Features invisible walls that block passage.
  - Gym Statues are located near the entrance at (3, 14)-(3, 15) and (6, 14)-(6, 15).

## Defeated Trainers
- **Turn 43455**: Defeated Juggler at (8, 9) (stood at (7, 8) facing Down).
  - Roster: Drowzee Lv31, Drowzee Lv31, Kadabra Lv31, Drowzee Lv31.
- **Turn 43517**: Defeated Tamer Phil at (8, 3) (stood at (8, 2) facing Down).
  - Roster: Arbok Lv33, Sandslash Lv33, Arbok Lv33.
- **Turn 43741**: Defeated Juggler at (8, 13) (stood at (8, 13) facing Up).
  - Roster: Hypno Lv38.
  - Battle won using: GEMMY (BLASTOISE) Lv58 (174/190 HP).

## Verified Gym Topology

### Passable Corridors & Loops (Verified on Foot)
- **Column 8**: Open and passable from Row 4 to Row 12.
- **Column 9**: Open and passable from Row 12 to Row 17.
- **Row 1**: Open and passable from Column 4 to Column 9.
- **Row 2**: (5, 2) to (6, 2) is passable.
- **Row 4**: (5, 4) to (6, 4) is passable, and (8, 4) to (9, 4) is passable.
- **Row 5**: (5, 5) to (6, 5) is passable.
- **Row 6**: (4, 6) to (5, 6) is passable, and (7, 6) to (8, 6) is passable.
- **Row 7**: (3, 7) to (4, 7) is passable, (4, 7) to (5, 7) is passable, and (7, 7) to (8, 7) is passable.
- **Row 8**: (8, 8) to (8, 9) is passable.
- **Row 9**: (8, 9) to (7, 9) is passable.
- **Row 12**: (8, 12) to (9, 12) is passable.
- **Row 17**: (7, 17) to (9, 17) is passable.
- **Vertical Transitions**:
  - Column 4: Passable between Row 1 and Row 2, and Row 6 to Row 7.
  - Column 5: Passable between Row 1 and Row 2, and Row 6 to Row 7.
  - Column 6: Passable between Row 2 and Row 4.

### Invisible Walls (Empirically Confirmed Blocks)
- **Row 1**: Blocked between (3, 1) and (4, 1).
- **Row 2**: Blocked between (4, 2) and (5, 2).
- **Row 7**: Blocked between (2, 7) and (3, 7) (blocks trainer's sight).
- **Row 11/12 boundary**: Blocked on Column 9 between (9, 11) and (9, 12).
- **Row 12/13 boundary**: Blocked on Column 8 between (8, 12) and (8, 13).
- **Around (7, 8)**:
  - Blocked between (7, 7) and (7, 8) (North side of Juggler).
  - Blocked between (8, 8) and (7, 8) (East side of Juggler).
  - Blocked between (7, 9) and (7, 8) (South side of Juggler).
  - Note: You can still talk to/interact with NPCs across these invisible walls (verified on Turn 43709).

### Physical Obstacles
- **Tile (7, 12)**: Solid wall block (TYPE_2889).
- **Tile (7, 10)**: Solid wall block (TYPE_2889).

## Static NPC Positions
- **Gym Guide**: (7, 15) near the entrance.
- **Juggler (Defeated)**: (7, 8).
- **Tamer Phil (Defeated)**: Moved from (8, 2) to (8, 3).
- **Juggler at (8, 13)**: Faces Up, blocked from Row 12 by invisible wall at (8, 12)/(8, 13) boundary. Can be reached/interacted with from (9, 13) facing Left.