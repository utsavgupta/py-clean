from fastapi import APIRouter

from py_clean.schema import APIResponse

router = APIRouter(prefix="/hello-world")


@router.get(path="/", response_model=APIResponse)
def index():

    return APIResponse(message="Hello, World")
