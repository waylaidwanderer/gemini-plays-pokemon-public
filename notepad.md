# I. Core Principles & Lessons Learned
- **Immediate Maintenance is Paramount:** I must be vigilant in performing maintenance tasks (notepad, agents, tools) immediately. Deferring them is a critical process failure.
- **Agent Trust is Mandatory:** I MUST trust my custom agents' advice, even if it contradicts my own intuition. Their purpose is to perform complex reasoning I cannot. If an agent is wrong, I must refine it, not ignore it.
- **Tool Trust is Mandatory:** My `pathfinder` tool wasn't broken; my understanding of the map was. I assumed the tool was failing because it didn't match my visual interpretation. **Lesson:** Trust the tool's output over visual inspection, as it reads the ground-truth map data.
- **Disprove Hypotheses:** I must actively try to prove my own assumptions wrong, not just seek confirmation. When I thought my pathfinder was broken, I should have tested the hypothesis "What if the tool is right and I'm wrong?" This would have revealed I was trapped much sooner.

# II. Game Mechanics & Battle Intel

## A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls, except for Pikachu.
- **Grass:** Walkable tiles where wild Pokémon can be encountered.
- **Water:** Surfable tiles. To initiate SURF, I must be **facing the water** on a `ground` or `steps` tile and then use the move from the party menu.
- **Ledges:** One-way only. Can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Spinner Tiles:** Force movement in a specific direction. 
- **Warp Tiles:** Instantaneous teleporters between maps or within the same map. Must step off and back on to reuse.
- **Hole Tiles:** One-way warps that cause the player to fall to the floor below, often into isolated areas.
- **Steps:** Allows vertical movement between `ground` and `elevated_ground` tiles.
- **Elevated Ground:** Walkable ground at a different elevation, accessible only via `steps`.
- **Cuttable:** A tree that can be cut with HM Cut. Becomes `ground` after cutting.
- **Secret Switches:** Some statues contain hidden switches. Activating them can toggle the state of nearby gates, opening new paths. 
- **Positional Triggers:** Specific tiles that, when stepped on, can open or close gates or trigger other events elsewhere on the map. 
- **Gate Offscreen/Closed/Open:** Gates whose state (unknown, impassable, or passable) depends on whether they are on-screen and whether a controlling switch has been activated.
- **Scripted Event Tiles:** Some tiles trigger events. The tile in front of the Cinnabar Gym door (19, 5) pushes the player back and displays a 'locked' message. The water on Seafoam Islands B4F has a scripted current that prevents surfing south.
- **Hidden Passages:** Some maps contain hidden passages that allow traversal through what appear to be solid walls.
- **Invisible Barriers:** Some areas contain invisible, impassable barriers that are not tied to a specific tile type.

## B. Confirmed ROM Hack Changes
### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground
- **Immunities:** Flying-type immune to Ground-type moves; Ground-type Pokémon are immune to Electric-type moves; MUK immune to Poison-type moves; HYPNO immune to STUN SPORE (powder moves); MUK immune to THUNDER WAVE (Electric-type status move).

### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts.
- **'No Will to Fight':** A fainted or sleeping Pokémon cannot be switched into battle.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.
- **Gym Battle Loss:** Losing a battle inside a gym does NOT warp you to a Pokémon Center.
- **Run from Battle Mechanic:** Attempting to switch Pokémon from the party screen can sometimes result in running from the battle instead.
- **FLY in battle:** The move FLY can be used to defeat a wild Pokémon and end the battle, even when indoors. This acts as an escape method.
- **ROAR in battle:** Can end a wild battle by forcing the player's Pokémon to run away.
- **'Passing the Turn':** When the goal is to lose a battle, my battle strategist agent's advice to 'pass the turn' means using the *least effective* action possible (e.g., a non-damaging move, or switching to a disadvantaged Pokemon), not simply using any attack.

# III. Active Puzzles & Solved Puzzles

## A. Pokemon Mansion - Trapped Room (Active)
- **Goal:** Escape the current isolated room in Pokemon Mansion 1F.
- **Current Situation:** I am trapped in an isolated section of 1F. All my pokemon except CRAG are fainted. The `is_in_dead_end_area` flag is true.
- **Hypothesis Log:**
  - **Hypothesis 1: Blackout Escape.** (Active) This is the only remaining viable escape method. Previous attempts failed because my Pokémon were too strong. With only CRAG left, I will try again, using my battle strategist agent to ensure I faint.
  - **Hypothesis 2: Hidden Item/Trigger.** (Failed) Walked over all tiles and used ITEMFINDER. No results.
  - **Hypothesis 3: Burn/Poison Fainting.** (Failed) Status effects do not cause HP loss outside of battle.

## B. Pokemon Mansion - Solved Puzzles
- **SECRET KEY:** The game state indicates I have all 8 badges, so the Secret Key must have been found and the Cinnabar Gym defeated. My previous notes on this were outdated.
- **1F Gate Puzzle:** The switches on 1F and 2F have a combined effect. To open the eastern gates at (25, 14), first activate the switch on 2F at (3, 12), then activate the switch on 1F at (3, 6).