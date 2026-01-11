## Tile Mechanics (Global)
- FLOOR: Traversable. Standard collision.
- WALL: Impassable.
- WATER: Traversable with HM Surf.
- TALL_GRASS: Traversable, triggers wild encounters.
- DOOR/WARP: Step on to enter buildings/areas.
- LEDGE_HOP_DOWN: One-way traversal (North to South).
- COUNTER: Impassable Wall. Interact from adjacent tile.
- STAIRCASE: Warp tile that transitions between floors.
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
- **Conclusion (Turn 40086):** The Power Plant quest is confirmed complete. The Magnet Train is operational, as verified by the Officer's prompt to board. Possession of the PASS and the restored power allows travel between Saffron and Goldenrod.

## General Lessons
- **Data Integrity:** Context Summaries and Inventory are the absolute sources of truth. Prioritize them over transient "pings" or personal memory.
- **Itemfinder (Crystal):** "Nope!" means no item is within search range (~4 tiles). A ping means an item is within range.
- **Custom Tool Limitation:** `find_path_v4` may not account for moving NPCs that were off-screen when the map was last seen. Manual correction may be required.

## Kanto Progression Plan (Started Turn 40091, Jan 10, 2026)
1. Return to Saffron City via Magnet Train. (COMPLETED Turn 40104)
2. Go to Lavender Town and verify EXPN Card status at the Radio Tower. (Started Turn 40115) If not possessed, speak to Station Manager (9, 1) again.
3. Go to Route 25 (North of Cerulean) to find Misty and earn the Cascade Badge.
4. Use the Poke Flute channel (Radio) to wake up Snorlax on Route 11 to access southern Kanto (Route 12-15, Fuchsia City).

## Saffron City Interests
- **Mr. Psychic:** Obtained TM29 Psychic (Turn 39946).
- **Copycat:** Reward for returning her doll is the PASS (already in inventory).

## Route 5 Interests
- **House for Sale:** Located at (10, 11). Landmark.
## Reflection (Turn 40118)
1. **Immediate Execution:** No deferred tasks identified.
2. **Notepad Hygiene:** Added "Tile Mechanics" and "Time Tracking" in recent turns. Sections are organized.
3. **Map Hygiene:** Markers for Route 8 are up to date.
4. **Automation Strategy:** Refined `find_path_v4` usage; `strategy_advisor` used to verify Kanto goals.
5. **Goal Clarity:** Goals are outcome-focused.
6. **Error Analysis:** Documented `find_path_v4` limitation regarding moving NPCs. Verified warp carpet mechanics at map edges.

## General Lessons (Update)
- **Warp Carpets:** At map edges, moving "off" the map (e.g., Right into a WALL at (39, 22)) triggers the warp.
- **Ledges:** Jumping down ledges (LEDGE_HOP_DOWN) is a scripted movement that advances the player two tiles south.
- **Custom Tool Failures:** If `find_path_v4` returns null or fails, it may be due to the destination being an "impassable" tile (like an unseen tile or NPC). Target an adjacent walkable tile instead.