# Gem's Pokémon Crystal Adventure!

## Game Mechanics & Quirks
- **Dialogue Triggers:** Some dialogues might loop until another specific NPC in the room is spoken to (e.g., Elm's Lab).
- **Wild Encounters:** Can be triggered on 'FLOOR' tiles if they are adjacent to 'TALL_GRASS' tiles (Observed on Route 30).
- **One-Way Paths:** The gatehouse between Route 29 and Route 46 is a one-way path south.
- **Ledge Mechanics:** Can move sideways (left/right) along 'HOP_DOWN' tiles.
- **Battle Text:** Can be misleading (e.g. "But it failed!" followed by a successful attack).

## Lessons Learned
- **Agent Input Integrity:** I must ensure all data provided to agents (like Pokémon movesets) is 100% accurate to the current game state.
- **Systematic Updates:** When a new game mechanic or impassable tile type is discovered, ALL relevant agents must be updated immediately.
- **Unresponsive UI:** If an input fails repeatedly (like the nickname screen), I must change my approach (e.g., selecting 'END') rather than repeating the same failed action.
- **World Knowledge Graph:** I MUST use `manage_world_knowledge` to record every inter-map transition (warps, map edges) immediately after it occurs. This is critical for building a complete and accurate map of the world.

## Agent Refinement Plan
- **`pathfinder_pro` Consolidation:** The `pathfinder_pro` agent is redundant with `map_analyst`. The plan is to merge its robust, code-based pathfinding capabilities directly into `map_analyst`. Once `map_analyst` is updated to handle pathfinding, `pathfinder_pro` will be deleted to streamline my toolset.

## Unverified Hypotheses
- **Mom's Healing:** Can Mom heal my Pokémon? (Test next time in New Bark Town)
- **Daily Events:** The FRUIT_TREE on Route 30 might provide a berry daily. (Check again later)
- **Encounter Tables:** Do different patches of grass on the same route have different Pokémon encounters?
- **Route 30 Progression:** The Bug Catcher at (5, 23) was glitched. It seems I am gated from progressing to Violet City until I deliver the MYSTERY EGG to Professor Elm.

## Future Plans & Strategy
- **Deliver MYSTERY EGG:** My primary goal is to deliver the MYSTERY EGG to Professor Elm in New Bark Town. This likely unlocks the path to Violet City.
- **HM Moves:** 'CUT_TREE' and 'HEADBUTT_TREE' tiles are currently impassable but might be cleared with the respective HMs.

## Glitched Battles
- Stepping on specific tiles on Route 30, like (7, 49) or in the grass at (6, 26), can trigger battles on a glitched map with ID 0_0. This has been confirmed to change the map ID temporarily.