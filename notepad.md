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
- **Secondary:** Trigger the starter Pokémon event by attempting to leave Pallet Town to the North (towards Route 1).
- **Tertiary:** If attempting to leave town does not trigger the event, systematically explore all `Reachable Unseen Tiles` in Pallet Town.

## Strategy Notes & Lessons Learned
- **World Knowledge Graph (WKG):** Record transitions (map changes) immediately. `add_node` payload should NOT include an `id`.
- **Map Markers:** Mark used warps (entry/exit), defeated trainers, strategic points, interaction loops, dead ends, and static info signs.
- **Interaction Strategy:** Avoid repeating interactions with objects/NPCs in confirmed loops without a new trigger.
- **Default vs. Event Locations:** During events, interactions might be required at default sprite locations, not visual event locations.
- **Notepad `replace` Action:** Must use the exact current text from the notepad for `old_text`. Game suggestions for `old_text` can be outdated and unreliable.
- **Event Triggers:** Prioritize common Pokémon game event triggers (e.g., attempting to leave the starting town) when other interactions fail or lead to loops.
- **Path Planning:** Consult Map Memory more carefully to identify obstacles. Use `pathfinding_agent` cautiously.

## Tile Types Discovered
- **ground**: Walkable tile.
- **impassable**: Walls, objects, bookcases, etc. Cannot be entered or traversed.
- **warp**: Tile that initiates a map transition. Rules for activation vary.
- **water**: Requires Surf to cross.

## Type Matchup Discoveries
- Ghost-type > Psychic-type.
- Poison-type > Bug-type; Bug-type !> Poison-type.

## Defeated Trainers
(Format: [Trainer Name] - [Map Name] at (X,Y))

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
- **Oak's Lab Notes (Map ID 40):**
    - **Initial State Interactions:**
        - Poké Ball (default location (8,4)) results in loop: "That's a POKé BALL...".
        - BLAZe (default location (5,4)) results in loop: "Yo Gem! Gramps isn't around!...".
        - Scientist 1 (OAKSLAB_SCIENTIST1) at (3,11): Ghost > Psychic.
        - Girl (OAKSLAB_GIRL) at (2,10): Poison > Bug; Bug !> Poison.
        - Scientist 2 (OAKSLAB_SCIENTIST2) at (9,11): Repeated Ghost > Psychic.
        - Pokédexes at (3,2) & (4,2): "pages are blank!".
    - **Event State Interactions (Triggered by Mom's dialogue & re-entering lab):**
        - Visual event sprites: Professor Oak (visually at (2,9)), BLAZe (visually at (3,11)), event Poké Ball (visually at (2,11)).
        - Professor Oak (visual (2,9), sprite OAKSLAB_GIRL at (2,9)) in dialogue loop: Poison > Bug.
        - Scientist (Oak's Aide, visually at (3,11), sprite OAKSLAB_SCIENTIST1 at (3,11)) in dialogue loop: Ghost > Psychic. Triggered by trying to interact with event BLAZe.
        - Event Poké Ball (visual (2,11)) unresponsive to interaction from adjacent tiles or while standing on it.
        - Exiting and re-entering Oak's Lab did NOT reset the event state.
    - **Return to Default Location Interactions (Post-Event State Loops):**
        - Interacted with default Poké Ball (Item ID 2) at (8,4): "BALL. There's a POKéMON inside!". Supported hypothesis about default locations.
        - BLAZe (OAKSLAB_RIVAL) at default location (5,4) after Poké Ball interaction: "Yo Gem! Gramps isn't around! I ran here 'cos he said he had a POKéMON for me."
        - Re-interacted with default Poké Ball at (8,4) after BLAZe's dialogue. Still says "BALL. There's a POKéMON inside!". Sprite facings changed. Poké Ball at (8,4) is likely BLAZe's.
        - Professor Oak not at default location (5,8). Lab appeared in default configuration.
        - Exiting Oak's Lab did not trigger Oak's appearance in Pallet Town.
- **Player's House First Floor (Map ID 37):**
    - Mom (PLAYERSHOUSE1F_MOM) at (6,5) said: "Right. All kids leave home someday. It said so on TV. PROF.OAK, next door, is looking for you." (Key trigger for Oak's Lab event).

## Future Agent Ideas
(No specific agent ideas at this moment. Focus on core gameplay and reliable manual strategies first.)