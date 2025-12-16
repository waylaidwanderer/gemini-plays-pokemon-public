# Gem's Journey in Pokémon Crystal

## Current Objectives
- **Primary:** Earn the Zephyr Badge in Violet City.
- **Secondary:** Explore Violet City.
- **Tertiary:** Locate Sprout Tower.

## Tile Mechanics
- **LEDGE_HOP_RIGHT:** One-way jump from Left to Right. Blocks movement from Right to Left.
- **LEDGE_HOP_DOWN:** One-way jump from Up to Down. Blocks movement from Down to Up.
- **WALL:** Impassable.
- **HEADBUTT_TREE/CUT_TREE:** Impassable (unless interacting with specific move).
- **TALL_GRASS:** High encounter rate.
- **WARP_CARPET:** Transports to new map.
- **COUNTER:** Acts as a wall. Interact across it to talk to NPCs behind it.

## Navigation History & World Knowledge
- **New Bark Town:** Elm's Lab (6,3), Player's House (13,5).
- **Route 29:** Connects New Bark to Cherrygrove.
- **Cherrygrove City:** Center (29,3), Mart (17,7).
- **Route 30:** Right Path (East) -> Mr. Pokemon. Left Path (West) -> Route 31.
- **Route 31:** East Entrance (26, 17) -> Violet City Gatehouse.
- **Violet City:** Reached via Gatehouse.

## Trainer Card (Gem)
- **ID:** 24_6
- **Party:**
    1. GARNET (Quilava) Lv14 - Tackle, Leer, Smokescreen, Ember.
    2. TOPAZ (Sentret) Lv4 - Tackle.

## Dialogue Log
- **Officer (Route 31 Gatehouse):** Asked if I visited **Sprout Tower**. Implies it's a key location.
- **Wade (Phone):** Found Berries. Waiting on Route 31.
- **Gentleman (Violet Center):** Team Rocket broken up 3 years ago by a kid.
- **Gameboy Kid (Violet Center):** Bill made the Pokemon PC storage system.
- **Youngster (Violet Center):** Traded Pokemon need badges to obey.

## Immediate Plan
- **Earl's Academy Sign:** Confirmed location at (27, 17).
- **Super Nerd (Violet City):** Beat the Gym Leader to be ready for prime time.
- **Teacher (Sprout Tower 1F):** Pillar is shaking. People training upstairs.
- **Sage Nico (Sprout Tower 2F):** Defeated.
- **Statue at (12, 15):** "It looks very distinguished." (Flavor text).
- **Sage Edmond (Sprout Tower 2F):** Defeated.
- **Ladder at (17, 3):** Investigating.
- **South-East Area (Rows 4-8):** Explored. Dead end with walls at Row 8.
- **Granny (Sprout Tower 1F):** Legend says a 100ft Bellsprout became the center pillar.
- **Sprout Tower 3F:** Retrieved Potion at (6, 14).
- **Sage Jin (Sprout Tower 3F):** Defeated at (8, 13).
- **Sage Neal (Sprout Tower 3F):** Defeated at (10, 11). Mentioned the Elder's HM lights darkness.
- **Sage Troy (Sprout Tower 3F):** Defeated.
- **Silver (Rival):** Defeated the Elder and used an Escape Rope to leave.
- **Elder Li (Sprout Tower 3F):** Defeated at (10, 2). Awarded HM05 (Flash).
- **HM05 (Flash):** Requires Zephyr Badge to use outside battle.
- **Wade (Phone):** Called to chat about his bug catching.
- **Item at (14, 1):** Picking up now.
- **Battle Mechanic:** Cursor memory persists in Fight menu. Built-in `execute_battle_move` assumes reset. Will rely on manual input or define custom tool when out of battle.