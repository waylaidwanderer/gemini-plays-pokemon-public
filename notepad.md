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
- **Secondary:** Receive a starter Pokémon from Professor Oak.
- **Tertiary:** Follow Professor Oak's instructions.

## Strategy Notes & Lessons Learned
- **World Knowledge Graph (WKG):** Record transitions (map changes) immediately. `add_node` payload should NOT include an `id`. Use descriptive names and tags for nodes. Ensure `destination_entry_point` is accurate for warp edges.
- **Map Markers:** Mark used warps (entry/exit), defeated trainers, strategic points, interaction loops, dead ends, and static info signs. Use distinct emojis for clarity.
- **Interaction Strategy:** Avoid repeating interactions with objects/NPCs in confirmed loops without a new trigger. If an NPC or object is unresponsive or in a loop after 2-3 attempts, move on. Mark loops clearly.
- **Default vs. Event Locations:** During events, interactions might be required at default sprite locations, not visual event locations, or vice-versa. Test both if stuck.
- **Notepad `replace` Action:** Must use the exact current text from the notepad for `old_text`. Game suggestions for `old_text` can be outdated. Copy-paste is safest.
- **Event Triggers:** Prioritize common Pokémon game event triggers (e.g., attempting to leave the starting town, Mom's dialogue) when other interactions fail or lead to loops.
- **Path Planning:** Consult Map Memory carefully to identify obstacles (fences, impassable tiles). Plan routes to avoid known blockages. For simple maps, manual pathing is often faster than relying on agents that might fail.
- **NPC Movement:** NPCs can move and block paths. Be prepared to reroute.
- **Warp Mechanics:** 1x1 warps are usually instant. 2x1 or 1x2 warps (like exit mats) require moving onto the warp then into the boundary/direction of warp.

## Tile Types Discovered
- **ground**: Walkable tile.
- **impassable**: Walls, objects, bookcases, fences etc. Cannot be entered or traversed.
- **warp**: Tile that initiates a map transition. Rules for activation vary.
- **water**: Requires Surf to cross.
- **grass**: Tall grass where wild Pokémon encounters occur.

## Type Matchup Discoveries
- Ghost-type > Psychic-type.
- Poison-type > Bug-type; Bug-type !> Poison-type.

## Defeated Trainers
(Format: [Trainer Name] - [Map Name] at (X,Y))

## Key Discoveries & Event Chronology
- **Player's House Second Floor (Map ID 38):** PC at (1,2).
- **Pallet Town (Map ID 0):
    - PALLETTOWN_PLAYERSHOUSE_SIGN at (4,6) interacted: "PLAYER's HOUSE".
    - PALLETTOWN_SIGN at (8,10) interacted: "PALLET TOWN - Shades of your journey await!".
    - Rival's House entrance (Warp): (14,6). Leads to Rival's House (Map ID 39).
    - Oak's Lab entrance (Warp): (13,12). Leads to Oak's Lab (Map ID 40).
- **Rival's House (Map ID 39):
    - Spoke to Daisy at (3,4). She said BLAZe is at Grandpa's lab.
    - Obtained Town Map from Rival's House at (4,4) after talking to Daisy.
- **Player's House First Floor (Map ID 37):
    - Mom (PLAYERSHOUSE1F_MOM) at (6,5) said: "Right. All kids leave home someday. It said so on TV. PROF.OAK, next door, is looking for you." (Key trigger for Oak's Lab event).
- **Oak's Lab (Map ID 40) - Initial Interactions & Loops:
    - Poké Ball (default location (8,4)) initial loop: "That's a POKé BALL...".
    - BLAZe (default location (5,4)) initial loop: "Yo Gem! Gramps isn't around!...".
    - Scientist 1 (OAKSLAB_SCIENTIST1) at (3,11): Ghost > Psychic.
    - Girl (OAKSLAB_GIRL) at (2,10): Poison > Bug; Bug !> Poison.
    - Scientist 2 (OAKSLAB_SCIENTIST2) at (9,11): Repeated Ghost > Psychic.
    - Pokédexes at (3,2) & (4,2): "pages are blank!".
    - **Event State (Triggered by Mom's dialogue & re-entering lab - visual sprites different from default):**
        - Professor Oak (visually at (2,9), sprite OAKSLAB_GIRL at (2,9)) in dialogue loop: Poison > Bug.
        - Scientist (Oak's Aide, visually at (3,11), sprite OAKSLAB_SCIENTIST1 at (3,11)) in dialogue loop: Ghost > Psychic. Triggered by trying to interact with event BLAZe.
        - Event Poké Ball (visual (2,11)) unresponsive to interaction from adjacent tiles or while standing on it.
        - Exiting and re-entering Oak's Lab did NOT reset this event state.
    - **Return to Default Location Interactions (Post-Event State Loops):
        - Interacted with default Poké Ball (Item ID 2) at (8,4): "BALL. There's a POKéMON inside!". Supported hypothesis about default locations.
        - BLAZe (OAKSLAB_RIVAL) at default location (5,4) after Poké Ball interaction: "Yo Gem! Gramps isn't around! I ran here 'cos he said he had a POKéMON for me."
        - Re-interacted with default Poké Ball at (8,4) after BLAZe's dialogue. Still says "BALL. There's a POKéMON inside!". Sprite facings changed. Poké Ball at (8,4) is likely BLAZe's.
        - Professor Oak not at default location (5,8). Lab appeared in default configuration.
        - Exiting Oak's Lab did not trigger Oak's appearance in Pallet Town initially.
- **Pallet Town (Map ID 0) - Starter Event Trigger:**
    - Attempting to walk north into the grass at (11,1) (towards Route 1) triggered Professor Oak's appearance.
    - Oak's dialogue: "Hey! Wait! Don't go out!" -> "Wild POKéMON live in tall grass!" -> (Oak catches Pikachu) -> "Whew..." -> "A POKéMON can appear anytime in tall grass. You need your own POKéMON for your protection. I know! Here, come with me!"
    - Player automatically followed Oak back into Oak's Lab.

## Future Agent Ideas
(No specific agent ideas at this moment. Focus on core gameplay and reliable manual strategies first.)