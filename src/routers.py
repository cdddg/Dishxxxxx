from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src import facade
from src.schemas import APISigninRequest, APISigninResponse

router = APIRouter()


@router.post(
    "/signin",
    responses={
        status.HTTP_200_OK: {"model": APISigninResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": APISigninResponse},
    },
)
def signin(body: APISigninRequest) -> APISigninResponse:
    info = facade.login(username=body.username, password=body.password)
    resp = APISigninResponse(msg=info.message)

    if info.status:
        return JSONResponse(status_code=status.HTTP_200_OK, content=resp.dict())
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, content=resp.dict()
        )
