from typing import TypedDict

from httpx import QueryParams, Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """
    Описание структуры операции.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationReceiptDict(TypedDict):
    """
    Описание структуры чека (receipt) по операции.
    """
    url: str
    document: str


class OperationsSummaryDict(TypedDict):
    """
    Описание структуры статистики (summary) по операциям.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationsResponseDict(TypedDict):
    """
    Описание структуры ответа получения списка операций.
    """
    operations: list[OperationDict]


class GetOperationReceiptResponseDict(TypedDict):
    """
    Описание структуры ответа получения чека по операции.
    """
    receipt: OperationReceiptDict


class GetOperationResponseDict(TypedDict):
    """
    Описание структуры ответа получения операции.
    """
    operation: OperationDict


class GetOperationsSummaryResponseDict(TypedDict):
    """
    Описание структуры ответа получения статистики (summary) по операциям.
    """
    summary: OperationsSummaryDict


class MakeFeeOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции комиссии.
    """
    operation: OperationDict


class MakeTopUpOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции пополнения.
    """
    operation: OperationDict


class MakeCashbackOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции кэшбэка.
    """
    operation: OperationDict


class MakeTransferOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции перевода.
    """
    operation: OperationDict


class MakePurchaseOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции покупки.
    """
    operation: OperationDict


class MakeBillPaymentOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции оплаты по счёту.
    """
    operation: OperationDict


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции снятия наличных.
    """
    operation: OperationDict


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

    def get_operation(self, operation_id: str) -> GetOperationsResponseDict:
        """
        Высокоуровневый метод: получить информацию об операции по её идентификатору.

        :param operation_id: Идентификатор операции.
        :return: JSON-ответ API, приведённый к TypedDict.
        """
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        """
        Высокоуровневый метод: получить чек (receipt) по операции.

        :param operation_id: Идентификатор операции.
        :return: JSON-ответ API, приведённый к TypedDict.
        """
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """
        Высокоуровневый метод: получить список операций по счёту.

        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API со списком операций.
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        """
        Высокоуровневый метод: получить статистику (summary) по операциям для счёта.

        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API со статистикой по операциям.
        """
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        """
        Высокоуровневый метод: создать операцию комиссии.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API с созданной операцией.
        """
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        """
        Высокоуровневый метод: создать операцию пополнения счёта.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API с созданной операцией.
        """
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        """
        Высокоуровневый метод: создать операцию кэшбэка.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API с созданной операцией.
        """
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        """
        Высокоуровневый метод: создать операцию перевода.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API с созданной операцией.
        """
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        """
        Высокоуровневый метод: создать операцию покупки.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API с созданной операцией.
        """
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
            category="test"
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        """
        Высокоуровневый метод: создать операцию оплаты по счёту.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API с созданной операцией.
        """
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        """
        Высокоуровневый метод: создать операцию снятия наличных денег.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API с созданной операцией.
        """
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
