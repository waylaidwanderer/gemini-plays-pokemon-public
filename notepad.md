# Gem's Gameplay Log & Strategies

## 1. Game Mechanics & Lessons Learned
*   **Source of Truth:** The `Map Sprites` list is the definitive source for interactable items.
*   **NPC Interaction:** Repeatedly talking to an NPC with static dialogue is a waste of time. Some key events are triggered by advancing through ALL of an NPC's dialogue.
*   **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
*   **Warp Mechanics:** It's possible to move between 'ground' and 'elevated_ground' tiles if one of the tiles is a warp.
*   **Mobile NPCs:** For evasive NPCs that move around, use the `stun_npc` tool to freeze them in place before attempting to interact or battle. Chasing them is inefficient.
*   **Defeated Trainers as Obstacles:** This is NOT a universal rule. While the Rocket Grunt on Mt. Moon B2F at (16, 23) became a permanent blocker, other defeated trainers are passable. Must be verified on a case-by-case basis.

## 2. Battle & Pokémon Intel
*   **Battle Tactics:** Ground-types appear to be immune to the poison status effect. Low accuracy moves should be avoided.
*   **Type Weaknesses (Verified):
    *   Zubat (Poison/Flying): Weak to Electric, Ice, Psychic, Rock.
    *   Geodude (Rock/Ground): 4x weak to Grass/Water.
    *   Sandshrew (Ground): Weak to Water, Grass, Ice. Immune to Poison status.
    *   Paras (Bug/Grass): 4x weak to Fire/Flying.

## 3. Area Notes
### Route 4 (ID: 15)
*   The Cool Trainer F is extremely mobile. Attempting to battle her near (7, 6) or (8, 5) can trigger what appears to be a bugged phantom encounter.

## 4. Custom Agent Log
*   **Pathfinding Agent:** Unreliable in complex, multi-level dungeons like Mt. Moon. Its pathing logic does not handle verticality well and can lead to inefficient routes or loops. Manual navigation or the `dungeon_navigator_agent` should be used instead in these areas.
*   **npc_movement_predictor_agent:** Created to predict the movement patterns of mobile NPCs, helping to intercept them for battles or interactions.
*   **systematic_explorer_agent:** Its traversal logic is flawed in Mt. Moon and cannot be trusted. It has failed by generating paths into impassable walls. Requires refinement.

## 5. Lessons from Critiques
*   **Abandon Failing Objectives:** If an objective (especially an optional one) proves unproductive after a few well-documented attempts, disengage immediately. The primary goal of progression is paramount.
*   **Systematic Navigation:** When navigating complex dungeons, avoid trying to force shortcuts. Adopt a methodical exploration pattern (like wall-following) to prevent getting lost in loops.
*   **Agent Refinement:** A failing agent should be refined immediately rather than being used again without changes. Note failures and then fix them.

*   **Commit to Exploration:** When arriving in a new, unexplored map area, explore it thoroughly before backtracking. Immediately returning to a previous map is counter-productive and leads to loops. Trust that new areas contain the path forward.

## 6. Critical Lessons from Major Failures
*   **Mt. Moon Western Maze Fiasco:** I became completely stuck in the western, isolated sections of Mt. Moon (1F/B1F/B2F). The core error was strategic, not technical. I refused to accept that the area was a dead end and instead got trapped in a loop of trying to 'fix' my agents to find a non-existent path. **Lesson:** When multiple tools and exploration attempts confirm an area is isolated, TRUST THE DATA. The problem is the strategy, not the tool. Abandon the dead end and backtrack to the last known promising location. Do not waste time on tool refinement as a form of procrastination.

## 6. Critical Lessons from Major Failures
*   **Mt. Moon Western Maze Fiasco:** I became completely stuck in the western, isolated sections of Mt. Moon (1F/B1F/B2F). The core error was strategic, not technical. I refused to accept that the area was a dead end and instead got trapped in a loop of trying to 'fix' my agents to find a non-existent path. **Lesson:** When multiple tools and exploration attempts confirm an area is isolated, TRUST THE DATA. The problem is the strategy, not the tool. Abandon the dead end and backtrack to the last known promising location. Do not waste time on tool refinement as a form of procrastination.