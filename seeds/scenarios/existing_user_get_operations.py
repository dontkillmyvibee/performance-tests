from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedOperationsPlan


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для получения информации об операциях.
    Создаёт 300 пользователей, каждому из которых открывается кредитный счёт с набором операций:
    - 5 операций покупки
    - 1 операция пополнения
    - 1 операция снятия наличных
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        Возвращает план сидинга для создания 300 пользователей с кредитным счётом и операциями.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                credit_card_accounts=SeedAccountsPlan(
                    count=1,
                    purchase_operations=SeedOperationsPlan(count=5),
                    top_up_operations=SeedOperationsPlan(count=1),
                    cash_withdrawal_operations=SeedOperationsPlan(count=1)
                )
            ),
        )

    @property
    def scenario(self) -> str:
        """
        Возвращает название сценария для формирования имени файла дампа.
        """
        return "existing_user_get_operations"


if __name__ == '__main__':
    """
    Точка входа для запуска процесса сидинга.
    Генерирует данные и сохраняет их в dumps/existing_user_get_operations_seeds.json.
    """
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()

