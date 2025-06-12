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
    - Mark interacted signs/objects that provide static info.
- **Reflection (Turn 50):** Repeatedly failed `manage_world_knowledge` due to incorrect payload for `add_node`. Must read tool docs carefully. Need to start using map markers and update notepad more proactively.
- **Reflection (Turn 153):**
    - Misidentified Rival's House as Oak's Lab, costing turns. Pay closer attention to map data and dialogue.
    - Repetitive interactions with non-progressing objects/NPCs (Oak's Lab Poké Ball, BLAZe) are inefficient. Switch strategies faster.
    - Systematically explore all interaction points before repeating failed attempts.
- **Reflection (Turn 205):**
    - **Navigation:** Pallet Town navigation was inefficient due to not carefully checking map memory for obstacles (fences, signs). This cost multiple turns (e.g., reaching Player's House, Oak's Lab). Plan paths more carefully or use the `pathfinding_agent`.
    - **Tool Usage:** Ensure exactness with `old_text` for `notepad_edit`'s "replace" action.
    - **Agent Usage:** Could have used `pathfinding_agent` for recent tricky navigation in Pallet Town.
    - **Interaction Strategy:** Avoid repeating interactions with objects/NPCs that result in loops (e.g., Oak's Lab Poké Ball, BLAZe) without first exploring all other options.

## Tile Types Discovered
- (To be populated as new types are encountered and understood)

## Type Matchup Discoveries
- Ghost-type is super effective against Psychic-types. (Source: Oak's Lab Scientist 1 at (3,11) & Scientist 2 at (9,11))
- Poison-type is super effective against Bug-types. Bug-type is no longer super effective against Poison-types. (Source: Oak's Lab Girl at (2,10))

## Defeated Trainers
- (Format: [Trainer Name] - [Map Name] at (X,Y))

## Key Discoveries & Event Chronology
- **Player's House Second Floor (Map ID 38):** PC at (1,2).
- **Pallet Town (Map ID 0):**
    - PALLETTOWN_PLAYERSHOUSE_SIGN at (4,6) interacted: "PLAYER's HOUSE".
    - PALLETTOWN_SIGN at (8,10) interacted: "PALLET TOWN - Shades of your journey await!".
    - Rival's House entrance (Warp): (14,6). Leads to Rival's House (Map ID 39).
    - Oak's Lab entrance (Warp): (13,12). Leads to Oak's Lab (Map ID 40).
- **Rival's House (Map ID 39):**
    - Spoke to Daisy at (3,4). She said BLAZe is at Grandpa's lab.
    - Obtained Town Map from Rival's House at (4,4) after talking to Daisy.
- **Oak's Lab (Map ID 40):**
    - Poké Ball at (8,4) results in an interaction loop ("That's a POKé BALL..."). Not a starter.
    - BLAZe (OAKSLAB_RIVAL) at (5,4) results in an interaction loop ("Yo Gem! Gramps isn't around!...).
    - Scientist 1 (OAKSLAB_SCIENTIST1) at (3,11): Ghost > Psychic.
    - Girl (OAKSLAB_GIRL) at (2,10): Poison > Bug; Bug !> Poison.
    - Scientist 2 (OAKSLAB_SCIENTIST2) at (9,11): Repeated Ghost > Psychic.
    - Pokédexes at (3,2) & (4,2) (OAKSLAB_POKEDEX1, OAKSLAB_POKEDEX2): "pages are blank!".
    - Conclusion: Starter Pokémon trigger is not a static object/NPC interaction in the lab's initial state.
- **Player's House First Floor (Map ID 37):**
    - Mom (PLAYERSHOUSE1F_MOM) at (6,5) said: "Right. All kids leave home someday. It said so on TV. PROF.OAK, next door, is looking for you." This is the current lead.
- **Warp Visit Counts:** `num_visits: 0` for an entry warp in Game State seems to be a display characteristic and doesn't mean it's truly unvisited if WKG indicates prior use.

## Future Agent Ideas
- **Strategic Advisor Agent:** Analyzes upcoming challenges (e.g., Gym Leaders), suggests team compositions/strategies based on known data. Requires code execution.