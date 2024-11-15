import pytest
from httpx import AsyncClient
from app.main import app

pytest_plugins = "celery.contrib.pytest"


@pytest.fixture(scope="function")
async def test_client():
    # Create an AsyncClient instance to make requests to the FastAPI api
    async with AsyncClient(
        app=app, base_url="http://test", follow_redirects=True
    ) as ac:
        yield ac


@pytest.fixture(scope="session")
def celery_config():
    return {
        "broker_url": "redis://localhost:6379/0",
        "backend_url": "redis://localhost:6379/0",
    }


@pytest.fixture
def celery_worker_parameters():
    # type: () -> Mapping[str, Any]
    """Redefine this fixture to change the init parameters of Celery workers.

    This can be used e. g. to define queues the worker will consume tasks from.

    The dict returned by your fixture will then be used
    as parameters when instantiating :class:`~celery.worker.WorkController`.
    """
    return {
        # For some reason this `celery.ping` is not registed IF our own worker is still
        # running. To avoid failing tests in that case, we disable the ping check.
        # see: https://github.com/celery/celery/issues/3642#issuecomment-369057682
        # here is the ping task: `from celery.contrib.testing.tasks import ping`
        "perform_ping_check": False,
    }


@pytest.fixture(scope="function")
def anyio_backend():
    return "asyncio"
