import json
from fastapi import APIRouter, HTTPException, Request, responses
from app.configs.config import settings
import stripe

router = APIRouter()
stripe.api_key = settings.STRIPE_API_KEY


@router.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    event = None
    try:
        event = stripe.Event.construct_from(json.loads(payload), stripe.api_key)
    except ValueError as e:
        # Invalid payload
        raise HTTPException(status_code=400, detail=str(e))
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        raise HTTPException(status_code=400, detail=str(e))
        return
    if event["type"] == "checkout.session.completed":
        print("Payment was successful.")
        print(event["data"]["object"])


@router.get("/checkout")
async def checkout_session(product_id: str, quantity: int = 1):
    product = get_product(product_id)
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                "price": product["default_price"],
                "quantity": quantity,
            }
        ],
        mode="payment",
        success_url=settings.BASE_URL + "/success",
        cancel_url=settings.BASE_URL + "/cancel",
    )
    return responses.RedirectResponse(checkout_session.url, status_code=303)


@router.get("/products")
async def get_products():
    return stripe.Product.list()


def get_product(id):
    product = stripe.Product.retrieve(id)
    return product


