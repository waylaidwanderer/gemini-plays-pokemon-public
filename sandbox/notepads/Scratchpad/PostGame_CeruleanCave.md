# Post-Game: Cerulean Cave & Mewtwo Investigation

## Hypotheses to Empirically Verify
- Hypothesis 2: Legendary Pokémon Mewtwo resides within Cerulean Cave B1F at Level 70.
- Hypothesis 3 (Unverified): 1F Ladder (0, 6) connects to 2F Ladder (1, 3); corridor (5, 4..5) hypothesized to connect to B1F descent.
- Hypothesis 4 (Unverified): 2F Northwest Enclave (Cols 0..2, Rows 1..4) is accessible via physical bump testing along Columns 3..2 on Rows 1..3.

## Post-Game Routing Strategy: 2F Sector A & Northwest Enclave
1. Reconstructed topology: 1F and 2F each possess 6 ladders. Five pairs verified 2-way connections. The 6th pair is hypothesized 1F (0, 6) <---> 2F (1, 3).
2. Physical Goal: Reach 2F Ladder (9, 1) via 1F Northern Terrace Ladder (7, 1).
3. Collision Testing: Rigorously collision-test every western step along Rows 1, 2, and 3 from Column 3 into Column 2 to locate the physical opening into the Northwest Enclave and Ladder (1, 3).

## Active Route & Next Steps
- Current Location: Cerulean Cave 2F at (9, 1) on Ladder (Sector A).
- Active Plan:
  1. Walk west across Northern Terrace along Row 2 to (7, 2), then step North onto Ladder (7, 1).
  2. Ascend Ladder (7, 1) to arrive at 2F Ladder (9, 1).
  3. On 2F, walk west along Row 1 to (3, 1).
  4. Systematically bump-test stepping Left into Column 2 at (3, 1) [testing tile 2, 1], (3, 2) [testing tile 2, 2], and (3, 3) [testing tile 2, 3].
  5. Once opening is found, enter Northwest Enclave and reach Ladder (1, 3).

## Cerulean Cave Multi-Floor Ladder Topology
| 1F Coordinate | 2F Coordinate | Verified Status | Notes |
|:---:|:---:|:---:|:---|
| (23, 7) | (22, 6) | CONFIRMED 2-WAY | Connects 1F Entrance Terrace to 2F Central Network |
| (18, 9) | (19, 7) | CONFIRMED 2-WAY | Connects 1F Central-Western Terrace to 2F Secluded Pocket (Dead End) |
| (27, 1) | (29, 1) | CONFIRMED 2-WAY | Connects 1F Northern Terrace to 2F Sector B loop (no Sector A access) |
| (7, 1) | (9, 1) | CONFIRMED 2-WAY | Connects 1F Northern Terrace to 2F Sector A (Gateway to NW Enclave) |
| (3, 11) | (3, 11) | CONFIRMED 2-WAY | Connects 1F Western Terrace to 2F Western Network |
| (0, 6) | (1, 3)? | UNTESTED HYPOTHESIS | 1F (0, 6) has south exit ledge; connects to 2F NW Enclave & B1F route |
