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

## Union Cave 1F
- X ATTACK: Found at (4, 2).
- Hiker Daniel (3, 6): Facing right. Battling.
- Pokefan M (11, 8): Facing down. Likely a trainer.
- Switch-training vs Daniel's Onix: Skipped. 
  - Observation: Onix is Lv11 and uses Bind. 
  - Hypothesis: Low-level trainees (Lv4-5) will faint from cumulative Bind damage or a single move before they can be switched out. 
  - Test: Observed Gneiss taking damage from Bind (approx. 1-2 per turn). 
  - Conclusion: The risk of losing a teammate is too high; Gneiss will finish the battle solo to ensure safety.
## Lessons Learned
- Ledge Mechanics: LEDGE_HOP_DOWN tiles can only be traversed from north to south. Attempting to move 'Up' onto one from the south will fail.
- Marker Hygiene: Always verify and delete redundant or outdated markers (e.g., 'Trainer' vs 'Defeated') to maintain map clarity.
- Battle Risk Assessment: High-defense opponents with multi-turn moves (like Bind) are poor targets for switch-training low-level Pokémon. Lead with a heavy hitter to minimize risk.