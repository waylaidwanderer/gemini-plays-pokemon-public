# Gem's Pokémon Crystal Journey

## Current Goals
- [ ] Find the missing Farfetch'd (Primary)
  - Chasing the bird. Moved North from (14, 31) to (14, 26).
- [ ] Hatch the Mystery Egg (Secondary)

## Ilex Forest
- **Farfetch'd Quest:** Found at (14, 31). Moves away when interacted with. Currently at (15, 25).
- **Geography:** Dense forest. Cut required for small trees.

## Quest Log
- **Badges:** Zephyr (Violet), Hive (Azalea).
- **Events:**
  - Defeated Rival Silver (Azalea Town).
  - Cleared Sprout Tower (Flash) & Slowpoke Well.
  - Defeated Leader Bugsy.
  - Paprika evolved into Quilava.
  - Received Mystery Egg.

## Game Mechanics
- Saving Money: Mom saves a portion of winnings.
- COUNTER: Impassable object. Interact from the front to speak with NPCs behind it.
- LADDER: Warps between floors.
- FLOOR_UP_WALL: Context-dependent. Acts as a ramp (climbable South->North) and ridge (walkable horizontally) in Union Cave.
- Accuracy Debuffs: Verified effective survival tactic against strong opponents (e.g. Silver's Croconaw).

## Strategy Notes
- Team Strategy: Paprika (Quilava) is the carry. Basalt (Geodude) needs training.
- Tactics: Smokescreen vs physical attackers/type disadvantages.
- Protocol: Mark NPCs immediately.

## Lessons Learned
- Record new Pokémon discoveries immediately, even during battle.
- Always verify object existence before interacting.
- **NPC Interaction:** Use `stun_npc` on moving NPCs to ensure successful interaction.
- **Smokescreen Survival:** Against stronger/type-advantaged opponents, stacking accuracy debuffs is a verified survival strategy.

## Route 33
- Geography: Short route connecting Union Cave and Azalea Town.
- Trainers: Hiker Anthony (Geodude Lv11) - Defeated. Swapped phone numbers.

## Azalea Town & Slowpoke Well
- Status: Fully healed. Heading to Ilex Forest.
- Mission: Enter Ilex Forest.
- Note: Cleared Slowpoke Well. Received Lure Ball. Defeated Rival Silver.
- Locations: Kurt's House (9, 5), Slowpoke Well (31, 7), Pokémon Center (15, 9), Poké Mart (21, 5), Azalea Gym (10, 15).

### Azalea Gym (Cleared)
- Status: Defeated Leader Bugsy. Earned Hive Badge & TM49 (Fury Cutter).
- Strategy: Paprika (Quilava) dominated with Ember.

### Slowpoke Well B1F
- **Progress:**
  - Defeated Grunt (Entrance), Grunt (F) (13, 4), Grunt (6, 6).
  - Retrieved Super Potion (10, 3).
  - Spotted Grunt (5, 2), Slowpoke (6, 2), Boulder (3, 2).
- **Interactions:**
  - Slowpoke (7, 4): Has Mail. "Be good and look after the house. Love, Dad".
- **Navigation & Hypotheses:**
  - **Path to East:** Accessible via gap at (8, 6).
  - **FLOOR_UP_WALL (Row 2):** Verified climbable ramps (South->North). Can be traversed horizontally and jumped down from (North->South).