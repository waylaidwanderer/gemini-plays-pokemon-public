# Strategic Objectives
- **Primary:** Earn Rising Badge.
- **Secondary:** Pass Dragon User Challenge.
- **Immediate:** Cross Whirlpool at (24, 23) using Lapis (Slot 3).

# Navigation & Discovery
- **Connections:** 1F (5, 15) <-> B1F (20, 3).
- **Location:** Dragon's Den B1F (East Side).
- **Target:** Dragon Shrine (likely South/Central island).
- **Insight:** Whirlpools (BUOY tiles) require HM06. Direct interaction ('A') failed. Must use Party Menu.

# Team Status
- **Health:** Full.
- **Party:** Gyarados, Quilava, Lapis (HM Slave), Machoke, Sneasel, Swinub.

# Tile Mechanics
- **LEDGE_HOP_DOWN**: One-way (South).
- **FLOOR/WALL**: Standard.
- **PIT**: Drops to lower floor.
- **LADDER**: Vertical transport.
- **WARP**: Map transition.
- **WATER**: Surf required.
- **BUOY**: Whirlpool (Requires HM06).
- Insight: "Facing: up" in GameState confirms alignment issue. Menu usage failed because of this.
- Plan: Close All Menus (B, B), Face DOWN (Down), then Restart Menu Sequence.
- Requirement: Must face BUOY/Whirlpool to use HM.
- Status: Party Menu Open (Cursor on Kunai). Game State shows Facing UP (Alignment Issue).
- Issue: Previous 'Down' inputs failed to update facing, likely due to menu handling.
- Action: Closing all menus (B x3) and MOVING RIGHT to (25, 22) to break potential loop and force state update.
- Next: Face DOWN at (25, 23) and Interact.