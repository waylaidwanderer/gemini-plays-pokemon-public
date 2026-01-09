# Johto Journey - Final Phase
- Primary Goal: Challenge the Pokémon League at Indigo Plateau [Started Turn 35416, 5:00 PM]
- Secondary Goal: Participate in the Bug-Catching Contest (Thursday) [Started Turn 35644, 7:00 PM]
- Badges Obtained: 8/8 (Rising Badge obtained Turn 35416).

## Strategy: Preparing for the Elite Four
- Training: Level all active members (especially XENON and Ouroboros) to 45+ at Route 45 or Route 27.
- Coverage: Dragonite (Ouroboros) is the primary candidate for Ice-type coverage (TM33) against Lance.
- Evolution: Obtain Sun Stone from Bug-Catching Contest for KIMCHI (Gloom). [Started Turn 35644, 7:00 PM]
- Route: Surf east from New Bark Town to Route 27 once preparations are complete.
- Fast Travel: Swap Ravioli (KRABBY) for ICARUS (PIDGEY) to use Fly. [Started Turn 35704]

## Strategy: Bug-Catching Contest (Thursday)
- Goal: Obtain Sun Stone for KIMCHI (Gloom).
- Steps:
  1. Exit Dragon's Den and go to Blackthorn Pokecenter. [Done]
  2. Swap Ravioli (KRABBY) for ICARUS (PIDGEY) at the PC. [In Progress]
  3. Fly to Goldenrod City.
  4. Head north to National Park (Route 35 Gate).
  5. Participate in the contest and aim for 1st place (Sun Stone).

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
- **Move Compatibility (CRITICAL):**
  - XENON (Haunter): NOT ABLE to learn TM33 Ice Punch (Turn 35663).
  - Calcifer (Typhlosion): NOT ABLE to learn TM33 Ice Punch (Turn 35538).
  - Ouroboros (Dratini): NOT ABLE to learn TM33 Ice Punch (Turn 35691).
  - Note: Ignore League Analyst advice regarding Ice Punch compatibility for these three; in-game verification is the source of truth.

## Pokemon Info
- Ouroboros (DRATINI): Lv15. Moves: Wrap, Thunder Wave, Twister, ExtremeSpeed (Gift move). [Turn 35684]

## Failed Hypotheses
- **Hypothesis:** Typhlosion can learn Ice Punch in Crystal. **Conclusion:** Denied (Turn 35538).
- **Hypothesis:** Haunter can learn Ice Punch in Crystal. **Conclusion:** Denied (Turn 35663).
- **Hypothesis:** Ouroboros (Dratini) can learn TM33 Ice Punch in Crystal. **Conclusion:** Denied (Turn 35691).
- **Hypothesis:** Interacting with the elevator button at (3, 0) from (3, 1) facing up on 5F calls the elevator. **Conclusion:** Confirmed (Turn 35558).

## Active Hypotheses
- **Hypothesis:** Dragonite can learn TM33 Ice Punch in Crystal. **Test:** Attempt to teach TM33 after evolving Ouroboros.

## Tool Maintenance
- **find_path_v2:** Refined on Turn 35701 to treat WHIRLPOOL as traversable.