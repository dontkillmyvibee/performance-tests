from locust import task, events
from locust.env import Environment

from clients.http.gateway.locust import GatewayHTTPTaskSet
from seeds.scenarios.existing_user_issue_virtual_card import ExistingUserIssueVirtualCardSeedsScenario
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser


@events.init.add_listener
def init(environment: Environment, **kwargs):
    """
    Хук инициализации теста: выполнение сидинга данных.
    Создаёт 300 пользователей с дебетовым счётом.
    """
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenario.build()
    environment.seeds = seeds_scenario.load()


class IssueVirtualCardTaskSet(GatewayHTTPTaskSet):
    """
    TaskSet для сценария выпуска новой виртуальной карты существующим пользователем.
    """
    seed_user: SeedUserResult

    def on_start(self) -> None:
        """
        Выбор случайного пользователя из сгенерированных данных.
        """
        super().on_start()
        self.seed_user = self.user.environment.seeds.get_random_user()

    @task(5)
    def get_accounts(self) -> None:
        """
        Задача: получение списка счетов пользователя.
        Пользователь проверяет состояние своих счетов и карт.
        """
        self.accounts_gateway_client.get_accounts(user_id=self.seed_user.user_id)

    @task(1)
    def issue_virtual_card(self) -> None:
        """
        Задача: выпуск новой виртуальной карты для дебетового счета.
        """
        self.cards_gateway_client.issue_virtual_card(
            user_id=self.seed_user.user_id,
            account_id=self.seed_user.debit_card_accounts[0].account_id
        )


class IssueVirtualCardScenarioUser(LocustBaseUser):
    """
    Виртуальный пользователь для сценария выпуска виртуальной карты.
    """
    tasks = [IssueVirtualCardTaskSet]
