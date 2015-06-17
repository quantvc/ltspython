# -*- coding=utf-8 -*-
"""
生成结构化的代码

"""


class Base(object):
    def to_dict(self):
        """

        :return:
        """

        return {key: value for key, value in self.__dict__.iteritems() if value}

    def __repr__(self):
        """
        :return:
        """
        return "<%s>" % ",".join(["%s:%s" % (item, value) for item, value in self.__dict__.iteritems()])


class CSecurityFtdcRspInfoField(Base):
    """

    """

    def __init__(self, ErrorID, ErrorMsg):
        """

        :param ErrorID:
        :param ErrorMsg:
        :return:
        """
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg


class CSecurityFtdcRspUserLoginField(Base):
    """

    """

    def __init__(self, TradingDay, LoginTime, BrokerID, UserID, SystemName, FrontID, SessionID, MaxOrderRef):
        """

        :param TradingDay:
        :param LoginTime:
        :param BrokerID:
        :param UserID:
        :param SystemName:
        :param FrontID:
        :param SessionID:
        :param MaxOrderRef:
        :return:
        """
        self.TradingDay = TradingDay
        self.LoginTime = LoginTime
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.SystemName = SystemName
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.MaxOrderRef = MaxOrderRef


class CSecurityFtdcUserLogoutField(Base):
    """

    """

    def __init__(self, BrokerID, UserID):
        """

        :param BrokerID:
        :param UserID:
        :return:
        """
        self.BrokerID = BrokerID
        self.UserID = UserID


class CSecurityFtdcSpecificInstrumentField(Base):
    def __init__(self, InstrumentID, ExchangeID):
        """

        :param InstrumentID:
        :param ExchangeID:
        :return:
        """
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID


class CSecurityFtdcDepthMarketDataField(Base):
    """

    """

    def __init__(self, TradingDay, InstrumentID, ExchangeID, ExchangeInstID, LastPrice, PreSettlementPrice,
                 PreClosePrice, PreOpenInterest, OpenPrice, HighestPrice, LowestPrice, Volume, Turnover, OpenInterest,
                 ClosePrice, SettlementPrice, UpperLimitPrice, LowerLimitPrice, PreDelta, CurrDelta, UpdateTime,
                 UpdateMillisec, BidPrice1, BidVolume1, AskPrice1, AskVolume1, BidPrice2, BidVolume2, AskPrice2,
                 AskVolume2, BidPrice3, BidVolume3, AskPrice3, AskVolume3, BidPrice4, BidVolume4, AskPrice4, AskVolume4,
                 BidPrice5, BidVolume5, AskPrice5, AskVolume5, AveragePrice, ActionDay):
        """

        :param TradingDay:
        :param InstrumentID:
        :param ExchangeID:
        :param ExchangeInstID:
        :param LastPrice:
        :param PreSettlementPrice:
        :param PreClosePrice:
        :param PreOpenInterest:
        :param OpenPrice:
        :param HighestPrice:
        :param LowestPrice:
        :param Volume:
        :param Turnover:
        :param OpenInterest:
        :param ClosePrice:
        :param SettlementPrice:
        :param UpperLimitPrice:
        :param LowerLimitPrice:
        :param PreDelta:
        :param CurrDelta:
        :param UpdateTime:
        :param UpdateMillisec:
        :param BidPrice1:
        :param BidVolume1:
        :param AskPrice1:
        :param AskVolume1:
        :param BidPrice2:
        :param BidVolume2:
        :param AskPrice2:
        :param AskVolume2:
        :param BidPrice3:
        :param BidVolume3:
        :param AskPrice3:
        :param AskVolume3:
        :param BidPrice4:
        :param BidVolume4:
        :param AskPrice4:
        :param AskVolume4:
        :param BidPrice5:
        :param BidVolume5:
        :param AskPrice5:
        :param AskVolume5:
        :param AveragePrice:
        :param ActionDay:
        :return:
        """
        self.TradingDay = TradingDay
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.ExchangeInstID = ExchangeInstID
        self.LastPrice = float(LastPrice)
        self.PreSettlementPrice = float(PreSettlementPrice)
        self.PreClosePrice = float(PreClosePrice)
        self.PreOpenInterest = float(PreOpenInterest)
        self.OpenPrice = float(OpenPrice)
        self.HighestPrice = float(HighestPrice)
        self.LowestPrice = float(LowestPrice)
        self.Volume = int(Volume)
        self.Turnover = float(Turnover)
        self.OpenInterest = float(OpenInterest)
        self.ClosePrice = float(ClosePrice)
        self.SettlementPrice = float(SettlementPrice)
        self.UpperLimitPrice = float(UpperLimitPrice)
        self.LowerLimitPrice = float(LowerLimitPrice)
        self.PreDelta = float(PreDelta)
        self.CurrDelta = float(CurrDelta)
        self.UpdateTime = UpdateTime
        self.UpdateMillisec = int(UpdateMillisec)
        self.BidPrice1 = float(BidPrice1)
        self.BidVolume1 = int(BidVolume1)
        self.AskPrice1 = float(AskPrice1)
        self.AskVolume1 = int(AskVolume1)
        self.BidPrice2 = float(BidPrice2)
        self.BidVolume2 = int(BidVolume2)
        self.AskPrice2 = float(AskPrice2)
        self.AskVolume2 = int(AskVolume2)
        self.BidPrice3 = float(BidPrice3)
        self.BidVolume3 = int(BidVolume3)
        self.AskPrice3 = float(AskPrice3)
        self.AskVolume3 = int(AskVolume3)
        self.BidPrice4 = float(BidPrice4)
        self.BidVolume4 = int(BidVolume4)
        self.AskPrice4 = float(AskPrice4)
        self.AskVolume4 = int(AskVolume4)
        self.BidPrice5 = float(BidPrice5)
        self.BidVolume5 = int(BidVolume5)
        self.AskPrice5 = float(AskPrice5)
        self.AskVolume5 = int(AskVolume5)
        self.AveragePrice = float(AveragePrice)
        self.ActionDay = ActionDay


class CSecurityFtdcReqUserLoginField(Base):
    """

    """

    def __init__(self, TradingDay, BrokerID, UserID, Password, UserProductInfo, InterfaceProductInfo, ProtocolInfo,
                 MacAddress, OneTimePassword, ClientIPAddress, AuthCode):
        """

        :param TradingDay:
        :param BrokerID:
        :param UserID:
        :param Password:
        :param UserProductInfo:
        :param InterfaceProductInfo:
        :param ProtocolInfo:
        :param MacAddress:
        :param OneTimePassword:
        :param ClientIPAddress:
        :param AuthCode:
        :return:
        """
        self.TradingDay = TradingDay
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.Password = Password
        self.UserProductInfo = UserProductInfo
        self.InterfaceProductInfo = InterfaceProductInfo
        self.ProtocolInfo = ProtocolInfo
        self.MacAddress = MacAddress
        self.OneTimePassword = OneTimePassword
        self.ClientIPAddress = ClientIPAddress
        self.AuthCode = AuthCode


RspInfo = CSecurityFtdcRspInfoField
RspUserLogin = CSecurityFtdcRspInfoField
UserLogout = CSecurityFtdcUserLogoutField
SpecificInstrument = CSecurityFtdcSpecificInstrumentField
DepthMarketData = CSecurityFtdcDepthMarketDataField
ReqUserLogin = CSecurityFtdcReqUserLoginField
