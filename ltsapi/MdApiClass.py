__author__ = 'weichenwang'

CSecurityFtdcRspInfoField,
CSecurityFtdcRspUserLoginField,
CSecurityFtdcSpecificInstrumentField,
CSecurityFtdcUserLogoutField,
CSecurityFtdcDepthMarketDataField,
CSecurityFtdcReqUserLoginField


class Base(object):
    """

    """
    def __str__(self):
        pass

class CSecurityFtdcRspInfoField(Base):
    """
    响应信息
    """
    def __init__(self, error_id, error_msg):
        """
        :param error_id: int, 错误代码
        :param error_msg: str,length:81 错误信息
        :return:
        """
        self.error_id = error_id
        self.error_msg = error_msg
