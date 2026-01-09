# Johto Journey - Final Phase
- Primary Goal: Challenge the Pokémon League at Indigo Plateau [Started Turn 35416, 5:00 PM]
- Secondary Goal: Participate in the Bug-Catching Contest (Thursday) [Started Turn 35644, 7:00 PM]
- Badges Obtained: 8/8 (Rising Badge obtained Turn 35416).

## Strategy: Preparing for the Elite Four
- Training: Level all active members (especially XENON and Ouroboros) to 45+.
- Coverage: Dragonite (Ouroboros) is the primary candidate for Ice-type coverage (TM33) against Lance.
- Evolution: Obtain Sun Stone from Bug-Catching Contest for KIMCHI (Gloom).
- Route: Surf east from New Bark Town to Route 27 once preparations are complete.

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
- **Move Compatibility:** Confirmed on Turn 35663 that XENON (Haunter) and Calcifer (Typhlosion) are "NOT ABLE" to learn TM33 Ice Punch. Dratini (Ouroboros) is also "NOT ABLE" (Turn 35691).

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
- **Hypothesis:** Ouroboros (Dratini) can learn TM33 Ice Punch in Crystal. **Test:** Attempted to teach TM33 on Turn 35691. **Conclusion:** Denied.
- **Hypothesis:** Interacting with the elevator button at (3, 0) from (3, 1) facing up on 5F calls the elevator. **Test:** Pressed A at (3, 1) facing up. **Conclusion:** Confirmed (Turn 35558).

## Active Hypotheses
- **Hypothesis:** Dragonite can learn TM33 Ice Punch in Crystal. **Test:** Attempt to teach TM33 after evolving Ouroboros.

## Tool Maintenance
- **find_path_v2:** Refined on Turn 35701 to treat WHIRLPOOL as traversable.