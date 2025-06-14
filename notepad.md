# Gem's Strategic Plan & Learnings

## Operational Rules (CRITICAL)
1.  **Crisis Protocol:** When the party is in a critical state (e.g., multiple Pokémon with low HP, no healing items), the Primary Goal of reaching a safe location (like a Pokémon Center) is ABSOLUTE. No deviations for training, item collection, or optional battles are permitted.
2.  **Systematic Navigation:** In complex mazes like Viridian Forest, abandon random wandering. Adopt a systematic maze-solving algorithm (e.g., wall-following) to guarantee an exit and prevent looping.

## Current Plan
1.  Escape Viridian Forest using the 'left-hand rule' wall-following method.
2.  Proceed directly to the Pewter City Pokémon Center to heal.
3.  Do not deviate for any reason until the party is healed.

## Key Learnings
*   **Navigational Discipline:** Aimless wandering in mazes leads to resource depletion and crisis. A systematic approach is required. (Learned after getting lost for >50 turns).
*   **Strategic Discipline:** Adhere to the Crisis Protocol. Risking a critically injured party for low-value objectives (like EXP from a wild Kakuna) is an unacceptable error.
*   **Agent Reliability:** The `pathfinding_agent` is unreliable in complex, enclosed maps like Viridian Forest. Do not use it for intra-maze navigation here. Manual, systematic methods are superior.

*   **Agent Redundancy:** The `maze_solver_agent` is redundant with the `pathfinding_agent`. Instead of creating new agents for similar tasks, I should refine and improve existing ones. Future task: consolidate these two agents.
*   **Tool Utilization:** I need to remember to use the agents I've already created, like the `pre_adventure_checker_agent`, in their intended scenarios. Forgetting to use my own tools is a major oversight.

### World Clues
*   A Gentleman in the Pewter City Pokémon Center mentioned that **Team Rocket is at Mt. Moon**.