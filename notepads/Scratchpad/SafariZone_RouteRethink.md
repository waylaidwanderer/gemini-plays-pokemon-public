# Safari Zone Route Rethink & Testing (Turn 44777)
- **Objective**: Reach the Secret House (HM03 Surf) and Gold Teeth in Safari Zone West (Area 3).
- **Hypothesis**: The standard path is Center -> East -> North -> West.
  - The previous agent's conclusion that "the eastern basin of Safari Zone North is completely isolated with no path to the rest of Area 2" is likely a false assumption resulting from incomplete exploration.
  - Specifically, they found a barrier at Row 11 in Safari Zone North preventing them from going north to Rows 8-10, but they did not test walking West along the lower ground (Rows 12-20).
  - In vanilla Pokémon, the path to the West exit of Safari Zone North goes precisely along the lower ground of the map, and we can bypass any northern barriers to reach the western side of the map which connects to Safari Zone West (Area 3).
- **Verification Plan**:
  1. Travel from current position (8, 16) in Safari Zone Center to the East exit at (29, 10) to enter Safari Zone East (Area 1).
  2. Follow the verified route through Safari Zone East to the Northwest exit at (0, 5) to enter Safari Zone North (Area 2) at (39, 31).
  3. Climb the plateau at (28, 27) and walk to the Northwest stairs at (34, 15).
  4. Descend the stairs to the lower ground at Row 15/16.
  5. Instead of trying to go North to Rows 8-10, walk West along the lower ground (Rows 12-20) to find the connection to the western section of Safari Zone North.
  6. From the western section of Safari Zone North, locate the western transition to Safari Zone West (Area 3).
  7. Retrieve Gold Teeth and HM03 Surf.
- **Starting Step**: Walking East in Safari Zone Center from (8, 16).