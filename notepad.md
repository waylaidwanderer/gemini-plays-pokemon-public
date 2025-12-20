# Tile Mechanics
- FLOOR: Traversable standard ground.
- WALL / WINDOW / BUOY / ROCK / BOOKSHELF / TV / RADIO / TOWN_MAP / STATUE: Impassable barriers.
- COUNTER: Impassable; interact with NPC behind it from adjacent tile.
- WATER: Traversable only while surfing. Requires Surf and Fog Badge.
- WHIRLPOOL: Impassable water hazard. Requires HM06 (Whirlpool).
- WARP_CARPET_DOWN / WARP: Leads to a different map.
- BOULDER: Impassable, can be crushed with Rock Smash.
- PC: Interactable object for Pokémon/Item storage.

# Lessons Learned
- Menu Precision: Slow down during move learning and item usage. Double-check before confirming.
- Route 41 Navigation: Row 29 is a reliable corridor west.
- Ecruteak Gym Path: (3,9)->(3,7)->(6,7)->(6,5)->(7,5)->Martha; (6,5)->(5,5)->(5,1)->Morty.
- Moomoo Farm: Sick Miltank needs 7 standard BERRY items.
- Input Handling: Do not mix directional and action buttons in the same `press_buttons` call.
- NPC Interaction: Face the counter, not the NPC, to interact with Nurses/Clerks.
- Battle Mechanics: FIRE moves are Special in Gen 2.

# Battle Strategy: Cianwood Gym (Chuck)
- Type: Fighting. Weaknesses: Flying, Psychic.
- Chuck's Team (Crystal): Primeape (27), Poliwrath (30).
- My Team Analysis:
  - Calcifer (QUILAVA) Lv31: Flame Wheel/Headbutt. Neutral typing.
  - GNEISS (GRAVELER) Lv34: Weak to Fighting (and Water). Backup only.
  - KIMCHI (ODDISH) Lv10: Poison resists Fighting. Needs training.
  - SHUCKIE (SHUCKLE) Lv15: High defense, but weak to Water.
- Strategy: Level up Calcifer. Use Ravioli for Surf if needed (Poliwrath is Water/Fighting).

# PC Storage (Box 1)
- Blarney (SUDOWOODO) Lv20, ROCKY (ONIX) Lv6, ICARUS (PIDGEY) Lv11, EGG (CLEFFA) Lv5, XFDW (MEOWTH) Lv16.

# Gym Progress
- Start Turn: 6328 (Entering Gym)

# Gym Strategy: Boulders
- Boulders at (3,7), (4,7), (5,7) require Rock Smash to break (per Pokefan M).
- Plan: Teach Rock Smash to GNEISS after healing Calcifer.