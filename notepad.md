# Gem's Pokémon Crystal Knowledge Base

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
- WARP_CARPET_RIGHT/LEFT/UP/DOWN: Warp tiles at map edges. Move in the specified direction to trigger.

## Core Principles & Strategy
- **Immediate Execution:** Perform tasks the moment they are identified.
- **Scientific Method:** Observe -> Hypothesize -> Test -> Conclude.
- **Efficiency:** Running from wild battles is preferred unless training or catching.

## Menu Mechanics
- **Pokegear:** 3 clicks down from POKEDEX in the Start menu.
- **Pokegear Cards:** Map (1st), Radio (2nd), Phone (3rd). One 'Right' from Map reaches Radio.
- **Radio:** Frequency 20 (Poke Flute) is at the very top of the dial in Kanto. Requires EXPN Card upgrade.

## Battle Mechanics (Verified)
- Status Moves: Misses are reported as "The attack missed!".
- Night Shade: Deals fixed damage equal to user level.
- Psychic: Weak to Bug, Ghost, Dark.
- Ghost: Weak to Ghost, Dark. Immune to Normal, Fighting.

## Party & PC Management
- **Lead Pokémon:** Swapped Calcifer (LV58) to lead (Turn 40222).
- **HM Users:**
  - KIMCHI (GLOOM): FLASH, CUT
  - GNEISS (GRAVELER): STRENGTH
  - LAPIS (POLIWAG): SURF, WHIRLPOOL, WATERFALL
  - ICARUS (PIDGEOTTO): FLY
- **PC Box 1:** SPINARAK (13), SCYTHER (14), SEEL (24), MANTINE (20), KRABBY (22), TENTACOOL (17), KRABBY (10), DRATINI (15)

## Kanto Progression Tracking
- **Magnet Train:** Operational. TRAVEL VERIFIED.
- **EXPN Card:** Obtained from Lavender Radio Tower (Turn 40164). This is a POKEGEAR UPGRADE.
- **Snorlax Roadblock:** Route 12/11 junction. Requires Poke Flute to wake.

### Kanto Badge Tracker
- [ ] Boulder Badge (Pewter City)
- [ ] Cascade Badge (Cerulean City) - Objective: Find Misty on Route 25.
- [ ] Rainbow Badge (Celadon City)
- [ ] Soul Badge (Fuchsia City)
- [ ] Volcano Badge (Seafoam Islands)
- [ ] Earth Badge (Viridian City)

## Area Interests & Discoveries
### Route 12
- Bridge gap at (10, 13). Rows 14-15 are water. Requires Surf.
- Fisher Kyle defeated at (6, 7).
- Fishing Spot sign at (13, 9).
- Hypothesis: Can land from water onto LADDER (bridge). -> CONFIRMED (Turn 40263).
- Second Bridge gap at (10, 17). Rows 18-19 are water.
- Target: Land at (10, 20) FLOOR.

### Saffron City
- Copycat's Doll quest completed (PASS obtained). TM29 Psychic obtained.

### Route 5
- House for Sale at (10, 11). Landmark.

## General Lessons & Error Log
- **Dialogue Boxes:** Close dialogue boxes before attempting movement.
- **Ledges:** Jumping down ledges advances the player two tiles.
- **Menu Depth:** Verify cursor position and menu level before executing button sequences.
- **Surfing to Bridges:** Landing directly on a LADDER (bridge) tile from WATER is possible. (Verified Turn 40263).
- Turn 40283: Entered Route 11 from Route 12 junction. 
- Goal: Find Snorlax on Route 11 (blocking the path west).
- Plan: Move West along the corridor until Snorlax is reached. Then use Radio (Poke Flute) to wake him.
- Turn 40286: Spotted Youngster at (28, 7) on Route 11.
- Navigation: Continuing west to find Snorlax.
- Note: Snorlax should be a large sprite blocking the path. I will tune the radio ONLY when adjacent to it.