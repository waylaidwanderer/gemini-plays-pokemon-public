Mansion 1F Routing Solution (Final Verified):
1. The Mansion has two global shutter states.
2. State B (Yellow-Open): Yellow Shutters (16,16), (9,6) OPEN. Dark Grey Shutters (13,22), (9,14) CLOSED.
3. State A (Yellow-Closed): Yellow Shutters CLOSED. Dark Grey Shutters (13,22), (9,14) OPEN.
4. Crucial Fact: The Center section is permanently blocked at y=8 (spans x=10 to 24). Thus, the Yellow Shutter at (9, 6) CANNOT be reached from the South. State B is a dead end for reaching 2F.
5. The ONLY path to the 2F stairs at (5, 10) is via State A.
6. Route to 2F Stairs at (5, 10):
   - We must end up in State A.
   - Currently in State B.
   - From Center (12, 22), walk North to (12, 15), East to (18, 15) through OPEN (16,16).
   - Walk South to switch at (18, 25) and toggle to State A.
   - Walk North to (18, 22), West to (12, 22) through newly OPEN (13,22).
   - Walk North to (12, 14), West to (5, 14) through OPEN (9, 14).
   - Walk North to stairs at (5, 10).