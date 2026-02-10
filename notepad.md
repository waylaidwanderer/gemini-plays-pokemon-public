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

- Status: At B1F (3, 6) "Dead End Room".
- Confirmed: B2F (3, 6) Warp sends to B1F (3, 6).
- Goal: Exit this room to the South to bypass B1F Row 4 Blockage.
- Obstacle: Shutter at B1F (3, 8).
- Plan:
  1. Inspect Shutter at (3, 8).
  2. Search room for hidden switches (Dowsing/Check).
  3. If stuck, trigger Warp at (3, 6) to see if it returns to B2F or elsewhere.