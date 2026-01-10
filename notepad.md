# persistent_knowledge
## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with HM Surf.
- TALL_GRASS: Traversable, triggers wild encounters.
- DOOR/WARP: Step on to enter buildings/areas.
- LEDGE_HOP_DOWN: One-way traversal (North to South).
- FLOOR_UP_WALL: Impassable Wall from the North; cannot be jumped down from this side.
- COUNTER: Impassable Wall. Interact from adjacent tile.
- GYM_PLATFORM: Raised floor area. Accessible via stairs (LADDER tile type) or by Surfing onto it from water.

## Battle Mechanics (Verified)
- Hypnosis (Gen 2): Misses are reported as "It didn't affect Enemy [Pokemon]!". This does not imply type immunity.
- Night Shade: Deals fixed damage equal to the user's level.
- Type Effectiveness: Dark is super-effective against Ghost/Poison (Haunter).

## PC Storage (Box 1)
1. SPINARAK (Lv13), 2. SCYTHER (Lv14), 3. SEEL (Lv24), 4. MANTINE (Lv20), 5. KRABBY (Lv22), 6. TENTACOOL (Lv17), 7. KRABBY (Lv10), 8. DRATINI (Lv15)

## Movesets (HM Users)
- KIMCHI (GLOOM): Lv40 | CUT, FLASH
- GNEISS (GRAVELER): Lv53 | STRENGTH
- LAPIS (POLIWAG): Lv12 | SURF, WHIRLPOOL, WATERFALL
- ICARUS (PIDGEOTTO): Lv19 | FLY

## TMs & HMs Obtained
- HM01 CUT, HM02 FLY, HM03 SURF, HM04 STRENGTH, HM05 FLASH, HM06 WHIRLPOOL, HM07 WATERFALL
- TM07 ZAP CANNON (Power Plant Manager)
- TM24 DRAGONBREATH, TM28 DIG, TM33 ICE PUNCH, TM37 SANDSTORM, TM44 REST, TM47 STEEL WING

## Magnet Train Restoration
- **Start Turn:** 39646
- **Fly to Saffron Phase Start:** 39649
- **Status:** Power Plant restored. TM07 received.
- **Plan:**
  1. Fly to Saffron City.
  2. Visit the Magnet Train station at (24, 11) in Saffron City.
  3. Locate Copycat's lost Poké Doll.
  4. Obtain the Rail Pass.

## Power Plant Investigation (Resolved)
- Machine Part returned to Manager. Power restored to Kanto.

## Lessons Learned
- **FLY Map Navigation:** Use `press_menu_buttons_v2` and verify the destination text before pressing A.
- **Hidden Items in Water:** Can be found by facing the water tile and pressing A from an adjacent walkway. 
- **Itemfinder:** Range is limited (~4-5 tiles). Triangulation by checking multiple spots is effective.
- **Pathing:** 2D top-down paths are often wider than they look. Analyze all adjacent tiles when blocked.
## Long-Term Strategy (Advisor Tips)
- Defeat all 8 Kanto Gym Leaders to unlock Mt. Silver.
- Train ICARUS, LAPIS, and KIMCHI to close the level gap.
- Visit Lavender Radio Tower for the EXPN Card (to wake Snorlax on Route 11).