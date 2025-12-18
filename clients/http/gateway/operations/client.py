from httpx import QueryParams, Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import (
    GetOperationReceiptResponseSchema,
    GetOperationResponseSchema,
    GetOperationsQuerySchema,
    GetOperationsResponseSchema,
    GetOperationsSummaryQuerySchema,
    GetOperationsSummaryResponseSchema,
    MakeBillPaymentOperationRequestSchema,
    MakeBillPaymentOperationResponseSchema,
    MakeCashWithdrawalOperationRequestSchema,
    MakeCashWithdrawalOperationResponseSchema,
    MakeCashbackOperationRequestSchema,
    MakeCashbackOperationResponseSchema,
    MakeFeeOperationRequestSchema,
    MakeFeeOperationResponseSchema,
    MakePurchaseOperationRequestSchema,
    MakePurchaseOperationResponseSchema,
    MakeTopUpOperationRequestSchema,
    MakeTopUpOperationResponseSchema,
    MakeTransferOperationRequestSchema,
    MakeTransferOperationResponseSchema,
)


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

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Получение списка операций для определённого счёта.

        Выполняет GET-запрос к эндпоинту /api/v1/operations.

        :param query: Query-параметры запроса (например, accountId).
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            "/api/v1/operations",
            params=QueryParams(**query.model_dump(by_alias=True)),
        )

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Получение статистики по операциям для определённого счёта.

        Выполняет GET-запрос к эндпоинту /api/v1/operations/operations-summary.

        :param query: Query-параметры запроса (например, accountId).
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            "/api/v1/operations/operations-summary",
            params=QueryParams(**query.model_dump(by_alias=True)),
        )

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        Создание операции комиссии.

        Выполняет POST-запрос к эндпоинту /api/v1/operations/make-fee-operation.

        :param request: Тело запроса на создание операции комиссии.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            "/api/v1/operations/make-fee-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Создание операции пополнения.

        Выполняет POST-запрос к эндпоинту /api/v1/operations/make-top-up-operation.

        :param request: Тело запроса на создание операции пополнения.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            "/api/v1/operations/make-top-up-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        Создание операции кэшбэка.

        Выполняет POST-запрос к эндпоинту /api/v1/operations/make-cashback-operation.

        :param request: Тело запроса на создание операции кэшбэка.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            "/api/v1/operations/make-cashback-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Создание операции перевода.

        Выполняет POST-запрос к эндпоинту /api/v1/operations/make-transfer-operation.

        :param request: Тело запроса на создание операции перевода.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            "/api/v1/operations/make-transfer-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Создание операции покупки.

        Выполняет POST-запрос к эндпоинту /api/v1/operations/make-purchase-operation.

        :param request: Тело запроса на создание операции покупки.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            "/api/v1/operations/make-purchase-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestSchema) -> Response:
        """
        Создание операции оплаты по счёту.

        Выполняет POST-запрос к эндпоинту /api/v1/operations/make-bill-payment-operation.

        :param request: Тело запроса на создание операции оплаты по счёту.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            "/api/v1/operations/make-bill-payment-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_cash_withdrawal_operation_api(
        self,
        request: MakeCashWithdrawalOperationRequestSchema,
    ) -> Response:
        """
        Создание операции снятия наличных денег.

        Выполняет POST-запрос к эндпоинту /api/v1/operations/make-cash-withdrawal-operation.

        :param request: Тело запроса на создание операции снятия наличных денег.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            "/api/v1/operations/make-cash-withdrawal-operation",
            json=request.model_dump(by_alias=True),
        )

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        """
        Высокоуровневый метод: получить информацию об операции по её идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Ответ API, валидированный в Pydantic-модель.
        """
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        """
        Высокоуровневый метод: получить чек (receipt) по операции.

        :param operation_id: Идентификатор операции.
        :return: Ответ API, валидированный в Pydantic-модель.
        """
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        """
        Высокоуровневый метод: получить список операций по счёту.

        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API со списком операций.
        """
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        """
        Высокоуровневый метод: получить статистику (summary) по операциям для счёта.

        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API со статистикой по операциям.
        """
        query = GetOperationsSummaryQuerySchema(account_id=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        """
        Высокоуровневый метод: создать операцию комиссии.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API с созданной операцией.
        """
        request = MakeFeeOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeTopUpOperationResponseSchema:
        """
        Высокоуровневый метод: создать операцию пополнения счёта.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API с созданной операцией.
        """
        request = MakeTopUpOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeCashbackOperationResponseSchema:
        """
        Высокоуровневый метод: создать операцию кэшбэка.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API с созданной операцией.
        """
        request = MakeCashbackOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeTransferOperationResponseSchema:
        """
        Высокоуровневый метод: создать операцию перевода.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API с созданной операцией.
        """
        request = MakeTransferOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakePurchaseOperationResponseSchema:
        """
        Высокоуровневый метод: создать операцию покупки.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API с созданной операцией.
        """
        request = MakePurchaseOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeBillPaymentOperationResponseSchema:
        """
        Высокоуровневый метод: создать операцию оплаты по счёту.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API с созданной операцией.
        """
        request = MakeBillPaymentOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeCashWithdrawalOperationResponseSchema:
        """
        Высокоуровневый метод: создать операцию снятия наличных денег.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: JSON-ответ API с созданной операцией.
        """
        request = MakeCashWithdrawalOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
