Mansion 1F Routing Solution (Final Verified):
1. The Mansion has two global shutter states.
2. State B (Yellow-Open): Yellow Shutters are OPEN. Dark Grey Shutters are CLOSED.
3. State A (Yellow-Closed): Yellow Shutters are CLOSED. Dark Grey Shutters are OPEN.
4. Verified Shutter Types:
   - (16, 16) and (17, 16): Yellow Shutter (horizontal)
   - (13, 22) and (13, 23): Yellow Shutter (vertical)
   - (9, 6) and (9, 7): Yellow Shutter
   - (9, 14): Solid Wall
5. Route to 2F/3F Stairs at 1F (5, 10):
   - The ONLY path to the West Wing is via the Yellow Shutter at (9, 6).
   - This means we MUST be in State B (Yellow-Open).
   - If starting in State A (current state):
     - Walk from Center (12, 22) North to (12, 15), then East to (21, 15).
     - Walk South down East Wing to (21, 25).
     - Walk West to switch base at (18, 25) and toggle to State B.
     - Walk back East to (21, 25), North to (21, 15), West to (12, 15).
     - Walk North to (12, 6).
     - Walk West through OPEN Yellow Shutter at (9, 6) to reach West Wing.
     - Walk North to stairs at (5, 10).