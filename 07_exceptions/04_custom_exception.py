"""
    自定义异常
"""


class BusinessExceptionError(Exception):
    pass

raise BusinessExceptionError("自定义异常")