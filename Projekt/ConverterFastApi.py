from fastapi import APIRouter, Query
from converter.converter import Converter
converter_app_router = APIRouter()


@converter_app_router.get("/converter/{type}")
def api_convert(
        type: str,
        src: str = Query(..., title="Source Unit", description="Source unit for conversion"),
        val: float = Query(..., title="Value", description="Value to be converted"),
        dst: str = Query(..., title="Destination Unit", description="Destination unit for conversion")):
    return {
        "type": type,
        "src": src,
        "val": val,
        "dst": dst,
        "Converted val": Converter.convert(type, dst, val, src)}


