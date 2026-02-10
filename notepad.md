# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics
- **Mimicry**: Murkrow COPIES input.
- **Switches**: 
  - B1F (6, 1): Statue Switch (West) - Activated Turn 35131.
  - B1F (24, 1): Statue Switch (East) - Activated Turn 35099.
  - Switches likely toggle shutters. Shutter at (15, 10) confirmed CLOSED.

## Current State
- **Location**: B1F (7, 10).
- **Goal**: Reach NE Stairs at B1F (27, 2) to access East side of B2F.
- **Observation**: Access to East side depends on Shutter at (15, 10).

## Plan
1. Move East to check Shutter at B1F (15, 10).
2. If Open: Proceed to NE Stairs (27, 2).
3. If Closed: 
   - Check if toggling the switch at (6, 1) again helps.
   - Or search for other switches in Central Area.
4. Once in East Side (B2F):
   - Go to SE Corner (27, 14).
   - Find switches/keys for Boss Door/Shutters.
   - Solve Murkrow puzzle if needed (Murkrow is at B2F West).

## Murkrow Strategy
- Use `simulate_murkrow` before moving.
- Trap it against walls/obstacles to align it.