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

# Observed Movesets
- Tangela: Absorb, Vine Whip, PoisonPowder.
- Bellsprout: Vine Whip, PoisonPowder, Sleep Powder.
- Weepinbell: PoisonPowder, Acid, Wrap.
- Natu: Future Sight, Night Shade.
- Remoraid: Psybeam.

# Suicune Strategy (Lead: XENON Gastly Lv19)
- Goal: Reach Lv27 (Repel Trick threshold).
- Start Turn: 16309.
- Method: Mean Look (Turn 1) + Hypnosis. Switch to Calcifer for damage if needed.
- Note: Suicune moves on map transitions. Use roamer_tracker_v2.
- Efficiency Tip: Ghost moves (Lick) are Physical in this game. Gastly is a Special attacker. For training, start with XENON then switch to Calcifer to finish battles quickly.

# Future Tasks
- Reach Lv27 with XENON.
- Intercept Suicune using roamer_tracker_v2 (once XENON is Lv27).
- Test find_path_v2 fix.
- Test FLOOR_UP_WALL at (50, 14).
- Retrieve item from Fisher Tully (Route 42, 40, 10). (Turn 16158)
- XENON (Gastly) learns Night Shade at Lv21. Fixed damage (equal to level) is ideal for weakening Suicune without over-killing.
- Training Progress: XENON Lv20. Need ~900 EXP for Lv21 (~5 Poliwags). Poliwag (Lv22-24) gives ~180-200 EXP.