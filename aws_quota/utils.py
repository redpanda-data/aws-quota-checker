import boto3


_account_id = None


def get_account_id(session: boto3.Session) -> str:
    global _account_id
    if _account_id is None:
        _account_id = session.client('sts').get_caller_identity()['Account']
    return _account_id
