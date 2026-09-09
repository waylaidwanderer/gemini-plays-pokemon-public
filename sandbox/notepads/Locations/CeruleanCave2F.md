# Cerulean Cave (Unknown Dungeon) 2F - Layout & Notes

## Connected Component Graph (2F)
- **Component A (Main 2F Maze)**: Continuous walkable maze spanning cols 1-24 and rows 3-19.
  - Entry/Exit Ladder A1: (1, 3) <-> 1F (1, 3) (NW ground entrance).
  - Entry/Exit Ladder A2: (3, 11) <-> 1F (3, 11) (Western ridge entrance).
  - Both (1, 3) and (3, 11) connect directly through the continuous 2F corridors without needing to traverse 1F!
- **Component B (Isolated Landing)**: (22, 6) <-> 1F (23, 7) (isolated 2-tile dead-end).
- **Component C (Isolated Alcove)**: (19, 7) <-> 1F (18, 9) (isolated 3x3 dead-end).
- **Component D (Isolated NE Landing)**: (29, 1) <-> 1F (27, 1) (isolated 7-tile dead-end).
- **Component E (Isolated NW Terrace)**: (9, 1) <-> 1F (7, 1) (isolated 6-tile corridor with item at 5, 0).

## Verified Items (2F)
- Item Pokéball at (29, 9) collected.
- Item Pokéball at (13, 6) collected.
- Item Pokéball at (4, 15) collected (TM14 Blizzard) [Turn 39796].

## Wild Encounters (2F)
- Ditto (Normal)
- Chansey (Normal)
- Venomoth (Bug/Poison)
- Kadabra (Psychic)
- Dodrio (Normal/Flying)
- Rhydon (Ground/Rock)
- Electrode (Electric)
- Marowak (Ground)
- Wigglytuff (Normal)
