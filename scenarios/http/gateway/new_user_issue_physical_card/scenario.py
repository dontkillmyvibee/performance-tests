from locust import task
from clients.http.gateway.locust import GatewayHTTPSequentialTaskSet
from clients.http.gateway.users.schema import CreateUserResponseSchema
from clients.http.gateway.accounts.schema import OpenDebitCardAccountResponseSchema
from tools.locust.user import LocustBaseUser


class IssuePhysicalCardSequentialTaskSet(GatewayHTTPSequentialTaskSet):
    """
    Последовательный сценарий для выпуска физической карты новым пользователем.
    Шаги:
    1. Создание нового пользователя.
    2. Открытие дебетового счета.
    3. Выпуск физической карты.
    """

    create_user_response: CreateUserResponseSchema
    open_account_response: OpenDebitCardAccountResponseSchema

    @task
    def create_user(self) -> None:
        """
        Шаг 1: Создание нового пользователя.
        """
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_card_account(self) -> None:
        """
        Шаг 2: Открытие дебетового счета для созданного пользователя.
        """
        self.open_account_response = self.accounts_gateway_client.open_debit_card_account(
            user_id=self.create_user_response.user.id
        )

    @task
    def issue_physical_card(self) -> None:
        """
        Шаг 3: Выпуск физической карты, привязанной к открытому счету.
        """
        self.cards_gateway_client.issue_physical_card(
            user_id=self.create_user_response.user.id,
            account_id=self.open_account_response.account.id
        )


class IssuePhysicalCardScenarioUser(LocustBaseUser):
    """
    Виртуальный пользователь для сценария выпуска физической карты.
    """
    tasks = [IssuePhysicalCardSequentialTaskSet]
