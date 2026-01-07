# Key Locations & Mechanics
- New Bark Town (Mom's House): Mom at (2, 2) manages money and Daylight Saving Time.
- New Bark Town (Elm's Lab): Healing Machine at (2, 2).
- Blackthorn City (Pokemon Center): Warp at (21, 30).
- Route 45: High-level training area.

## Global Tile Mechanics
- FLOOR: Walkable. Verified.
- WALL: Impassable. Verified.
- TALL_GRASS: Walkable. Triggers wild encounters. Verified.
- WATER: Requires Surf to traverse. Verified.
- WARP_CARPET_DOWN: Triggers map transition when walking down. Verified.
- DOOR: Triggers map transition when entered. Verified.
- HEADBUTT_TREE: Interact to use Headbutt (if learned). Verified.
- LEDGE_HOP_DOWN: One-way movement (down). Verified.
- LEDGE_HOP_LEFT: One-way movement (left). Verified.
- LEDGE_HOP_RIGHT: One-way movement (right). Verified.
- FLOOR_UP_WALL: Impassable from the North (moving Down onto it). Likely a ledge face or similar barrier. Verified (Turn 33461).
- COUNTER: Impassable. Interact from adjacent tile to talk to NPC behind it. Verified.
- PC (Pokemon Center): Interact to manage Pokemon and items. Verified.
- LADDER: Triggers map transition between floors. Verified.
- GRASS: Walkable. Triggers wild encounters. Verified.

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
- **Status Effectiveness:** Sleep Powder and Hypnosis reportedly failed against wild Gligar with 'It didn't affect' (Turns 33475, 33482). Overwatch suggests this is a misunderstanding of mechanics; re-verification required if encountered again.
- **Type Effectiveness:** Acid (Poison) is not very effective against Gligar (Ground/Flying). (Turn 33436).
- **Input Precision:** Avoid mixing directional and action buttons in a single sequence. Verify turn count against Game State before acting. (Turn 33423).
- **Turn Counter Sync:** Always verify the turn number against the 'Turn #' in the Game State or the top of the prompt. (Turn 33433).

# Training Log: Route 45 (Started Turn 33130)
- Goal: Xenon & Kimchi to Lv 40.
- Strategy: Lead Gneiss (Lv 47), switch to targets for participation. Xenon holds Exp.Share.
- Logistics: Fly to Blackthorn PC for healing.
- Current Status: Training. Kimchi fainted to wild Graveler's Selfdestruct. Heading to Blackthorn PC to heal. (Turn 33524).
- Party Status (Turn 33521):
  - Gneiss: Lv 47 (102292 EXP)
  - Kimchi: Lv 32 (28259 EXP)
  - Xenon: Lv 35 (38624 EXP)
  - Calcifer: Lv 48 (109535 EXP)

## Route 45 Exploration Status
- Progress: 67.9% explored. Remaining unseen tiles are mostly in the lower sections. (Turn 33361).
- Priority: Check for missed items/trainers while grinding.

## Strategy for Rising Badge (Gym Leader Clair)
- Status: Gym trainers defeated. Boulders pushed into pits to clear the path.
- Opponent: Clair uses Dragon-type Pokemon.
- Plan: Train Xenon and Kimchi to Lv 40 on Route 45 to match her levels. Use Gneiss (Rock/Ground) and Calcifer (Fire) as primary attackers.
- Start Turn (Grinding): 33466.

## Historical Data (Archive)
- Gligar Capture (Turn 33500): Caught Lv 24 Male Gligar (Telson).