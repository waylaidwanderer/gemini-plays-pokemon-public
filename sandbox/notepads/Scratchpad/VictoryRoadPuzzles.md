# Victory Road Puzzle Mechanics & Empirical Test Log

## Floor 1F Puzzle System

### Active Test: Switch Plate 1 & Shutter Pairing
- **Boulder 1 Initial Coordinate:** (5, 15)
- **Switch Plate 1 Coordinate:** (5, 14) (directly 1 tile North of Boulder 1)
- **Baseline Shutter States (Before Push - Verified Turn 22317):**
  - Shutter at (5, 13): CLOSED (purple horizontal bars blocking path north into western corridor)
  - Shutter at (7, 7): Unverified / off-screen
  - Shutter at (15, 7): Unverified / off-screen
- **Empirical Hypothesis:** Pushing Boulder 1 North from (5, 15) onto Switch Plate 1 at (5, 14) depresses the switch and opens Shutter at (5, 13).
- **Verification Protocol:**
  1. Stand at (5, 16) facing Up into Boulder 1.
  2. Activate Strength via ATLAS (Machop).
  3. Step Up to push Boulder 1 onto (5, 14).
  4. Visually inspect tile (5, 13) to confirm Shutter state change from CLOSED (bars) to OPEN (clear passageway).
  5. Explore northern sector to inspect physical states of shutters at (7, 7) and (15, 7).

### Unverified Structural Hypotheses (To Be Tested)
- Ascent to 2F: Hypothesis that stairs/ladder exists in western/central sector (e.g. near row 10..11). Must be visually located and confirmed in-game.
- Switch Plate 2 at (17, 13): Must test which shutter it operates once reached.