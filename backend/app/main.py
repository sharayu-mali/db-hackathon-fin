from fastapi import FastAPI, Request
from rag_pipeline import generate_response

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
# Allow all origins, methods, headers (for development only)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this in production
    allow_credentials=True,
    allow_methods=["*"],  # ← This is crucial to allow OPTIONS
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    query = body['contents'][0]['parts'][0]['query']
    scenario = body['contents'][0]['parts'][0]['business']
    profile = body['contents'][0]['parts'][0]['profile']
    print("Received query:", body['contents'][0]['parts'][0]['business'],query,profile)
    response = generate_response(scenario,query, profile)
    return {"answer": response}
