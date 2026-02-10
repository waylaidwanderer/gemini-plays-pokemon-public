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
- Player: (14, 10).
- Murkrow: LOST (Not at expected coords).
- Shutter (15, 10): LOCKED.
- Action: Returning to B1F Stairs (3, 2) to hard reset the room.