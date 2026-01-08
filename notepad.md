# Post-Game Goals
- **Primary:** Complete Pokedex (Current: 40 Owned).
- **Major Target:** CATCH LUGIA.
- **Start Time:** Jan 7, 2026 (Turn 27211).
- **Location:** Whirl Islands (Route 41).
- **Key Item:** Silver Wing (Owned).
- **Requirements:** Flash, Whirlpool, Surf, Strength.

# Current Status
- **Location:** Saffron City.
- **Action:** Going to Copycat's House (Northwest).
- **Party Check:**
  - Flash: Belladonna (Oddish).
  - Surf: Qaagmaqnjw (Gyarados).
  - Whirlpool: Lapis (Poliwag).
  - Strength: Muscle (Machoke).
  - Fly: Mistral (Pidgey).
- **Quest:** 
    1. Travel to Saffron City -> Talk to Copycat (Done).
    2. Return to Vermilion Fan Club -> Get Doll (Done - Have 'Lost Item').
    3. Saffron Copycat -> Get Pass.
    4. Goldenrod -> Whirl Islands.

## Tile Mechanics
- **FLOOR:** Standard traversable tile.
- **WALL:** Impassable.
- **WARP_CARPET:** Triggers a warp.
- **DOOR:** Warp tile.
- **WATER:** Requires Surf to traverse.
- **Note:** Verification of tile mechanics is ongoing.

## Travel Notes
- **Lesson:** Kanto Fly map cursor movement is non-linear/wrapping. Always verify destination visually.
- **Route 6:** Head North to Saffron Gatehouse (6, 1).
- **Warp Connection:** Vermilion Port Passage (15, 4) <-> (3, 2) (Internal Ladder).
- **Warp Connection:** Vermilion Port Passage (3, 14) <-> Vermilion Port (9, 5).
- **Route 6 Navigation:** Water pond at Row 11 blocks direct path. Must navigate via the eastern side (approx x=16) to cross North.
- **Tool Issue:** `find_path` incorrectly attempts to traverse ledges backwards. Needs update to respect one-way mechanics.
- **Map Correction:** House at (13, 13) is Magnet Train Speech House, NOT Fan Club.
- **Plan:** Check house at (21, 17) (South of Mart). (21, 13) is the Mart.
- **Investigation:** Confirmed 'Magnet Train House' (12_8) is NOT Fan Club.
- **Search:** Fan Club must be in the Southwest, near the Gym.
- **Map Correction:** House at (21, 17) is Diglett's Cave Speech House.
- **Search:** Fan Club must be elsewhere. Checking near Gym (Southwest).
- **Exploration:** Searching west of Magnet Train House (13, 13).
- **Target:** Unexplored area around (7, 13). Fan Club likely there.