#### Resumo do Projeto

Este projeto demonstra como configurar e utilizar views assíncronas e síncronas no Django. A aplicação inclui exemplos de requisições HTTP não bloqueantes e bloqueantes.

#### Estrutura dos Arquivos do Projeto

- **views.py**
  - Contém a lógica das views assíncronas e síncronas.
- **urls.py**
  - Mapeia as URLs para as respectivas views.
- **asgi.py**
  - Configuração do ASGI para suportar a execução assíncrona.

#### Estrutura do Projeto

- `views.py`
  ```python
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
      return HttpResponse("Requisição HTTP não bloqueante")

  def sync_view(request):
      http_call_sync()
      return HttpResponse("Requisição HTTP bloqueante")

  def home_view(request):
      return HttpResponse(
          "<br> Aula 5: Views Assíncronas com Django Async Views OK <br>"
          "127.0.0.1:8000/ - Página inicial (home_view) OK<br>"
          "127.0.0.1:8000/api/ - Requisição HTTP não bloqueante OK <br>"
          "127.0.0.1:8000/sync/ - Requisição HTTP bloqueante OK"
      )
  ```

- `urls.py`
  ```python
  from django.contrib import admin
  from django.urls import path
  from . import views

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/', views.async_view),
      path('sync/', views.sync_view),
      path('', views.home_view),
  ]
  ```

- `asgi.py`
  ```python
  import os
  from django.core.asgi import get_asgi_application

  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asyncviews.settings')

  application = get_asgi_application()
  ```

#### Configuração do Ambiente de Desenvolvimento

1. Crie o diretório do projeto e navegue até ele:
   ```bash
   mkdir mysite
   cd mysite
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv env
   source env/Scripts/activate  # No Windows
   ```

3. Instale o Django e outras dependências:
   ```bash
   pip install django uvicorn httpx
   ```

4. Crie o projeto Django:
   ```bash
   django-admin startproject asyncviews .
   ```

5. Execute as migrações iniciais:
   ```bash
   python manage.py migrate
   ```

6. Execute o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

7. (Opcional) Para executar o projeto com Uvicorn:
   ```bash
   uvicorn --reload asyncviews.asgi:application
   ```

#### Acessando as Views

- Página inicial:
  ```
  http://127.0.0.1:8000/
  ```

- View assíncrona (requisição não bloqueante):
  ```
  http://127.0.0.1:8000/api/
  ```

- View síncrona (requisição bloqueante):
  ```
  http://127.0.0.1:8000/sync/
  ```

#### Comandos Úteis

- Ativar o ambiente virtual:
  ```bash
  source env/Scripts/activate  # No Windows
  ```

- Instalar dependências:
  ```bash
  pip install -r requirements.txt
  ```

- Aplicar migrações:
  ```bash
  python manage.py migrate
  ```

- Executar o servidor com Uvicorn:
  ```bash
  uvicorn --reload asyncviews.asgi:application
  ```

### Fim do Projeto

Siga as instruções acima para configurar, executar e testar o projeto.