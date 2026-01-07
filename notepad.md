# Key Locations & Mechanics
- New Bark Town (Mom's House): Mom at (2, 2) manages money and Daylight Saving Time.
- New Bark Town (Elm's Lab): Healing Machine at (2, 2).
- Blackthorn City (Pokemon Center): Warp at (21, 30).
- Route 45: High-level training area.

# Tile Mechanics: Johto
- FLOOR: Walkable. Verified.
- WALL: Impassable. Verified.
- TALL_GRASS: Walkable. Triggers wild encounters. Verified.
- WATER: Requires Surf to traverse.
- WARP_CARPET_DOWN: Triggers map transition when walking down.
- DOOR: Triggers map transition when entered.
- HEADBUTT_TREE: Interact to use Headbutt (if learned).
- LEDGE_HOP_DOWN: One-way movement (down). Verified.
- LEDGE_HOP_LEFT: One-way movement (left). Verified.
- LEDGE_HOP_RIGHT: One-way movement (right). Verified.

# Fly Navigation (Johto Cycle)
- Sequence (using Up): New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod -> Ecruteak -> Olivine -> Cianwood -> Mahogany -> Lake of Rage -> Blackthorn.
- Strategy: Use fly_navigator_v2. Verify town name on screen.

# Item Tracking
- AMULET COIN: In Bag (Turn 33085).
- EXP.SHARE: Held by XENON.
- PNK APRICORN: In Bag (Turn 33081).
- HARD STONE: Held by GNEISS.

# Lessons Learned
- **Inventory Verification:** Never assume ownership of TMs/items based on external knowledge. Always verify Bag/PC contents. (Turn 33203).
- **Move Matchups:** Check party movesets before switching. Kimchi lacked Grass moves for Graveler. (Turn 33260).
- **Ghost Immunity:** Haunter is immune to Normal moves like Selfdestruct, making it a safe switch against exploding foes. (Turn 33265).

# Current Plan
1. Training Phase: Lv40+ for Xenon and Kimchi on Route 45. (Started Turn 33130).
   - Xenon: Lv34 -> Lv40
   - Kimchi: Lv32 -> Lv40
2. Gym Phase: Challenge Blackthorn Gym for the Rising Badge.

## Training Strategy: Route 45
- Lead: GNEISS (Lv47).
- Participation: Switch to Xenon/Kimchi for shared EXP when safe.
- Passive: XENON holds EXP.SHARE.
- Logistics: Fly to Blackthorn PC for healing when PP/HP is low.

## Route 45 Exploration Status
- Unseen tiles remaining. Priority: Check for missed items/trainers while grinding.
- Verified Trainers: Hiker Erik (10, 16), Hiker Parry (5, 28), Cooltrainer Kelly (5, 34), Hiker Timothy (9, 65), Camper Quentin (4, 70).
- Verified Items: Max Repel (7, 33).