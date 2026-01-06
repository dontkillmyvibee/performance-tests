from locust import HttpUser, task, between
from clients.http.gateway.locust import GatewayHTTPTaskSet
from clients.http.gateway.users.schema import CreateUserResponseSchema


class GetAccountsTaskSet(GatewayHTTPTaskSet):
    """
    TaskSet для сценария получения счетов через HTTP.
    Включает создание пользователя, открытие депозита и получение списка счетов.
    """

    create_user_response: CreateUserResponseSchema | None = None

    @task(2)
    def create_user(self) -> None:
        """
        Задача создания пользователя.
        """
        self.create_user_response = self.users_gateway_client.create_user()

    @task(2)
    def open_deposit_account(self) -> None:
        """
        Задача открытия депозитного счета.
        Выполняется только если пользователь создан.
        """
        if self.create_user_response:
            self.accounts_gateway_client.open_deposit_account(
                user_id=self.create_user_response.user.id
            )

    @task(6)
    def get_accounts(self) -> None:
        """
        Задача получения списка счетов.
        Выполняется только если пользователь создан.
        """
        if self.create_user_response:
            self.accounts_gateway_client.get_accounts(
                user_id=self.create_user_response.user.id
            )


class GetAccountsUser(HttpUser):
    """
    Виртуальный пользователь для HTTP сценария.
    """
    host = "localhost"
    tasks = [GetAccountsTaskSet]
    wait_time = between(1, 3)
