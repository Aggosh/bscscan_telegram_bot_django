from bot_conf.celery import app


from bscscan.models import Address
from bscscan.managers import Parser


@app.task(
    time_limit=600,
    resultrepr_maxsize=100000,
)
def update_following_addresses():
    addresses = Address.objects.filter(user__isnull=False)
    for address in addresses:
        update_address.delay({"address": address.name, "page": 1, "offset": 100})


@app.task(
    time_limit=600,
    resultrepr_maxsize=100000,
)
def update_address(payload: dict):
    parser = Parser()
    parser.scrap_and_save_transaction(payload=payload)
