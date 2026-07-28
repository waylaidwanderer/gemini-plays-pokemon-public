# Search Scripting Pitfalls

## Turn 79 Baseline Drift Pitfall
- **Description:** When running navigation scripts, if you execute a sequence of movements and then a reset sequence without first verifying that the initial movements were successful (e.g. they weren't blocked by a wall, NPC, or wild battle), the actual position of the player will drift from the expected position.
- **Prevention:** Always verify that each step or sequence of steps succeeded (checking GameState coordinates and screen visual) before continuing or executing corrective/reset steps.
## time.sleep() and Concurrent Execution Pitfall
- **Description:** Python's `time.sleep()` does NOT advance the emulator. The emulator is completely paused during Python code execution except when `mgba.press_buttons()` is running. If you use Python loops with `time.sleep()` expecting the player's coordinates to change, the coordinates will never update, leading to infinite loops and script timeouts.
- **Prevention:** Do not use `time.sleep()`. The emulator advances synchronously during `mgba.press_buttons()`. Insert `"sleep <ms>"` directly inside the button list if you need delays, and read coordinates/screenshots only after `mgba.press_buttons()` returns.