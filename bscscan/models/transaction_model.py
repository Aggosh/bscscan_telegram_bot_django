from django.db import models

from bscscan.models import Address


class Transaction(models.Model):
    from_address = models.ForeignKey(
        Address,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="from_address",
    )
    to_address = models.ForeignKey(
        Address,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="to_address",
    )

    type = models.CharField(max_length=77, blank=False, null=False)
    block_number = models.BigIntegerField(blank=False, null=False, unique=True)
    time_stamp = models.DateTimeField(blank=False, null=False)
    hash = models.CharField(max_length=77, blank=False, null=False)
    nonce = models.BigIntegerField(blank=True, null=True)
    block_hash = models.CharField(max_length=77, blank=False, null=False)
    transaction_index = models.BigIntegerField(blank=True, null=True)
    value = models.BigIntegerField(blank=False, null=False)
    gas = models.BigIntegerField(blank=False, null=False)
    gas_price = models.BigIntegerField(blank=False, null=False)
    is_error = models.BooleanField(blank=True, null=True)
    txreceipt_status = models.BooleanField(blank=True, null=True)
    input = models.TextField()
    contract_address = models.TextField()
    cumulative_gas_used = models.BigIntegerField(blank=False, null=False)
    gas_used = models.BigIntegerField(blank=False, null=False)
    confirmations = models.BigIntegerField(blank=False, null=False)
    method_id = models.CharField(max_length=70, blank=True, null=True)
    function_name = models.TextField(blank=True, null=True)
    token_name = models.CharField(max_length=70, blank=True, null=True)
    token_symbol = models.CharField(max_length=70, blank=True, null=True)
    token_decimal = models.BigIntegerField(blank=True, null=True)
    transaction_type = models.CharField(max_length=70, blank=True, null=True)
    error_code = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self):
        return f"{self.from_address} -> {self.to_address}"
