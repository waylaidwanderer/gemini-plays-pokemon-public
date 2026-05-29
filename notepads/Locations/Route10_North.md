# Route 10 North Geographical Records (Map 0_21)
- Map ID: 0_21
- Created Turn: 26834
- Updated Turn: 27006

## Overview:
- This is the northern segment of Route 10, located outside the northern exit of Rock Tunnel.
- The area connects to Route 9 in the west.

## Points of Interest:
- **Route 10 Pokémon Center (North)**: Located at (11, 19). The door is at (11, 19).
- **Rock Tunnel North Entrance**: Located at (8, 17) (passable cave mouth TYPE_3fe2).

## Overworld Blockages & Key Features:
- A cuttable bush is located directly to the east at (9, 18) (TYPE_5519).
- Another cuttable bush is located at (9, 20) (TYPE_5519).
- A solid fence (TYPE_2889) runs horizontally along Row 19 on Columns 4-7, isolating the northern cave mouth area from the southern path unless we cut the bush at (9, 18).
- Row 19 Column 8 is a solid tree (TYPE_2889).
- Row 19 Column 9 is passable grass (TYPE_3fe2).

## Physical Verification Logs:
- **Turn 26829**: Successfully exited Rock Tunnel onto Route 10 North at (8, 18).
- **Turn 26856**: Used PETAL's CUT to remove the second bush at (9, 20). Path to Route 10 Pokémon Center is now fully open.
- **Turn 26860**: Entered Route 10 Pokémon Center and fully healed our team.
- **Turn 26863**: Leaving Route 10 Pokémon Center to resume south navigation towards Lavender Town.
- **Turn 26871**: Navigated to (11, 24) on Route 10 North. Visually confirmed a red-haired trainer at (7, 25) facing Right, whose sightline on Row 25 is blocked by a solid tree at (8, 25) (TYPE_2889).
- **Ledge Jump Hypothesis (Turn 26874)**: We hypothesize that (14, 29) is a one-way south-facing ledge. Standing at (14, 28) and pressing Down will successfully jump over the ledge at (14, 29) and land us at (14, 30) or (14, 31).
- **Navigation Plan**: Walk Right from (11, 28) to (14, 28) (3 steps Right) and then press Down to test the ledge jump.
- **Ledge Jump Test (Turn 26878)**: Attempted to jump Down from (14, 28) over (14, 29). The movement failed (visited 0 tiles, bumped), proving that (14, 29) is a solid rock wall (TYPE_2889) and not a jumpable ledge. Hypothesis disproven.
- **New Exploration Strategy**: Walk west along Row 28 to investigate the western portion of the map (Columns 0-6) for the correct path or ledge jump.

## CRITICAL REALIZATION & CORRECTION (Turn 26898):
- **Visually & Geographically Proven**: We discovered that the area we are in is Route 10 North, not Route 10 South!
- **Proof of Work**:
  1. We exited Rock Tunnel at (8, 17) which is the same entrance we first entered on Turn 20624.
  2. The Pokémon Center at (11, 19) is the Route 10 North Pokémon Center.
  3. Row 30 is completely blocked by a solid, impassable mountain wall (TYPE_2889) across all columns because Route 10 North is separated from Route 10 South by this mountain.
  4. There is no horizontal or vertical passage leading south of Row 29 on the left side of this map.
- **Conclusion**: We did not traverse Rock Tunnel; we just walked in a circle and backtracked out of the north entrance. We must go back into Rock Tunnel to find the correct route to the true south exit!