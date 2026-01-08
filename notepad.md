# Game Mechanics & Systems
## Tile Mechanics (Confirmed)
- FLOOR / TALL_GRASS / GRASS: Walkable.
- WALL / COUNTER / PC / FLOOR_UP_WALL (from North): Impassable. (Verified FLOOR_UP_WALL at 13, 12; 11-14, 58).
- WATER: Requires Surf to traverse.
- WARP_CARPET_DOWN / DOOR / LADDER: Triggers map transition.
- HEADBUTT_TREE: Interact to use Headbutt.
- LEDGE_HOP_DOWN (⤵️): One-way movement from North to South. Landing on the tile below. (Verified at 17, 13; 12, 25; 12, 29; 10, 45; 10, 47; 10, 53; 16, 59; 17, 59).

## Type Effectiveness Chart (Verified)
- Acid (Poison) -> Gligar (Ground/Flying): Not very effective.
- Flame Wheel (Fire) -> Donphan (Ground): Neutral.

## Money & Economy
- AMULET COIN: Doubles prize money from trainer battles. (Held by ICARUS).

# Pokemon & Party Information
## Party Strategy
- **Training Session (Route 45):** Started Turn 33466. (Last Updated: Turn 33884).
  - Goal: Xenon and Kimchi to Lv40.
  - Method: KIMCHI holds EXP.SHARE. Lead GNEISS (Lv48) or CALCIFER (Lv49) to finish battles efficiently. Avoid switching KIMCHI into Gravelers due to Selfdestruct risk.
  - Progress: Xenon Lv36, Kimchi Lv33. (Verified EXP.SHARE on KIMCHI Turn 33825).

# Area Mechanics & Strategy
## Strategy for Rising Badge (Gym Leader Clair)
- Status: Gym trainers defeated. Boulders pushed into pits.
- Opponent: Clair uses Dragon-type Pokemon (Dragonair, Kingdra).
- Strategy:
  - GNEISS (Lv48): Earthquake/Strength for high physical damage. (Dragonair is pure Dragon, vulnerable to Ground).
  - XENON (Lv36): Night Shade for fixed damage and Hypnosis for control (critical for Kingdra).
  - CALCIFER (Lv49): Thunderpunch (Electric) for coverage vs Kingdra (Water/Dragon) and Return for general damage.
  - KIMCHI (Lv33): Sleep Powder for secondary status control.

# Exploration Log
- Items: Max Potion collected at (7, 33) Turn 33849.
- Black Belt Kenji at (11, 50) defeated (Turn 33873).
- Hiker Michael at (15, 65) battle started (Turn 33887).
- Blocked Unseen: (14, 61-62). (Blocked from North by FLOOR_UP_WALL at y=58).

# Lessons Learned
- **Menu/Item Loop:** Direct verification via Stats/battle XP is more reliable than repeated menu navigation if cursor memory causes misclicks.
- **Ghost Immunity:** Haunter immune to Normal moves like Selfdestruct.
- **Gligar Typing:** Ground/Flying. Immune to Ground.
- **Gen 2 Haunter Weakness:** No Levitate. Vulnerable to Ground.
- **Menu Cursor Memory:** Menus like the Pack and Party remember the last cursor position. Verify the cursor location before executing long button sequences.
- **Phone Calls:** Can interrupt movement and trigger wild battles if you land on a grass tile after the call. (Turn 33875).