import marshal
import os
import types

def is_coordinate_tuple(item):
    return (isinstance(item, tuple) and len(item) == 2 and 
            isinstance(item[0], int) and isinstance(item[1], int) and
            0 <= item[0] <= 40 and 0 <= item[1] <= 40)

def extract_routes(co_obj):
    routes = []
    # If co_obj itself is a tuple of coordinates, return it
    if isinstance(co_obj, tuple) and len(co_obj) > 10 and all(is_coordinate_tuple(x) for x in co_obj):
        routes.append(co_obj)
        return routes
        
    if hasattr(co_obj, "co_consts"):
        for const in co_obj.co_consts:
            if isinstance(const, tuple):
                if len(const) > 10 and all(is_coordinate_tuple(x) for x in const):
                    routes.append(const)
                else:
                    # Recursively search elements of the tuple
                    for item in const:
                        if isinstance(item, types.CodeType):
                            routes.extend(extract_routes(item))
            elif isinstance(const, types.CodeType):
                routes.extend(extract_routes(const))
    return routes

def inspect_all_pyc():
    pyc_dir = "__pycache__"
    for f in os.listdir(pyc_dir):
        if f.endswith(".pyc"):
            path = os.path.join(pyc_dir, f)
            print(f"=== Searching {path} ===")
            try:
                with open(path, "rb") as file:
                    file.read(16)
                    code_obj = marshal.load(file)
                    routes = extract_routes(code_obj)
                    if routes:
                        for r in routes:
                            print(f"  Found route of length {len(r)}!")
                            print(f"  First 30: {r[:30]}")
                    else:
                        print("  No route found.")
            except Exception as e:
                print(f"  Error loading {path}: {e}")

if __name__ == "__main__":
    inspect_all_pyc()
