from pyproj import Transformer


def transfomation(lat, long):
        transformer = Transformer.from_crs(4326, 2154);
        transformer = Transformer.from_crs("EPSG:4326", "EPSG:2154")

        #result = transformer.transform(3.298493,45.648949)
        result = transformer.transform(lat, long)
        print(result)
        return result


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    result = transfomation(34.0571709,-117.1942978)
    return result

@app.post("/transform")
def read_root(lat, long):
    result = transfomation(lat, long)
    return result