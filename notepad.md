# Pokémon Yellow Legacy - Hard Mode Notes

## Game Mechanics & Rules
- Battle Style: Set
- No items in battle.
- HMs can be forgotten, used from menu, not storable in PC.
- All 151 Pokémon obtainable.
- Trade evolutions by level (e.g., Haunter -> Gengar at 42, Machoke -> Machamp at 38).
- Smarter Trainer AI with anti-sweep tactics.
- Tougher boss fights.
- Dynamic scaling for Gyms 4-6.
- EXP. All obtainable without special requirements.
- Poisoned Pokémon lose 1 HP every 4 steps outside battle.

## Level Caps
- 0 badges: 12
- 1 badge: 21
- 2 badges: 24
- 3 badges: 35
- 4 badges: 43
- 5 badges: 50
- 6 badges: 53
- 7 badges: 55
- 8 badges: 57
- After Lorelei: 58
- After Bruno: 59
- After Agatha: 62
- After Lance: 65

## Current Goals & Plans
- **Primary:** Obtain my first Pokémon.
- **Secondary:** Explore Pallet Town to find Professor Oak's Lab.
- **Tertiary:** Identify and interact with all characters in Pallet Town.

## Tile Types Discovered
- (To be populated as new types are encountered and understood)

## Defeated Trainers
- (Format: [Trainer Name] - [Map Name] at (X,Y))

## Item Locations & Key Objects
- Player's House Second Floor: PC at (1,2).

## General Notes & Discoveries
- 

## Strategy Notes & Lessons Learned
- **World Knowledge Graph (WKG):** 
    - `add_node` operation: Payload should NOT include an `id` field; it is auto-generated.
    - Record transitions (map changes) immediately.
- **Map Markers:** 
    - Mark used warps on both entry and exit tiles immediately.
    - Mark defeated trainers.
    - Mark strategic points and dead ends.
- **Agent Ideas:**
    - Route planning agent using WKG (future).
    - Pokémon matchup analyzer (future).
- **Reflection (Turn 50):** Repeatedly failed `manage_world_knowledge` due to incorrect payload for `add_node`. Must read tool docs carefully. Need to start using map markers and update notepad more proactively.

## Pallet Town Exploration Notes
- Player's House 1F: Stairs to 2F at (8,2).
- Player's House 2F: Stairs to 1F at (8,2).

## Pallet Town Exploration Notes (Continued)
- Player's House Entrance/Exit (Warp): (6,6) on Pallet Town map.
- PALLETTOWN_GIRL NPC located at (3,11).
- PALLETTOWN_PLAYERSHOUSE_SIGN at (4,6).
- PALLETTOWN_SIGN at (8,10).

- Professor Oak's Lab entrance (Warp): (14,6) on Pallet Town map.
- PALLETTOWN_RIVALSHOUSE_SIGN at (12,6).

## Rival's House Notes
- Spoke to Daisy at (3,4). She said BLAZe is at Grandpa's lab.
- Obtained Town Map from (4,4).