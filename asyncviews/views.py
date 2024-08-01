import asyncio
from time import sleep
import httpx
from django.http import HttpResponse

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)

def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org/")
    print(r)

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")

def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")

def home_view(request):
    return HttpResponse(
        "<br> Aula 5: Views Assíncronas com Django Async Views OK <br>"
        "127.0.0.1:8000/ - Página inicial (home_view) OK<br>"
        "127.0.0.1:8000/api/ - Requisição HTTP não-bloqueante OK <br>"
        "127.0.0.1:8000/sync/ - Requisição HTTP bloqueante OK"
    )