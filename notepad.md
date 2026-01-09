# Johto Journey - Final Phase
- Primary Goal: Challenge the Pokémon League at Indigo Plateau [Started Turn 35416, 5:00 PM]
- Secondary Goal: Prepare team for the Elite Four.
- Badges Obtained: 8/8 (Rising Badge obtained Turn 35416).

## Strategy: Heading to the Pokémon League
- Plan:
  1. Obtain gift Dratini from Dragon Clan Elder in Dragon Shrine (Dragon's Den). [Completed Turn 35678]
  2. Level XENON (Haunter) to 45+. [Started Turn 35480, 5:30 PM]
  3. Level Ouroboros (Dratini) and evolve to Dragonite. [Started Turn 35684]
  4. Replace ICARUS (Pidgey) and Ravioli (Krabby) with high-level members (e.g., Red Gyarados, Ouroboros). [Started Turn 35480, 5:30 PM]
  5. Evolve KIMCHI (Gloom) using a Sun or Leaf Stone. [Started Turn 35480, 5:30 PM, Bug Contest Started Turn 35644, 7:00 PM]
     - How: Sun Stone from Bug Contest (Tue/Thu/Sat) or Leaf Stone gift from Gina on Route 34.
  6. Surf east from New Bark Town to Route 27 and reach the Pokémon League via Victory Road. [Started Turn 35480, 5:30 PM]

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
- **Move Compatibility:** Confirmed on Turn 35663 that XENON (Haunter) and Calcifer (Typhlosion) are "NOT ABLE" to learn TM33 Ice Punch.
- **Dratini (Ouroboros):** Moves: Wrap, Thunder Wave, Twister, ExtremeSpeed. [Turn 35684]

## League Analyst Advice
- Evaluation: Team is top-heavy (Typhlosion 49, Graveler 48). Others are underleveled (Haunter 37, Dratini 15).
- Key Threats: Will's Psychic-types (outspeed/OHKO Haunter). Lance's Dragonites (lack of Ice coverage).
- Recommendations:
  - Level Ouroboros (Dratini) to Dragonite; it might learn TM33 Ice Punch (Hypothesis to be verified).
  - Level XENON (Haunter) to 45+. Teach it TM24 DragonBreath.
  - Evolve KIMCHI (Gloom) using a Sun or Leaf Stone.
  - Use Gneiss (Graveler) with Earthquake for Koga/Bruno, but avoid Bruno's Fighting-types.
- Master Ball: Obtained from Prof. Elm [Turn 35463]. Save for legendary beasts.

## Failed Hypotheses
- **Hypothesis:** Typhlosion can learn Ice Punch in Crystal. **Test:** Tried teaching TM33. **Conclusion:** Denied (Turn 35538).
- **Hypothesis:** Haunter can learn Ice Punch in Crystal. **Test:** Tried teaching TM33. **Conclusion:** Denied (Turn 35663).
- **Hypothesis:** Interacting with the elevator button at (3, 0) from (3, 1) facing up on 5F calls the elevator. **Test:** Pressed A at (3, 1) facing up. **Conclusion:** Confirmed (Turn 35558).

## Active Hypotheses
- **Hypothesis:** Dragonite can learn TM33 Ice Punch in Crystal. **Test:** Attempt to teach TM33 after evolving Ouroboros.
- **Hypothesis:** Ouroboros (Dratini) can learn TM33 Ice Punch in Crystal. **Test:** Attempt to teach TM33 now.

## Tool Maintenance
- **find_path_v2:** Refined on Turn 35646 to support Surf and Ledge transitions. [Started Turn 35646]