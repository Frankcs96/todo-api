from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health Check"],
)


@router.get("")
async def root():
    return {"health": True}
