# Johto Journey: Gem's Log

## Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL: Impassable boundary.
- HEADBUTT_TREE: Impassable tree; may react to Headbutt move.
- TALL_GRASS: Traversable; triggers wild battles.
- LEDGE_HOP_DOWN: One-way jump South.
- LEDGE_HOP_LEFT: One-way jump West (jumps 2 tiles).
- CAVE: Warp tile leading to an interior area.
- FLOOR_UP_WALL: Impassable; functions as a wall above a floor.
- LADDER: Warp tile; functions as stairs between floors.
- WATER: Impassable without HM03 Surf.

## Gym Progress
- Zephyr Badge: Obtained from Falkner (Violet City).
- Hive Badge: Next target (Azalea City).

## Strategy: Azalea Gym (Bug-type)
- Target: Gym Leader Bugsy.
- Team: Bug-type Pokemon (Scyther is the ace).
- Advice: Bug Pokemon are weak to Fire and Flying moves.
- Counter: Calcifer (Quilava) with Ember. Icarus (Pidgey) with Gust. Gneiss (Geodude) with Rock Throw.
- Plan:
  1. Talk to Gym Guide at (7, 13) - DONE.
  2. Defeat trainers (Twins at 4, 10 and 5, 10) - DONE.
  3. Defeat Bug Catcher Al at (8, 10) - DONE.
  4. Defeat Bug Catcher Benny at (5, 3).
  5. Explore for remaining trainers.
  6. Defeat Gym Leader Bugsy.
- Time Tracking: Exploration started at Turn 2596.

## TM/HM & Items
- HM05 FLASH: Obtained (Requires Zephyr Badge to use outside).
- TM31 MUD-SLAP: Obtained.
- Mystery Egg: Received from Elm's Aide.
- Super Potion x2: One from Mom, one from Well B1F (10, 3).
- Lure Ball: From Kurt.

## Trainer Rosters (Johto)
- Rocket Grunt (Well 1): Rattata x2 (Lv9).
- Rocket Grunt (Well 2, F): Zubat (Lv9), Ekans (Lv11).
- Rocket Grunt (Well 3): Rattata (Lv7), Zubat (Lv9) - Defeated.
- Rocket Grunt (Well 4): Koffing (Lv14) - Defeated.
- Twins Amy & May: Ledyba (Lv10), Spinarak (Lv10) - Defeated.
- Bug Catcher Al: Caterpie (Lv12), Weedle (Lv12) - Defeated.
- Bug Catcher Benny: Weedle (Lv7) - Defeated, Kakuna (Lv9) - Battling.

## Azalea Town Summary
- Slowpoke Well entrance at (31, 7).
- Charcoal Kiln at (21, 13).
- Poké Mart at (21, 5).
- Pokémon Center at (15, 9).
- Team Rocket Grunt at (31, 9): Defeated/Gone.
- Kurt's House at (9, 5). Inside: Kurt (3, 2), Granddaughter (5, 3).
- Apricorn Mechanic: Bring Apricorns to Kurt at (3, 2).

## Lessons Learned
- Always double-check map orientations and neighboring routes before making strategic claims.
- Link moving NPC markers to their object_id to ensure they track correctly.
- Verify all foundational assumptions in-game.
- Moving NPCs can block `navigate` and `find_path`. Stun them or wait.