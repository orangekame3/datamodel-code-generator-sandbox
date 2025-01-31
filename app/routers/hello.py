from fastapi import APIRouter
from ..schemas.hello import SayHelloResponse  # type: ignore
from ..schemas.error import InternalServerError

router: APIRouter = APIRouter()

@router.get("/hello/{name}", response_model=SayHelloResponse | InternalServerError)
def say_hello(name: str) -> SayHelloResponse | InternalServerError:
    try:
        return SayHelloResponse(message=f"Hello, {name}!")
    except Exception as e:
        return InternalServerError(message=str(e))
