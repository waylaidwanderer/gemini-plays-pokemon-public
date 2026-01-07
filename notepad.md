# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25965 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** Clear Text -> Watch Gyarados Die (or survive).
- **Battle Plan:**
    1. **Current State:** Muscle Revived (280/280). Gyarados active.
    2. **Action:** Press B to clear "Revitalized" text.
    3. **Opponent Turn:** Charizard attacks Gyarados.
       - If Gyarados faints: Send Muscle.
       - If Gyarados survives: Switch to Muscle manually (Charizard is faster, so switching is safe if we accept Gyarados dies on the switch, but wait... if I switch, Muscle takes the hit. No. If Gyarados survives, I should let him die next turn or use an item? No, just let him die to get Muscle in clean).
    4. **Next:** Muscle vs Charizard. Strength.
- **Resources:** Muscle (280/280). Gyarados (Active). 0 Max Revive. 2 Hyper Potions.

# Recent Discoveries
- Found Max Revive at (6, 3) in the isolated Left Section of the Item Room.

# Tile Mechanics
- **FLOOR_UP_WALL:** Acts as a South-facing Ledge (verified). Blocks North movement.
- **Warp Carpet:** Located at Row 29/31. Avoid stepping on them unless exiting.
- **Waterfalls:** Found at Row 28/29. Requires HM07 Waterfall.
- **Waterfall Mechanics:** Walking into a waterfall causes a slide-back, setting facing to DOWN. To ascend, ensure facing UP (move away and back if needed) then press A to interact. Requires HM07.
- **Tile Mechanics Update:** `FLOOR_UP_WALL` at Row 4 blocked South movement. Treating as impassable for now.
- **Map Structure:** Upper Ledge is segmented. Center (13) connects to Left (6), but Right (17) is blocked by Wall at Col 16.