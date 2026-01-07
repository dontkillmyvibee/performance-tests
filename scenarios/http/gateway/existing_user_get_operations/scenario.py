from locust import task, events
from locust.env import Environment

from clients.http.gateway.locust import GatewayHTTPTaskSet
from seeds.scenarios.existing_user_get_operations import ExistingUserGetOperationsSeedsScenario
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser


@events.init.add_listener
def init(environment: Environment, **kwargs):
    """
    Хук инициализации теста: выполнение сидинга данных.
    Создаёт 300 пользователей с кредитным счётом и историей операций.
    """
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()
    environment.seeds = seeds_scenario.load()


class GetOperationsTaskSet(GatewayHTTPTaskSet):
    """
    TaskSet для сценария получения информации об операциях существующим пользователем.
    Включает просмотр списка счетов, списка операций и статистики.
    """
    seed_user: SeedUserResult

    def on_start(self) -> None:
        """
        Выбор случайного пользователя из сгенерированных данных.
        """
        super().on_start()
        self.seed_user = self.user.environment.seeds.get_random_user()

    @task(1)
    def get_accounts(self) -> None:
        """
        Задача: получение списка счетов пользователя.
        """
        self.accounts_gateway_client.get_accounts(user_id=self.seed_user.user_id)

    @task(5)
    def get_operations(self) -> None:
        """
        Задача: получение списка операций по счёту.
        """
        self.operations_gateway_client.get_operations(
            account_id=self.seed_user.credit_card_accounts[0].account_id
        )

    @task(2)
    def get_operations_summary(self) -> None:
        """
        Задача: получение статистики по операциям для счёта.
        """
        self.operations_gateway_client.get_operations_summary(
            account_id=self.seed_user.credit_card_accounts[0].account_id
        )


class GetOperationsScenarioUser(LocustBaseUser):
    """
    Виртуальный пользователь для сценария получения операций.
    """
    tasks = [GetOperationsTaskSet]

