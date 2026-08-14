import bridge
import json

# Let's try to query some standard endpoints or probe /
try:
    res = bridge.send_request("/")
    print("GET / response:", json.dumps(res, indent=2))
except Exception as e:
    print("GET / failed:", e)

try:
    res = bridge.send_request("/api")
    print("GET /api response:", json.dumps(res, indent=2))
except Exception as e:
    print("GET /api failed:", e)

try:
    res = bridge.send_request("/api/inventory")
    print("GET /api/inventory response:", json.dumps(res, indent=2))
except Exception as e:
    print("GET /api/inventory failed:", e)
