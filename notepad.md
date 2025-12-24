# Tile Mechanics
- FLOOR: Traversable.
- WALL / TREE / MOUNTAIN / HEADBUTT_TREE: Impassable.
- WATER: Requires Surf (HM03).
- TALL_GRASS: Traversable. Triggers wild encounters.
- CUT_TREE: Requires Cut (HM01). Regrows on map reload.
- LEDGE: One-way jump.
- FLOOR_UP_WALL: One-way barrier (Southward).
- WARP: Traversable.

# Type Effectiveness (Verified)
- Ghost vs Normal: Immune.
- Ghost vs Psychic: Super Effective.
- Psychic vs Ghost/Poison: Super Effective.
- Poison vs Ghost/Poison: Not very effective.
- Grass vs Ghost/Poison: Not very effective.

# Suicune Strategy (Lead: XENON Gastly Lv19)
- Goal: Reach Lv27 (Repel Trick threshold).
- Start Turn: 16309.
- Method: Mean Look (Turn 1) + Hypnosis/Lick.
- Note: Suicune moves on map transitions. Use roamer_tracker_v2.

# Future Tasks
- Reach Lv27 with XENON.
- Intercept Suicune using roamer_tracker_v2 (once XENON is Lv27).
- Test find_path_v2 fix.
- Test FLOOR_UP_WALL at (50, 14).
- Retrieve item from Fisher Tully (Route 42, 40, 10). (Turn 16158)

# Observed Movesets (Additions)
- Tangela: Absorb, Vine Whip, PoisonPowder.
- Bellsprout: Vine Whip, PoisonPowder, Sleep Powder.
- Weepinbell: PoisonPowder, Acid, Wrap.