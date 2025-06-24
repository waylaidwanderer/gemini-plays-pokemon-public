# Gem's Pokémon Crystal Adventure!

## Current Mission
- **Primary Objective:** Return to Professor Elm's lab in New Bark Town with the MYSTERY EGG.

## Game Mechanics & Quirks
- **Headbutt Trees:** Some trees are 'HEADBUTT_TREE' type and are impassable.
- **Dialogue Triggers:** Some dialogues might loop until another specific NPC in the room is spoken to (e.g., Elm's Lab).
- **Wild Encounters:** Can be triggered on 'FLOOR' tiles if they are adjacent to 'TALL_GRASS' tiles. (Observed on Route 30).
- **One-Way Paths:** The gatehouse between Route 29 and Route 46 appears to be a one-way path. After exiting into Route 29, the door becomes a wall.
- **Buggy Battle:** The trainer battle with the Youngster at (5, 26) on Route 30 was buggy. It got stuck in a dialogue loop and then ended abruptly by moving my character.
- **Shifting Route:** Route 29 is a dynamic map where tiles change every few steps, requiring constant re-routing.

## Agent Performance & Lessons
- **Trust Agents:** I must trust my agents' calculations over my own intuition, especially when they suggest a counter-intuitive path.
- **Systematic Updates:** When a new game mechanic is discovered (e.g., an impassable tile type), ALL relevant agents must be updated immediately to prevent repeated errors.
- **shifty_navigator_agent:** This agent is essential for Route 29 but has limitations. It can get stuck in loops by recommending the same back-and-forth movements. Giving it an `avoid_coordinates` list helps, but it is fundamentally a single-step planner. A more advanced, multi-step planning agent is needed for complex shifting maps.

## World Knowledge & NPCs
- **New Bark Town:** A Fisher at (12, 9) mentioned Prof. Elm discovered new Pokémon.

## Unverified Assumptions & Hypotheses
- **Mom's Healing:** Can Mom heal my Pokémon?
- **Ledge Mechanics:** Are ledges in this ROM hack strictly one-way?
- **Cherrygrove Mart:** Is the Poké Mart still inaccessible?
- **Route 29 Path:** Is the only way forward east through the shifting maze, or has another path (like the one behind the CUT_TREE) become available?
- **Trap Tiles:** Is deliberately entering a 'trap' tile a viable strategy to force a favorable map shift, even when other non-backtracking moves are available?

## New Agent Ideas

## Completed Objectives & Past Events
- **Youngster Block:** The Youngster at (27, 16) on Route 29 was a temporary obstacle that moved after the Mr. Pokémon quest was initiated.

- **route_29_solver_agent Failure:** The agent's initial hypothesis that trees ('HEADBUTT_TREE', 'CUT_TREE') are passable was incorrect. My attempt to follow its path was blocked. The agent has been updated to correctly treat these tiles as impassable obstacles.

- **route_29_solver_agent Design Flaw:** The agent was fundamentally flawed as it cannot predict map shifts. It was deleted.

## Failed Strategies & Dead Ends
- **Route 29 Ledge Trap:** Jumping the ledge at (16, 11) leads to a dead end at (16, 12), where it appears I am completely trapped. This strategy is a failure.