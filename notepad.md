# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026

### Current Task
- **Status**: Trapped in Burned Tower 1F.
- **Location**: (10, 15).
- **Correction**: Tiles (9, 15) and (10, 15) are NOT holes (Wall/Floor).
- **Goal**: Return to (7, 15) (`TYPE_8564`) which is the confirmed hole graphic.
- **Hypothesis**: The map switch 3_14 <-> 3_13 indicates the hole mechanism. Must persist on tile.
- **Route**: Up to (10, 14) -> Left to (7, 14) -> Down to (7, 15).
- **Party**: Garnet (77/90).
- **Next**: Fall to B1F.

### Party Status
- Garnet (32) [Critical], Basil (9), Amethyst (10) [Fainted], Spinarak (14), Topaz (15) [Fainted], Harrz (14) [Fainted].

### Reflection & Plan
- **Reflection**: I've been hallucinating exits. `find_reachable_exits` confirmed I am trapped. I must rely on game mechanics (triggers/holes) rather than hoping for walls to disappear.
- **Eusine**: He ran away to the SE. Following his path might reveal the way.
- **Plan**: Move South to (10, 10). Search adjacent tiles.
- **Route**: (10, 5) -> South to (10, 10).