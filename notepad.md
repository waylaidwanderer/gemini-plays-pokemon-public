# Game Mechanics & Learnings

## Navigation & Exploration
- **Mt. Moon Layout:** The southern ladder system on B1F/B2F is an isolated dead-end loop. It does not connect to the main path or the fossil trainer area. The correct path must be found by exploring the main section of Mt. Moon 1F.
- **Defeated Trainers as Obstacles:** Confirmed that defeated trainers act as impassable obstacles. This must be accounted for in all navigation.
- **Agent Reliance:** In large, unexplored mazes, systematic manual exploration (like the 'left-hand rule') is superior to pathfinding agents, which are unreliable without complete map data.

## Battle Strategy
- **Proactive Tactics:** Don't wait until HP is critical to use priority moves like Quick Attack.
- **Run Efficiency:** If running from a wild battle fails more than twice, it is more efficient to defeat the opponent, unless trying to conserve resources.
- **Risk Assessment:** Underestimated damage from a Lv. 11 Paras's Absorb. Switching in a low-level, non-resistant Pokémon is too risky for weakening wild encounters.

## Type Matchup Discoveries
- **Electric vs. Bug/Grass:** Electric-type moves (Thundershock) are 'not very effective' against Paras.

## Reminders
- Stock up on healing items like Paralyze Heals and Potions at the next Poké Mart.

## Battle Lessons
- **Trainers Have Multiple Pokémon:** Do not assume a battle is over after defeating one opponent. Wait for the victory message and prize money.
- **Type Matchup Correction:** Electric-type moves are 'not very effective' against Grass/Poison types like Oddish and Bellsprout. This is a critical distinction for this hack.

## Agent Development
- **`battle_switch_agent` Created:** To address inefficiency in battle menu navigation, I've created an agent to automate the process of switching Pokémon. This will prevent me from getting stuck in menus and wasting turns.

- **Mt. Moon 1F/B1F Loop:** The ladder at (18, 12) on 1F leads to a small, isolated section of B1F that contains a warp at (26, 10) which leads directly back to (18, 12) on 1F. This is a dead-end loop and not the path forward.