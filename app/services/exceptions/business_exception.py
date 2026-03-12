class BusinessException(Exception):
    """
    Exceção utilizada para representar erros de regra de negócio da aplicação.

    Esse tipo de exceção deve ser utilizado sempre que uma regra do sistema
    for violada, por exemplo:

    - cliente não encontrado
    - estoque insuficiente
    - quantidade inválida
    - pedido sem itens
    - pagamento maior que o valor do pedido

    O objetivo é separar erros de negócio de erros técnicos
    (como erro de banco de dados ou erro de programação).
    """

    def __init__(self, message: str, code: str = None):
        """
        Construtor da exceção de negócio.

        Parâmetros
        ----------
        message : str
            Mensagem descritiva do erro.

        code : str (opcional)
            Código identificador do erro.
            Pode ser útil no futuro para APIs ou logs.
        """

        self.message = message
        self.code = code

        super().__init__(self.message)

    def __str__(self):
        """
        Representação em texto da exceção.
        """

        if self.code:
            return f"[{self.code}] {self.message}"

        return self.message