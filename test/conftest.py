import pytest
from app import create_app
from app.models import blog_storage

# 🧪 Fixture que crea una instancia de la aplicación para testing
@pytest.fixture
def app():
    """
    Crea la aplicación en modo testing.

    ¿Qué es un fixture?
    - Función que prepara datos/objetos para las pruebas
    - Se ejecuta antes de cada test que lo necesite
    - Garantiza un estado limpio para cada prueba
    """
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # Desactivar CSRF para testing
    return app

# 🌐 Fixture que crea un cliente de testing para hacer peticiones HTTP
@pytest.fixture
def client(app):
    """
    Simula un navegador web para realizar pruebas HTTP.

    ¿Para qué sirve?
    - Permite hacer GET, POST, PUT, DELETE
    - No necesita servidor real corriendo
    """
    return app.test_client()

# 💻 Fixture para testing de comandos CLI (si se usan)
@pytest.fixture
def runner(app):
    """
    Proporciona un runner para ejecutar comandos CLI durante tests.
    """
    return app.test_cli_runner()

# 🔁 Fixture que resetea el almacenamiento antes de cada test
@pytest.fixture(autouse=True)
def reset_storage():
    """
    Resetea el almacenamiento de posts antes de cada test.

    ¿Por qué usar autouse=True?
    - Se ejecuta automáticamente antes de cada test
    - Garantiza que cada test empiece con datos limpios
    - Evita que los tests se afecten entre sí
    """
    blog_storage._posts.clear()
    blog_storage._next_id = 1
    blog_storage._create_sample_posts()
    yield  # Aquí se ejecuta el test
    # Cleanup (si se necesitara después del test)
    pass