import marshal
import os
import types

def is_coordinate_tuple(item):
    return (isinstance(item, tuple) and len(item) == 2 and 
            isinstance(item[0], int) and isinstance(item[1], int) and
            0 <= item[0] <= 40 and 0 <= item[1] <= 40)

def extract_flat_consts(co_obj):
    coords = []
    if hasattr(co_obj, "co_consts"):
        for const in co_obj.co_consts:
            if is_coordinate_tuple(const):
                coords.append(const)
            elif isinstance(const, types.CodeType):
                coords.extend(extract_flat_consts(const))
    return coords

def inspect_pyc(path):
    print(f"=== Flat Coords in {path} ===")
    try:
        with open(path, "rb") as f:
            f.read(16)
            code_obj = marshal.load(f)
            coords = extract_flat_consts(code_obj)
            print(f"  Found {len(coords)} flat coordinate tuples:")
            # If there are coords, print them
            if coords:
                print(coords)
    except Exception as e:
        print(f"  Error: {e}")

if __name__ == "__main__":
    pyc_dir = "__pycache__"
    for f in os.listdir(pyc_dir):
        if f.endswith(".pyc") and "complete_speedrun" in f:
            inspect_pyc(os.path.join(pyc_dir, f))
