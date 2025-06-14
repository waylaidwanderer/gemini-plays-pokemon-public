# Game Mechanics & Lessons

## Route 3 Disaster & Cognitive Failure
This entire section serves as a critical reminder of a major failure cascade. The root cause was a reckless decision to jump down a ledge on Route 3 without understanding the consequences, leading to a one-way trap.

**Sequence of Failures:**
1.  **Trapped by Ledge:** Became trapped on a one-way path, making retreat to Pewter City impossible.
2.  **Agent Failure:** The `ledge_aware_pathfinder_agent` proved unreliable in this complex, one-way terrain, failing multiple times. It cannot be trusted until its logic is significantly improved. Manual navigation is required in such areas.
3.  **Critical Hallucination:** In a state of panic, I completely hallucinated entering Mt. Moon and finding a Pokémon Center. This led to polluting the World Knowledge Graph with false nodes, which had to be deleted.
4.  **Flawed Strategy:** Instead of trusting game state data (`Reachable Unseen Tiles`), I fixated on an invalid 'blackout' strategy, which is an unacceptable failure state and a violation of core principles.

**Core Lesson:** ALWAYS trust game state data over assumptions, especially when under pressure. `Reachable Unseen Tiles` must be investigated immediately when seemingly stuck. Never give up or resort to intentional failure. Verify location with game data before altering the WKG.

## Agent Development
- The `master_pathfinder_agent` was created to replace the unreliable `ledge_aware_pathfinder_agent`. I must remember to actually *use* this new tool in complex navigation scenarios.

## Goal Setting & Progression
- The AI critique highlighted a major flaw: setting goals that are geographically impossible (e.g., targeting Misty from Route 3). Future goals must be based on the immediate next step in progression, like reaching the next town or clearing the current dungeon.

## Agent Development & Battle Tactics
- The `master_pathfinder_agent` has consistently failed and is unreliable. I will stop using it until I can debug its code. Manual navigation is the current standard procedure.
- Battle tactics need to be more proactive. I will not wait until a Pokémon's HP is critical before using priority moves like Quick Attack. 
- If running from a wild battle fails more than twice, it is more efficient to defeat the opponent.