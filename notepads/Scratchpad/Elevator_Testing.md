Hypothesis: Elevator Menu is a 2-column list. Left column is 1F-8F, right column is 9F-11F. If true, pressing RIGHT once from the default (1F) will select 9F.
- Elevator Panel Testing: Interacting with the visual panel at (3, 0) while standing at (3, 1) and facing Up DOES NOT open the floor menu. Testing X=2 and X=1 next.
- Hypothesis: The elevator panel at (3,0) didn't open because the 'A' button press was part of a movement macro and might have been dropped or I wasn't aligned correctly. I will test pressing 'A' as a standalone action.
- Elevator Panel Debugging: I am going to try interacting with the panel at (3, 0) by just standing at (3, 1), facing Up, and pressing 'A' once, then wait to see if the menu actually appears.
- Retesting elevator panel: Previous tests at (2,0) and (1,0) failed. Testing (0,0), left wall, right wall, and (3,0) again.

- Elevator menu is a single vertical column. Pressing Right does not move the cursor.