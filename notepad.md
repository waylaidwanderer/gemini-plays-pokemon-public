# Underground Warehouse Strategy
- **Status:** Switch 1 (OFF), Switch 2 (OFF), Switch 3 (ON).
- **Action:** Checking if [OFF, OFF, ON] opened any gates.
- **Plan:** Use check_gate_states. If fail, try Switch 1 (Right) as "End Switch".
- **Hypothesis:** "End Switch First" might mean Switch 1 (Rightmost) or Switch 3 (Leftmost).
- **tested_combinations:** [ON, ON, ON] (Fail), [ON, ON, OFF] (Fail), [ON, OFF, ON] (Fail), [ON, OFF, OFF] (Fail), [OFF, ON, ON] (Fail), [OFF, ON, OFF] (Fail), [OFF, OFF, OFF] (Fail), [OFF, OFF, ON] (Testing).
- **Reminder:** Inventory full (20/20). Must toss/use item to loot (1,12).