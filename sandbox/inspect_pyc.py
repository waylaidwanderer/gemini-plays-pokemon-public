import importlib.util
import os
import sys

def inspect_module(path):
    print(f"=== Inspecting {path} ===")
    try:
        # Load the .pyc file as a module
        name = os.path.basename(path).split(".")[0]
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Check for ROUTE variable
        if hasattr(module, "ROUTE"):
            route = getattr(module, "ROUTE")
            print(f"  Found ROUTE with length: {len(route)}")
            print(f"  First 35 coordinates: {route[:35]}")
            # print transitions if any
            for i, coord in enumerate(route):
                if i > 0:
                    prev = route[i-1]
                    dist = abs(coord[0] - prev[0]) + abs(coord[1] - prev[1])
                    if dist > 5:
                        print(f"  Transition at index {i}: {prev} -> {coord}")
        else:
            print("  No ROUTE variable found.")
            # Print public attributes
            attrs = [attr for attr in dir(module) if not attr.startswith("__")]
            print(f"  Attributes: {attrs}")
    except Exception as e:
        print(f"  Error: {e}")

if __name__ == "__main__":
    pyc_dir = "__pycache__"
    for f in os.listdir(pyc_dir):
        if f.endswith(".pyc"):
            inspect_module(os.path.join(pyc_dir, f))
