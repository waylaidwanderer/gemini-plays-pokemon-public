# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25984 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** FIGHT -> THUNDERPUNCH.
- **Battle Plan:**
    1. **Current State:** Muscle (65/280, Burned). Charizard (~60%).
    2. **Analysis:**
       - Incoming Damage (Flamethrower) ~115 + Burn (35) = 150.
       - Healing with Lemonade (+80) leaves us at max 145 HP. We still die to Flamethrower.
       - Healing is a death spiral.
    3. **The Play:** **ATTACK.**
       - If Charizard uses a weak move (Fire Spin) or misses, we survive the hit.
       - Muscle moves second. If we survive the hit (even with 1 HP), we execute the move.
       - Burn damage happens *end of turn*. We get the hit off.
       - Move: **ThunderPunch**. (Special 150 BP vs Physical Burned Strength 40 BP).
    4. **Outcome:** Hope for a kill or massive damage before fainting.
- **Resources:** Muscle (65/280). 8 Lemonades. No Revives. Last Stand.

# Recent Discoveries
- Found Max Revive at (6, 3) in the isolated Left Section of the Item Room.

# Tile Mechanics
- **FLOOR_UP_WALL:** Acts as a South-facing Ledge (verified). Blocks North movement.
- **Warp Carpet:** Located at Row 29/31. Avoid stepping on them unless exiting.
- **Waterfalls:** Found at Row 28/29. Requires HM07 Waterfall.
- **Waterfall Mechanics:** Walking into a waterfall causes a slide-back, setting facing to DOWN. To ascend, ensure facing UP (move away and back if needed) then press A to interact. Requires HM07.
- **Tile Mechanics Update:** `FLOOR_UP_WALL` at Row 4 blocked South movement. Treating as impassable for now.
- **Map Structure:** Upper Ledge is segmented. Center (13) connects to Left (6), but Right (17) is blocked by Wall at Col 16.