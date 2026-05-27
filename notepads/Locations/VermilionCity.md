# Vermilion City Location Records (Map 0_5)
- Map 0_5 is the native, unmodded Vermilion City.
- Entrance from Route 6: (19, 0) inside Map 0_5.

## Points of Interest:
- **Pidgey House (Map 0_93)**:
  - Entrance door at (23, 19) on Map 0_5.
  - Inside, there is a youngster NPC at (5, 3) and a Pidgey Pokémon sprite wandering around.
- **Pokémon Fan Club (Map 0_90)**:
  - Entrance door at (9, 13) on Map 0_5.
  - Inside, the Chairman sits behind the table at Row 2. We can talk to him to get the Bike Voucher.
- **Vermilion Pokémon Center**:
  - Expected on the north-west side (approx. Column 11, Row 5) or north-east side. We will search for its red roof.
- **Vermilion Poké Mart**:
  - Expected directly north of the Pidgey House (approx. Columns 23-25, Row 13).

## Overworld Navigation & Layout:
- Column 19 between Row 18 and Row 21 is a water/dock barrier (TYPE_4e8c).
- Row 17 is a clear paved horizontal street (TYPE_3fe2) that allows bypassing Column 19's water barrier to travel west.
- Row 22 and below is sea water (TYPE_4e8c).
- **Vermilion City Landmarks**:
  - Poké Mart Entrance: (23, 13) (🏪 marked)
  - Fishing Guru House Entrance: (15, 13) (🚪 marked)
  - Pokémon Center Entrance: (11, 3) (🏥 marked)
  - Pokémon Fan Club Entrance: (9, 13) (🚪 marked)
  - Pidgey House Entrance: (23, 19) (🚪 marked)
- Column 6 & 7 Western Corridor (Blocked): Columns 6 and 7 are blocked at Row 19 by a solid fence (TYPE_2889 at (6, 19)) and a post/mailbox (TYPE_2889 at (7, 19)), meaning they do NOT form a continuous passable vertical street to the southern docks. This was empirically verified on Turn 16325. The correct path to reach the southern docks/pier is via the eastern pier along Column 30.

## Snorlax Blockage (Verified Turn 17930):
- A sleeping Snorlax occupies (35, 13) on Map 0_5, completely blocking the entrance to Diglett's Cave at (34, 13) and (35, 13). Diglett's Cave is currently inaccessible from the Vermilion City side until Snorlax is awakened.