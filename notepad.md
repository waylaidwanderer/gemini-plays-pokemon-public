# Warehouse Switch Puzzle - Strategy
- Status: Shutter 2 (6, 8) is CLOSED.
- Current State: Switch 3 ON, Switch 2 ON, Switch 1 ON.
- Action: Turning Switch 1 OFF.
- Goal State: [Switch 3 ON, Switch 2 ON, Switch 1 OFF].
- Reasoning: Switch 1 opens the TRAP path. I want the SAFE path. Switch 3 (Left End) might be the key.

## Plan
1. Navigate to (16, 2) and Toggle Switch 1 (Turn OFF).
2. Check Shutter 2 (6, 8).
3. If Closed, turn Switch 2 OFF (Goal: Only Switch 3 ON).
4. If Open, proceed to Director.