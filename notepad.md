# Lessons Learned
- **Tool Insight:** Fly Map cursor movement REQUIRES `hold_ms` >= 500. Default (150ms) is insufficient.
- **Automation vs. Interruptions:** Phone calls/events freeze the game, desyncing fixed-input sequences. Monitor and manually reset.
- **Efficiency:** "Checking with your face" (running into grass) is faster than checking the Pokedex for Roamers.
- **Fly Map Logic:**
  - `New Bark -> Left, Up, Right, Right` -> Lake of Rage.
  - `Lake of Rage -> Down (500ms)` -> Violet City.
  - `Violet City -> Right (500ms x3)` -> Target: Blackthorn City.
- **Current Strategy:** From Violet, press Right x3 with long holds to reach Blackthorn.

# Current Status
- **Location:** Ecruteak City (Physically), Violet City (Fly Map Cursor).
- **Activity:** Menu Navigation (Flying to Blackthorn).
- **Time Started:** Turn 29657.
- **Party:** Gyarados (Lv 36) Lead. Lugia in party. Pidgey (Slot 4) has Fly.
- **Objective:** Fly to Blackthorn City to buy Max Repels.
- **Repel Logic:** Lv 36 Lead + Repel blocks local wilds (Lv ~15) but allows Roamers (Lv 40).
- **Shopping Log:**
  - Goldenrod Dept Store: No Max/Super Repels found (2F-5F checked).
  - Ecruteak Mart: No Repels found (Standard inventory only).

# Exploration Queue
- **Mahogany Town:** West edge (x=0-2) unseen tiles. Investigate later.

# Legendary Beast Hunt Strategy
- **Target:** Raikou (#238) & Entei (#239).
- **Method:** Blind Hunt Loop (Route 37 <-> Ecruteak).
- **Tactics:** Enter Rt 37 -> Grass (Down x2, Wiggle) -> If none, Return to Ecruteak -> Repeat.

# Tile Mechanics
- GRASS: Traversable, encounters.
- FLOOR/DOOR/STAIRS: Traversable.
- WALL/OBSTACLES: Impassable.
- WARP_CARPET: Transition.
- WATER: Surfable.
- **Phone Call (Turn 29598):** Wade (Route 31) found Berries.