from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def Greeting():
    """Returns a greeting message"""
    return{
        "message": "Hello beautiful"
    }



