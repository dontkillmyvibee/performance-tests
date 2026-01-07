from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedCardsPlan


class ExistingUserIssueVirtualCardSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для выпуска новой виртуальной карты существующим пользователем.
    Создаёт 300 пользователей, каждому из которых открывается один дебетовый счёт.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        План сидинга: 300 пользователей, у каждого по 1 дебетовому счёту.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                debit_card_accounts=SeedAccountsPlan(
                    count=1,
                    virtual_cards=SeedCardsPlan(count=1)
                )
            ),
        )

    @property
    def scenario(self) -> str:
        """
        Название сценария для именования файла дампа.
        """
        return "existing_user_issue_virtual_card"


if __name__ == '__main__':
    """
    Точка входа для запуска сидинга.
    Выполняет генерацию данных и сохранение в dumps/existing_user_issue_virtual_card_seeds.json.
    """
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenario.build()
