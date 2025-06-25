# Gem's Pokémon Crystal Adventure!

## Game Mechanics & Quirks
- **Dialogue Triggers:** Some dialogues might loop until another specific NPC in the room is spoken to (e.g., Elm's Lab).
- **Wild Encounters:** Can be triggered on 'FLOOR' tiles if they are adjacent to 'TALL_GRASS' tiles (Observed on Route 30).
- **One-Way Paths:** The gatehouse between Route 29 and Route 46 is a one-way path south.
- **Ledge Mechanics:** Can move sideways (left/right) along 'HOP_DOWN' tiles.
- **Battle Text:** Can be misleading (e.g. "But it failed!" followed by a successful attack).
- **Glitched Battles:** Stepping on specific tiles can trigger battles in a glitched 'Unknown' map (ID: 0_0). Observed on Route 30 at (7, 49) and during the battle with Youngster Joey at (3, 28).

## Lessons Learned & Agent Performance
- **Agent Input Integrity:** I must ensure all data provided to agents (like Pokémon movesets) is 100% accurate to the current game state. A faulty input will lead to a faulty output. I hallucinated that Hearth knew Ember, which caused an error.
- **Systematic Updates:** When a new game mechanic or impassable tile type is discovered, ALL relevant agents must be updated immediately.
- **Unresponsive UI:** If an input fails repeatedly (like the nickname screen), I must change my approach (e.g., selecting 'END') rather than repeating the same failed action.

## Unverified Hypotheses
- **Mom's Healing:** Can Mom heal my Pokémon? (Test next time in New Bark Town)
- **Daily Events:** The FRUIT_TREE on Route 30 might provide a berry daily. (Check again later)

## Future Plans & Strategy
- **Violet City Gym Strategy:** My current team is the best option. Lead with Hearth (Cyndaquil) to overpower the Flying-type Pokémon.
- **HM Moves:** 'CUT_TREE' and 'HEADBUTT_TREE' tiles are currently impassable but might be cleared with the respective HMs.