import pyautogui
import asyncio
import aioredis

async def main():
    # await redis = aioredis.
    redis = await aioredis.create_redis_pool(
    'redis://localhost/')
    p=pyautogui.screenshot()
    print(redis,p)
# async def main():
#     redis = await aioredis.create_redis_pool('redis://localhost')
#     await redis.set('key', 'string-value')
#     bin_value = await redis.get('key')
#     assert bin_value == b'string-value'

#     str_value = await redis.get('key', encoding='utf-8')
#     assert str_value == 'string-value'

#     redis.close()
#     await redis.wait_closed()

asyncio.run(main())
# this is the core.
#         f