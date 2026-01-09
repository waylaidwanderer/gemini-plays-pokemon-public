# Johto Journey - Final Phase

## Strategy: Preparing for the Elite Four
- Training: Level all active members (especially XENON and Ouroboros) to 45+ at Route 45 or Route 27.
- Coverage: Dragonite (Ouroboros) is the primary candidate for Ice-type coverage (TM33) against Lance.
- Evolution: Obtain Sun Stone from Bug-Catching Contest for KIMCHI (Gloom).
- Route: Surf east from New Bark Town to Route 27 once preparations are complete.
- Fast Travel: Swap Ravioli (KRABBY) for ICARUS (PIDGEY) to use Fly. [Completed Turn 35719]

## Game Mechanics: FLY Map
- Navigation: Unlike the overworld, the FLY map cursor does not always follow strict directional inputs.
- List Cycling: Pressing 'Down' cycles through visited locations in a predetermined list order.
- Outdoor Use Only: FLY can only be used when the player is outdoors.

## Area Mechanics: National Park (Bug-Catching Contest)
- Start Turn: 35788 | Start Time: 8:23 PM (Thursday)
- Rules: 20-minute time limit, 20 Park Balls provided.
- Party Restriction: Only the lead Pokémon participates; others are held by the contest helper.
- Scoring: Based on the strength and rarity of the bug Pokémon caught.
- Prizes: 1st Place awards a Sun Stone (the primary target for KIMCHI's evolution).
- Pokémon Retention: You keep only the last Pokémon caught during the contest.

## Tile Mechanics (Global)
- FLOOR: Standard traversable tile. Verified.
- GRASS: Traversable. Triggers wild encounters. Verified.
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
- Fly: Use 'Down' to cycle through cities if directional inputs fail.
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
## Battle Strategies
- Bug-Catching Contest: Use XENON's Hypnosis to put targets to sleep before throwing Park Balls. Avoid damaging low-level targets with Night Shade (fixed 37 HP damage) to prevent fainting. Verified that XENON's Night Shade deals damage equal to its level (Lv37).