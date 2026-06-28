# Post-Game Mewtwo Quest Log & Active Routing
- Quest Started: Turn 111394
- Current Turn: 131075
- Current Position: standing on foot at (3, 11) on Map 0_228 (1F)

## Active Progress & Discoveries:
- **Empirical Proof of Water Separation (Verified Turn 131004)**:
  - Stood at (10, 6) surfing and visually verified that Rows 4 and 5 are completely blocked by solid rock walls (TYPE_2889) across Columns 6 to 13.
  - Visually verified that Columns 6 and 7 are blocked by solid rock walls (TYPE_2889) on Rows 6 and 7.
  - This conclusively disproves any direct horizontal water connection between the eastern and western water canals on 1F.
- **Unconstrained Surfing Route (The Segmented Master Path)**:
  - Since direct horizontal surfing is blocked, we must take a segmented path.
  - Path:
    1. From (11, 7) surfing, we cannot dismount Down directly onto (11, 8) because Row 8 is an elevated cliff. We must surf Left to (8, 7), Down Column 8 to (8, 14) water, Right to (11, 14) water, and Up to (11, 13) Water Ramp 2 to dismount on foot.
    2. Walk on foot along the southern corridor (Row 17) to the southwest corner.
    3. Climb the wooden staircase at (1, 13) to reach the southwest plateau.
    4. Note: On Turn 131071, we realized that the overworld engine does not permit boarding lower-level water from an elevated plateau (z=1 to z=0 transition) without a ramp, and we cannot walk right from (1, 8) due to a height boundary. Thus, the 1F elevated plateau is a dead end.
    5. The only viable path to reach the Northwest Ladder (1, 3) on foot is by climbing the Southwest Ladder at (3, 11) to 2F West (Map 0_226) and walking to (1, 3) there, by detouring around the rock at (3, 4).
- **Previous Spatial Hallucinations**:
  - Falsely assumed direct horizontal water passage was open on Rows 4-5. Turn 131004 visual verification proved this is blocked by continuous rock walls.
  - Falsely assumed we could dismount Down onto (11, 8) from (11, 7). Turn 131008 test proved this is blocked by an elevated cliff wall.
  - Falsely assumed we could surf from the elevated southwest plateau (z=1) onto Row 5 water (z=0) directly. This is a height transition violation.
  - Falsely assumed Row 4 on 2F West was completely blocked based on a single bump at (3, 4). REDEFINED the BFS solver on Turn 131073 to remove the false blockages (Columns 1-8 except Column 3), opening the true path to (1, 3) on 2F West.