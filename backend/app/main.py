from fastapi import FastAPI

app = FastAPI(title="My-RPA")


@app.get("/health")
def health():
    return {"ok": True, "app": "My-RPA"}
