import asyncio
import httpx
from django.http import HttpResponse


async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)


async def print_numbers():
    for num in range(1000, 1010):
        await asyncio.sleep(2)
        print(num)


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    loop.create_task(print_numbers())

    return HttpResponse('Non-blocking HTTP request')

