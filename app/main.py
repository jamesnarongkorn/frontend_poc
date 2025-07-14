from fastapi import FastAPI

from app.services import chat

app = FastAPI(title='BMA Chatbot POC')

# Include chat routes
app.include_router(chat.router, prefix='/api/v1')


@app.get('/')
async def root():
    return {'message': 'API is running'}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)
