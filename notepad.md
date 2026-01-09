# Johto Journey - Final Phase
- Primary Goal: Challenge the Pokémon League at Indigo Plateau [Started Turn 35416, 5:00 PM]
- Secondary Goal: Prepare team for the Elite Four.
- Badges Obtained: 8/8 (Rising Badge obtained Turn 35416).

## Strategy: Heading to the Pokémon League
- Plan:
  1. Obtain gift Dratini from Dragon Clan Elder in Dragon Shrine (Dragon's Den). [Started Turn 35538, 7:00 PM]
  2. Level XENON (Haunter) to 45+. Teach it TM33 Ice Punch. [Started Turn 35480, 5:30 PM]
  3. Replace ICARUS (Pidgey) and Ravioli (Krabby) with high-level members (e.g., Red Gyarados, gift Dratini). [Started Turn 35480, 5:30 PM]
  4. Evolve KIMCHI (Gloom) using a Sun or Leaf Stone. [Started Turn 35480, 5:30 PM, Bug Contest Started Turn 35644, 7:00 PM]
     - How: Sun Stone from Bug Contest (Tue/Thu/Sat) or Leaf Stone gift from Gina on Route 34.
  5. Surf east from New Bark Town to Route 27 and reach the Pokémon League via Victory Road. [Started Turn 35480, 5:30 PM]

## Tile Mechanics (Global)
- FLOOR: Standard traversable tile. Verified.
- WATER: Traversable while Surfing. Verified.
- WALL: Impassable boundary. Verified.
- BUOY: Impassable water barrier. Verified.
- WHIRLPOOL: Requires HM06 to cross. Verified.
- LADDER/STAIRS: Warp between floors/sections. Verified.
- LEDGE: One-way jump transition (South). Verified.
- COUNTER: Impassable. Interaction with NPC behind it possible from adjacent tile. Verified.
- DOOR: Warp to building/area. Verified.
- CAVE: Warp to cave area. Verified.
- LEDGE_HOP_DOWN: One-way jump transition (South). Verified.
- FLOOR_UP_WALL: Impassable boundary (ledge face). Verified.
- WARP_CARPET: Usually map exit, but can be standard floor. Verified.
- HEADBUTT_TREE: Impassable boundary. Verified.

## Lessons Learned
- Dragon Shrine Entrance: Located on the south side (19, 29).
- Whirlpool Mechanics: Re-appears if you leave and re-enter the map.
- Fly: Can be used to quickly travel between cities from the Pokémon menu.
- Landing from Water: Can land on any adjacent FLOOR-type tile.
- **Move Compatibility:** Verifying TM33 Ice Punch compatibility for XENON (Haunter) on Turn 35653. Previous "NOT ABLE" observation on Turn 35645 was likely due to accidentally selecting HM01 CUT. Typhlosion is confirmed incompatible with Ice Punch in Crystal.

## League Analyst Advice
- Evaluation: Team is top-heavy (Typhlosion 49, Graveler 48). Others are underleveled (Haunter 37, others <20).
- Key Threats: Will's Psychic-types (outspeed/OHKO Haunter). Lance's Dragonites (lack of Ice coverage).
- Recommendations:
  - Obtain the gift Dratini; Dragonite can learn TM33 Ice Punch to counter Lance.
  - Level XENON (Haunter) to 45+. Teach it TM24 DragonBreath.
  - Replace ICARUS (Pidgey) and Ravioli (Krabby) with high-level encounters (e.g., Red Gyarados and gift Dratini).
  - Evolve KIMCHI (Gloom) using a Sun or Leaf Stone.
  - Use Gneiss (Graveler) with Earthquake for Koga/Bruno, but avoid Bruno's Fighting-types.
- Training Goal: Level all active party members (especially Xenon) to 45+ for the Pokémon League.
- Master Ball: Obtained from Prof. Elm [Turn 35463]. Save for legendary beasts (Suicune, Raikou, Entei).

## Failed Hypotheses
- **Hypothesis:** Typhlosion can learn Ice Punch in Crystal. **Test:** Tried teaching TM33. **Conclusion:** Denied (Turn 35538). Typhlosion is incompatible with Ice Punch in Crystal.
- **Hypothesis:** Interacting with the elevator button at (3, 0) from (3, 1) facing up on 5F calls the elevator. **Test:** Pressed A at (3, 1) facing up. **Conclusion:** Confirmed (Turn 35558). The menu appeared after the press.
## Strategy: Verified Conflict Resolution
- **Ice Punch Compatibility:** Despite external suggestions (League Analyst), in-game observation on Turn 35644 confirms Haunter (XENON) and Typhlosion (Calcifer) are "NOT ABLE" to learn TM33 Ice Punch. This is a verified fact for this specific game state. Strategy remains focused on gift Dratini.
- **Tool Fix:** Refined `find_path_v2` on Turn 35646 to support Surf and Ledge transitions. [Started Turn 35646]