import re

# Read the file
path = "notepads/Locations/Route8.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Define new coordinates to add
new_coords = {
    10: [30, 31, 36, 39, 40],
    11: [41],
    13: [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 45],
    14: [42, 43, 44],
    15: [42, 43]
}

# Parse existing coordinates
coord_section_pat = re.compile(r"### Verified Walkable Coordinates.*?\n\n", re.DOTALL)
match = coord_section_pat.search(content)

existing_coords = {}
if match:
    section_text = match.group(0)
    # Find all Row lines like "- Row 8: (51, 8), (52, 8)..."
    row_lines = re.findall(r"- Row (\d+):\s*(.*)", section_text)
    for row_str, coords_str in row_lines:
        row = int(row_str)
        # Find all numbers inside parentheses
        coords = [int(x) for x in re.findall(r"\((\d+),\s*\d+\)", coords_str)]
        existing_coords[row] = coords

# Merge existing and new coordinates
all_coords = {}
for r in set(list(existing_coords.keys()) + list(new_coords.keys())):
    all_coords[r] = sorted(list(set(existing_coords.get(r, []) + new_coords.get(r, []))))

# Format the new coordinate section
new_section = "### Verified Walkable Coordinates (Physically stepped on in this session):\n"
for r in sorted(all_coords.keys()):
    coords_list = all_coords[r]
    coords_formatted = ", ".join(f"({x}, {r})" for x in coords_list)
    new_section += f"- Row {r}: {coords_formatted}\n"
new_section += "\n"

# Replace the coordinate section in content
if match:
    updated_content = content.replace(match.group(0), new_section)
else:
    # If not found, append to the end of the mapped layout or file
    updated_content = content + "\n\n" + new_section

# Write back
with open(path, "w", encoding="utf-8") as f:
    f.write(updated_content)

print("Route 8 coordinates updated successfully!")
