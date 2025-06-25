# Gem's Pokémon Crystal Adventure!

## Game Mechanics & Quirks
- **Dialogue Triggers:** Some dialogues might loop until another specific NPC in the room is spoken to (e.g., Elm's Lab).
- **Wild Encounters:** Can be triggered on 'FLOOR' tiles if they are adjacent to 'TALL_GRASS' tiles (Observed on Route 30).
- **One-Way Paths:** The gatehouse between Route 29 and Route 46 is a one-way path south.
- **Ledge Mechanics:** Can move sideways (left/right) along 'HOP_DOWN' tiles.
- **Battle Text:** Can be misleading (e.g. "But it failed!" followed by a successful attack).

## Lessons Learned & Agent Performance
- **Agent Input Integrity:** I must ensure all data provided to agents (like Pokémon movesets) is 100% accurate to the current game state.
- **Systematic Updates:** When a new game mechanic or impassable tile type is discovered, ALL relevant agents must be updated immediately.
- **Unresponsive UI:** If an input fails repeatedly (like the nickname screen), I must change my approach (e.g., selecting 'END') rather than repeating the same failed action.
- **World Knowledge Graph:** I MUST use `manage_world_knowledge` to record every inter-map transition (warps, map edges) immediately after it occurs. This is critical for building a complete and accurate map of the world.
- **Pathfinding Logic:** The eastern path on Route 30 is a dead end. The western path is also a dead end blocked by ledges. The correct path must be through the central area, past the Bug Catcher.

## Agent Refinement Plan
- **`path_navigator` Failures (DELETED):** This agent repeatedly failed to path around NPCs and walls, even after multiple prompt revisions. It has been deleted. A new, more robust navigation agent, `pathfinder_pro`, needs to be designed. This new agent MUST use its code tool to explicitly parse the XML for `<Object>` and `<WALL>` tags in its generated path and verify their absence before outputting a solution.
- **`map_analyst` Development:** I should integrate pathfinding and soft-lock detection capabilities into the `map_analyst` agent to create a single, powerful tool for map analysis. This will consolidate functionality and avoid redundancy.

## Unverified Hypotheses
- **Mom's Healing:** Can Mom heal my Pokémon? (Test next time in New Bark Town)
- **Daily Events:** The FRUIT_TREE on Route 30 might provide a berry daily. (Check again later)
- **Encounter Tables:** Do different patches of grass on the same route have different Pokémon encounters?
- **Route 30 Progression:** The Bug Catcher at (5, 23) is glitched and blocking the only known path forward. Hypothesis: Leaving the map and returning might reset his state.

## Future Plans & Strategy
- **Violet City Gym Strategy:** My current team is the best option. Lead with Hearth (Cyndaquil) to overpower the Flying-type Pokémon.
- **HM Moves:** 'CUT_TREE' and 'HEADBUTT_TREE' tiles are currently impassable but might be cleared with the respective HMs.

## Glitched Battles
- Stepping on specific tiles on Route 30, like (7, 49) or in the grass at (6, 26), can trigger battles on a glitched map with ID 0_0. This has been confirmed to change the map ID temporarily.