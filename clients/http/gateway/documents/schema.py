from pydantic import BaseModel


class TariffDocumentSchema(BaseModel):
    """
    Схема документа тарифа, возвращаемого сервисом documents.
    """

    url: str
    document: str


class ContractDocumentSchema(BaseModel):
    """
    Схема документа контракта, возвращаемого сервисом documents.
    """

    url: str
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """
    Схема ответа на получение документа тарифа по счёту.
    """

    tariff: TariffDocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """
    Схема ответа на получение документа контракта по счёту.
    """

    contract: ContractDocumentSchema
