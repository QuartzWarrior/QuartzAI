from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json
from utils.key_check import check_api_key
app = FastAPI()

@app.get("/v1/models")
def models():
    with open('models.json') as f:
        models = json.load(f)
        return JSONResponse(content=models, media_type="application/json")
    

@app.post("/v1/chat/completions")
async def chat_completions(
    authorization: str = Header(None),
    content_type: str = Header(None)
):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid Authorization format")
    if content_type is None:
        raise HTTPException(status_code=415, detail="Missing Content-Type header")
    
    if content_type != "application/json":
        raise HTTPException(status_code=415, detail="Invalid Content-Type. Must be application/json")

    api_key = authorization.split(" ")[1]
    auth_result = check_api_key(api_key)
    
    if auth_result["status"] == "error":
        raise HTTPException(status_code=401, detail=auth_result["message"])
    
    return JSONResponse(content={"status": "success", "message": "API key is valid."})



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)