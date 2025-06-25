# Gem's Pokémon Crystal Adventure!

## Game Mechanics & Quirks
- **Dialogue Triggers:** Some dialogues might loop until another specific NPC in the room is spoken to (e.g., Elm's Lab).
- **Wild Encounters:** Can be triggered on 'FLOOR' tiles if they are adjacent to 'TALL_GRASS' tiles (Observed on Route 30).
- **One-Way Paths:** The gatehouse between Route 29 and Route 46 is a one-way path south.
- **Ledge Mechanics:** Can move sideways (left/right) along 'HOP_DOWN' tiles. Jumping down ledges is a one-way action.
- **Battle Text:** Can be misleading (e.g. "But it failed!" followed by a successful attack).
- **Glitched Battles:** Stepping on specific tiles on Route 30 can trigger battles on a glitched map with ID 0_0.
- **Bugged NPCs:** The Youngster at (5, 23) on Route 30 is bugged and will trap the player in a dialogue loop, making him impassable.

## Lessons Learned
- **Agent Input Integrity:** I must ensure all data provided to agents (like Pokémon movesets) is 100% accurate to the current game state.
- **Systematic Updates:** When a new game mechanic or impassable tile type is discovered, ALL relevant agents must be updated immediately.
- **Unresponsive UI:** If an input fails repeatedly (like the nickname screen), I must change my approach (e.g., selecting 'END') rather than repeating the same failed action.
- **World Knowledge Graph:** I MUST use `manage_world_knowledge` to record every inter-map transition (warps, map edges) immediately after it occurs.
- **Pathfinding:** Always use the `map_analyst` agent to verify a path before attempting to traverse it, especially in complex areas with ledges or potential dead ends. Jumping down ledges without a confirmed exit is a recipe for getting trapped.

## Unverified Hypotheses
- **Mom's Healing:** Can Mom heal my Pokémon? (Test next time in New Bark Town)
- **Daily Events:** The FRUIT_TREE on Route 30 might provide a berry daily. (Check again later)
- **Encounter Tables:** Do different patches of grass on the same route have different Pokémon encounters?

## Future Plans & Strategy
- **Primary Goal:** Defeat the Violet City Gym Leader and earn the Zephyr Badge.
- **Secondary Goal:** Find an alternate route to Violet City, as Route 30 is a one-way trap from the north.
- **HM Moves:** 'CUT_TREE' and 'HEADBUTT_TREE' tiles are currently impassable but might be cleared with the respective HMs.