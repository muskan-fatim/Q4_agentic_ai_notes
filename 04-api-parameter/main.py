from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str = Path(...)):
    return {"item_id": item_id}
# that is path parameter it's similar like setting a dynamic url according to the user input
# Path parameter is a part of the URL path that is used to identify a specific resource.

@app.get("/items")
async def read_item(item_id: str = None):
    return {"item_id": item_id}
 # that is query parameter query parameter indicate from = and ? mark sign





