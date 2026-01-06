from locust import User, task, between
from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse


class GetAccountsTaskSet(GatewayGRPCTaskSet):
    """
    TaskSet для сценария получения счетов через gRPC.
    Включает создание пользователя, открытие депозита и получение списка счетов.
    """

    create_user_response: CreateUserResponse | None = None

    @task(2)
    def create_user(self) -> None:
        """
        Задача создания пользователя через gRPC.
        """
        self.create_user_response = self.users_gateway_client.create_user()

    @task(2)
    def open_deposit_account(self) -> None:
        """
        Задача открытия депозитного счета через gRPC.
        Выполняется только если пользователь создан.
        """
        if self.create_user_response:
            self.accounts_gateway_client.open_deposit_account(
                user_id=self.create_user_response.user.id
            )

    @task(6)
    def get_accounts(self) -> None:
        """
        Задача получения списка счетов через gRPC.
        Выполняется только если пользователь создан.
        """
        if self.create_user_response:
            self.accounts_gateway_client.get_accounts(
                user_id=self.create_user_response.user.id
            )


class GetAccountsUser(User):
    """
    Виртуальный пользователь для gRPC сценария.
    """
    host = "localhost"
    tasks = [GetAccountsTaskSet]
    wait_time = between(1, 3)
