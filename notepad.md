# Current Status
- **Location:** Celadon City.
- **Goal:** Defeat Erika (Rainbow Badge).
- **Plan:**
  1. (Done) Heal and gather intel at Pokemon Center.
  2. Explore West Celadon.
  3. Locate Game Corner (investigate Pharmacist's claim).
  4. Locate Gym and defeat Erika.

# Celadon City Notes
- **Pokemon Center:**
  - Gentleman (0,5): Checks Friendship.
  - Pharmacist (0,3): Claims Rocket Hideout in Game Corner basement (then retracted "3 years ago"). Suspicious.
  - Eusine (4,3): Visiting hometown.
  - Cooltrainer F (7,6): Warns that Erika is a master of Grass Pokemon and very tough.
- **Outdoors:**
  - Youngster (16, 13): Mentions hidden back door in Celadon Mansion.
  - Teacher (7, 15): Advertises Celadon Dept. Store.

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
- **Game Corner:** Located at (18, 19). Investigating for Team Rocket Hideout.
- **Game Corner Access:** Entrance is at (18, 19). Must wrap around the fence at x=26 to reach it.
- **Prize Exchange:** Located at (23, 19).
- **Suspicious Finding:** Slot machine at (18, 8) uses `CeladonGameCornerLighterScript` instead of the standard `LuckySlotMachine`. This is likely the secret switch.
- **Game Corner Investigation:** Interacted with slot machine at (18, 8). Found a lighter. No obvious immediate effect, but checking for hidden stairs in the top area.
- **Layout:** Rows 2-3 appear to be a dividing wall. Attempting to flank left to reach the northernmost area (Row 1).
- **Blocked Path:** The path at (13, 4) appears blocked despite looking like a floor tile. Attempting to cross to the left side via the bottom path (Row 13).
- **Tool Note:** `bfs_pathfinder` attempted to route through a COUNTER tile at (13, 5). It may not recognize COUNTER as an obstacle. Manually routing around obstacles may be safer.
- **Left Area Access:** Gap at Row 4 (y=4) allows access to the left side of the room (Columns 0-6).
- **Poster Check:** Both posters (15, 0) and (9, 0) checked. Result: "There's nothing!".
- **Game Corner Conclusion:** The "Lighter" script and posters appear to be red herrings or references to Gen 1. The Pharmacist's comment about "3 years ago" implies the Rocket Hideout is no longer accessible here.
- **Gym Guide:** Found slacking off in Game Corner (11,3). Useless - just gambling. Did not provide Gym location.
- **Gym Location:** Unknown. Need to explore city (likely South). Expecting a Cut tree.