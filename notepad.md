# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics
- **Mimicry**: Murkrow COPIES input.
- **Switches**: B1F Statues/Computers *should* open B2F shutters.
- **Hypothesis**: Defeating Grunts near the switches activates them or provides the key.

## Current State

# Reflection (Turn 35411)
- Progress: Located Murkrow, Password requirements, and Boss Door.
- Issue: Repeatedly losing track of Murkrow and hitting walls.
- Correction: MUST use `simulate_murkrow` or visual confirmation before moving when Murkrow is off-screen.
- Plan:
  1. Warp to B2F.
  2. Verify Murkrow at (7, 2).
  3. Scan B2F Column 7 for obstacles (Grunts/Traps).
  4. Execute "Align and Push" with obstacle awareness.

# Current Status
- Map: B2F (3_51).
- Player: (2, 4).
- Goal: Verify existence of Stairs at SW Corner (3, 14).
- Constraint: Avoid Warp Trap at (3, 6).
- Plan:
  1. Move South along Column 2 to (2, 14).
  2. Check (3, 14) for Stairs.
  3. If NO stairs, return to B1F and solving the Row 4 Blockage is the ONLY option.
- Murkrow Puzzle: Suspended until B2F Shutters are unlocked.