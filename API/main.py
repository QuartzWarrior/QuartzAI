from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json
from utils.key_check import check_api_key
from providers.one import text_gen
from typing import List
import logging

app = FastAPI()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    model: str

@app.get("/v1/models")
def models():
    with open('models.json') as f:
        models = json.load(f)
        return JSONResponse(content=models, media_type="application/json")
    
@app.post("/v1/chat/completions")
async def chat_completions(
    authorization: str = Header(None),
    content_type: str = Header(None),
    chat_request: ChatRequest = None,
    stream: bool = False
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
    if not chat_request or not chat_request.messages or not chat_request.model:
        raise HTTPException(status_code=400, detail="Missing messages or model in request body")
    messages_list = [{"role": msg.role, "content": msg.content} for msg in chat_request.messages]
    try:
        completion = text_gen(messages_list, chat_request.model, stream=stream)
        return JSONResponse(content=completion)

    except ValueError as e:
        raise HTTPException(status_code=404, detail={
            "status": "error",
            "message": str(e)
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)