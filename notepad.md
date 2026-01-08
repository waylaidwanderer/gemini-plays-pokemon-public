# Game Mechanics & Systems
## Global Tile Mechanics
- FLOOR: Walkable. Verified.
- WALL: Impassable. Verified.
- TALL_GRASS / GRASS: Walkable. Triggers wild encounters. Verified.
- WATER: Requires Surf to traverse. Verified.
- WARP_CARPET_DOWN / DOOR / LADDER: Triggers map transition. Verified.
- HEADBUTT_TREE: Interact to use Headbutt. Verified.
- LEDGE_HOP (⤵️, ↩️, ↪️): One-way movement in the indicated direction. Impassable from the opposite side. Verified.
- FLOOR_UP_WALL: Impassable from the North (moving Down onto it). Likely a ledge face. Verified.
- COUNTER: Impassable. Interact from adjacent tile for NPC dialogue. Verified.
- PC (Pokemon Center): Interact to manage Pokemon/items. Verified.

## Type Effectiveness Chart (Verified)
- Acid (Poison) -> Gligar (Ground/Flying): Not very effective. (Turn 33436).
- Flame Wheel (Fire) -> Donphan (Ground): Neutral. (Turn 33613 observed 'A critical hit', not super effective).

## Money & Economy
- AMULET COIN: Held by ICARUS (Turn 33626). Doubles prize money from trainer battles.

# Pokemon & Party Information
## Party Strategy
- EXP.SHARE: Held by XENON. Receives 50% XP from all battles.
- Training Strategy (Route 45): Lead Gneiss (Lv 48) to absorb hits. Switch in Kimchi/Xenon for participation XP. Gneiss or Calcifer as finisher. (Session started Turn 33466. Progress: Xenon Lv36, Kimchi Lv32. Turn 33730).

# Area Mechanics & Strategy
## Route 45 (Training Area)
- Encounter Rate: High in TALL_GRASS at (12, 10). Frequent Gligar (Lv24) and Graveler (Lv23).

## Strategy for Rising Badge (Gym Leader Clair)
- Status: Gym trainers defeated. Boulders pushed into pits.
- Opponent: Clair uses Dragon-type Pokemon.

# Lessons Learned
- **Inventory Verification:** Always verify Bag/PC contents. (Turn 33203).
- **Move Matchups:** Kimchi lacked Grass moves for Graveler early on. (Turn 33260).
- **Ghost Immunity:** Haunter is immune to Normal moves like Selfdestruct. (Turn 33265).
- **Gligar Typing:** Ground/Flying. Immune to Ground. (Turn 33361).
- **Gen 2 Haunter Weakness:** No Levitate. Vulnerable to Ground. (Turn 33588).
- **Menu Precision:** Avoid rushing in deep menus to prevent errors like opening Pokedex instead of Pack. (Turn 33626).

# Historical Data (Archive)
- Gligar Capture (Turn 33500): Caught Lv 24 Male Gligar (Telson) on Route 45.
- **Menu Cursor Memory:** Menus like the Pack and Party remember the last cursor position. Verify the cursor location before executing long button sequences to avoid selection errors. (Turn 33694).