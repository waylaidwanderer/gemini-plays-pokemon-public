# 1. Party Composition & Strategy
- **SPARKY (Pikachu):** Electric Sweeper. Fast, good for paralysis support. Level-capped at 24.
- **SPROUT (Gloom):** Grass/Poison Utility. Good for status effects like Leech Seed and Stun Spore.
- **THISTLE (Nidoran♀):** Physical Attacker. Currently under-leveled.
- **PIP (Pidgeotto):** Flying Attacker. Currently fainted.
- **PARCH (Sandshrew):** Ground Type. Good counter for Electric types, but critically injured and under-leveled.

# 2. Game Mechanics & Insights
- **EXP Sharing:** EXP is shared among all Pokémon that participated in the battle against a single opponent's Pokémon, even if they were just switched in and out.
- **Poison Damage:** Deals 1 HP damage every 4 steps outside of battle.
- **Level Cap:** Pokémon at the level cap show a fake EXP gain message, but their EXP value does not actually change.
- **Status Cure:** Non-volatile status conditions are cured after trainer battles.
- **PC System:** 'SOMEONE's PC' is for Pokémon, 'Gem's PC' is for Items.
- **Defeated Trainers:** Remain as impassable obstacles after battle.
- **Diglett's Cave:** Connects Route 11 (Vermilion area) to Route 2 (Pewter area).
- **FLASH:** An NPC in the Diglett's Cave exit house mentioned FLASH is needed for the dark Rock Tunnel.

# 3. Type Matchup Discoveries
- **Magnemite:** Resists Flying-type moves. Hypothesis: It has a Steel type in this ROM hack.
- **Ground-types:** Appear to be immune to Paralysis from moves like Stun Spore.
- **Poison vs. Ground:** Poison-type moves (like Acid) are not very effective against Ground-types.

# 4. Critical Lessons & Risk Management
- **(FAILURE LOG):** I have repeatedly misjudged areas as dead ends, ignoring the `Reachable Unseen Tiles` list. I must trust the game state information over my own intuition. (Failed on Route 11 twice).
- **(FAILURE LOG):** I have repeatedly forgotten that defeated trainers are impassable, leading to failed pathing. (Failed on Mt. Moon B2F, Route 11).
- **(RISK ASSESSMENT):** I must use my `heal_priority_agent` *before* entering new areas to make informed decisions, not after my party is already crippled.
- **(BATTLE STRATEGY):** Avoid reckless gambles in battle, like relying on a confused Pokémon or keeping a sleeping Pokémon in against a strong attacker. Sacrificing a Pokémon for a free switch can be a valid and necessary strategy.
- **(TOOL USAGE):** Use `select_battle_option` for main battle menu choices to improve reliability. Trust agents to find paths when I am stuck.