# Key Locations & Mechanics
- New Bark Town (Mom's House): Mom at (2, 2) manages money and Daylight Saving Time.
- New Bark Town (Elm's Lab): Healing Machine at (2, 2).
- Blackthorn City (Pokemon Center): Warp at (21, 30).
- Route 45: High-level training area.

## Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable.
- TALL_GRASS: Walkable. Triggers wild encounters.
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
- **Gligar Typing:** Gligar is Ground/Flying. It is immune to Ground moves and neutral to Normal. It does not learn Faint Attack by level-up in this game. (Turn 33361).

# Catch Log: History
- Donphan (Wild, Lv 25, Female): Caught Turn 33389 (Route 45). Nicknamed "Armor", sent to Box 1. (Strategy: Sleep Powder/Great Ball).

# Training Log: Route 45 (Started Turn 33130)
- Goal: Xenon & Kimchi to Lv 40.
- Current Status (Turn 33418): Xenon Lv 35, Kimchi Lv 32 (55/85 HP). Donphan woke up.
- Strategy: Lead Gneiss (Lv 47), switch to targets for participation. Xenon holds Exp.Share.
- Logistics: Fly to Blackthorn PC for healing.

## Route 45 Exploration Status
- Progress: 67.9% explored. Remaining unseen tiles are mostly in the lower sections. (Turn 33361).
- Priority: Check for missed items/trainers while grinding.
- Verified Trainers: Hiker Erik (10, 16), Hiker Parry (5, 28), Cooltrainer Kelly (5, 34), Hiker Timothy (9, 65), Camper Quentin (4, 70). All marked as defeated.
- Verified Items: Max Repel (7, 33). Picked up. (Turn 32915).