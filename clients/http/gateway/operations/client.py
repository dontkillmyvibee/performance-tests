from typing import TypedDict

from httpx import QueryParams, Response

from clients.http.client import HTTPClient


class GetOperationsQueryDict(TypedDict):
    """
    Структура query-параметров для получения списка операций по счёту.
    """
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура query-параметров для получения статистики по операциям по счёту.
    """
    accountId: str


class MakeOperationRequestDict(TypedDict):
    """
    Базовая структура тела запроса для создания операции.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """
    Структура тела запроса для создания операции комиссии.
    """


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
    Структура тела запроса для создания операции пополнения.
    """


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """
    Структура тела запроса для создания операции кэшбэка.
    """


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
    Структура тела запроса для создания операции перевода.
    """


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура тела запроса для создания операции покупки.
    """
    category: str


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """
    Структура тела запроса для создания операции оплаты по счёту.
    """


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """
    Структура тела запроса для создания операции снятия наличных денег.
    """


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id.

        Выполняет GET-запрос к эндпоинту /api/v1/operations/{operation_id}.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id.

        Выполняет GET-запрос к эндпоинту /api/v1/operations/operation-receipt/{operation_id}.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получение списка операций для определённого счёта.

        Выполняет GET-запрос к эндпоинту /api/v1/operations.

        :param query: Query-параметры запроса (например, accountId).
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Получение статистики по операциям для определённого счёта.

        Выполняет GET-запрос к эндпоинту /api/v1/operations/operations-summary.

        :param query: Query-параметры запроса (например, accountId).
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Создание операции комиссии.

        Выполняет POST-запрос к эндпоинту /api/v1/operations/make-fee-operation.

        :param request: Тело запроса на создание операции комиссии.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Создание операции пополнения.

        Выполняет POST-запрос к эндпоинту /api/v1/operations/make-top-up-operation.

        :param request: Тело запроса на создание операции пополнения.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Создание операции кэшбэка.

        Выполняет POST-запрос к эндпоинту /api/v1/operations/make-cashback-operation.

        :param request: Тело запроса на создание операции кэшбэка.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Создание операции перевода.

        Выполняет POST-запрос к эндпоинту /api/v1/operations/make-transfer-operation.

        :param request: Тело запроса на создание операции перевода.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создание операции покупки.

        Выполняет POST-запрос к эндпоинту /api/v1/operations/make-purchase-operation.

        :param request: Тело запроса на создание операции покупки.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Создание операции оплаты по счёту.

        Выполняет POST-запрос к эндпоинту /api/v1/operations/make-bill-payment-operation.

        :param request: Тело запроса на создание операции оплаты по счёту.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Создание операции снятия наличных денег.

        Выполняет POST-запрос к эндпоинту /api/v1/operations/make-cash-withdrawal-operation.

        :param request: Тело запроса на создание операции снятия наличных денег.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)
