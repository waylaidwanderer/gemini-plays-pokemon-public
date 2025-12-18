# Johto Journey: Gem's Log

## Global Tile Mechanics (Verified)
- FLOOR: Traversable. Standard ground.
- WALL / FLOOR_UP_WALL: Impassable collision.
- TALL_GRASS: Traversable. Triggers wild Pokémon encounters.
- LEDGE_HOP_DOWN: One-way traversal (South).
- LEDGE_HOP_RIGHT: One-way traversal (East).
- LEDGE_HOP_UP: Impassable.
- COUNTER: Impassable. Stand in front to interact with NPCs behind (Nurses, Clerks).
- HEADBUTT_TREE: Impassable.
- CUT_TREE: Impassable. Requires CUT.
- WARP_CARPET: Map transition at edges or building entrances.
- LADDER / DOOR / CAVE: Instant warp upon entry.
- PC / BOOKSHELF / RADIO / SIGN: Interactable from an adjacent tile (usually below for PC/Bookshelf).
- WATER / ROCK / INCENSE_BURNER / MART_SHELF: Impassable.

## Gym Progress
- Zephyr Badge: Obtained from Falkner.

## NPC Archive - Route 32
- Fisher (15, 13): Eastern path.
- Fisher (19, 14): Eastern path. Likely near water.
- Fisher (6, 48): Eastern path docks.
- Fisher (8, 49): Eastern path docks.
- Fisher (7, 70): Slowpoketail Scam. Declined ¥1,000,000 offer.

## Training Strategy
- Switch Training: Lead with a strong Pokémon (e.g., Gneiss or Calcifer) and immediately switch to a lower-level Pokémon (e.g., Rocky, Egg, Apophis) on Turn 1 of a battle. This splits EXP and ensures safety.

## Route Documentation
- Route 32: Traveled from Violet City south along the western path. The path is divided by water and walls from an eastern section.
- Union Cave 1F: Entered from Route 32 (6, 79). Exploring the western tunnel system.
- Old Rod: Obtained from Fishing Guru in Route 32 Pokémon Center.
- Navigation Method: Following the western path of Route 32 south leads directly to the Union Cave entrance. Inside the cave, prioritizing the exploration of western tunnels before proceeding south.

## Union Cave 1F
- X ATTACK: Found at (4, 2).
- Hiker Daniel (3, 6): Facing right. Defeated. Gneiss reached Lv15.
- Hiker Russell (11, 8): Facing down. Battling.
- Switch-training vs Daniel's Onix: Skipped. 
  - Observation: Onix is Lv11 and uses Bind. 
  - Hypothesis: Low-level trainees (Lv4-5) will faint from cumulative Bind damage (1/16 max HP per turn) or a single move before they can be safely switched out. 
  - Test: Observed Gneiss taking damage from Bind (1 HP per turn at Lv15). For a Lv4-5 Pokémon with ~16-19 HP, 2-3 turns of Bind plus one direct hit would be fatal.
  - Conclusion: The risk of fainting is too high; Gneiss must finish the battle solo to ensure team safety.
## Lessons Learned
- Ledge Mechanics: LEDGE_HOP_DOWN tiles can only be traversed from north to south. Attempting to move 'Up' onto one from the south will fail.
- Marker Hygiene: Always verify and delete redundant or outdated markers (e.g., 'Trainer' vs 'Defeated') to maintain map clarity.
- Battle Risk Assessment: High-defense opponents with multi-turn moves (like Bind) are poor targets for switch-training low-level Pokémon. Lead with a heavy hitter to minimize risk.
- Mystery Egg: Occupies party slot 5. Verified that it cannot battle (Game message: "An EGG can't battle!").
- Switch Training Analysis: High-defense opponents or those with multi-turn/passive damage moves (e.g., Onix with Bind) are unsuitable for switch-training low-level trainees (Lv4-5). The cumulative damage from moves like Bind (1/16 HP per turn) plus potential direct hits makes the risk of fainting too high before the switch-out can be completed.