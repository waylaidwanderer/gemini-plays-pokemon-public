# Mechanics & State
- **Fly Mechanics:** Blocked on door mats (29,4) AND (29,5).
- **Movement:** At (29,4). Need to move to (29,5) or (30,5) to Fly.
- **Menu:** Cursor on Pokemon -> Mistral (Slot 6).
- **Map Navigation:** Cherrygrove -> Violet (Up) -> Ecruteak (Left).
- **Error:** Last turn flew to Cherrygrove (Self-Fly) due to map input timing or wrong coords.
- **Correction:** Adding longer sleeps between Map inputs.

# Strategy
1. Move Down to (29, 5).
2. Execute Fly Sequence with delays.
3. Sequence: Start -> A (Pokemon) -> A (Mistral) -> A (Fly) -> Map: Wait 3s -> Up -> Wait 1s -> Left -> Wait 1s -> A.