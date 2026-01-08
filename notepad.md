# Game Mechanics & Systems
## Tile Mechanics (Confirmed)
- FLOOR / TALL_GRASS / GRASS: Walkable.
- WALL / COUNTER / PC / FLOOR_UP_WALL (from North): Impassable. (Verified FLOOR_UP_WALL at 13, 12).
- WATER: Requires Surf to traverse.
- WARP_CARPET_DOWN / DOOR / LADDER: Triggers map transition.
- HEADBUTT_TREE: Interact to use Headbutt.
- LEDGE_HOP (⤵️, ↩️, ↪️): One-way movement. (Confirmed: LEDGE_HOP_DOWN at 17, 13 triggers 2-tile descent; 12, 25 confirmed).

## Type Effectiveness Chart (Verified)
- Acid (Poison) -> Gligar (Ground/Flying): Not very effective.
- Flame Wheel (Fire) -> Donphan (Ground): Neutral.

## Money & Economy
- AMULET COIN: Doubles prize money from trainer battles. (Held by ICARUS).

# Pokemon & Party Information
## Party Strategy
- **Training Session (Route 45):** Started Turn 33466. (Last Updated: Turn 33838).
  - Goal: Xenon and Kimchi to Lv40.
  - Method: KIMCHI holds EXP.SHARE. Lead GNEISS (Lv48) or CALCIFER (Lv49). Avoid switching KIMCHI into Gravelers.
  - Progress: Xenon Lv36, Kimchi Lv33. (EXP.SHARE verified on KIMCHI).

## Strategy for Rising Badge (Gym Leader Clair)
- Status: Gym trainers defeated. Boulders pushed.
- Opponent: Clair uses Dragon-type Pokemon (Dragonair, Kingdra).
- Strategy:
  - GNEISS (Lv48): Earthquake/Strength for high physical damage.
  - XENON (Lv36): Night Shade for fixed damage and Hypnosis for control (critical for Kingdra).
  - CALCIFER (Lv49): Thunderpunch (Electric) for coverage vs Kingdra (Water/Dragon) and Return for general damage.
  - KIMCHI (Lv33): Sleep Powder for secondary status control.

# Lessons Learned
- **Menu/Item Loop:** Direct verification via Stats/battle XP is more reliable than repeated menu navigation if cursor memory causes misclicks.
- **Ghost Immunity:** Haunter immune to Normal moves.
- **Gligar Typing:** Ground/Flying. Immune to Ground.
- **Gen 2 Haunter Weakness:** No Levitate. Vulnerable to Ground.

# Historical Data (Archive)
- Gligar Capture (Turn 33500): Caught Lv 24 Male Gligar (Telson) on Route 45.
- Turn 50 Reflection (Turn 33838): Consistently verified mechanics (ledges, walls). Consolidated training strategy. Resolved menu loop. Pivot to exploration of south-east tiles.

# Exploration Log
- Potentially Reachable Unseen Tiles detected in column 11 and south-east. Tool 'find_reachable_unseen_tiles' refined for ledge logic.