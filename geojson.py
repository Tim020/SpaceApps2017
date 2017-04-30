import simplejson as json

def process(in_file, out_file):
    data = json.load(open(in_file))

    geojson = {"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": {"type": "Point", "coordinates": [d["lng"], d["lat"]], }, "properties": d, } for d in data]}

    output = open(out_file, 'w')
    json.dump(geojson, output)

#process("Website/Data/dolphin.json", "Website/Data/dolphin_geo.json")
process("Website/Data/turtle.json", "Website/Data/turtle_geo.json")