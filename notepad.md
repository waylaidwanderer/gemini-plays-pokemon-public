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
- Suicune Location (Turn 16301): Route 42.
- Plan: Exit Pokecenter -> Route 44 -> Train XENON to Lv27.
- Strategy: Use Repel Trick on Route 44 once XENON is Lv27.
## Strategy for XENON Training (Turn 16309)
- Goal: Reach Lv27.
- Location: Route 44 tall grass (approx. (30, 9)).
- Method: Battle wild Pokemon until level reached.
- Note: Max wild level here is 26 (Weepinbell/Lickitung).

## Reflection (Turn 16309)
1. **Immediate Execution:** No deferred tasks.
2. **Notepad Hygiene:** Added training strategy. Tile mechanics and Suicune strategy are up to date.
3. **Map Hygiene:** Markers for Route 44 sign and Psychic Phil are set. 
4. **Automation Strategy:** `find_path_v2` and `get_reachable_unseen_tiles_v2` are current. No new tools needed for training.
5. **Goal Clarity:** Primary goal is concrete (Lv27+). Notepad has the "How".
6. **Error Analysis:** No recent major errors. Root hypothesis for Suicune (Mean Look + Repel Trick) is standard for GSC.