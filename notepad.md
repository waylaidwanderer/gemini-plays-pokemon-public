# Tile Mechanics
- FLOOR: Traversable standard ground.
- WALL / WINDOW / BUOY / ROCK / BOOKSHELF / TV / RADIO / TOWN_MAP / STATUE: Impassable barriers.
- COUNTER: Impassable; interact with NPC behind it from adjacent tile.
- WATER: Traversable only while surfing. Requires Surf and Fog Badge.
- BUOY: Impassable barrier in water.
- WHIRLPOOL: Impassable water hazard. Requires HM06 (Whirlpool).
- WARP_CARPET_DOWN / WARP: Leads to a different map.
- BOULDER: Impassable; requires HM04 Strength to move (verified Turn 6387).
- ROCK: Impassable; can be crushed with Rock Smash.
- PC: Interactable object for Pokémon/Item storage.

# Lessons Learned
- Boulder Dialogue: "A POKéMON may be able to move this" = Strength (HM04). "A POKéMON may be able to smash this" = Rock Smash.
- Gym Access: Cianwood Gym requires Strength to reach the Leader.
- Battle Mechanics: FIRE moves are Special in Gen 2. HEADBUTT is a Physical Normal-type move that can cause flinching.
- NPC Interaction: Face the counter, not the NPC, to interact with Nurses/Clerks.
- Input Handling: Do not mix directional and action buttons in the same `press_buttons` call.
- Swimmer Kaylee (17, 2): Uses Goldeen (Lv18).

# Battle Strategy: Cianwood Gym (Chuck)
- Type: Fighting. Weaknesses: Flying, Psychic.
- Chuck's Team (Crystal): Primeape (27), Poliwrath (30).
- My Team Analysis:
  - Calcifer (QUILAVA) Lv32: Flame Wheel/Headbutt. Neutral typing.
  - GNEISS (GRAVELER) Lv34: Weak to Fighting (and Water). Backup only.
  - KIMCHI (ODDISH) Lv10: Poison resists Fighting. Needs training.
  - SHUCKIE (SHUCKLE) Lv15: High defense, but weak to Water.
- Strategy: Level up Calcifer. Use Ravioli for Surf if needed (Poliwrath is Water/Fighting).

# PC Storage (Box 1)
- Blarney (SUDOWOODO) Lv20, ROCKY (ONIX) Lv6, ICARUS (PIDGEY) Lv11, EGG (CLEFFA) Lv5, XFDW (MEOWTH) Lv16.

# Gym Progress
- Start Turn: 6328 (Entering Gym)
- Defeated: Yoshi (3, 12), Lao (5, 12), Nob (3, 9).
- Blocked: Boulders at (3, 7), (4, 7), (5, 7).
- Target: Get HM04 Strength from the house next to the Pokémon Center in Olivine City.