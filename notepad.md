# Game Mechanics & Lessons

## Route 3 Ledge Puzzle
The primary lesson from the Route 3 disaster is to **trust game state data over visual perception.**

- **Contradiction:** The game state insisted Pewter City was `Reachable: Yes`, while my visual interpretation suggested I was trapped by ledges and impassable walls.
- **Solution:** The contradiction was resolved by using `run_code` to parse the `map_xml_string`. This revealed that tile **(16, 12)** was `type="ground"`, not `type="ledge"`, creating a hidden path back to the northern section of the route.
- **Core Principle:** When a contradiction arises between what I see and what the game data says, I must use tools to analyze the raw data to find the truth. Do not resort to panicked, brute-force exploration.

## Agent Limitations
- The `npc_aware_pathfinder_agent` proved incapable of navigating maps with complex verticality and one-way ledges. It repeatedly failed or provided invalid paths on Route 3.
- **Conclusion:** A general-purpose pathfinder is not sufficient. For complex mazes, either use direct data analysis with `run_code` or create a specialized agent with more detailed instructions on handling specific map mechanics like ledges.