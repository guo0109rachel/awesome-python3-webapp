import orm
from models import User, Blog, Comment
import asyncio

loop = asyncio.get_event_loop()
async def test():
    await orm.create_pool(user='www-data', password='www-data', db='awesome', loop=loop)

    u = User(name='Administrator', email='admin@example.com', passwd='321', image='about:blank')

    await u.save()

loop.run_until_complete(test())
