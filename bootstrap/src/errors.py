"""Contains errors that are specific to the bootstrap server"""


class InternalError(Exception):
    """Internal error to use when when an unexpected exception happens"""
    error = 'Internal server error'
    code = 500

    def to_dict(self):
        return {'code': self.code, 'message': self.error}


class BootstrapError(Exception):
    """Base class for errors that are specific to the bootstrap server"""
    def __init__(self, message):
        self.error = message

    def to_dict(self):
        return {'code': self.code, 'message': self.error}

    def __str__(self):
        return f'{type(self).__name__}: {self.error}'

    def __repr__(self):
        return self.__str__()


class InvalidParamError(BootstrapError, ValueError):
    """Inherit from ValueError so that pydantic will catch this in validators"""
    def __init__(self, message):
        self.code = 4001
        self.http_code = 400
        super(InvalidParamError, self).__init__(message)


class MissingParamError(BootstrapError):
    def __init__(self, missing_param):
        self.code = 4006
        self.http_code = 400
        message = f'The parameter "{missing_param}" was missing from the requests body'
        super(MissingParamError, self).__init__(message)


class ExtraParamError(BootstrapError):
    def __init__(self, extra_param):
        self.code = 4007
        self.http_code = 400
        message = f'The parameter "{extra_param}" was missing from the requests body'
        super(ExtraParamError, self).__init__(message)


class DestinationDoesNotExistError(BootstrapError):
    def __init__(self, destination):
        self.code = 4002
        self.http_code = 400
        message = f'Destination {destination} does not exist'
        super(DestinationDoesNotExistError, self).__init__(message)


class LowBalanceError(BootstrapError):
    def __init__(self):
        self.code = 4003
        self.http_code = 400
        message = f'The account does not have enough kin to perform this operation'
        super(LowBalanceError, self).__init__(message)


class AccountNotFoundError(BootstrapError):
    def __init__(self, account):
        self.code = 4041
        self.http_code = 404
        message = f'Account {account} was not found'
        super(AccountNotFoundError, self).__init__(message)


class TransactionNotFoundError(BootstrapError):
    def __init__(self, tx_id):
        self.code = 4042
        self.http_code = 404
        message = f'Transaction {tx_id} was not found'
        super(TransactionNotFoundError, self).__init__(message)


class InvalidTransactionError(BootstrapError):
    def __init__(self):
        self.code = 4004
        self.http_code = 400
        message = f'The specified transaction was not a valid kin payment transaction'
        super(InvalidTransactionError, self).__init__(message)


class CantDecodeTransactionError(BootstrapError):
    def __init__(self):
        self.code = 4005
        self.http_code = 400
        message = f'The service was unable to decode the received transaction envelope'
        super(CantDecodeTransactionError, self).__init__(message)


class InvalidBodyError(BootstrapError):
    def __init__(self):
        self.code = 4008
        self.http_code = 400
        message = f'The received body was not a valid json'
        super(InvalidBodyError, self).__init__(message)
