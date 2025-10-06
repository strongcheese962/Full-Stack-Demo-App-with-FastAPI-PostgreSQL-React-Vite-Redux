# main.py
# acts as our entry point to:
# start Fastapi app
# include tasks.py routes
# create tabels based on models.py when we start


from fastapi import FastAPI
from .database import engine, Base
from . import schemas # relative import since everything is in the same backend file
from . import models
from . import tasks
from fastapi.middleware.cors import CORSMiddleware # no idea what this is, but this was for debugging with frontend issues




app = FastAPI() # we build our FastAPI instance/boject

# No idea what this is, but this was for debugging with frontend issues
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development, allow everything
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(tasks.router) ## I wanted to see this schema as well on the webpage when building file-by-file

# Without decorator
#def ping():
    #return {"message": "pong"}
#app.add_route("/ping", ping, methods=["GET"])

# So basically the decorator makes it so that we don't need to do the above add_route thing, automatically does it for us
# Above is incorrect. Decorator simply runs the function automaticlaly when our app is instantiated


# This is our hook
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn: # async allows us to use await
        await conn.run_sync(Base.metadata.create_all) # Base.metadata.create_all creates all tables based on models.py, since we also imported base from database.py

# we earlier importated engine from database, so we have:
# engine = create_async_engine(DATABASE_URL, echo=True)
# SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


# These are our GET endpoints
@app.get("/ping")
async def ping(): # async is not really necessary here
    return {"message": "ping working!!!"}

@app.get("/hello")
def say_hello():
    return {"message": "Hi! :)"}

# initially confusing how the paramters are for GET functions, but clarified that we can do however we like, since FastAPI autommatically does for us
@app.get("/test_schema", response_model=schemas.TaskResponse) # response_model makes sure that the output matches the schema
async def test_schema(): # this defines the endpoint function, this is just like fake data
    return {
        "id": 1,
        "title": "Demo",
        "description": "testing schema",
        "created_at": "2025-10-05T12:00:00"
    }