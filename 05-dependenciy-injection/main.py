from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

# Dependency 1: Get item_id from query param
def get_item_id(item_id: int = None):
    if item_id is None:
        raise HTTPException(status_code=400, detail="Missing item_id in query")
    return item_id

# Dependency 2: Get token from header
def get_token(x_token: str = Header(...)):
    if x_token != "mysecrettoken":
        raise HTTPException(status_code=403, detail="Invalid or missing token")
    return x_token

# Final route: depends on both dependencies above
@app.get("/favorite")
def get_favorite_item(
    token: str = Depends(get_token),
    item_id: int = Depends(get_item_id)
):
    return {
        "user": "authorized",
        "favorite_item": f"Item {item_id}"
    }
# In summary, the above code demonstrates how to use FastAPI's dependency injection system to create a route that requires both a query parameter and a header parameter. The `Depends` function is used to specify that the route depends on the two dependencies defined above. If either of the dependencies fails, an HTTPException is raised with an appropriate status code and detail message.