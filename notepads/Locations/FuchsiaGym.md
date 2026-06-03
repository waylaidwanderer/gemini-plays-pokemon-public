# Fuchsia Gym Verified Location Records (Map 0_157)

- **Entrance Warp Connection**:
  - Entrance door is connected to Fuchsia City (Map 0_7) at (5, 27). Inside warp lands at (4, 17).
- **Physical Landmarks & Obstacles**:
  - Features invisible walls that block passage.
  - Gym Statues are located near the entrance.

## Defeated Trainers
- **Turn 43455**: Defeated Juggler at (8, 9) (stood at (7, 8) facing Down).
  - Roster: Drowzee Lv31, Drowzee Lv31, Kadabra Lv31, Drowzee Lv31.
- **Turn 43517**: Defeated Tamer Phil at (8, 3) (stood at (8, 2) facing Down).
  - Roster: Arbok Lv33, Sandslash Lv33, Arbok Lv33.
- **Turn 43741**: Defeated Juggler at (8, 13) (stood at (8, 13) facing Up).
  - Roster: Hypno Lv38.
  - Battle won using: GEMMY (BLASTOISE) Lv58 (174/190 HP).
- **Turn 43813**: Defeated Juggler at (1, 12) (stood at (1, 12) facing Down).
  - Roster: Drowzee Lv34, Kadabra Lv34.
  - Battle won using: GEMMY (BLASTOISE) Lv58 (157/190 HP).

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
- **Row 17**: Completely open and fully passable on foot from Column 0 to Column 9 (Verified on Turn 43844).
- **Vertical Transitions**:
  - Column 1: Passable between Row 7 and Row 8 (Verified on Turn 44156).
  - Column 4: Passable between Row 1 and Row 2, and Row 6 to Row 7.
  - Column 5: Passable between Row 1 and Row 2, and Row 6 to Row 7, and Row 16 to Row 17 (Verified on Turn 44110).
  - Column 6: Passable between Row 2 and Row 4.

### Invisible Walls (Empirically Confirmed Blocks)
- **Row 1**: Passable! Checked on Turn 43884 by walking from (4, 1) directly left to (3, 1). There is NO invisible wall between (3, 1) and (4, 1).
- **Row 2**: Blocked between (4, 2) and (5, 2).
- **Row 7**: Blocked between (2, 7) and (3, 7) (blocks trainer's sight).
- **Row 11/12 boundary**: Blocked on Column 9 between (9, 11) and (9, 12).
- **Row 12/13 boundary**: Blocked on Column 8 between (8, 12) and (8, 13).
- **Around (7, 8)**:
  - Blocked between (7, 7) and (7, 8) (North side of Juggler).
  - Blocked between (8, 8) and (7, 8) (East side of Juggler).
  - Blocked between (7, 9) and (7, 8) (South side of Juggler).
  - Note: You can still talk to/interact with NPCs across these invisible walls (verified on Turn 43709).

### Physical Obstacles (Solid Walls & Blocks)
- **Row 4**: (0, 4), (1, 4), (4, 4), (7, 4) are solid wall blocks (TYPE_2889).
- **Row 5**: (4, 5), (7, 5) are solid wall blocks (TYPE_2889).
- **Row 10**: (7, 10) is a solid wall block (TYPE_2889).
- **Row 11**: (0, 11), (1, 11), (2, 11), (7, 11) are solid wall blocks (TYPE_2889).
- **Row 12**: (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12) are solid wall blocks (TYPE_2889).
- **Gym Statues**: (3, 14)-(3, 15) and (6, 14)-(6, 15) are solid wall blocks (TYPE_2889).

## Static NPC Positions
- **Gym Guide**: (7, 15) near the entrance.
- **Juggler (Defeated)**: (7, 8).
- **Tamer Phil (Defeated)**: Moved from (8, 2) to (8, 3).
- **Juggler at (8, 13)**: Faces Up, blocked from Row 12 by invisible wall at (8, 12)/(8, 13) boundary. Can be reached/interacted with from (9, 13) facing Left.
- **Turn 43904**: Defeated Juggler at (2, 7) (stood at (2, 8) facing Up).
  - Roster: Drowzee Lv34, Drowzee Lv34, Kadabra Lv34.
  - Battle won using: GEMMY (BLASTOISE) Lv58.
- **Turn 43951**: Defeated Gym Leader Koga at (4, 10) (stood at (5, 10) facing Left).
  - Roster: Koffing Lv37, Muk Lv39, Koffing Lv37, Weezing Lv43.
  - Battle won using: GEMMY (BLASTOISE) Lv58. Obtained the Soul Badge!
- **Turn 44168**: Successfully spoke to Koga at (4, 10) inside Fuchsia Gym to retrieve TM06 (Toxic) in our newly freed inventory slot. Gym objectives are now 100% complete.