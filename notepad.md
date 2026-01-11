## Tile Mechanics (Global)
- FLOOR: Traversable. Standard collision.
- WALL: Impassable.
- WATER: Traversable with HM Surf.
- TALL_GRASS: Traversable, triggers wild encounters.
- DOOR/WARP: Step on to enter buildings/areas.
- LEDGE_HOP_DOWN: One-way traversal (North to South).
- COUNTER: Impassable Wall. Interact from adjacent tile.
- STAIRCASE: Warp tile that transitions between floors.
- LADDER: Traversable. Used for bridges on Route 12.
- WARP_PANEL: Teleports player between rooms. Interaction is immediate upon entry.
- WARP_CARPET_RIGHT: Warp tile at map edge. Move Right to trigger.
- WARP_CARPET_LEFT: Warp tile at map edge. Move Left to trigger.
- WARP_CARPET_UP: Warp tile at map edge. Move Up to trigger.
- WARP_CARPET_DOWN: Warp tile at map edge. Move Down to trigger.

## Core Principles & Strategy
- **Immediate Execution:** Tasks are performed the moment they are identified.
- **Scientific Method:** Observe -> Hypothesize -> Test -> Conclude.
- **Falsification:** Actively try to disprove hypotheses.
- **Root Assumption Audit:** If a complex strategy fails, re-verify the base assumption.

## Battle Mechanics (Verified)
- Status Moves: Misses are reported as "The attack missed!".
- Night Shade: Deals fixed damage equal to user level.
- Type Effectiveness (Psychic): Weak to Bug, Ghost, Dark.
- Type Effectiveness (Ghost): Weak to Ghost, Dark. Immune to Normal, Fighting.

## PC Storage (Box 1)
- SPINARAK (13), SCYTHER (14), SEEL (24), MANTINE (20), KRABBY (22), TENTACOOL (17), KRABBY (10), DRATINI (15)

## Movesets (HM Users)
- KIMCHI (GLOOM): FLASH, CUT
- GNEISS (GRAVELER): STRENGTH
- LAPIS (POLIWAG): SURF, WHIRLPOOL, WATERFALL
- ICARUS (PIDGEOTTO): FLY

## Machine Part Investigation (Resolved)
- **Conclusion (Turn 40086):** The Power Plant quest is confirmed complete. The Magnet Train is operational. Travel between regions is verified.

## General Lessons
- **Data Integrity:** Context Summaries and Inventory are the absolute sources of truth.
- **Pokegear Upgrades:** The EXPN Card is a Pokegear upgrade, not a physical item in the Bag. Verify by checking the Radio for the Poke Flute channel (top of the dial).
- **Warp Carpets:** At map edges, moving "off" the map triggers the warp.
- **Ledges:** Jumping down ledges (LEDGE_HOP_DOWN) advances the player two tiles south.
- **Custom Tool Hygiene:** Always use `find_path_v4_fixed` and `strategy_advisor_v2`.
- **Moving NPCs:** NPCs can block paths dynamically. Use `stun_npc` to freeze them or navigate around.
- **Tile Collision Assumptions:** Do not assume all tiles of the same visual type (e.g., floor patterns) have identical collision without testing.

## Kanto Progression Plan (Started Turn 40091, Jan 10, 2026)
1. Return to Saffron City via Magnet Train. (COMPLETED Turn 40104)
2. Obtain EXPN Card from Lavender Radio Tower. (COMPLETED Turn 40164)
3. Wake up Snorlax on Route 11. (Started Turn 40169)
   - Location: Route 11 (East of Vermilion City).
   - Method: Use Pokegear Radio, tune to Poke Flute channel (top of the dial).
4. Go to Route 25 (North of Cerulean) to find Misty and earn the Cascade Badge.
5. Explore southern Kanto (Fuchsia City, etc.).

## Saffron City Interests
- **Mr. Psychic:** Obtained TM29 Psychic (Turn 39946).
- **Copycat:** Reward for returning her doll is the PASS (already in inventory).

## Route 5 Interests
- **House for Sale:** Located at (10, 11). Landmark.
## Kanto Badge Tracker
- [ ] Boulder Badge (Pewter City)
- [ ] Cascade Badge (Cerulean City) - Goal 4
- [ ] Rainbow Badge (Celadon City)
- [ ] Soul Badge (Fuchsia City) - Goal 5
- [ ] Volcano Badge (Seafoam Islands)
- [ ] Earth Badge (Viridian City)