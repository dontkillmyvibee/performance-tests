from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient


class IssuePhysicalCardRequestDict(TypedDict):
    """
    Структура данных для выпуска физической карты.
    """
    userId: str
    accountId: str


class IssueVirtualCardRequestDict(TypedDict):
    """
    Структура данных для выпуска виртуальной карты.
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestDict) -> Response:
        """
        Выпуск виртуальной карты.

        Выполняет POST-запрос к эндпоинту /api/v1/cards/issue-virtual-card.

        :param request: Словарь с параметрами выпуска виртуальной карты (userId, accountId).
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestDict) -> Response:
        """
        Выпуск физической карты.

        Выполняет POST-запрос к эндпоинту /api/v1/cards/issue-physical-card.

        :param request: Словарь с параметрами выпуска физической карты (userId, accountId).
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)
