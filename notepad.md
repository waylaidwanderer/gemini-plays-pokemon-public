# Gem's Pokémon Crystal Adventure!

## Game Mechanics & Quirks
- **Dialogue Triggers:** Some dialogues might loop until another specific NPC in the room is spoken to (e.g., Elm's Lab).
- **Wild Encounters:** Can be triggered on 'FLOOR' tiles if they are adjacent to 'TALL_GRASS' tiles (Observed on Route 30).
- **One-Way Paths:** The gatehouse between Route 29 and Route 46 is a one-way path south.
- **Ledge Mechanics:** Can move sideways (left/right) along 'HOP_DOWN' tiles. Jumping down ledges is a one-way action.
- **Battle Text:** Can be misleading (e.g. "But it failed!" followed by a successful attack).
- **'Shadowing' NPCs:** Some NPCs follow the player onto the same tile, preventing direct interaction. They are not solid obstacles; the player can move through them, and the NPC will simply teleport to the new tile. (Observed on Route 30)

## Lessons Learned
- **Agent Refinement is Key:** Agents are not perfect on the first try. My `map_analyst` agent provided an invalid path through a bugged tile at (5, 23) on Route 30. I must update agents immediately when new mechanics or impassable tiles are discovered. Trust, but verify and refine.
- **Trust Documentation:** My own map markers and notes are reliable. The bugged tile at (5, 23) on Route 30 remained impassable even when the associated NPC sprite disappeared. I must trust my own verified findings.
- **Pivoting Strategy:** When all documented paths are confirmed blocked, I must pivot to a new hypothesis rather than repeating failed attempts. Stagnation is inefficiency.
- **World Knowledge Graph:** I MUST use `manage_world_knowledge` to record every inter-map transition immediately.
- **Softlock Solutions:** Some NPC-related softlocks can be resolved through non-obvious means, such as opening the menu, changing the lead Pokémon, or simply moving away. The 'shadowing' NPCs and dialogue loops on Route 30 were not hardlocks.
- **Verify Basic Assumptions:** My biggest mistake was assuming I was hardlocked. I must always re-verify my most fundamental assumptions (like 'can I move?') before concluding I am stuck.

## Failed Hypotheses
- **FRUIT_TREE Interaction:** The FRUIT_TREE on Route 30 at (12, 8) cannot be interacted with from any adjacent tile. The assumption that it provides a daily item is false under present conditions.

## Unverified Hypotheses
- **Mom's Healing:** Can Mom heal my Pokémon? (Test next time in New Bark Town)
- **Encounter Tables:** Do different patches of grass on the same route have different Pokémon encounters?

## Agent Ideas
- **Pokedex Agent:** Could track seen/caught Pokémon and suggest locations for finding uncaught ones.
- **Puzzle Solver Agent:** Could analyze complex environmental puzzles and NPC behavior patterns beyond simple pathfinding.

## Unverified Assumptions (To Test)
- The eastern loop on Route 30 is the *only* way north.
- The 'shadowing NPC' mechanic is just a visual quirk with no deeper gameplay purpose.
- All trainers on this route will battle on sight, with no special conditions.

- **Trust the Agent:** The `map_analyst` correctly identified that the eastern part of Route 30 is a dead-end loop, forcing me to backtrack. This confirms the agent's pathfinding is reliable and should be trusted over my own assumptions about map layout.

- **Route 30 is a one-way path from north to south.** The western path is blocked by one-way ledges, making it impossible to travel north from Cherrygrove City. My `map_analyst` agent confirmed this. I must find an alternative route to Violet City.

- **Route 46 is also a one-way path from north to south.** The ledges make it impossible to travel north from the gatehouse. All known routes to Violet City are currently blocked.