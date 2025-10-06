engine = create_async_engine(DATABASE_URL, echo=True)
-->
SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession,expire_on_commit=False)




Request hits an endpoint → FastAPI gives you a session = SessionLocal().

Your code runs await session.execute(...) or session.add(...) + await session.commit().

The session asks the engine for a connection; engine gives one from the pool.

SQL is sent (you’ll see it because echo=True).

You commit/close; the session returns the connection; dependency exits and cleans up.




async def get_session():
    async with SessionLocal() as session:
        yield session
SessionLocal() creates a brand-new AsyncSession per request.
Functionally, this is our first database call, since it is our first hook. 
When the request ends, the async with block closes the session and returns the connection our pool of connections. 