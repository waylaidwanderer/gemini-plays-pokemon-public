# Post-Game Goals
- **Primary:** Complete Pokedex (Current: 40 Owned).
- **Major Target:** CATCH LUGIA.
- **Start Time:** Jan 7, 2026 (Turn 27211).
- **Location:** Whirl Islands (Route 41).
- **Key Item:** Silver Wing (Owned).
- **Requirements:** Flash, Whirlpool, Surf, Strength.

# Current Status
- **Location:** New Bark Town (6, 11).
- **Action:** Navigating Fly Map (Ecruteak -> Goldenrod -> ?).
- **Hypothesis:** 'Left' from Ecruteak is blocked. Trying 'Down' then 'Left'.
- **Immediate Plan:** Press Down (to Goldenrod) -> Left (to Olivine?). Verify destination.
- **Goal:** Fly to Cianwood -> Surf to Whirl Islands.
- **Party Check:**
  - Flash: Belladonna (Oddish).
  - Surf: Qaagmaqnjw (Gyarados).
  - Whirlpool: Lapis (Poliwag).
  - Strength: Muscle (Machoke).
  - Fly: Mistral (Pidgey).
- **Quest:** 
    1. Travel to Saffron City -> Talk to Copycat (Done).
    2. Return to Vermilion Fan Club -> Get Doll (Done).
    3. Saffron Copycat -> Get Pass (Done - Have 'PASS').
    4. Take Magnet Train to Goldenrod.
    5. Goldenrod -> Whirl Islands.

## Tile Mechanics
- **FLOOR:** Standard traversable tile.
- **WALL:** Impassable.
- **WARP_CARPET:** Triggers a warp.
- **DOOR:** Warp tile.
- **WATER:** Requires Surf to traverse.
- **Note:** Verification of tile mechanics is ongoing.

## Travel Notes
- **Route 6:** Head North to Saffron Gatehouse (6, 1). Pond at Row 11 blocks direct path; go east.
- **Warp Connection:** Vermilion Port Passage (15, 4) <-> (3, 2) (Internal Ladder).
- **Warp Connection:** Vermilion Port Passage (3, 14) <-> Vermilion Port (9, 5).
- **Tool Issue:** `find_path` incorrectly attempts to traverse ledges backwards. Needs update to respect one-way mechanics.
- **Locations:**
    - Vermilion Fan Club: Southwest Vermilion.
    - Magnet Train Speech House: Vermilion (13, 13).
    - Diglett's Cave Speech House: Vermilion (21, 17).