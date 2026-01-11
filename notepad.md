# Hall of Fame Entry
- **Achievement:** **CHAMPION OF THE JOHTO LEAGUE!**
- **Date:** Turn 33314
- **MVP:** Muscle (Machoke) Lv88.
- **Support:** Maelstrom (Lugia).

# Objectives
- **Primary:** Hunt Roamers (Raikou/Entei).
- **Secondary:** Complete Pokedex.
- **Immediate Task:** Hunt Roamers on Route 37.
- **Status:** Cycling Ecruteak <-> Route 37.
- **Strategy:**
    1. Enter Route 37.
    2. Run in grass with Max Repel active.
    3. If no encounter, reset map.

# Store Inventories
- **Goldenrod Dept Store 2F:** Standard Balls, Potions, Revive, Full Heal, Poke Doll. **NO** Max/Super Repels.
- **Celadon Dept Store 2F (Right Clerk):** Poke Ball, Great Ball, **ULTRA BALL**, Escape Rope...
- **Celadon Dept Store 2F (Left Clerk):** Potion, Super/Hyper/Max Potion, Revive, Super Repel, **MAX REPEL**.

# Roaming Beasts Status
- **Target:** Raikou & Entei.
- **Strategy:** Lead with Lv36 Gyarados + Max Repel.
- **Location:** Roaming Johto (Random).
- **Current Task:** Cycling Route 37 <-> Ecruteak City to force movement.
- **Inventory:** 13 Max Repels left.

# Tile Mechanics
- **FLOOR:** Traversable.
- **WALL:** Impassable.
- **TALL_GRASS:** Traversable. Wild encounters possible.
- **LEDGE_HOP:** One-way traversal (Down/Right observed).
- **WARP_CARPET:** Triggers map transition.
- **WATER:** Traversable with SURF.

# Lessons Learned
- **Fly Map Navigation:** The Fly map cursor animation is slow. Fast inputs (automated or manual) are often eaten. **STRATEGY:** Use strictly manual, single-step inputs with visual verification of the destination text between each move, OR use `sequence_press` with `sleep 1000` between inputs.
- **Navigation Verification:** Always verify `current_map_id` and screen text after a transition failure. Do not rely on "assumed" location.

# Roamer Hunt Log
- **Strategy:** Camp Route 37. Transition Ecruteak <-> Rt 37 to force Roamer movement.
- **Stats:** 63 Iterations. 0 Encounters.
- **Current Action:** Inspecting Lugia's Ball Icon.
- **Status:** Stats screen opening.
- **Objective:** Visually identify the capture ball.
- **Hypothesis:** Master Ball (M) vs Ultra Ball.