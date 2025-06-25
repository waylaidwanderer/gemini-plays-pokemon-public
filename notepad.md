# Gem's Pokémon Crystal Adventure!

## Game Mechanics & Quirks
- **Dialogue Triggers:** Some dialogues might loop until another specific NPC in the room is spoken to (e.g., Elm's Lab).
- **Wild Encounters:** Can be triggered on 'FLOOR' tiles if they are adjacent to 'TALL_GRASS' tiles (Observed on Route 30).
- **One-Way Paths:** The gatehouse between Route 29 and Route 46 is a one-way path south.
- **Ledge Mechanics:** Can move sideways (left/right) along 'HOP_DOWN' tiles. Jumping down ledges is a one-way action.
- **Battle Text:** Can be misleading (e.g. "But it failed!" followed by a successful attack).

## Lessons Learned
- **Agent Refinement:** Agents are not perfect on the first try. My `map_analyst` agent required updates after I discovered new impassable tile types. I must update agents immediately when new mechanics are discovered.
- **Trust Documentation:** My own map markers and notes are reliable. The 'bugged' trainer at (5, 23) was still there as an invisible wall, even when the sprite disappeared. I must trust my findings.
- **Pivoting Strategy:** When all documented paths are confirmed blocked, I must pivot to a new hypothesis rather than repeating failed attempts. Stagnation is inefficiency.
- **World Knowledge Graph:** I MUST use `manage_world_knowledge` to record every inter-map transition immediately.
- **Softlock Solutions:** Some NPC-related softlocks can be resolved through non-obvious means, such as opening the menu, changing the lead Pokémon, or simply moving away. The 'shadowing' Youngster on Route 30 was not a hardlock, just a persistent follower that despawned when I moved far enough away.
- **Verify Basic Assumptions:** My biggest mistake was assuming I was hardlocked. I must always re-verify my most fundamental assumptions (like 'can I move?') before concluding I am stuck.

## Unverified Hypotheses
- **Mom's Healing:** Can Mom heal my Pokémon? (Test next time in New Bark Town)
- **Daily Events:** The FRUIT_TREE on Route 30 might provide a berry daily. (Check again later)
- **Encounter Tables:** Do different patches of grass on the same route have different Pokémon encounters?
- The northern paths on Route 30 were thought to be blocked by a story trigger, but it was discovered that the 'shadowing' NPCs were the true obstacles.
- 'Shadowing' NPCs follow the player onto the same tile, preventing direct interaction. However, they are not solid obstacles; the player can move through them, and the NPC will simply teleport to the new tile.