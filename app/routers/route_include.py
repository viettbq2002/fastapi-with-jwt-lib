from fastapi import APIRouter

from ..routers import payment

router = APIRouter()

router.include_router(payment.router, prefix="/payment", tags=["payment"])
