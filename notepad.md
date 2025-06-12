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
- **Secondary:** Go to Oak's Lab as Professor Oak is looking for me.
- **Tertiary:** Re-evaluate exploration of Player's House 2F after visiting Oak.

## Strategy Notes & Lessons Learned
- **World Knowledge Graph (WKG):**
    - `add_node` operation: Payload should NOT include an `id` field; it is auto-generated.
    - Record transitions (map changes) immediately.
- **Map Markers:**
    - Mark used warps on both entry and exit tiles immediately.
    - Mark defeated trainers.
    - Mark strategic points, interaction loops, and dead ends.
- **Reflection (Turn 50):** Repeatedly failed `manage_world_knowledge` due to incorrect payload for `add_node`. Must read tool docs carefully. Need to start using map markers and update notepad more proactively.
- **Reflection (Turn 153):**
    - Misidentified Rival's House as Oak's Lab, costing turns. Pay closer attention to map data and dialogue.
    - Repetitive interactions with non-progressing objects/NPCs (Oak's Lab Poké Ball, BLAZe) are inefficient. Switch strategies faster.
    - Systematically explore all interaction points before repeating failed attempts.

## Tile Types Discovered
- (To be populated as new types are encountered and understood)

## Type Matchup Discoveries
- Ghost-type is super effective against Psychic-types (Source: Oak's Lab Scientist 1).
- Poison-type is super effective against Bug-types. Bug-type is no longer super effective against Poison-types. (Source: Oak's Lab Girl at (2,9)).

## Defeated Trainers
- (Format: [Trainer Name] - [Map Name] at (X,Y))

## Key Discoveries & Item Locations
- Player's House Second Floor: PC at (1,2).
- Pallet Town:
    - PALLETTOWN_GIRL NPC at (3,11).
    - PALLETTOWN_PLAYERSHOUSE_SIGN at (4,6).
    - PALLETTOWN_SIGN at (8,10).
    - Rival's House entrance (Warp): (14,6).
    - PALLETTOWN_RIVALSHOUSE_SIGN at (12,6).
    - Oak's Lab entrance (Warp): (13,12). Leads to Oak's Lab (map_id 40) at (5,12) or (6,12).
- Rival's House:
    - Spoke to Daisy at (3,4). She said BLAZe is at Grandpa's lab.
    - Obtained Town Map from Rival's House at (4,4) after talking to Daisy.
- Oak's Lab:
    - Poké Ball at (8,4) results in an interaction loop ("That's a POKé BALL. There's a POKéMON inside!"). Not a starter.
    - BLAZe at (5,4) results in an interaction loop ("Yo Gem! Gramps isn't around!...").
    - Scientist 1 at (3,11) provides type matchup info (Ghost > Psychic).

## Future Agent Ideas
- **Strategic Advisor Agent:** Analyzes upcoming challenges (e.g., Gym Leaders), suggests team compositions/strategies based on known data. Requires code execution.

- Poison-type is super effective against Bug-types. Bug-type is no longer super effective against Poison-types. (Source: Oak's Lab Girl at (2,9))

- Scientist 2 at (9,11) repeated Scientist 1's dialogue (Ghost > Psychic).

## Oak's Lab Exhaustion (Turn 178)
- Interacted with OAKSLAB_POKEDEX2 at (4,2): "It's encyclopedia-like, but the pages are blank!". Same as POKEDEX1.
- All interactable objects in Oak's Lab have now been checked (Rival, Poké Ball, 3 NPCs, 2 Pokédexes) without obtaining a Pokémon. 
- Hypothesis: The trigger for obtaining a starter Pokémon is not a direct interaction with a static object in Oak's Lab as it currently is. It may require leaving the lab, Professor Oak returning, or another event occurring in Pallet Town.

## Pallet Town Exploration (Post-Oak's Lab Attempt 1)
- Interacted with PALLETTOWN_SIGN at (8,10): "PALLET TOWN - Shades of your journey await!". No event triggered.
- Next step: Investigate the warp at (6,6) (Player's House entrance). Game state lists it as `num_visits: 0`, which is inconsistent with WKG. This is a priority.

## Player's House Exploration (Turn 191)
- Entered Player's House. No immediate Pokémon event triggered.
- The warp at (6,6) in Pallet Town (Player's House entrance) showed `num_visits: 0` before use. This seems to be a display characteristic for entry warps, as the WKG connection was correct and the warp worked. The discrepancy is considered resolved.
- New secondary goal: Explore Player's House (both floors) for event triggers or Pokémon.
- New tertiary goal: Interact with Mom on the first floor.