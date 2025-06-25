from fastapi import APIRouter

from py_clean.routes.v1.hello_world import router as hw_router

router = APIRouter(prefix="/v1")
router.include_router(hw_router)

__all__ = ["router"]
