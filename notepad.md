# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026

### Current Task
- **Status**: Searching for B1F Warp.
- **Location**: (7, 15) -> Moving to (9, 15).
- **Observation**: Standing on (7, 15) (Hole Graphic) did not warp me.
- **Discovery**: Map 3_13 has `TYPE_ffbb` tiles at (9, 15) and (10, 15). These are likely the active warps.
- **Action**: Move Right x2 to step on (9, 15).
- **Party**: Garnet (77/90).
- **Goal**: Fall to B1F.

### Party Status
- Garnet (32) [Critical], Basil (9), Amethyst (10) [Fainted], Spinarak (14), Topaz (15) [Fainted], Harrz (14) [Fainted].

### Reflection & Plan
- **Reflection**: I've been hallucinating exits. `find_reachable_exits` confirmed I am trapped. I must rely on game mechanics (triggers/holes) rather than hoping for walls to disappear.
- **Eusine**: He ran away to the SE. Following his path might reveal the way.
- **Plan**: Move South to (10, 10). Search adjacent tiles.
- **Route**: (10, 5) -> South to (10, 10).