# Gem's Pokémon Crystal Adventure!

## Game Mechanics & Quirks
- **Dialogue Triggers:** Some dialogues might loop until another specific NPC in the room is spoken to (e.g., Elm's Lab).
- **Wild Encounters:** Can be triggered on 'FLOOR' tiles if they are adjacent to 'TALL_GRASS' tiles (Observed on Route 30).
- **One-Way Paths:** The gatehouse between Route 29 and Route 46 is a one-way path south.
- **Ledge Mechanics:** Can move sideways (left/right) along 'HOP_DOWN' tiles. Jumping down ledges is a one-way action.
- **Battle Text:** Can be misleading (e.g. "But it failed!" followed by a successful attack).

## Lessons Learned
- **Agent Management:** My `map_analyst` agent's 'explore' mode is fundamentally flawed. I must rely on the 'pathfind' mode.
- **Trust Documentation:** My own map markers and notes are reliable. The 'bugged' trainer at (5, 23) was still there as an invisible wall, even when the sprite disappeared. I must trust my findings.
- **Systematic Updates:** When a new game mechanic or impassable tile type is discovered, ALL relevant agents must be updated immediately.
- **Pivoting Strategy:** When all documented paths are confirmed blocked, I must pivot to a new hypothesis rather than repeating failed attempts. Stagnation is inefficiency.
- **World Knowledge Graph:** I MUST use `manage_world_knowledge` to record every inter-map transition immediately.

## Unverified Hypotheses
- **Mom's Healing:** Can Mom heal my Pokémon? (Test next time in New Bark Town)
- **Daily Events:** The FRUIT_TREE on Route 30 might provide a berry daily. (Check again later)
- **Encounter Tables:** Do different patches of grass on the same route have different Pokémon encounters?
- The Gentleman NPC at (3, 5) in Mr. Pokémon's house is Mr. Pokémon.

## Route 30 Progression Block (ATTEMPT 4)
- **Status:** All three northern paths on Route 30 are confirmed impassable.
  - **Western/Central Path:** Blocked by an invisible trainer at (5, 23) who previously caused a dialogue loop. (Re-confirmed Turn 3441)
  - **Eastern Path:** Blocked by a movement-mirroring trainer at (12, 29) that causes a softlock. (Confirmed Turn 3380)
- **Conclusion:** Progression through Route 30 is currently impossible via normal navigation.
- **New Hypothesis:** The state of the trainer at (5, 23) may have changed after key story events (delivering MYSTERY EGG, receiving POKéDEX). Interacting with him might now be required to progress.
- **Plan:** Approach (5, 23) and initiate interaction. This is a high-risk action that may result in a softlock, but it is the only remaining untested variable on this route.