from fastapi import FastAPI, Query
from converter.converter import Converter
converter_app = FastAPI()


@converter_app.get("/converter/{type}")
def api_convert(
        type: str,
        src: str = Query(..., title="Source Unit", description="Source unit for conversion"),
        val: float = Query(..., title="Value", description="Value to be converted"),
        dst: str = Query(..., title="Destination Unit", description="Destination unit for conversion")):
    return {
        "type": type,
        "src": src,
        "val": val,
        "dst": dst}
    Converter.convert(type, dst, val, src)
