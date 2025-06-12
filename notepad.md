# Pokémon Yellow Legacy - Hard Mode Notes (Gem's Log)

## Current Status
- Location: Viridian City (Map ID 1) at (18,11).
- Badges: 0
- Level Cap: 12

## Active Pokémon Party
1. SPARKY (PIKACHU): Lv7 (26/26 HP, EXP: 442/512 to Lv8) | Moves: THUNDERSHOCK, GROWL, QUICK ATTACK

## Current Objectives & Plans
- **Primary:** Defeat Brock, the Pewter City Gym Leader.
  - *Plan:* Locate Pewter City (likely north of Viridian, through Viridian Forest). Train SPARKY towards Lv12 cap. Acquire more Pokémon once Poké Balls are obtained.
- **Secondary:** Acquire Poké Balls from Viridian City's Poké Mart.
  - *Plan:* Systematically explore Viridian City, prioritizing unvisited warps and unseen areas that might house the Poké Mart.
- **Tertiary:** Explore Viridian City for other items, information, and trainers.
  - *Plan:* Interact with reachable NPCs and objects. Battle available trainers if encountered (none so far in Viridian).

## Game Mechanics & Rules Summary
- Battle Style: Set. No items in battle.
- HMs: Forgettable, menu-use, not PC-storable.
- All 151 Pokémon obtainable. Trade evos by level.
- Smarter AI, tougher bosses, dynamic gym scaling (4-6).
- EXP. All obtainable without special requirements.
- Poison: 1 HP lost per 4 steps outside battle.
- STAT Experience: Significant stat boosts from battling/leveling, enemies don't get this. (Source: Youngster, Route 1)
- Enemy Trainer PP: Unlimited. (Source: Sign, Viridian City)
- PC Log Off: Saves game.
- CUT: Bug-type HM. (Source: Girl, Viridian School House)
- Evolution: By training, no trading needed. (Source: Little Girl, Viridian School House)
- Status Conditions (from School Blackboard):
  - SLP: No attack, persists. Cure: AWAKENING.
  - BRN: Power down, damage, persists. Cure: BURN HEAL.
  - PSN: HP drop, persists. Cure: ANTIDOTE.
  - FRZ: Immobile, persists. Cure: ICE HEAL.
  - PAR: Misfire chance, persists. Cure: PARLYZ HEAL.

## Discovered Tile Types & Movement Rules
- **ground**: Walkable.
- **impassable**: Walls, objects, etc. Not traversable.
- **warp**: Map transition. Activation varies (instant 1x1, or 2-step for larger).
- **water**: Requires Surf.
- **grass**: Wild encounters.
- **ledge**: Jump down only.
- **NPC Blocking**: Cannot move onto a tile occupied by a stationary NPC if it's the first step of a path from pathfinder. (Hypothesis - Attempt 1, Turn 649, Balding Guy in Nickname House). If an NPC is directly adjacent in the path and player isn't facing them, first press turns, second *may* move if NPC is not a hard blocker.
- **Pikachu Movement**: If Pikachu is adjacent in movement direction & player not facing him, 2 presses needed (1st turns, 2nd moves). Normal otherwise.
- **PC Interaction**: Stand below, face up, press A.

## Type Matchup Discoveries
- Ghost > Psychic.
- Poison > Bug; Bug !> Poison.

## Key NPCs & Trainers Log
(Format: [Name/Type] - [Map] (X,Y) - Outcome/Info)
- Youngster - Route 1 (6,26) - Gave Potion.
- Youngster - Route 1 (16,14) - Explained STAT Experience.
- Girl (Brunette) - Viridian School (4,6) - CUT is Bug HM.
- Girl (Little) - Viridian School (5,6) - Pokémon evolve by training.
- Cooltrainer F - Viridian School (5,2) - Advised reading blackboard.
- Girl - Viridian City (18,10) - "Grandpa needs coffee." (Re: Old Man at (19,10)).
- Old Man - Viridian City (19,10) - Blocks path N. "Private property!" Pushed player back. (Attempt 1 to pass).
- Balding Guy - Viridian Nickname House (6,4) - Nickname advice.

## Agent Development & Performance
### Defined Agents:
1.  **route_pathfinder**: Calculates move sequence. Input: {start_x, start_y, end_x, end_y}. Output: {path_found, steps[]}. (Code-enabled)
2.  **exploration_prioritizer_agent**: Suggests exploration target. Input: {player_x, player_y, current_objectives}. Output: {prioritized_target_type, target_coordinates, reasoning}. (Code-enabled)

### Planned Agents:
-   `item_finder_agent`: Locates items/buildings or suggests paths to them.
-   `npc_interaction_strategist_agent`: Analyzes NPCs for interaction strategies.
-   `team_builder_agent`: Suggests team comps for challenges.
-   `level_grinding_optimizer_agent`: Identifies optimal training spots.

### Agent Failures & Notes:
-   **route_pathfinder**:
    -   Turn 477 (Route 1): Failed (Agent LLM resp missing content).
    -   Turn 649 (Nickname House): Path (Up, Up, Left, Left, Left, Down) from (6,5) to (3,4) failed. First 'Up' to (6,4) blocked by Balding Guy. Prompt needs to consider NPCs as obstacles.
-   **exploration_prioritizer_agent**:
    -   Turn 534 (Viridian): Suggested Pokécenter after exiting. Unhelpful.
    -   Turn 621 (Viridian): Suggested Pokécenter again after exiting. Unhelpful. Prompt needs significant refinement to avoid recently used/explored locations.

## Lessons Learned & Strategy Refinements
-   **WKG**: Record transitions immediately. Use descriptive names/tags. Verify entry points.
-   **Map Markers**: Mark used warps, defeated/info NPCs, key points, obstacles, static signs. Use distinct emojis.
-   **Interaction**: Avoid repeated interactions if first attempt yields no new info/progress. Mark loops.
-   **NPCs**: Can block paths unexpectedly. Be prepared to reroute or use `stun_npc` if essential.
-   **Efficiency**: Avoid excessive time in optional areas if main goals are pending (e.g., Nickname House). Plan longer movement sequences instead of single steps for exploration.