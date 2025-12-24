# Tile Mechanics
- FLOOR: Traversable.
- WALL / TREE / MOUNTAIN / HEADBUTT_TREE: Impassable.
- WATER: Requires Surf (HM03). 
- CUT_TREE: Requires Cut (HM01). Regrows on map reload.
- LEDGE: One-way jump (South/Right/Left/Up). Jump 2 tiles.
- FLOOR_UP_WALL: One-way barrier. Blocks Southward movement. (Hypothesis - To be tested)

# Type Effectiveness (Verified)
- Ghost (Gastly) vs Normal: Immune.
- Ghost (Gastly) vs Psychic: Super Effective.
- Psychic vs Ghost/Poison (Gastly): Super Effective.

# Observed Movesets
- Natu: Future Sight, Night Shade.
- Remoraid: Psybeam.
- Bellsprout: Stun Spore.
- Weepinbell: PoisonPowder, Acid, Wrap.

# Suicune Capture Strategy
- Lead: XENON (Gastly, Lv19) - Speed: 38.
- Strategy:
  - Repel Trick: Lead level must be > Lv26 (Route 44 max) but < Lv40. Target: Lv27+.
  - Mean Look on Turn 1 is mandatory.
  - If Mean Look fails: Track via Pokedex/Pokegear and re-intercept.
  - Backup: Switch to Calcifer (Lv45) to tank. Use Ultra/Great Balls.
  - Priority: Find Quick Claw and a second trapping Pokemon (e.g. Spider Web).

## To-Do
- Confirm Suicune location via Pokegear map.
- Test find_path_v2 after fix (Priority: HIGH).
- Test FLOOR_UP_WALL at (50, 14) or (19, 16) after training session.
- Catch second trapper Pokemon.
## Reminders
- Fisher Tully (Route 42, 40, 10) has an item for me. (Turn 16158)
- Test find_path_v2 again to ensure fix is robust.