# Current Status
- **Location:** Celadon City (Outdoors).
- **Goal:** Find and Defeat Erika (Rainbow Badge).
- **Plan:**
  1. Search Southern Celadon for the Gym (look for Cut trees).
  2. Defeat Erika.
  3. Explore rest of Celadon.

# Celadon City Notes
- **Game Corner:** (18, 19). Investigated. No Rocket Hideout found.
- **Prize Exchange:** (23, 19).
- **Pokemon Center:** (29, 9).
- **Mansion:** (16, 9) & (6, 9 back door?).
- **Gym Location:** Unknown. Searching South.

# Quest Logic (Kanto Badges)
- **Badges:** 12/16.
- **Obtained:** Boulder, Cascade, Thunder, Marsh.
- **Remaining:**
  - **Rainbow (Celadon):** Erika (Giga Drain TM?).
  - **Soul (Fuchsia):** Janine (Toxic TM?).
  - **Volcano (Seafoam):** Blaine.
  - **Earth (Viridian):** Blue.

# Game Mechanics Notes
- **Kanto TMs:** Misty did not give a TM. Note that most Kanto leaders in Gen 2 do not give TMs (exceptions: Janine and Erika).
- **Tile Mechanics:** `COUNTER` tiles act as walls/obstacles.

# Navigation Notes
- **Saffron City:** Hub for Celadon, Lavender, Vermilion, Cerulean.
  - **Key Locs:** PokeCenter (9, 29), Gym (34, 3), Dojo (26, 3), Silph Co (18, 21), Mr. Psychic (27, 29).
  - **Gates:** West (to R7), North (to R5), East (to R8), South (to R6).
- **Route 7:** Locked Door (Underground Path), gap in ledges at x=12. Northern path leads to Celadon.
- **Game Corner:** Located at (18, 19).
  - **Obstacle:** A wall/fence at Y=21 blocks direct south movement from the entrance. Must go around via X=26 (East) or X=12 (West - but blocked by water).
  - **Investigation:** No Hideout found.
  - **Interactions:** Fisher (Coins), Guru (Coins). Teacher at (21, 24) mentions slots.
- **Gym Location:** Unknown. Searching South.
  - **Hypothesis:** Gym is in the Southwest.
  - **Exploration:** Entered Celadon Cafe (25, 29).
  - **NPCs (Cafe):** Fisher (eating), Teacher (concentration), Super Nerd (Eatathon), Gaven (Phone call). All useless.
  - **Conclusion:** Cafe is a dead end.
- **Gym Location:** Unknown. Searching South.
  - **Hypothesis:** Gym is in the Southwest, possibly behind a Cut tree.
  - **Action:** Exit Cafe and look for Cut trees or paths East/South.
- **Tool Diagnostic:** `bfs_pathfinder` updated with debug prints. Monitoring performance.
- **Quest Start:** Turn 24041 (Searching Celadon Cafe).