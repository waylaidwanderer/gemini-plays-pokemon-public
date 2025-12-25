# Ice Path Strategy: B1F Boulder Puzzle

- **Status:** Searching for Boulders. Turn: 17415.
- **Goal:** Locate and push 4 Boulders into 4 Pits.
    - **Boulder 1:** Target Pit (12, 13). Not at (18, 12) or (17, 7).
    - **Boulder 2:** Target Pit (4, 7). Not at (5, 6).
    - **Boulder 3:** Target Pit (11, 2). Not at (11, 5).
    - **Boulder 4:** Target Pit (5, 12).
- **Pits:** `(11, 2)`, `(4, 7)`, `(5, 12)`, `(12, 13)` (Open).

## Navigation & Mechanics
- **Current Position:** `(3, 2)`.
- **Immediate Goal:** Navigate East to `(11, 1)` to check for Boulder 3.
- **Bag Status:** Full.
- Observation: Blockage at (9, 10) was a wild encounter, not a boulder.
- Status: B2F East Side (Navigating to Exit).
- Goal: Exit Ice Path.
    - Path to Ladder (3, 15):
        1. (Done) Navigate to (6, 8).
        2. Slide Up to (6, 5).
        3. Navigate to (3, 15) via:
           - (6, 5) -> (6, 4) -> (5, 4) -> (4, 4) -> (4, 5) -> (3, 5).
           - Walk to (3, 7).
           - Slide Down to (3, 14).
           - Take Ladder at (3, 15).
- Note: (3, 4) is FLOOR_UP_WALL (Obstacle). Bypass via (4, 4).
- Pits: N/A on this floor.
- Pits: `(11, 2)`, `(4, 7)`, `(5, 12)`, `(12, 13)` (Open).