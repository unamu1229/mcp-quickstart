from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage
import os

app = FastAPI(title="LangChain FastAPI", description="A simple AI API using LangChain and FastAPI")

class ChatRequest(BaseModel):
    message: str
    temperature: float = 0.7

class ChatResponse(BaseModel):
    response: str

# Initialize LangChain components
def get_llm():
    try:
        # Use OpenAI ChatGPT (requires OPENAI_API_KEY environment variable)
        llm = ChatOpenAI(temperature=0.7)
        return llm
    except Exception as e:
        print(f"Error initializing LLM: {e}")
        return None

@app.get("/")
async def root():
    return {"message": "LangChain FastAPI is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        llm = get_llm()
        if llm is None:
            raise HTTPException(status_code=500, detail="LLM not available")
        
        prompt = f"あなたは親切なAIアシスタントです。以下の質問に日本語で答えてください:\n\n{request.message}"
        messages = [HumanMessage(content=prompt)]
        response = llm.invoke(messages)
        return ChatResponse(response=response.content)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)