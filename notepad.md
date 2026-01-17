# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026 at 5:08 PM PST

### Current Objectives & Strategy
- **Main Quest**: Begin the Gym Challenge (Violet City).

- **Battle Strategy**: Train Garnet (Lv 9), Amethyst (Lv 3), and "T" (Hoothoot Lv 3). Heading to Cherrygrove (Mom does NOT heal).
- **Healing**: Mom (New Bark) or Cherrygrove PC.

### Tile Mechanics
- **Ledges (TYPE_fed7)**: One-way jumpable (South). On Route 29, these are often walkable slopes. Verify by testing upward movement.
- **Trees (TYPE_2889)**: Impassable.
- **Small Trees (Cut)**: Breakable with Cut HM (e.g. Route 29 x=21).
- **Water (TYPE_4e8c)**: Impassable without Surf.
- **Tall Grass**: Wild Pokemon encounters.
- **Warps**: Stairs (TYPE_17bc), Mats (TYPE_ffbb), Doors (TYPE_201b).

### Key Locations & Navigation
#### Cherrygrove City
- **Facilities**: Pokemon Center, Mart (No Poke Balls yet), Guide Gent's House.
- **Key Items**: Map Card (Guide Gent).
- **Exits**: Route 29 (East), Route 30 (North).

#### Route 30 (Map 26_1)
- **Layout**: Splits into West (Blocked by Event) and East (Trainers) paths. Currently on East path.
- **Obstacles**: Ledge at y=48 (Passable via gap at x=12).
- **Resources**: Berry Tree at (5, 39) [Looted].
- **NPCs**: Youngster Joey (12, 27), Youngster Mikey (6, 30).
- **Connections**: Violet City (North), Cherrygrove (South).

### Route 29 Notes (Completed)
- **North Lane (Row 6)**: Path to Cherrygrove.
- **Encounters**: Pidgey, Sentret, Hoppip (Day); Hoothoot, Rattata (Night).
- Note: TYPE_fed7 is NOT always a ledge. It is the common ground tile on Route 30. Movement confirms passability.
- Mr. Pokemon's House: Located at Route 30 (17, 5).
- Plot: Met Mr. Pokemon and Professor Oak inside.
- Items Acquired: Mystery Egg, Pokedex.
- Status: Healed by Oak.
- Current Objective: Return to Professor Elm in New Bark Town.
- Warning: Route 29 Navigation Complexity.
  - High Path (Row 6/8): Access via New Bark Town. Blocked at x=43 by One-Way Ledge if coming from West, but should be passable heading West?
  - Middle Path (Row 11): Blocked West at x=21 by Cut Tree. Blocked East by Ledge at x=43?
  - Lower Path (Row 13/14): Dead End East at x=54. Dead End West at x=13.
  - **Navigation Critical Info**:
    - **Ledge Barrier (x=43)**: This is a ONE-WAY barrier allowing EASTBOUND jumps (return to New Bark). It BLOCKS Westbound travel on Rows 8 and 11.
    - **Implication**: The High Road and Middle Road are return paths.
    - **Search Area**: The path to Cherrygrove MUST be elsewhere. 
      - Option A: Very Top Edge (Row 4-6) - Check for a gap North of the ledge barrier.
      - Option B: Lower Path (Row 14-16) - Verified Dead End at x=13.
      - Option C: Hidden path near the Gatehouse (if it exists).
  - **Plan**: Return to New Bark Town. Walk West on the High Road but hug the NORTH edge (Row 6/5) to see if I can bypass the x=43 barrier.

# Navigation Paradox: Route 29
- **Goal**: Reach Cherrygrove City (West).
- **Current Status**: All known paths appear blocked.
  1. **High Road (Row 6/8)**: Blocked at x=43 by One-Way Ledge (allows East, blocks West). Access to Row 6 blocked by trees at x=45.
  2. **Middle Road (Row 10/11)**: Investigating. Expected blockage at x=21 (Cut Tree).
  3. **Lower Road (Row 14/16)**: Previously identified as "Dead End" at x=13.
  4. **Gatehouse (52, 7)**: Front door locked/wall. Back/Side did not reveal path.

- **Hypothesis**:
  - **A**: The "Dead End" at Lower Road (x=13) is false. There is a gap or path North.
  - **B**: There is a hidden gap in the Ledge Barrier at x=43.
  - **C**: The Gatehouse has a specific trigger or entrance I missed.

- **Immediate Plan**:
  1. Confirm Cut Tree on Middle Road (x=21).
  2. **CRITICAL**: Return to Lower Road and painstakingly check every tile near x=13 for a passage.