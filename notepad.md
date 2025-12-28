# Current Status
- **Location:** Celadon City (Pokemon Center).
- **Goal:** Defeat Erika (Rainbow Badge).
- **Plan:**
  1. Heal at Pokemon Center.
  2. Talk to remaining NPCs (Super Nerd, Cooltrainer F).
  3. Investigate Game Corner (verify Pharmacist's claim).
  4. Locate Gym and defeat Erika.

# Celadon City Notes
- **Pokemon Center:**
  - Gentleman (0,5): Checks Friendship.
  - Pharmacist (0,3): Claims Rocket Hideout in Game Corner basement (then retracted "3 years ago"). Suspicious.
  - Eusine (4,3): Visiting hometown.
  - Cooltrainer F (7,6): Unspoken.

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

# Navigation Notes
- **Saffron City:** Central hub connecting to Celadon, Lavender, Vermilion, Cerulean.

# History
- **Turn 23808:** Defeated Misty (Cerulean Gym). Earned Cascade Badge. No TM received.
- **Turn 23789:** Defeated Trainers Parker and Diana.
- **Turn 23600:** Fixed Power Plant (Machine Part).
## Tool Notes
- `bfs_pathfinder`: Ignores Trainer LOS. Handles LEDGEs correctly.
- `smart_battle_move`: Remembers last cursor position in battle.

# Saffron City Locations
- **PokeCenter:** (9, 29)
- **Magnet Train:** (8, 3)
- **Gym:** (34, 3) (Psychic - Sabrina)
- **Dojo:** (26, 3) (Fighting)
- **Silph Co:** (18, 21)
- **Mr. Psychic:** (27, 29) (TM29 Psychic acquired)
- **Copycat's House:** (9, 11) (Suspected)
- **West Gate (to Route 7):** (0, 24)
- **North Gate (to Route 5):** (18, 3)
- **East Gate (to Route 8):** (39, 22)
- **South Gate (to Route 6):** (16, 33)
- **Route 7:**
  - Locked Door at (6, 9) (likely Underground Path, inaccessible).
  - Gap in ledges at x=12 allows access to south side.
- **Route 7 Navigation:**
  - Southern path (row 2+) is blocked by walls on the west side.
  - Northern path (rows 0-1) appears open to the west. Taking this route to Celadon.