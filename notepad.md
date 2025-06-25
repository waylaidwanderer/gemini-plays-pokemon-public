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
- **Agent Management:** My `map_analyst` agent's 'explore' mode is fundamentally flawed and should not be used. After three redefinitions, it repeatedly identified an unreachable tile `(5, 19)` as a valid target. I must rely on the 'pathfind' mode.
- **Agent Input Integrity:** I must ensure all data provided to agents (like Pokémon movesets) is 100% accurate to the current game state.
- **Systematic Updates:** When a new game mechanic or impassable tile type is discovered, ALL relevant agents must be updated immediately.
- **Unresponsive UI:** If an input fails repeatedly (like the nickname screen), I must change my approach (e.g., selecting 'END') rather than repeating the same failed action.
- **World Knowledge Graph:** I MUST use `manage_world_knowledge` to record every inter-map transition (warps, map edges) immediately after it occurs.
- **Pathfinding:** Always use the `map_analyst` 'pathfind' mode to verify a path before attempting to traverse it, especially in complex areas with ledges or potential dead ends.
- **Puzzle Triggers & Dead Ends:**
    - A looping NPC dialogue might indicate an external trigger is needed.
    - After extensive testing on Route 30, I've confirmed the western path is blocked (impassable trees, bugged NPC) and the puzzle in Mr. Pokémon's house is unsolvable with my current capabilities. This area is a dead end for now, requiring me to backtrack.

## Unverified Hypotheses
- **Mom's Healing:** Can Mom heal my Pokémon? (Test next time in New Bark Town)
- **Daily Events:** The FRUIT_TREE on Route 30 might provide a berry daily. (Check again later)
- **Encounter Tables:** Do different patches of grass on the same route have different Pokémon encounters?
- The Gentleman NPC at (3, 5) in Mr. Pokémon's house is Mr. Pokémon.

## Live Encounter Notes
- Turn 3331: Interrupted by a wild Hoppip on Route 30 while backtracking.

- **Route 30 Eastern Path Blocked:** The Youngster at (12, 29) is bugged, mirroring player movement and creating an impassable softlock. This confirms all northern paths on Route 30 are currently dead ends.

## Current Plan: Finding Violet City (Attempt 3)
- **Status:** All previously explored northern paths on Route 30 have resulted in dead ends blocked by impassable trainers.
- **Hypothesis:** The central path, starting at (9, 35), is the correct route to Violet City.
- **Action:** Proceed north along this central path and document findings. Be prepared for a potential trainer battle with the Youngster at (9, 35).