# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026

### Current Task
- **Status**: Troubleshooting B1F Access.
- **Analysis**: The "Center Hole" at (10, 9) is inaccessible due to wall blocks on Rows 10-12.
- **Lead**: The hole Eusine used at (7, 15) (`TYPE_8564`) is the only reachable exit tile.
- **Action**: Move to (7, 15) and attempt to fall/interact.
- **Route**: Right to (7, 14) -> Down to (7, 15).
- **Party**: Garnet (77/90).
- **Goal**: Fall to B1F.

### Party Status
- Garnet (32) [Critical], Basil (9), Amethyst (10) [Fainted], Spinarak (14), Topaz (15) [Fainted], Harrz (14) [Fainted].

### Reflection & Plan
- **Reflection**: I've been hallucinating exits. `find_reachable_exits` confirmed I am trapped. I must rely on game mechanics (triggers/holes) rather than hoping for walls to disappear.
- **Eusine**: He ran away to the SE. Following his path might reveal the way.
- **Plan**: Move South to (10, 10). Search adjacent tiles.
- **Route**: (10, 5) -> South to (10, 10).