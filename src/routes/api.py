from fastapi import APIRouter
from src.routes import todos_routes
from src.routes import health_check

router = APIRouter()
router.include_router(health_check.router)
router.include_router(todos_routes.router)

# this is a bit too much for this small application but in the future if we have
# more resources it's more organized, you just need to add another file with
# all the routers for the new resource and this line

# router.include_router(newresource_routes.router)
