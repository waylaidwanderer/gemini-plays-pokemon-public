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

# Current Plan
## Training Strategy: Route 45
- Lead: GNEISS (Lv47).
- Participation: Switch to Xenon/Kimchi for shared EXP when safe.
- Passive: XENON holds EXP.SHARE.
- Logistics: Fly to Blackthorn PC for healing when PP/HP is low.

## Route 45 Exploration Status
- Task started: Turn 32625.
- Unseen tiles remaining. Priority: Check for missed items/trainers while grinding.
- Progress: 67.9% explored. Remaining unseen tiles are mostly in the lower sections. (Turn 33361).

# Catch Log: Donphan (Wild, Lv 25)
- Strategy: Sleep Powder with KIMCHI, then Great Balls.
- Turn 33363: Encounter.
- Turn 33371: Poké Ball failed.
- Turns 33372-33378: Great Ball attempts.
- Turn 33379: Donphan woke up.
- Turn 33380: Sleep Powder success.
- Turns 33382-33384: Great Ball attempts.
- Turn 33385: Donphan woke up.
- Turn 33386: Sleep Powder success.
- Turn 33387: Opened Pack.
- Turn 33388: Throwing Great Ball. status: SLP. Great Balls: 32.
- Turn 33389: Gotcha! DONPHAN was caught! Strategy: Great Ball success. Data added to Pokedex. Nicknaming to "Armor". Sent to Box 1.