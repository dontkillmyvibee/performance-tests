from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class DocumentDict(TypedDict):
    """
    Структура документа (tariff/contract), возвращаемого сервисом documents.
    """
    url: str
    document: str


class GetContractDocumentResponseDict(TypedDict):
    """
    Структура ответа на запрос документа контракта.
    """
    contract: DocumentDict


class GetTariffDocumentResponseDict(TypedDict):
    """
    Структура ответа на запрос документа тарифа.
    """
    tariff: DocumentDict


class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway.
    """

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Получить документ тарифа по счёту.

        :param account_id: Идентификатор счёта.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Получить документ контракта по счёту.

        :param account_id: Идентификатор счёта.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseDict:
        """
        Получить документ тарифа по счёту (высокоуровневый метод).

        Выполняет запрос к API, извлекает JSON-ответ и возвращает его в виде TypedDict-структуры.

        :param account_id: Идентификатор счёта.
        :return: JSON-ответ с данными тарифа (GetTariffDocumentResponseDict).
        """
        response = self.get_tariff_document_api(account_id)
        return response.json()

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseDict:
        """
        Получить документ контракта по счёту (высокоуровневый метод).

        Выполняет запрос к API, извлекает JSON-ответ и возвращает его в виде TypedDict-структуры.

        :param account_id: Идентификатор счёта.
        :return: JSON-ответ с данными контракта (GetContractDocumentResponseDict).
        """
        response = self.get_contract_document_api(account_id)
        return response.json()


def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())
