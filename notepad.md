# Suicune Quest Strategy (Crystal Version)
- **Status:** All overworld sightings confirmed. Gatehouse Sage (4_1) confirmed "Tower Shook" (Turn 27084).
- **Tracker Update:** `suicune_tracker_v2` confirms the Wise Trio stage is bypassed/complete and Suicune is waiting on Tin Tower 1F (Turn 27090).
- **Current Objective:** Battle and capture Suicune on 1F.
- **Battle Prep:** Xenon (Gastly) is in the lead for Mean Look and Hypnosis.

## Strategy for Suicune Capture
1. **Approach:** Move to the center area of 1F (around (10, 9)) to trigger the encounter.
2. **Mean Look:** Use Mean Look immediately to prevent Suicune from fleeing (though it may be stationary here).
3. **Hypnosis:** Put Suicune to sleep to increase capture rate and reduce damage.
4. **Chip Damage:** Use Night Shade for fixed damage or switch to a lower-level Pokemon if needed (be careful of Suicune's level).
5. **Capture:** Use Great Balls/Ultra Balls while it is asleep and at low HP.

## Tile Mechanics - Global
- **FLOOR**: Standard walkable tile. Traversable.
- **WALL / VOID / HEADBUTT_TREE**: Impassable terrain.
- **WATER**: Traversable via SURF.
- **CUT_TREE**: Requires CUT to clear.
- **LEDGE_HOP / LEDGE**: One-way traversal (jump). Impassable from most directions.
- **DOOR / STAIRS / LADDER**: Warp tiles.
- **WARP_CARPET**: Map transition tile.

## Key Discoveries & Lessons Learned
- **Dialogue Triggers:** "The Tin Tower shook!" is the definitive narrative flag that all overworld sightings are complete.
- **Sequential Requirements:** Clear Bell + Sightings -> "Shook" dialogue -> Wise Trio Battle -> Suicune Encounter.
- **NPC Solidity:** NPCs are solid objects; paths must detour around them.
- **Map Transitions:** Leaving a map from specific coordinates triggers transitions (e.g., Ecruteak (18, 11) -> Tin Tower Gatehouse).

## Trainer & Party Info
- **Lead:** XENON (Gastly) Lv21 with Mean Look/Hypnosis.
- **Current Party:** Gastly, Pidgey, Graveler, Krabby, Gloom, Typhlosion.