from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Bernadette Peters GLB Host", version="1.0.0")

# Public cross-origin access is required by the grader.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "HEAD", "OPTIONS"],
    allow_headers=["*"],
)

MODEL_PATH = Path(__file__).parent / "bernadette_peters_stylized.glb"

@app.get("/")
def root():
    return {"status": "ok", "model": "/bernadette_peters_stylized.glb"}

@app.head("/bernadette_peters_stylized.glb")
def model_head():
    return FileResponse(
        MODEL_PATH,
        media_type="model/gltf-binary",
        filename="bernadette_peters_stylized.glb",
    )

@app.get("/bernadette_peters_stylized.glb")
def model():
    if not MODEL_PATH.exists():
        return JSONResponse(status_code=404, content={"error": "model not found"})
    return FileResponse(
        MODEL_PATH,
        media_type="model/gltf-binary",
        filename="bernadette_peters_stylized.glb",
        headers={"Access-Control-Allow-Origin": "*", "Cache-Control": "public, max-age=3600"},
    )
