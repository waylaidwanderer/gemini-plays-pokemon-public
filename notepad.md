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
- **Secondary:** Interact with BLAZe at (3,11) in Oak's Lab (event state).
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
- **ground**: Walkable tile.
- **impassable**: Walls, objects, bookcases, etc. Cannot be entered or traversed.
- **warp**: Tile that initiates a map transition. Rules for activation vary (e.g., step-on for 1x1, step-on then move into boundary for 2x1).

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
(No specific ideas at the moment)

- Oak's Lab (Event State):
    - Professor Oak at (2,9) confirmed: Poison > Bug; Bug !> Poison.

- Oak's Lab (Event State):
    - Attempted to interact with event Poké Ball at (2,11) by standing on it and pressing A (facing Down). No text appeared. Hypothesis: Interaction may require being adjacent to the Poké Ball and facing it, or another NPC interaction is needed first.

- Oak's Lab (Event State):
    - Attempted to move Up from (2,11) to (2,10) (adjacent to event Poké Ball, Girl at (2,10) on screen) but was blocked. New plan: move to (1,11) (left of Poké Ball), then face Right and interact.

- Oak's Lab (Event State):
    - Scientist (Oak's Aide, visually at (3,11) but listed as OAKSLAB_SCIENTIST1 at (3,11) in default game state) at (3,11) spoke when I tried to interact with event Poké Ball from (1,11): "I study POKéMON as PROF.OAK's AIDE. We recently finished a paper proving a rumor false. As thought, the rare ghost-type is super effective to psychic-types."
    - Attempted interactions with event Poké Ball at (2,11) from multiple adjacent tiles and while standing on it have failed. It's likely not directly interactable or requires another trigger.

- Oak's Lab (Event State):
    - Scientist (Oak's Aide, visually at (3,11)) at (3,11) is in an interaction loop, repeating Ghost > Psychic dialogue. Interacting with BLAZe at (3,11) also triggers this.
    - Event Poké Ball at (2,11) is unresponsive to interaction from adjacent tiles or while standing on it.
    - Next target: Professor Oak (visually at (2,9)).

- Oak's Lab (Event State):
    - Professor Oak (visually at (2,9), sprite OAKSLAB_GIRL) is in an interaction loop, repeating type matchup dialogue (Poison > Bug, Bug !> Poison).

- Oak's Lab (Event State):
    - Exiting and re-entering Oak's Lab did NOT reset the event state. Professor Oak remains in a dialogue loop.

- Oak's Lab (Event State):
    - Scientist (Oak's Aide, visually at (3,11)) at (3,11) is in an interaction loop, repeating Ghost > Psychic dialogue. Interacting with BLAZe at (3,11) also triggers this.
    - New Hypothesis: Event progression might require interacting with NPCs/objects at their *default* map locations (e.g., BLAZe at (5,4), Poké Ball at (8,4)) rather than their visual event locations.

## Reflection (Turn 256)
- **Oak's Lab Event Summary:** Interactions with visual event sprites (Oak at (2,9), Scientist at (3,11), event Poké Ball at (2,11)) resulted in dialogue loops or no response. Exiting and re-entering Oak's Lab did not reset the event state. Successfully interacted with the *default* Poké Ball (Item ID 2) at (8,4), which triggered the dialogue "BALL. There's a POKéMON inside!". This strongly supports the hypothesis that event progression requires interacting with objects/NPCs at their standard, non-event map positions as listed in the `Map Sprites` data.
- **Agent Usage Reflection:** The `pathfinding_agent` should have been utilized for navigating the complex and obstacle-laden interior of Oak's Lab, especially when attempting to reach the default Poké Ball location. Future complex indoor navigation will prioritize its use to prevent wasted turns from being blocked.
- **Hypothesis Generation & Event Mechanics:** When encountering event-altered environments where initial interactions with visually apparent event sprites fail or loop, the hypothesis to test interactions with *default* NPC/object locations (as per `Map Sprites` list) should be formed and tested more rapidly. Spending excessive turns on unresponsive or looping event elements is inefficient.
- **Loop Avoidance Strategy:** Must maintain stricter discipline in avoiding re-interaction with NPCs or objects that have been confirmed to be in dialogue or interaction loops. Mark them and move on to other hypotheses or targets.

## Future Agent Ideas
- **Battle Strategy Agent:** Could be defined to analyze upcoming significant battles (e.g., Rival, Gym Leaders). Input would include player's party, known opponent Pokémon/levels, and current level cap. Output could suggest optimal move choices, switch strategies, or identify key threats/weaknesses. Would likely require `run_code` capability for type matchup calculations and strategic analysis based on Hard Mode rules.

- Oak's Lab (Event State):
    - BLAZe (OAKSLAB_RIVAL) at default location (5,4) said: "Yo Gem! Gramps isn't around! I ran here 'cos he said he had a POKéMON for me."
    - This interaction supports the hypothesis that event progression requires interacting with objects/NPCs at their default map locations.

- Oak's Lab (Event State):
    - Re-interacted with default Poké Ball at (8,4) after BLAZe's dialogue. Still says "BALL. There's a POKéMON inside!". Sprite facing for BLAZe (5,4) changed to Up, and Poké Ball (8,4) changed to Left. This Poké Ball is likely BLAZe's.

- Oak's Lab (Default State):
    - Checked Professor Oak's default location (5,8). He is not present. The lab appears to be in its default configuration (no event NPCs visible on screen at event locations).

- Oak's Lab (Default State):
    - Default Poké Ball at (8,4) still says "There's a POKéMON inside!" after BLAZe's dialogue loop. Likely BLAZe's Pokémon.
    - Professor Oak not at default location (5,8). Lab appears to be in default visual configuration.

- Pallet Town (After exiting Oak's Lab):
    - Exiting Oak's Lab did not immediately trigger Professor Oak's appearance or any other event in Pallet Town. Hypothesis to revisit Player's House for further clues.