# Warehouse Switch Puzzle - Solution Testing
- State: Sw1 ON, Sw2 ON (Toggling NOW), Sw3 ON.
- Goal: Test [All ON].
- Check: Shutter (6, 6) and (6, 8).
- Previous Logic: "Sw1 ON opens (6, 6)" vs "Sw3 ON closes (6, 6)".
- Plan: Toggle Sw2 ON. Go to (6, 5). Inspect (6, 6).

## Plan
1. Turn Switch 2 ON (Press A x3).
2. Move to (6, 5) via (10, 5).
3. Check Shutter (6, 6).
4. If Open, proceed to (6, 8).