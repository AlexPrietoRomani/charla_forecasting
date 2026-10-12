import httpx

token_url = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"
cid = "sh-62cd3506-dc81-4a93-8a1e-aab597e2930a"
secret = "CVOBs1YiF2Ncxn7NygcJaWiZRAAN0zwN"

r_token = httpx.post(token_url, data={"grant_type": "client_credentials", "client_id": cid, "client_secret": secret})
token = r_token.json()["access_token"]

stats_url = "https://sh.dataspace.copernicus.eu/api/v1/statistics"
geojson = {
    "type": "Polygon",
    "coordinates": [[
        [-78.775, -5.677],
        [-78.770, -5.677],
        [-78.770, -5.672],
        [-78.775, -5.672],
        [-78.775, -5.677]
    ]]
}
evalscript = """//VERSION=3
function setup() {
  return {
    input: [{bands: ["B04", "B08", "SCL", "dataMask"]}],
    output: [{id: "ndvi", bands: 1}, {id: "dataMask", bands: 1}]
  };
}
function evaluatePixel(s) {
  let val = (s.B08 - s.B04) / (s.B08 + s.B04);
  let cloudy = [3, 8, 9, 10, 11].indexOf(s.SCL) > -1;
  return {ndvi: [val], dataMask: [cloudy ? 0 : s.dataMask]};
}"""

body = {
    "input": {
        "bounds": {"geometry": geojson, "properties": {"crs": "http://www.opengis.net/def/crs/EPSG/0/4326"}},
        "data": [{"type": "sentinel-2-l2a"}]
    },
    "aggregation": {
        "timeRange": {"from": "2024-01-01T00:00:00Z", "to": "2024-03-01T00:00:00Z"},
        "aggregationInterval": {"of": "P1M"},
        "evalscript": evalscript,
        "resx": 0.0001,
        "resy": 0.0001
    }
}

r = httpx.post(stats_url, headers={"Authorization": f"Bearer {token}"}, json=body, timeout=30)
print("Status:", r.status_code)
print("Response:", r.text[:500])
