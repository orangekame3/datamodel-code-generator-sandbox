from fastapi import APIRouter, HTTPException
from ..schemas.hello import SayHelloResponse  # type: ignore
from ..schemas.error import InternalServerError

router: APIRouter = APIRouter()

@router.get("/hello/{name}", response_model=SayHelloResponse)
def say_hello(name: str) -> SayHelloResponse:
    try:
        return SayHelloResponse(message=f"Hello, {name}!")
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=InternalServerError(message=str(e)).model_dump()
        )
