#Purpose:
#DatabaseURL Location
#Connection to PostGreSQL Database
#Makes sessions --> little temporary connectgions that CRUD functions use

import os # import os is used to get environment variables, which are set outside of the code, so we don't hardcode sensitive info like passwords, like in .env
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base # allows us to work with models as objects, all objects inherit from Base (naming convention usually)
from dotenv import load_dotenv #loads env for sql alchemy stuff




from pathlib import Path # not sure what this is...

# GPT gave this to debug frontend issues
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv("DATABASE_URL")


# some debugging
print("DEBUG: DATABASE_URL =", DATABASE_URL)
print("DEBUG: Current working directory =", os.getcwd())

# engine: opens connections to databses, sends commands, fetch results, close connections
# can also reuse connections
engine = create_async_engine(DATABASE_URL, echo=True)
# we set this as async because then, we can make many requests at once
# DATABASE_URL is our connection to the database
# echo lets us decide whether we want to see all of our SQL statements we are sending to the database
# later we do engine = create_async_engine(DATABASE_URL, echo=True)



SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
#just a factory, doesn't connecrt now, but just builds recipe for building 
#new AsyncSession objects
#--> later can call SessionLoc al() to open a session
#bind=engine says to use our database engine
#saves object/database in memory

# engine is a temporary workspace with our database
# SessionLocal allows us to make sessions later with session = SessionLocal()
# This is what we do below.
# This allows us to do async functions with sessions


Base = declarative_base() # sets up our Base class for models
# We just make one model, which is task
# Base.metadata is a catalog of all ORM models that inherit from Base. 
# create_all() method creates all tables stored in this metadata by issuing the appropriate CREATE TABLE statements to the database

async def get_session():
    async with SessionLocal() as session:
        yield session #honestly, not really sure what yield does, but all I know is that it does not require us to return 
# what yield does is that is lets us get the session object and give it to our endpoint
# then endpoint runs using that session, then when it finishes, FastAPI goes back and resumes
# then, we close the connection 
# async with is used to initialize the database session  and also automatically close it after use

# I am particularly confused about how yield session allows us send it to our endpoint,
# since that implies some sort of ordered in our functions, but are we not asynchronous?

# without async with:
#session = SessionLocal()
#result = await session.execute(select(Task))
#tasks = result.scalars().all()
#await session.close() 