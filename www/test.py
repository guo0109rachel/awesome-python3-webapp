import orm
from models import User, Blog, Comment
import asyncio

loop = asyncio.get_event_loop()
async def test():
    await orm.create_pool(user='root', password='password', db='awesome', loop=loop)

    u = User(name='Administrator', email='admin@example.com', admin = True, passwd='1234567890', image='about:blank')

    await u.save()

loop.run_until_complete(test())
