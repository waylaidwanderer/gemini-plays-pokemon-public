# Tile Mechanics
- FLOOR: Traversable. Verified on multiple maps.
- WALL / TREE / MOUNTAIN / HEADBUTT_TREE: Impassable. Verified on multiple maps.
- WATER: Requires Surf (HM03). Verified on Route 42/44.
- TALL_GRASS: Traversable. Triggers wild encounters. Verified on Route 31/32/44.
- CUT_TREE: Requires Cut (HM01). Regrows on map reload. Verified in Ilex Forest/Route 36.
- LEDGE: One-way jump (South/Right/Left/Up). Jump 2 tiles. Verified on multiple routes.
- FLOOR_UP_WALL: One-way barrier. Blocks Southward movement. (Hypothesis - To be tested).
- WARP: Traversable. Transitions to another map. Verified on multiple maps.

# Type Effectiveness (Verified)
- Ghost (Gastly) vs Normal: Immune.
- Ghost (Gastly) vs Psychic: Super Effective.
- Psychic vs Ghost/Poison (Gastly): Super Effective.
- Poison (Bellsprout) vs Ghost/Poison (Gastly): Not very effective.
- Grass (Bellsprout) vs Ghost/Poison (Gastly): Not very effective.

# Observed Movesets
- Natu: Future Sight, Night Shade.
- Remoraid: Psybeam.
- Bellsprout: Vine Whip, PoisonPowder, Sleep Powder.
- Weepinbell: PoisonPowder, Acid, Wrap.

# Suicune Capture Strategy
- Lead: XENON (Gastly, Lv19) - Speed: 38.
- Strategy:
  - Repel Trick: Lead level must be > Lv26 (Route 44 max) but < Lv40. Target: Lv27+.
  - Mean Look on Turn 1 is mandatory.
  - If Mean Look fails: Track via Pokedex/Pokegear and re-intercept.
  - Note: Suicune changes its location every time the player transitions between maps (warps or map edges).
  - Backup: Switch to Calcifer (Lv45) to tank. Use Ultra/Great Balls.
  - Priority: Find Quick Claw and a second trapping Pokemon (e.g. Spider Web).

## Strategy for XENON Training
- Goal: Reach Lv27.
- Start Turn: 16309.
- Location: Route 44 tall grass island.
- Method: Battle wild Pokemon until level reached.
- Note: Max wild level here is 26 (Weepinbell/Lickitung). Bellsprout/Weepinbell can use Grass/Poison moves which Gastly resists.

## To-Do
- Confirm Suicune location via Pokedex Area search after training.
- Test find_path_v2 after fix (Priority: HIGH).
- Test FLOOR_UP_WALL at (50, 14) or (19, 16) after training session.
- Catch second trapper Pokemon.

## Reminders
- Fisher Tully (Route 42, 40, 10) has an item for me. (Turn 16158)