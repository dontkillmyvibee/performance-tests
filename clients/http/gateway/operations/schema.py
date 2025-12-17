from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class OperationType(StrEnum):
    """
    Тип операции.

    Значения должны совпадать с тем, что возвращает API.
    """

    FEE = "FEE"
    TOP_UP = "TOP_UP"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    PURCHASE = "PURCHASE"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    """
    Статус операции.

    Значения должны совпадать с тем, что ожидает/возвращает API.
    """

    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    UNSPECIFIED = "UNSPECIFIED"


class OperationsBaseModel(BaseModel):
    """
    Базовая модель для схем operations.

    populate_by_name=True позволяет принимать данные как по имени поля,
    так и по алиасу (если поле имеет Field(alias=...)).
    """

    model_config = ConfigDict(populate_by_name=True)


class OperationSchema(OperationsBaseModel):
    """
    Описание структуры операции.
    """

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: datetime = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(OperationsBaseModel):
    """
    Описание структуры чека (receipt) по операции.
    """

    url: HttpUrl
    document: str


class OperationsSummarySchema(OperationsBaseModel):
    """
    Описание структуры статистики (summary) по операциям.
    """

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class GetOperationsQuerySchema(OperationsBaseModel):
    """
    Query-параметры для получения списка операций по счёту.
    """

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(OperationsBaseModel):
    """
    Query-параметры для получения статистики по операциям по счёту.
    """

    account_id: str = Field(alias="accountId")


class MakeOperationRequestSchema(OperationsBaseModel):
    """
    Базовая структура тела запроса для создания операции.
    """

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Тело запроса для создания операции комиссии.
    """


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Тело запроса для создания операции пополнения.
    """


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Тело запроса для создания операции кэшбэка.
    """


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Тело запроса для создания операции перевода.
    """


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Тело запроса для создания операции покупки.
    """

    category: str


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Тело запроса для создания операции оплаты по счёту.
    """


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Тело запроса для создания операции снятия наличных денег.
    """


class GetOperationsResponseSchema(OperationsBaseModel):
    """
    Ответ получения списка операций.
    """

    operations: list[OperationSchema]


class GetOperationResponseSchema(OperationsBaseModel):
    """
    Ответ получения операции.
    """

    operation: OperationSchema


class GetOperationReceiptResponseSchema(OperationsBaseModel):
    """
    Ответ получения чека по операции.
    """

    receipt: OperationReceiptSchema


class GetOperationsSummaryResponseSchema(OperationsBaseModel):
    """
    Ответ получения статистики (summary) по операциям.
    """

    summary: OperationsSummarySchema


class MakeFeeOperationResponseSchema(OperationsBaseModel):
    """
    Ответ создания операции комиссии.
    """

    operation: OperationSchema


class MakeTopUpOperationResponseSchema(OperationsBaseModel):
    """
    Ответ создания операции пополнения.
    """

    operation: OperationSchema


class MakeCashbackOperationResponseSchema(OperationsBaseModel):
    """
    Ответ создания операции кэшбэка.
    """

    operation: OperationSchema


class MakeTransferOperationResponseSchema(OperationsBaseModel):
    """
    Ответ создания операции перевода.
    """

    operation: OperationSchema


class MakePurchaseOperationResponseSchema(OperationsBaseModel):
    """
    Ответ создания операции покупки.
    """

    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(OperationsBaseModel):
    """
    Ответ создания операции оплаты по счёту.
    """

    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(OperationsBaseModel):
    """
    Ответ создания операции снятия наличных денег.
    """

    operation: OperationSchema
