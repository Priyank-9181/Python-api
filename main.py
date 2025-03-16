from fastapi import FastAPI

from ollama import chat
from ollama import ChatResponse


app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/test")
def test(prompt: str):
    response: ChatResponse = chat(
        model="llama3.2:1b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    print(response["message"]["content"])
    # or access fields directly from the response object
    print(response.message.content)
    return {"message": prompt, "response": response.message.content}
