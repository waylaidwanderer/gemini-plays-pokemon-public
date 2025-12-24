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

# Battle Strategies
- Avoid leading XENON against Fishers/Psychic users until higher level.
- Paralysis: Reduces Speed by 75%, 25% chance to fail move.

# Suicune Capture Strategy
- **Status**: Roaming. Last confirmed on Route 44 (ID: 2_6). (Turn 16196)
- **Lead**: XENON (Gastly, Lv18) - Speed: 36 (9 when paralyzed).
- **Strategy**:
  - Repel Trick: Lead level must be > area wild max (Lv26 on Route 44) but < roamer level (Lv40). Target: Lv27+.
  - Mean Look on Turn 1 is mandatory.
  - If Mean Look fails: Track via Pokedex and re-intercept.
  - Backup: Switch to Calcifer (Lv45) to tank. Use Ultra/Great Balls.
  - Priority: Find Quick Claw and a second trapping Pokemon (e.g. Spider Web).

## Training Phase
- Start Turn: 16198
- Location: Route 44 tall grass.
- Goal: Level XENON to Lv27+.
## Battle Log (Turn 16219)
- Opponent: Poliwag (Lv22, SLP).
- Strategy: LICK while asleep. Re-apply HYPNOSIS if it wakes up.
- Current Status: XENON 31/43 HP. Poliwag asleep.
- To-Do: Test FLOOR_UP_WALL at (50, 14) after battle. Refine find_path_v2.