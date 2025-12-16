# Gem's Journey in Pokémon Crystal

## Strategy & Pathing
- **Goal:** Reach Azalea Town.
- **Current Task:** Backtrack North from dead end at (16,22), cross to West side, then South to ladder.
- **Map Notes:**
    - `FLOOR_UP_WALL` at (16,22) blocks movement South (Ledge/Wall).
    - `WALL` tiles at (14,13) blocked Westward path.
    - **Lesson:** Use `smart_navigate` for long paths to avoid manual errors.

## Party
- **GARNET (Quilava)** Lv17 | **TOPAZ (Sentret)** Lv4 | **EGG** | **UNAKITE (Unown)** Lv5 | **ROCKY (Onix)** Lv7

## Quest Log
- **Badges:** Zephyr (1/8)
- **Pending:**
    - Deliver Mystery Egg to Elm (Done?) -> No, waiting for call? Or is it done? (Check later).
    - Bug Contest (Today).
- **Key Items:** HM05 (Flash), TM31 (Mud-Slap).

## Mechanics
- **Poison:** -1 HP / 4 steps.
- **Ghosts:** Immune to Normal/Fighting.
- **Inventory:** Verify before shops.
- **Path Correction:** The ledge at (4,18) is blocked from the North.
- **South Loop Strategy:** Found a potential path South! Plan: Loop South to (7,26), West to (4,26), then North up the West channel to reach the ladder at (5,19).
- **Ledge Mechanics:** `FLOOR_UP_WALL` cannot be entered from the "Floor" side if it acts as a wall. It seems to block Southward movement here.