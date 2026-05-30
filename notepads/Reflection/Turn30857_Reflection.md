# Reflection - Turn 30857 (Gem)

## 1. Immediate Execution
- Defeated Kiyo in Fighting Dojo, obtained Hitmonlee (KICKY) sent to PC Box 1.
- Correctly located Saffron Poké Mart in Northeast Saffron at (25, 11) (not blocked).
- Purchased 10x Great Balls and 10x Hyper Potions. Remaining money: ¥28,718.
- Currently at (25, 12). Heading to Route 7 West Gatehouse at (0, 18) to exit Saffron and go to Celadon.

## 2. Socratic Challenge: Route 5 Building
- The building on Route 5 at columns 11-15, rows 32-35 is the Underground Path entrance (Saffron-to-Cerulean).
- In standard Gen 1, this building is the Underground Path. The sign reading "GYM" (or similar) is a well-known tileset graphic/mapping glitch caused by shared tile IDs when using Crystal-based visual styles on standard Gen 1 maps. It is not Saffron Gym (which is in the NE corner).

## 3. Systematic Gatehouse Passability Tests
- **Route 5 Gatehouse (North)**: Verified on Turn 30593. Passed freely without any drink prompts.
- **Route 7 Gatehouse (West)**: Will verify on exit to Route 7 (approx. Turn 30880).
- **Route 6 Gatehouse (South) & Route 8 Gatehouse (East)**: Will systematically test when we travel near those routes.

## 4. Silph Co. Warp mapping strategy
- We will create a dedicated notepad `Mechanics/SilphCoWarps` once we enter Silph Co.
- Structure:
  `| From Floor | Coordinate | To Floor | Coordinate | Verified Turn |`
  `|------------|------------|----------|------------|---------------|`
- This keeps the data extremely compact, structured, and easy for the `saffron_warp_agent` to read.

## 5. Tool Maintenance & Pathing Strategy
- We will avoid using `generate_path` for large city navigations due to unmodeled buildings. Instead, we will use small, visually verified increments or straight-line road segments (such as Column 36/Route 18 main streets) which are 100% reliable.