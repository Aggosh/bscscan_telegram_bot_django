from datetime import datetime
from django.utils.timezone import make_aware
from bscscan.models import Transaction, Address
from bscscan.managers import Scrapper


class Parser:
    def save_results(self, results: dict) -> None:
        for key in results.keys():
            for transaction in results[key]:
                if type(transaction) == str:
                    continue

                # Отримайте або створіть об'єкт Transaction за номером блоку
                block_number = int(transaction.get("blockNumber"))
                trn, created = Transaction.objects.get_or_create(
                    block_number=block_number,
                    defaults={
                        "from_address": Address.objects.get_or_create(
                            name=transaction.get("from")
                        )[0],
                        "to_address": Address.objects.get_or_create(
                            name=transaction.get("to")
                        )[0],
                        "type": key,
                        "time_stamp": make_aware(
                            datetime.fromtimestamp(int(transaction.get("timeStamp")))
                        ),
                        "hash": transaction.get("hash"),
                        "nonce": int(transaction.get("nonce")),
                        "block_hash": transaction.get("blockHash"),
                        "transaction_index": int(transaction.get("transactionIndex")),
                        "value": int(transaction.get("value")),
                        "gas": int(transaction.get("gas")),
                        "gas_price": int(transaction.get("gasPrice")),
                        "is_error": transaction.get("isError"),
                        "txreceipt_status": transaction.get("txreceipt_status"),
                        "input": transaction.get("input"),
                        "contract_address": transaction.get("contractAddress"),
                        "cumulative_gas_used": transaction.get("cumulativeGasUsed"),
                        "gas_used": int(transaction.get("gasUsed")),
                        "confirmations": transaction.get("confirmations"),
                        "method_id": transaction.get("methodId"),
                        "function_name": transaction.get("functionName"),
                        "token_name": transaction.get("tokenName"),
                        "token_symbol": transaction.get("tokenSymbol"),
                        "token_decimal": transaction.get("tokenDecimal"),
                        "transaction_type": transaction.get("type"),
                        "error_code": transaction.get("errCode"),
                    },
                )

                if not created:
                    trn.time_stamp = make_aware(
                        datetime.fromtimestamp(int(transaction.get("timeStamp")))
                    )
                    trn.hash = transaction.get("hash")
                    trn.block_hash = transaction.get("blockHash")
                    trn.is_error = (transaction.get("isError"),)
                    trn.txreceipt_status = (transaction.get("txreceipt_status"),)
                    trn.confirmations = (transaction.get("confirmations"),)
                    trn.save()

    def scrap_and_save_transaction(self, payload: dict) -> None:
        scrapper = Scrapper()
        results = scrapper.scrap_transaction(payload)
        self.save_results(results)
