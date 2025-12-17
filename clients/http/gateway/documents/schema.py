from pydantic import BaseModel, ConfigDict, HttpUrl


class DocumentsBaseModel(BaseModel):
    """
    Базовая модель для схем documents.

    populate_by_name=True позволяет принимать данные как по имени поля,
    так и по алиасу (если он будет добавлен через Field(alias=...)).
    """

    model_config = ConfigDict(populate_by_name=True)


class DocumentSchema(DocumentsBaseModel):
    """
    Универсальная схема документа, возвращаемого сервисом documents.
    """

    url: HttpUrl
    document: str


class TariffDocumentSchema(DocumentSchema):
    """
    Документ тарифа.
    """


class ContractDocumentSchema(DocumentSchema):
    """
    Документ контракта.
    """


class GetTariffDocumentResponseSchema(DocumentsBaseModel):
    """
    Схема ответа на получение документа тарифа по счёту.
    """

    tariff: TariffDocumentSchema


class GetContractDocumentResponseSchema(DocumentsBaseModel):
    """
    Схема ответа на получение документа контракта по счёту.
    """

    contract: ContractDocumentSchema
