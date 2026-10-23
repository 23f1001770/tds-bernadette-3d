# Bernadette Peters GLB host

A small FastAPI service that serves the GLB file with public CORS headers.

## Render settings
- Runtime: Python
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

After deployment, submit the direct model URL:
`https://YOUR-SERVICE.onrender.com/bernadette_peters_stylized.glb`

Check that the URL returns the binary model, not an HTML viewer page.
