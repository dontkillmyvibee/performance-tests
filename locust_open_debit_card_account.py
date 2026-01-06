from locust import User, task, between
from clients.http.gateway.users.client import (
    build_users_gateway_locust_http_client,
    UsersGatewayHTTPClient,
    CreateUserResponseSchema
)
from clients.http.gateway.accounts.client import (
    build_accounts_gateway_locust_http_client,
    AccountsGatewayHTTPClient
)


class OpenDebitCardAccountScenarioUser(User):
    """
    Класс виртуального пользователя для сценария открытия дебетового счета через API клиенты.
    """
    host = "localhost"

    wait_time = between(1, 3)

    users_gateway_client: UsersGatewayHTTPClient
    accounts_gateway_client: AccountsGatewayHTTPClient
    create_user_response: CreateUserResponseSchema

    def on_start(self) -> None:
        """
        Инициализация клиентов и создание пользователя при старте сессии.
        """
        self.users_gateway_client = build_users_gateway_locust_http_client(self.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.environment)

        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_card_account(self) -> None:
        """
        Задача открытия дебетового счета через API клиент.
        """
        self.accounts_gateway_client.open_debit_card_account(user_id=self.create_user_response.user.id)
