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
- Status: Roaming. Last confirmed on Route 44 (ID: 2_6). (Turn 16196)
- Lead: XENON (Gastly, Lv19) - Speed: 38 (9 when paralyzed).
- Strategy:
  - Repel Trick: Lead level must be > Lv26 but < Lv40. Target: Lv27+.
  - Mean Look on Turn 1 is mandatory.
  - If Mean Look fails: Track via Pokedex and re-intercept.
  - Backup: Switch to Calcifer (Lv45) to tank. Use Ultra/Great Balls.
  - Priority: Find Quick Claw and a second trapping Pokemon (e.g. Spider Web).

## Training Phase
- Start Turn: 16198
- Location: Route 44 tall grass.
- Goal: Level XENON to Lv27+.
- Current Battle: Bellsprout (Lv22). Start Turn: 16225. XENON 33/45 HP, PAR.

## To-Do
- Test find_path_v2 after battle (Turn 16244 fix).
- Test FLOOR_UP_WALL at (50, 14) or (19, 16) after training session.
- Catch second trapper Pokemon.