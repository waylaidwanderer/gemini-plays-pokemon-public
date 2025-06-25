# Gem's Pokémon Crystal Adventure!

## Game Mechanics & Quirks
- **Headbutt Trees:** Some trees are 'HEADBUTT_TREE' type and are impassable.
- **Dialogue Triggers:** Some dialogues might loop until another specific NPC in the room is spoken to (e.g., Elm's Lab).
- **Wild Encounters:** Can be triggered on 'FLOOR' tiles if they are adjacent to 'TALL_GRASS' tiles. (Observed on Route 30).
- **One-Way Paths:** The gatehouse between Route 29 and Route 46 appears to be a one-way path.
- **Ledge Mechanics:** I can move sideways (left/right) along 'HOP_DOWN' tiles.
- **Shifting Mazes:** Some routes can have dynamically changing layouts, requiring careful navigation.
- **Battle Text:** Sometimes battle text can be misleading (e.g. "But it failed!" followed by a successful attack).
- **Glitched Battles:** Stepping on specific tiles can trigger battles in a glitched 'Unknown' map (ID: 0_0). Observed on Route 30 at (7, 49) and during the battle with Youngster Joey at (3, 28).

## Agent Performance & Lessons
- **Trust Agents:** I must trust my agents' calculations over my own intuition. However, if an agent's output is based on faulty information (like a hallucinated moveset), I must correct the agent before proceeding.
- **Systematic Updates:** When a new game mechanic or impassable tile type is discovered, ALL relevant agents must be updated immediately.
- **Unresponsive UI:** The nickname screen taught me a valuable lesson. If an input fails repeatedly, I must change my approach (e.g., selecting 'END') rather than repeating the same failed action. It's a UI/input issue, not a game-breaking bug.

## Unverified Assumptions & Hypotheses
- **Mom's Healing:** Can Mom heal my Pokémon? (Test next time in New Bark Town)
- **Party Composition:** My current team might not be optimal. I should check for Rock-type Pokémon and use the `team_strategist` agent for analysis.
- **Daily Events:** The FRUIT_TREE on Route 30 might provide a berry daily. I need to check it again later.

## Actionable Plans
- Explore the northern part of Route 30 to find better training spots or unfought trainers.
- Retrieve the hidden Potion at (14, 9) on Route 30.