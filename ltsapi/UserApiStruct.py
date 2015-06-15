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


class CSecurityFtdcExchangeField(Base):
    """

    """

    def __init__(self, ExchangeID, ExchangeName, ExchangeProperty):
        """

        :param ExchangeID:
        :param ExchangeName:
        :param ExchangeProperty:
        :return:
        """
        self.ExchangeID = ExchangeID
        self.ExchangeName = ExchangeName
        self.ExchangeProperty = ExchangeProperty


class CSecurityFtdcProductField(Base):
    """

    """

    def __init__(self, ProductID, ProductName, ExchangeID, ProductClass, VolumeMultiple, PriceTick,
                 MaxMarketOrderVolume, MinMarketOrderVolume, MaxLimitOrderVolume, MinLimitOrderVolume, PositionType,
                 PositionDateType, EFTMinTradeVolume):
        """

        :param ProductID:
        :param ProductName:
        :param ExchangeID:
        :param ProductClass:
        :param VolumeMultiple:
        :param PriceTick:
        :param MaxMarketOrderVolume:
        :param MinMarketOrderVolume:
        :param MaxLimitOrderVolume:
        :param MinLimitOrderVolume:
        :param PositionType:
        :param PositionDateType:
        :param EFTMinTradeVolume:
        :return:
        """
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.ExchangeID = ExchangeID
        self.ProductClass = ProductClass
        self.VolumeMultiple = int(VolumeMultiple)
        self.PriceTick = float(PriceTick)
        self.MaxMarketOrderVolume = int(MaxMarketOrderVolume)
        self.MinMarketOrderVolume = int(MinMarketOrderVolume)
        self.MaxLimitOrderVolume = int(MaxLimitOrderVolume)
        self.MinLimitOrderVolume = int(MinLimitOrderVolume)
        self.PositionType = PositionType
        self.PositionDateType = PositionDateType
        self.EFTMinTradeVolume = int(EFTMinTradeVolume)


class CSecurityFtdcInstrumentField(Base):
    """

    """

    def __init__(self, InstrumentID, ExchangeID, InstrumentName, ExchangeInstID, ProductID, ProductClass, DeliveryYear,
                 DeliveryMonth, MaxMarketOrderVolume, MinMarketOrderVolume, MaxLimitOrderVolume, MinLimitOrderVolume,
                 VolumeMultiple, PriceTick, CreateDate, OpenDate, ExpireDate, StartDelivDate, EndDelivDate,
                 InstLifePhase, IsTrading, PositionType, OrderCanBeWithdraw, MinBuyVolume, MinSellVolume, RightModelID,
                 PosTradeType, MarketID):
        """

        :param InstrumentID:
        :param ExchangeID:
        :param InstrumentName:
        :param ExchangeInstID:
        :param ProductID:
        :param ProductClass:
        :param DeliveryYear:
        :param DeliveryMonth:
        :param MaxMarketOrderVolume:
        :param MinMarketOrderVolume:
        :param MaxLimitOrderVolume:
        :param MinLimitOrderVolume:
        :param VolumeMultiple:
        :param PriceTick:
        :param CreateDate:
        :param OpenDate:
        :param ExpireDate:
        :param StartDelivDate:
        :param EndDelivDate:
        :param InstLifePhase:
        :param IsTrading:
        :param PositionType:
        :param OrderCanBeWithdraw:
        :param MinBuyVolume:
        :param MinSellVolume:
        :param RightModelID:
        :param PosTradeType:
        :param MarketID:
        :return:
        """
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.InstrumentName = InstrumentName
        self.ExchangeInstID = ExchangeInstID
        self.ProductID = ProductID
        self.ProductClass = ProductClass
        self.DeliveryYear = int(DeliveryYear)
        self.DeliveryMonth = int(DeliveryMonth)
        self.MaxMarketOrderVolume = int(MaxMarketOrderVolume)
        self.MinMarketOrderVolume = int(MinMarketOrderVolume)
        self.MaxLimitOrderVolume = int(MaxLimitOrderVolume)
        self.MinLimitOrderVolume = int(MinLimitOrderVolume)
        self.VolumeMultiple = int(VolumeMultiple)
        self.PriceTick = float(PriceTick)
        self.CreateDate = CreateDate
        self.OpenDate = OpenDate
        self.ExpireDate = ExpireDate
        self.StartDelivDate = StartDelivDate
        self.EndDelivDate = EndDelivDate
        self.InstLifePhase = InstLifePhase
        self.IsTrading = int(IsTrading)
        self.PositionType = PositionType
        self.OrderCanBeWithdraw = int(OrderCanBeWithdraw)
        self.MinBuyVolume = int(MinBuyVolume)
        self.MinSellVolume = int(MinSellVolume)
        self.RightModelID = RightModelID
        self.PosTradeType = PosTradeType
        self.MarketID = MarketID


class CSecurityFtdcBrokerField(Base):
    """

    """

    def __init__(self, BrokerID, BrokerAbbr, BrokerName, IsActive):
        """

        :param BrokerID:
        :param BrokerAbbr:
        :param BrokerName:
        :param IsActive:
        :return:
        """
        self.BrokerID = BrokerID
        self.BrokerAbbr = BrokerAbbr
        self.BrokerName = BrokerName
        self.IsActive = int(IsActive)


class CSecurityFtdcPartBrokerField(Base):
    """

    """

    def __init__(self, BrokerID, ExchangeID, ParticipantID, IsActive):
        """

        :param BrokerID:
        :param ExchangeID:
        :param ParticipantID:
        :param IsActive:
        :return:
        """
        self.BrokerID = BrokerID
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.IsActive = int(IsActive)


class CSecurityFtdcInvestorField(Base):
    """

    """

    def __init__(self, InvestorID, BrokerID, InvestorGroupID, InvestorName, IdentifiedCardType, IdentifiedCardNo,
                 IsActive, SHBranchID, SZBranchID):
        """

        :param InvestorID:
        :param BrokerID:
        :param InvestorGroupID:
        :param InvestorName:
        :param IdentifiedCardType:
        :param IdentifiedCardNo:
        :param IsActive:
        :param SHBranchID:
        :param SZBranchID:
        :return:
        """
        self.InvestorID = InvestorID
        self.BrokerID = BrokerID
        self.InvestorGroupID = InvestorGroupID
        self.InvestorName = InvestorName
        self.IdentifiedCardType = IdentifiedCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.IsActive = int(IsActive)
        self.SHBranchID = SHBranchID
        self.SZBranchID = SZBranchID


class CSecurityFtdcTradingCodeField(Base):
    """

    """

    def __init__(self, InvestorID, BrokerID, ExchangeID, ClientID, IsActive, AccountID, PBU, ClientType):
        """

        :param InvestorID:
        :param BrokerID:
        :param ExchangeID:
        :param ClientID:
        :param IsActive:
        :param AccountID:
        :param PBU:
        :param ClientType:
        :return:
        """
        self.InvestorID = InvestorID
        self.BrokerID = BrokerID
        self.ExchangeID = ExchangeID
        self.ClientID = ClientID
        self.IsActive = int(IsActive)
        self.AccountID = AccountID
        self.PBU = PBU
        self.ClientType = ClientType


class CSecurityFtdcSuperUserField(Base):
    """

    """

    def __init__(self, UserID, UserName, Password, IsActive):
        """

        :param UserID:
        :param UserName:
        :param Password:
        :param IsActive:
        :return:
        """
        self.UserID = UserID
        self.UserName = UserName
        self.Password = Password
        self.IsActive = int(IsActive)


class CSecurityFtdcSuperUserFunctionField(Base):
    """

    """

    def __init__(self, UserID, FunctionCode):
        """

        :param UserID:
        :param FunctionCode:
        :return:
        """
        self.UserID = UserID
        self.FunctionCode = FunctionCode


class CSecurityFtdcBrokerUserField(Base):
    """

    """

    def __init__(self, BrokerID, UserID, UserName, UserType, IsActive, IsUsingOTP):
        """

        :param BrokerID:
        :param UserID:
        :param UserName:
        :param UserType:
        :param IsActive:
        :param IsUsingOTP:
        :return:
        """
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.UserName = UserName
        self.UserType = UserType
        self.IsActive = int(IsActive)
        self.IsUsingOTP = int(IsUsingOTP)


class CSecurityFtdcBrokerUserFunctionField(Base):
    """

    """

    def __init__(self, BrokerID, UserID, BrokerFunctionCode):
        """

        :param BrokerID:
        :param UserID:
        :param BrokerFunctionCode:
        :return:
        """
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.BrokerFunctionCode = BrokerFunctionCode


class CSecurityFtdcTradingAccountField(Base):
    """

    """

    def __init__(self, BrokerID, AccountID, PreMortgage, PreCredit, PreDeposit, PreBalance, PreMargin, InterestBase,
                 Interest, Deposit, Withdraw, FrozenMargin, FrozenCash, FrozenCommission, CurrMargin, CashIn,
                 Commission, Balance, Available, WithdrawQuota, Reserve, TradingDay, Credit, Mortgage, ExchangeMargin,
                 DeliveryMargin, ExchangeDeliveryMargin, FrozenTransferFee, FrozenStampTax, TransferFee, StampTax,
                 ConversionAmount, CreditAmount, StockValue, BondRepurchaseAmount, ReverseRepurchaseAmount,
                 CurrencyCode, AccountType, MarginTradeAmount, ShortSellAmount, MarginTradeProfit, ShortSellProfit,
                 SSStockValue, CreditRatio):
        """

        :param BrokerID:
        :param AccountID:
        :param PreMortgage:
        :param PreCredit:
        :param PreDeposit:
        :param PreBalance:
        :param PreMargin:
        :param InterestBase:
        :param Interest:
        :param Deposit:
        :param Withdraw:
        :param FrozenMargin:
        :param FrozenCash:
        :param FrozenCommission:
        :param CurrMargin:
        :param CashIn:
        :param Commission:
        :param Balance:
        :param Available:
        :param WithdrawQuota:
        :param Reserve:
        :param TradingDay:
        :param Credit:
        :param Mortgage:
        :param ExchangeMargin:
        :param DeliveryMargin:
        :param ExchangeDeliveryMargin:
        :param FrozenTransferFee:
        :param FrozenStampTax:
        :param TransferFee:
        :param StampTax:
        :param ConversionAmount:
        :param CreditAmount:
        :param StockValue:
        :param BondRepurchaseAmount:
        :param ReverseRepurchaseAmount:
        :param CurrencyCode:
        :param AccountType:
        :param MarginTradeAmount:
        :param ShortSellAmount:
        :param MarginTradeProfit:
        :param ShortSellProfit:
        :param SSStockValue:
        :param CreditRatio:
        :return:
        """
        self.BrokerID = BrokerID
        self.AccountID = AccountID
        self.PreMortgage = float(PreMortgage)
        self.PreCredit = float(PreCredit)
        self.PreDeposit = float(PreDeposit)
        self.PreBalance = float(PreBalance)
        self.PreMargin = float(PreMargin)
        self.InterestBase = float(InterestBase)
        self.Interest = float(Interest)
        self.Deposit = float(Deposit)
        self.Withdraw = float(Withdraw)
        self.FrozenMargin = float(FrozenMargin)
        self.FrozenCash = float(FrozenCash)
        self.FrozenCommission = float(FrozenCommission)
        self.CurrMargin = float(CurrMargin)
        self.CashIn = float(CashIn)
        self.Commission = float(Commission)
        self.Balance = float(Balance)
        self.Available = float(Available)
        self.WithdrawQuota = float(WithdrawQuota)
        self.Reserve = float(Reserve)
        self.TradingDay = TradingDay
        self.Credit = float(Credit)
        self.Mortgage = float(Mortgage)
        self.ExchangeMargin = float(ExchangeMargin)
        self.DeliveryMargin = float(DeliveryMargin)
        self.ExchangeDeliveryMargin = float(ExchangeDeliveryMargin)
        self.FrozenTransferFee = float(FrozenTransferFee)
        self.FrozenStampTax = float(FrozenStampTax)
        self.TransferFee = float(TransferFee)
        self.StampTax = float(StampTax)
        self.ConversionAmount = float(ConversionAmount)
        self.CreditAmount = float(CreditAmount)
        self.StockValue = float(StockValue)
        self.BondRepurchaseAmount = float(BondRepurchaseAmount)
        self.ReverseRepurchaseAmount = float(ReverseRepurchaseAmount)
        self.CurrencyCode = CurrencyCode
        self.AccountType = AccountType
        self.MarginTradeAmount = float(MarginTradeAmount)
        self.ShortSellAmount = float(ShortSellAmount)
        self.MarginTradeProfit = float(MarginTradeProfit)
        self.ShortSellProfit = float(ShortSellProfit)
        self.SSStockValue = float(SSStockValue)
        self.CreditRatio = float(CreditRatio)


class CSecurityFtdcLoginForbiddenUserField(Base):
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


class CSecurityFtdcInstrumentTradingRightField(Base):
    """

    """

    def __init__(self, InstrumentID, InvestorRange, BrokerID, InvestorID, Direction, TradingRight, ExchangeID,
                 InstrumentRange):
        """

        :param InstrumentID:
        :param InvestorRange:
        :param BrokerID:
        :param InvestorID:
        :param Direction:
        :param TradingRight:
        :param ExchangeID:
        :param InstrumentRange:
        :return:
        """
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.Direction = Direction
        self.TradingRight = TradingRight
        self.ExchangeID = ExchangeID
        self.InstrumentRange = InstrumentRange


class CSecurityFtdcInvestorPositionDetailField(Base):
    """

    """

    def __init__(self, InstrumentID, BrokerID, InvestorID, HedgeFlag, Direction, OpenDate, TradeID, Volume, OpenPrice,
                 TradingDay, TradeType, ExchangeID, Margin, ExchMargin, LastSettlementPrice, SettlementPrice,
                 CloseVolume, CloseAmount, TransferFee, StampTax, Commission, AccountID, PledgeInPosition,
                 PledgeInFrozenPosition, RepurchasePosition, Amount):
        """

        :param InstrumentID:
        :param BrokerID:
        :param InvestorID:
        :param HedgeFlag:
        :param Direction:
        :param OpenDate:
        :param TradeID:
        :param Volume:
        :param OpenPrice:
        :param TradingDay:
        :param TradeType:
        :param ExchangeID:
        :param Margin:
        :param ExchMargin:
        :param LastSettlementPrice:
        :param SettlementPrice:
        :param CloseVolume:
        :param CloseAmount:
        :param TransferFee:
        :param StampTax:
        :param Commission:
        :param AccountID:
        :param PledgeInPosition:
        :param PledgeInFrozenPosition:
        :param RepurchasePosition:
        :param Amount:
        :return:
        """
        self.InstrumentID = InstrumentID
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.HedgeFlag = HedgeFlag
        self.Direction = Direction
        self.OpenDate = OpenDate
        self.TradeID = TradeID
        self.Volume = int(Volume)
        self.OpenPrice = float(OpenPrice)
        self.TradingDay = TradingDay
        self.TradeType = TradeType
        self.ExchangeID = ExchangeID
        self.Margin = float(Margin)
        self.ExchMargin = float(ExchMargin)
        self.LastSettlementPrice = float(LastSettlementPrice)
        self.SettlementPrice = float(SettlementPrice)
        self.CloseVolume = int(CloseVolume)
        self.CloseAmount = float(CloseAmount)
        self.TransferFee = float(TransferFee)
        self.StampTax = float(StampTax)
        self.Commission = float(Commission)
        self.AccountID = AccountID
        self.PledgeInPosition = int(PledgeInPosition)
        self.PledgeInFrozenPosition = int(PledgeInFrozenPosition)
        self.RepurchasePosition = int(RepurchasePosition)
        self.Amount = float(Amount)


class CSecurityFtdcBondInterestField(Base):
    """

    """

    def __init__(self, TradingDay, ExchangeID, InstrumentID, Interest):
        """

        :param TradingDay:
        :param ExchangeID:
        :param InstrumentID:
        :param Interest:
        :return:
        """
        self.TradingDay = TradingDay
        self.ExchangeID = ExchangeID
        self.InstrumentID = InstrumentID
        self.Interest = float(Interest)


class CSecurityFtdcMarketRationInfoField(Base):
    """

    """

    def __init__(self, BrokerID, InvestorID, ExchangeID, RationVolume):
        """

        :param BrokerID:
        :param InvestorID:
        :param ExchangeID:
        :param RationVolume:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID
        self.RationVolume = int(RationVolume)


class CSecurityFtdcInstrumentCommissionRateField(Base):
    """

    """

    def __init__(self, ExchangeID, InstrumentID, InvestorRange, BrokerID, InvestorID, Direction, StampTaxRateByMoney,
                 StampTaxRateByVolume, TransferFeeRateByMoney, TransferFeeRateByVolume, TradeFeeByMoney,
                 TradeFeeByVolume, MarginByMoney, MinTradeFee):
        """

        :param ExchangeID:
        :param InstrumentID:
        :param InvestorRange:
        :param BrokerID:
        :param InvestorID:
        :param Direction:
        :param StampTaxRateByMoney:
        :param StampTaxRateByVolume:
        :param TransferFeeRateByMoney:
        :param TransferFeeRateByVolume:
        :param TradeFeeByMoney:
        :param TradeFeeByVolume:
        :param MarginByMoney:
        :param MinTradeFee:
        :return:
        """
        self.ExchangeID = ExchangeID
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.Direction = Direction
        self.StampTaxRateByMoney = float(StampTaxRateByMoney)
        self.StampTaxRateByVolume = float(StampTaxRateByVolume)
        self.TransferFeeRateByMoney = float(TransferFeeRateByMoney)
        self.TransferFeeRateByVolume = float(TransferFeeRateByVolume)
        self.TradeFeeByMoney = float(TradeFeeByMoney)
        self.TradeFeeByVolume = float(TradeFeeByVolume)
        self.MarginByMoney = float(MarginByMoney)
        self.MinTradeFee = float(MinTradeFee)


class CSecurityFtdcExcessStockInfoField(Base):
    def __init__(self, BrokerID, InvestorID, ExchangeID, InstrumentID, ExcessVolume, ExcessFrozenVolume):
        """

        :param BrokerID:
        :param InvestorID:
        :param ExchangeID:
        :param InstrumentID:
        :param ExcessVolume:
        :param ExcessFrozenVolume:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID
        self.InstrumentID = InstrumentID
        self.ExcessVolume = int(ExcessVolume)
        self.ExcessFrozenVolume = int(ExcessFrozenVolume)


class CSecurityFtdcTraderOfferField(Base):
    def __init__(self, ExchangeID, BranchPBU, ParticipantID, Password, InstallID, OrderLocalID, TraderConnectStatus,
                 ConnectRequestDate, ConnectRequestTime, LastReportDate, LastReportTime, ConnectDate, ConnectTime,
                 StartDate, StartTime, TradingDay, BrokerID):
        """

        :param ExchangeID:
        :param BranchPBU:
        :param ParticipantID:
        :param Password:
        :param InstallID:
        :param OrderLocalID:
        :param TraderConnectStatus:
        :param ConnectRequestDate:
        :param ConnectRequestTime:
        :param LastReportDate:
        :param LastReportTime:
        :param ConnectDate:
        :param ConnectTime:
        :param StartDate:
        :param StartTime:
        :param TradingDay:
        :param BrokerID:
        :return:
        """
        self.ExchangeID = ExchangeID
        self.BranchPBU = BranchPBU
        self.ParticipantID = ParticipantID
        self.Password = Password
        self.InstallID = int(InstallID)
        self.OrderLocalID = OrderLocalID
        self.TraderConnectStatus = TraderConnectStatus
        self.ConnectRequestDate = ConnectRequestDate
        self.ConnectRequestTime = ConnectRequestTime
        self.LastReportDate = LastReportDate
        self.LastReportTime = LastReportTime
        self.ConnectDate = ConnectDate
        self.ConnectTime = ConnectTime
        self.StartDate = StartDate
        self.StartTime = StartTime
        self.TradingDay = TradingDay
        self.BrokerID = BrokerID


class CSecurityFtdcMDTraderOfferField(Base):
    def __init__(self, ExchangeID, BranchPBU, ParticipantID, Password, InstallID, OrderLocalID, TraderConnectStatus,
                 ConnectRequestDate, ConnectRequestTime, LastReportDate, LastReportTime, ConnectDate, ConnectTime,
                 StartDate, StartTime, TradingDay, BrokerID):
        """

        :param ExchangeID:
        :param BranchPBU:
        :param ParticipantID:
        :param Password:
        :param InstallID:
        :param OrderLocalID:
        :param TraderConnectStatus:
        :param ConnectRequestDate:
        :param ConnectRequestTime:
        :param LastReportDate:
        :param LastReportTime:
        :param ConnectDate:
        :param ConnectTime:
        :param StartDate:
        :param StartTime:
        :param TradingDay:
        :param BrokerID:
        :return:
        """
        self.ExchangeID = ExchangeID
        self.BranchPBU = BranchPBU
        self.ParticipantID = ParticipantID
        self.Password = Password
        self.InstallID = int(InstallID)
        self.OrderLocalID = OrderLocalID
        self.TraderConnectStatus = TraderConnectStatus
        self.ConnectRequestDate = ConnectRequestDate
        self.ConnectRequestTime = ConnectRequestTime
        self.LastReportDate = LastReportDate
        self.LastReportTime = LastReportTime
        self.ConnectDate = ConnectDate
        self.ConnectTime = ConnectTime
        self.StartDate = StartDate
        self.StartTime = StartTime
        self.TradingDay = TradingDay
        self.BrokerID = BrokerID


class CSecurityFtdcFrontStatusField(Base):
    def __init__(self, FrontID, LastReportDate, LastReportTime, IsActive):
        """

        :param FrontID:
        :param LastReportDate:
        :param LastReportTime:
        :param IsActive:
        :return:
        """
        self.FrontID = int(FrontID)
        self.LastReportDate = LastReportDate
        self.LastReportTime = LastReportTime
        self.IsActive = int(IsActive)


class CSecurityFtdcUserSessionField(Base):
    def __init__(self, FrontID, SessionID, BrokerID, UserID, LoginDate, LoginTime, IPAddress, UserProductInfo,
                 InterfaceProductInfo, ProtocolInfo, MacAddress):
        """

        :param FrontID:
        :param SessionID:
        :param BrokerID:
        :param UserID:
        :param LoginDate:
        :param LoginTime:
        :param IPAddress:
        :param UserProductInfo:
        :param InterfaceProductInfo:
        :param ProtocolInfo:
        :param MacAddress:
        :return:
        """
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.LoginDate = LoginDate
        self.LoginTime = LoginTime
        self.IPAddress = IPAddress
        self.UserProductInfo = UserProductInfo
        self.InterfaceProductInfo = InterfaceProductInfo
        self.ProtocolInfo = ProtocolInfo
        self.MacAddress = MacAddress


class CSecurityFtdcOrderField(Base):
    def __init__(self, BrokerID, InvestorID, InstrumentID, OrderRef, UserID, ExchangeID, OrderPriceType, Direction,
                 CombOffsetFlag, CombHedgeFlag, LimitPrice, VolumeTotalOriginal, TimeCondition, GTDDate,
                 VolumeCondition, MinVolume, ContingentCondition, StopPrice, ForceCloseReason, IsAutoSuspend,
                 BusinessUnit, RequestID, OrderLocalID, ParticipantID, ClientID, ExchangeInstID, BranchPBU, InstallID,
                 OrderSubmitStatus, AccountID, NotifySequence, TradingDay, OrderSysID, OrderSource, OrderStatus,
                 OrderType, VolumeTraded, VolumeTotal, InsertDate, InsertTime, ActiveTime, SuspendTime, UpdateTime,
                 CancelTime, ActiveTraderID, ClearingPartID, SequenceNo, FrontID, SessionID, UserProductInfo, StatusMsg,
                 UserForceClose, ActiveUserID, BrokerOrderSeq, RelativeOrderSysID, BranchID, TradeAmount, IsETF):
        """

        :param BrokerID:
        :param InvestorID:
        :param InstrumentID:
        :param OrderRef:
        :param UserID:
        :param ExchangeID:
        :param OrderPriceType:
        :param Direction:
        :param CombOffsetFlag:
        :param CombHedgeFlag:
        :param LimitPrice:
        :param VolumeTotalOriginal:
        :param TimeCondition:
        :param GTDDate:
        :param VolumeCondition:
        :param MinVolume:
        :param ContingentCondition:
        :param StopPrice:
        :param ForceCloseReason:
        :param IsAutoSuspend:
        :param BusinessUnit:
        :param RequestID:
        :param OrderLocalID:
        :param ParticipantID:
        :param ClientID:
        :param ExchangeInstID:
        :param BranchPBU:
        :param InstallID:
        :param OrderSubmitStatus:
        :param AccountID:
        :param NotifySequence:
        :param TradingDay:
        :param OrderSysID:
        :param OrderSource:
        :param OrderStatus:
        :param OrderType:
        :param VolumeTraded:
        :param VolumeTotal:
        :param InsertDate:
        :param InsertTime:
        :param ActiveTime:
        :param SuspendTime:
        :param UpdateTime:
        :param CancelTime:
        :param ActiveTraderID:
        :param ClearingPartID:
        :param SequenceNo:
        :param FrontID:
        :param SessionID:
        :param UserProductInfo:
        :param StatusMsg:
        :param UserForceClose:
        :param ActiveUserID:
        :param BrokerOrderSeq:
        :param RelativeOrderSysID:
        :param BranchID:
        :param TradeAmount:
        :param IsETF:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.OrderRef = OrderRef
        self.UserID = UserID
        self.ExchangeID = ExchangeID
        self.OrderPriceType = OrderPriceType
        self.Direction = Direction
        self.CombOffsetFlag = CombOffsetFlag
        self.CombHedgeFlag = CombHedgeFlag
        self.LimitPrice = LimitPrice
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = TimeCondition
        self.GTDDate = GTDDate
        self.VolumeCondition = VolumeCondition
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = ContingentCondition
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = ForceCloseReason
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = BusinessUnit
        self.RequestID = int(RequestID)
        self.OrderLocalID = OrderLocalID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeInstID = ExchangeInstID
        self.BranchPBU = BranchPBU
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = OrderSubmitStatus
        self.AccountID = AccountID
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = TradingDay
        self.OrderSysID = OrderSysID
        self.OrderSource = OrderSource
        self.OrderStatus = OrderStatus
        self.OrderType = OrderType
        self.VolumeTraded = int(VolumeTraded)
        self.VolumeTotal = int(VolumeTotal)
        self.InsertDate = InsertDate
        self.InsertTime = InsertTime
        self.ActiveTime = ActiveTime
        self.SuspendTime = SuspendTime
        self.UpdateTime = UpdateTime
        self.CancelTime = CancelTime
        self.ActiveTraderID = ActiveTraderID
        self.ClearingPartID = ClearingPartID
        self.SequenceNo = int(SequenceNo)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.UserProductInfo = UserProductInfo
        self.StatusMsg = StatusMsg
        self.UserForceClose = int(UserForceClose)
        self.ActiveUserID = ActiveUserID
        self.BrokerOrderSeq = int(BrokerOrderSeq)
        self.RelativeOrderSysID = RelativeOrderSysID
        self.BranchID = BranchID
        self.TradeAmount = float(TradeAmount)
        self.IsETF = int(IsETF)


class CSecurityFtdcOrderActionField(Base):
    def __init__(self, BrokerID, InvestorID, OrderActionRef, OrderRef, RequestID, FrontID, SessionID, ExchangeID,
                 ActionFlag, LimitPrice, VolumeChange, ActionDate, ActionTime, BranchPBU, InstallID, OrderLocalID,
                 ActionLocalID, ParticipantID, ClientID, BusinessUnit, OrderActionStatus, UserID, BranchID, StatusMsg,
                 InstrumentID):
        """

        :param BrokerID:
        :param InvestorID:
        :param OrderActionRef:
        :param OrderRef:
        :param RequestID:
        :param FrontID:
        :param SessionID:
        :param ExchangeID:
        :param ActionFlag:
        :param LimitPrice:
        :param VolumeChange:
        :param ActionDate:
        :param ActionTime:
        :param BranchPBU:
        :param InstallID:
        :param OrderLocalID:
        :param ActionLocalID:
        :param ParticipantID:
        :param ClientID:
        :param BusinessUnit:
        :param OrderActionStatus:
        :param UserID:
        :param BranchID:
        :param StatusMsg:
        :param InstrumentID:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.OrderActionRef = int(OrderActionRef)
        self.OrderRef = OrderRef
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = ExchangeID
        self.ActionFlag = ActionFlag
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.ActionDate = ActionDate
        self.ActionTime = ActionTime
        self.BranchPBU = BranchPBU
        self.InstallID = int(InstallID)
        self.OrderLocalID = OrderLocalID
        self.ActionLocalID = ActionLocalID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.BusinessUnit = BusinessUnit
        self.OrderActionStatus = OrderActionStatus
        self.UserID = UserID
        self.BranchID = BranchID
        self.StatusMsg = StatusMsg
        self.InstrumentID = InstrumentID


class CSecurityFtdcErrOrderField(Base):
    def __init__(self, BrokerID, InvestorID, InstrumentID, OrderRef, UserID, ExchangeID, OrderPriceType, Direction,
                 CombOffsetFlag, CombHedgeFlag, LimitPrice, VolumeTotalOriginal, TimeCondition, GTDDate,
                 VolumeCondition, MinVolume, ContingentCondition, StopPrice, ForceCloseReason, IsAutoSuspend,
                 BusinessUnit, RequestID, UserForceClose, ErrorID, ErrorMsg):
        """

        :param BrokerID:
        :param InvestorID:
        :param InstrumentID:
        :param OrderRef:
        :param UserID:
        :param ExchangeID:
        :param OrderPriceType:
        :param Direction:
        :param CombOffsetFlag:
        :param CombHedgeFlag:
        :param LimitPrice:
        :param VolumeTotalOriginal:
        :param TimeCondition:
        :param GTDDate:
        :param VolumeCondition:
        :param MinVolume:
        :param ContingentCondition:
        :param StopPrice:
        :param ForceCloseReason:
        :param IsAutoSuspend:
        :param BusinessUnit:
        :param RequestID:
        :param UserForceClose:
        :param ErrorID:
        :param ErrorMsg:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.OrderRef = OrderRef
        self.UserID = UserID
        self.ExchangeID = ExchangeID
        self.OrderPriceType = OrderPriceType
        self.Direction = Direction
        self.CombOffsetFlag = CombOffsetFlag
        self.CombHedgeFlag = CombHedgeFlag
        self.LimitPrice = LimitPrice
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = TimeCondition
        self.GTDDate = GTDDate
        self.VolumeCondition = VolumeCondition
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = ContingentCondition
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = ForceCloseReason
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = BusinessUnit
        self.RequestID = int(RequestID)
        self.UserForceClose = int(UserForceClose)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg


class CSecurityFtdcErrOrderActionField(Base):
    def __init__(self, BrokerID, InvestorID, OrderActionRef, OrderRef, RequestID, FrontID, SessionID, ExchangeID,
                 ActionFlag, LimitPrice, VolumeChange, ActionDate, ActionTime, BranchPBU, InstallID, OrderLocalID,
                 ActionLocalID, ParticipantID, ClientID, BusinessUnit, OrderActionStatus, UserID, BranchID, StatusMsg,
                 InstrumentID, ErrorID, ErrorMsg):
        """

        :param BrokerID:
        :param InvestorID:
        :param OrderActionRef:
        :param OrderRef:
        :param RequestID:
        :param FrontID:
        :param SessionID:
        :param ExchangeID:
        :param ActionFlag:
        :param LimitPrice:
        :param VolumeChange:
        :param ActionDate:
        :param ActionTime:
        :param BranchPBU:
        :param InstallID:
        :param OrderLocalID:
        :param ActionLocalID:
        :param ParticipantID:
        :param ClientID:
        :param BusinessUnit:
        :param OrderActionStatus:
        :param UserID:
        :param BranchID:
        :param StatusMsg:
        :param InstrumentID:
        :param ErrorID:
        :param ErrorMsg:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.OrderActionRef = int(OrderActionRef)
        self.OrderRef = OrderRef
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = ExchangeID
        self.ActionFlag = ActionFlag
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.ActionDate = ActionDate
        self.ActionTime = ActionTime
        self.BranchPBU = BranchPBU
        self.InstallID = int(InstallID)
        self.OrderLocalID = OrderLocalID
        self.ActionLocalID = ActionLocalID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.BusinessUnit = BusinessUnit
        self.OrderActionStatus = OrderActionStatus
        self.UserID = UserID
        self.BranchID = BranchID
        self.StatusMsg = StatusMsg
        self.InstrumentID = InstrumentID
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg


class CSecurityFtdcTradeField(Base):
    def __init__(self, BrokerID, InvestorID, InstrumentID, OrderRef, UserID, ExchangeID, TradeID, Direction, OrderSysID,
                 ParticipantID, ClientID, TradingRole, ExchangeInstID, OffsetFlag, HedgeFlag, Price, Volume, TradeDate,
                 TradeTime, TradeType, PriceSource, BranchPBU, OrderLocalID, ClearingPartID, BusinessUnit, SequenceNo,
                 TradeSource, TradingDay, BrokerOrderSeq):
        """

        :param BrokerID:
        :param InvestorID:
        :param InstrumentID:
        :param OrderRef:
        :param UserID:
        :param ExchangeID:
        :param TradeID:
        :param Direction:
        :param OrderSysID:
        :param ParticipantID:
        :param ClientID:
        :param TradingRole:
        :param ExchangeInstID:
        :param OffsetFlag:
        :param HedgeFlag:
        :param Price:
        :param Volume:
        :param TradeDate:
        :param TradeTime:
        :param TradeType:
        :param PriceSource:
        :param BranchPBU:
        :param OrderLocalID:
        :param ClearingPartID:
        :param BusinessUnit:
        :param SequenceNo:
        :param TradeSource:
        :param TradingDay:
        :param BrokerOrderSeq:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.OrderRef = OrderRef
        self.UserID = UserID
        self.ExchangeID = ExchangeID
        self.TradeID = TradeID
        self.Direction = Direction
        self.OrderSysID = OrderSysID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.TradingRole = TradingRole
        self.ExchangeInstID = ExchangeInstID
        self.OffsetFlag = OffsetFlag
        self.HedgeFlag = HedgeFlag
        self.Price = Price
        self.Volume = int(Volume)
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.TradeType = TradeType
        self.PriceSource = PriceSource
        self.BranchPBU = BranchPBU
        self.OrderLocalID = OrderLocalID
        self.ClearingPartID = ClearingPartID
        self.BusinessUnit = BusinessUnit
        self.SequenceNo = int(SequenceNo)
        self.TradeSource = TradeSource
        self.TradingDay = TradingDay
        self.BrokerOrderSeq = int(BrokerOrderSeq)


class CSecurityFtdcInvestorPositionField(Base):
    def __init__(self, InstrumentID, BrokerID, InvestorID, PosiDirection, HedgeFlag, PositionDate, YdPosition, Position,
                 LongFrozen, ShortFrozen, LongFrozenAmount, ShortFrozenAmount, OpenVolume, CloseVolume, OpenAmount,
                 CloseAmount, PositionCost, FrozenCash, CashIn, Commission, PreSettlementPrice, SettlementPrice,
                 TradingDay, OpenCost, ExchangeMargin, TodayPosition, TransferFee, StampTax, TodayPurRedVolume,
                 ConversionRate, ConversionAmount, StockValue, ExchangeID, AccountID, PledgeInPosition,
                 RepurchasePosition, PurRedShortFrozen, MarginTradeVolume, MarginTradeAmount, MarginTradeFrozenVolume,
                 MarginTradeFrozenAmount, MarginTradeConversionProfit, ShortSellVolume, ShortSellAmount,
                 ShortSellFrozenVolume, ShortSellFrozenAmount, ShortSellConversionProfit, SSStockValue, TodayMTPosition,
                 TodaySSPosition, YdOpenCost):
        """

        :param InstrumentID:
        :param BrokerID:
        :param InvestorID:
        :param PosiDirection:
        :param HedgeFlag:
        :param PositionDate:
        :param YdPosition:
        :param Position:
        :param LongFrozen:
        :param ShortFrozen:
        :param LongFrozenAmount:
        :param ShortFrozenAmount:
        :param OpenVolume:
        :param CloseVolume:
        :param OpenAmount:
        :param CloseAmount:
        :param PositionCost:
        :param FrozenCash:
        :param CashIn:
        :param Commission:
        :param PreSettlementPrice:
        :param SettlementPrice:
        :param TradingDay:
        :param OpenCost:
        :param ExchangeMargin:
        :param TodayPosition:
        :param TransferFee:
        :param StampTax:
        :param TodayPurRedVolume:
        :param ConversionRate:
        :param ConversionAmount:
        :param StockValue:
        :param ExchangeID:
        :param AccountID:
        :param PledgeInPosition:
        :param RepurchasePosition:
        :param PurRedShortFrozen:
        :param MarginTradeVolume:
        :param MarginTradeAmount:
        :param MarginTradeFrozenVolume:
        :param MarginTradeFrozenAmount:
        :param MarginTradeConversionProfit:
        :param ShortSellVolume:
        :param ShortSellAmount:
        :param ShortSellFrozenVolume:
        :param ShortSellFrozenAmount:
        :param ShortSellConversionProfit:
        :param SSStockValue:
        :param TodayMTPosition:
        :param TodaySSPosition:
        :param YdOpenCost:
        :return:
        """
        self.InstrumentID = InstrumentID
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.PosiDirection = PosiDirection
        self.HedgeFlag = HedgeFlag
        self.PositionDate = PositionDate
        self.YdPosition = int(YdPosition)
        self.Position = int(Position)
        self.LongFrozen = int(LongFrozen)
        self.ShortFrozen = int(ShortFrozen)
        self.LongFrozenAmount = float(LongFrozenAmount)
        self.ShortFrozenAmount = float(ShortFrozenAmount)
        self.OpenVolume = int(OpenVolume)
        self.CloseVolume = int(CloseVolume)
        self.OpenAmount = float(OpenAmount)
        self.CloseAmount = float(CloseAmount)
        self.PositionCost = float(PositionCost)
        self.FrozenCash = float(FrozenCash)
        self.CashIn = float(CashIn)
        self.Commission = float(Commission)
        self.PreSettlementPrice = float(PreSettlementPrice)
        self.SettlementPrice = float(SettlementPrice)
        self.TradingDay = TradingDay
        self.OpenCost = float(OpenCost)
        self.ExchangeMargin = float(ExchangeMargin)
        self.TodayPosition = int(TodayPosition)
        self.TransferFee = float(TransferFee)
        self.StampTax = float(StampTax)
        self.TodayPurRedVolume = int(TodayPurRedVolume)
        self.ConversionRate = float(ConversionRate)
        self.ConversionAmount = float(ConversionAmount)
        self.StockValue = float(StockValue)
        self.ExchangeID = ExchangeID
        self.AccountID = AccountID
        self.PledgeInPosition = int(PledgeInPosition)
        self.RepurchasePosition = int(RepurchasePosition)
        self.PurRedShortFrozen = int(PurRedShortFrozen)
        self.MarginTradeVolume = int(MarginTradeVolume)
        self.MarginTradeAmount = float(MarginTradeAmount)
        self.MarginTradeFrozenVolume = int(MarginTradeFrozenVolume)
        self.MarginTradeFrozenAmount = float(MarginTradeFrozenAmount)
        self.MarginTradeConversionProfit = float(MarginTradeConversionProfit)
        self.ShortSellVolume = int(ShortSellVolume)
        self.ShortSellAmount = float(ShortSellAmount)
        self.ShortSellFrozenVolume = int(ShortSellFrozenVolume)
        self.ShortSellFrozenAmount = float(ShortSellFrozenAmount)
        self.ShortSellConversionProfit = float(ShortSellConversionProfit)
        self.SSStockValue = float(SSStockValue)
        self.TodayMTPosition = int(TodayMTPosition)
        self.TodaySSPosition = int(TodaySSPosition)
        self.YdOpenCost = float(YdOpenCost)


class CSecurityFtdcSyncDepositField(Base):
    def __init__(self, DepositSeqNo, BrokerID, InvestorID, Deposit, IsForce, AccountID):
        """

        :param DepositSeqNo:
        :param BrokerID:
        :param InvestorID:
        :param Deposit:
        :param IsForce:
        :param AccountID:
        :return:
        """
        self.DepositSeqNo = DepositSeqNo
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.Deposit = float(Deposit)
        self.IsForce = int(IsForce)
        self.AccountID = AccountID


class CSecurityFtdcQryExchangeField(Base):
    def __init__(self, ExchangeID):
        """

        :param ExchangeID:
        :return:
        """
        self.ExchangeID = ExchangeID


class CSecurityFtdcQryProductField(Base):
    def __init__(self, ProductID):
        """

        :param ProductID:
        :return:
        """
        self.ProductID = ProductID


class CSecurityFtdcQryInstrumentField(Base):
    def __init__(self, InstrumentID, ExchangeID, ExchangeInstID, ProductID):
        """

        :param InstrumentID:
        :param ExchangeID:
        :param ExchangeInstID:
        :param ProductID:
        :return:
        """
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.ExchangeInstID = ExchangeInstID
        self.ProductID = ProductID


class CSecurityFtdcQryBrokerField(Base):
    def __init__(self, BrokerID):
        """

        :param BrokerID:
        :return:
        """
        self.BrokerID = BrokerID


class CSecurityFtdcQryPartBrokerField(Base):
    def __init__(self, ExchangeID, BrokerID, ParticipantID):
        """

        :param ExchangeID:
        :param BrokerID:
        :param ParticipantID:
        :return:
        """
        self.ExchangeID = ExchangeID
        self.BrokerID = BrokerID
        self.ParticipantID = ParticipantID


class CSecurityFtdcQryInvestorField(Base):
    def __init__(self, BrokerID, InvestorID):
        """

        :param BrokerID:
        :param InvestorID:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class CSecurityFtdcQryTradingCodeField(Base):
    def __init__(self, BrokerID, InvestorID, ExchangeID, ClientID):
        """

        :param BrokerID:
        :param InvestorID:
        :param ExchangeID:
        :param ClientID:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID
        self.ClientID = ClientID


class CSecurityFtdcQrySuperUserField(Base):
    def __init__(self, UserID):
        """

        :param UserID:
        :return:
        """
        self.UserID = UserID


class CSecurityFtdcQrySuperUserFunctionField(Base):
    def __init__(self, UserID):
        """

        :param UserID:
        :return:
        """
        self.UserID = UserID


class CSecurityFtdcQryBrokerUserField(Base):
    def __init__(self, BrokerID, UserID):
        """

        :param BrokerID:
        :param UserID:
        :return:
        """
        self.BrokerID = BrokerID
        self.UserID = UserID


class CSecurityFtdcQryBrokerUserFunctionField(Base):
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


class CSecurityFtdcQryTradingAccountField(Base):
    """

    """

    def __init__(self, BrokerID, InvestorID):
        """

        :param BrokerID:
        :param InvestorID:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class CSecurityFtdcQryLoginForbiddenUserField(Base):
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


class CSecurityFtdcQryDepthMarketDataField(Base):
    """

    """

    def __init__(self, InstrumentID):
        """

        :param InstrumentID:
        :return:
        """
        self.InstrumentID = InstrumentID


class CSecurityFtdcQryInstrumentTradingRightField(Base):
    """

    """

    def __init__(self, ExchangeID, BrokerID, InvestorID, InstrumentID):
        """

        :param ExchangeID:
        :param BrokerID:
        :param InvestorID:
        :param InstrumentID:
        :return:
        """
        self.ExchangeID = ExchangeID
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID


class CSecurityFtdcQryInvestorPositionDetailField(Base):
    """

    """

    def __init__(self, BrokerID, InvestorID, InstrumentID):
        """

        :param BrokerID:
        :param InvestorID:
        :param InstrumentID:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID


class CSecurityFtdcQryBondInterestField(Base):
    """

    """

    def __init__(self, ExchangeID, InstrumentID):
        """

        :param ExchangeID:
        :param InstrumentID:
        :return:
        """
        self.ExchangeID = ExchangeID
        self.InstrumentID = InstrumentID


class CSecurityFtdcQryMarketRationInfoField(Base):
    """

    """

    def __init__(self, BrokerID, InvestorID, ExchangeID):
        """

        :param BrokerID:
        :param InvestorID:
        :param ExchangeID:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID


class CSecurityFtdcQryInstrumentCommissionRateField(Base):
    """

    """

    def __init__(self, ExchangeID, BrokerID, InvestorID, InstrumentID, Direction):
        """

        :param ExchangeID:
        :param BrokerID:
        :param InvestorID:
        :param InstrumentID:
        :param Direction:
        :return:
        """
        self.ExchangeID = ExchangeID
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.Direction = Direction


class CSecurityFtdcQryExcessStockInfoField(Base):
    """

    """

    def __init__(self, BrokerID, InvestorID, ExchangeID, InstrumentID):
        """

        :param BrokerID:
        :param InvestorID:
        :param ExchangeID:
        :param InstrumentID:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID
        self.InstrumentID = InstrumentID


class CSecurityFtdcQryTraderOfferField(Base):
    """

    """

    def __init__(self, ExchangeID, ParticipantID, BranchPBU):
        """

        :param ExchangeID:
        :param ParticipantID:
        :param BranchPBU:
        :return:
        """
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.BranchPBU = BranchPBU


class CSecurityFtdcQryMDTraderOfferField(Base):
    """

    """

    def __init__(self, ExchangeID, ParticipantID, BranchPBU):
        """

        :param ExchangeID:
        :param ParticipantID:
        :param BranchPBU:
        :return:
        """
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.BranchPBU = BranchPBU


class CSecurityFtdcQryFrontStatusField(Base):
    """

    """

    def __init__(self, FrontID):
        """

        :param FrontID:
        :return:
        """
        self.FrontID = int(FrontID)


class CSecurityFtdcQryUserSessionField(Base):
    """

    """

    def __init__(self, FrontID, SessionID, BrokerID, UserID):
        """

        :param FrontID:
        :param SessionID:
        :param BrokerID:
        :param UserID:
        :return:
        """
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.BrokerID = BrokerID
        self.UserID = UserID


class CSecurityFtdcQryOrderField(Base):
    """

    """

    def __init__(self, BrokerID, InvestorID, InstrumentID, ExchangeID, OrderSysID, InsertTimeStart, InsertTimeEnd):
        """

        :param BrokerID:
        :param InvestorID:
        :param InstrumentID:
        :param ExchangeID:
        :param OrderSysID:
        :param InsertTimeStart:
        :param InsertTimeEnd:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.OrderSysID = OrderSysID
        self.InsertTimeStart = InsertTimeStart
        self.InsertTimeEnd = InsertTimeEnd


class CSecurityFtdcQryOrderActionField(Base):
    """

    """

    def __init__(self, BrokerID, InvestorID, ExchangeID):
        """

        :param BrokerID:
        :param InvestorID:
        :param ExchangeID:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID


class CSecurityFtdcQryErrOrderField(Base):
    """

    """

    def __init__(self, BrokerID, InvestorID):
        """

        :param BrokerID:
        :param InvestorID:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class CSecurityFtdcQryErrOrderActionField(Base):
    """

    """

    def __init__(self, BrokerID, InvestorID):
        """

        :param BrokerID:
        :param InvestorID:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class CSecurityFtdcQryTradeField(Base):
    """

    """

    def __init__(self, BrokerID, InvestorID, InstrumentID, ExchangeID, TradeID, TradeTimeStart, TradeTimeEnd):
        """

        :param BrokerID:
        :param InvestorID:
        :param InstrumentID:
        :param ExchangeID:
        :param TradeID:
        :param TradeTimeStart:
        :param TradeTimeEnd:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.TradeID = TradeID
        self.TradeTimeStart = TradeTimeStart
        self.TradeTimeEnd = TradeTimeEnd


class CSecurityFtdcQryInvestorPositionField(Base):
    """

    """

    def __init__(self, BrokerID, InvestorID, InstrumentID):
        """

        :param BrokerID:
        :param InvestorID:
        :param InstrumentID:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID


class CSecurityFtdcQrySyncDepositField(Base):
    """

    """

    def __init__(self, BrokerID, DepositSeqNo):
        """

        :param BrokerID:
        :param DepositSeqNo:
        :return:
        """
        self.BrokerID = BrokerID
        self.DepositSeqNo = DepositSeqNo


class CSecurityFtdcUserPasswordUpdateField(Base):
    """

    """

    def __init__(self, BrokerID, UserID, OldPassword, NewPassword):
        """

        :param BrokerID:
        :param UserID:
        :param OldPassword:
        :param NewPassword:
        :return:
        """
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.OldPassword = OldPassword
        self.NewPassword = NewPassword


class CSecurityFtdcTradingAccountPasswordUpdateField(Base):
    """

    """

    def __init__(self, BrokerID, AccountID, OldPassword, NewPassword):
        """

        :param BrokerID:
        :param AccountID:
        :param OldPassword:
        :param NewPassword:
        :return:
        """
        self.BrokerID = BrokerID
        self.AccountID = AccountID
        self.OldPassword = OldPassword
        self.NewPassword = NewPassword


class CSecurityFtdcManualSyncBrokerUserOTPField(Base):
    """

    """

    def __init__(self, BrokerID, UserID, OTPType, FirstOTP, SecondOTP):
        """

        :param BrokerID:
        :param UserID:
        :param OTPType:
        :param FirstOTP:
        :param SecondOTP:
        :return:
        """
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.OTPType = OTPType
        self.FirstOTP = FirstOTP
        self.SecondOTP = SecondOTP


class CSecurityFtdcBrokerUserPasswordField(Base):
    """

    """

    def __init__(self, BrokerID, UserID, Password):
        """

        :param BrokerID:
        :param UserID:
        :param Password:
        :return:
        """
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.Password = Password


class CSecurityFtdcTradingAccountPasswordField(Base):
    """

    """

    def __init__(self, BrokerID, AccountID, Password):
        """

        :param BrokerID:
        :param AccountID:
        :param Password:
        :return:
        """
        self.BrokerID = BrokerID
        self.AccountID = AccountID
        self.Password = Password


class CSecurityFtdcUserRightField(Base):
    """

    """

    def __init__(self, BrokerID, UserID, UserRightType, IsForbidden):
        """

        :param BrokerID:
        :param UserID:
        :param UserRightType:
        :param IsForbidden:
        :return:
        """
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.UserRightType = UserRightType
        self.IsForbidden = int(IsForbidden)


class CSecurityFtdcInvestorAccountField(Base):
    """

    """

    def __init__(self, BrokerID, InvestorID, AccountID, IsDefault, AccountType, IsActive):
        """

        :param BrokerID:
        :param InvestorID:
        :param AccountID:
        :param IsDefault:
        :param AccountType:
        :param IsActive:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.AccountID = AccountID
        self.IsDefault = int(IsDefault)
        self.AccountType = AccountType
        self.IsActive = int(IsActive)


class CSecurityFtdcUserIPField(Base):
    """

    """

    def __init__(self, BrokerID, UserID, IPAddress, IPMask, MacAddress):
        """

        :param BrokerID:
        :param UserID:
        :param IPAddress:
        :param IPMask:
        :param MacAddress:
        :return:
        """
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.IPAddress = IPAddress
        self.IPMask = IPMask
        self.MacAddress = MacAddress


class CSecurityFtdcBrokerUserOTPParamField(Base):
    """

    """

    def __init__(self, BrokerID, UserID, OTPVendorsID, SerialNumber, AuthKey, LastDrift, LastSuccess, OTPType):
        """

        :param BrokerID:
        :param UserID:
        :param OTPVendorsID:
        :param SerialNumber:
        :param AuthKey:
        :param LastDrift:
        :param LastSuccess:
        :param OTPType:
        :return:
        """
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.OTPVendorsID = OTPVendorsID
        self.SerialNumber = SerialNumber
        self.AuthKey = AuthKey
        self.LastDrift = int(LastDrift)
        self.LastSuccess = int(LastSuccess)
        self.OTPType = OTPType


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


class CSecurityFtdcLogoutAllField(Base):
    """

    """

    def __init__(self, FrontID, SessionID, SystemName):
        """

        :param FrontID:
        :param SessionID:
        :param SystemName:
        :return:
        """
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.SystemName = SystemName


class CSecurityFtdcForceUserLogoutField(Base):
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


class CSecurityFtdcInputOrderField(Base):
    """

    """

    def __init__(self, BrokerID, InvestorID, InstrumentID, OrderRef, UserID, ExchangeID, OrderPriceType, Direction,
                 CombOffsetFlag, CombHedgeFlag, LimitPrice, VolumeTotalOriginal, TimeCondition, GTDDate,
                 VolumeCondition, MinVolume, ContingentCondition, StopPrice, ForceCloseReason, IsAutoSuspend,
                 BusinessUnit, RequestID, UserForceClose):
        """

        :param BrokerID:
        :param InvestorID:
        :param InstrumentID:
        :param OrderRef:
        :param UserID:
        :param ExchangeID:
        :param OrderPriceType:
        :param Direction:
        :param CombOffsetFlag:
        :param CombHedgeFlag:
        :param LimitPrice:
        :param VolumeTotalOriginal:
        :param TimeCondition:
        :param GTDDate:
        :param VolumeCondition:
        :param MinVolume:
        :param ContingentCondition:
        :param StopPrice:
        :param ForceCloseReason:
        :param IsAutoSuspend:
        :param BusinessUnit:
        :param RequestID:
        :param UserForceClose:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.OrderRef = OrderRef
        self.UserID = UserID
        self.ExchangeID = ExchangeID
        self.OrderPriceType = OrderPriceType
        self.Direction = Direction
        self.CombOffsetFlag = CombOffsetFlag
        self.CombHedgeFlag = CombHedgeFlag
        self.LimitPrice = LimitPrice
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = TimeCondition
        self.GTDDate = GTDDate
        self.VolumeCondition = VolumeCondition
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = ContingentCondition
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = ForceCloseReason
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = BusinessUnit
        self.RequestID = int(RequestID)
        self.UserForceClose = int(UserForceClose)


class CSecurityFtdcInputOrderActionField(Base):
    """

    """

    def __init__(self, BrokerID, InvestorID, OrderActionRef, OrderRef, RequestID, FrontID, SessionID, ExchangeID,
                 ActionFlag, LimitPrice, VolumeChange, UserID, InstrumentID, BranchPBU, OrderLocalID):
        """

        :param BrokerID:
        :param InvestorID:
        :param OrderActionRef:
        :param OrderRef:
        :param RequestID:
        :param FrontID:
        :param SessionID:
        :param ExchangeID:
        :param ActionFlag:
        :param LimitPrice:
        :param VolumeChange:
        :param UserID:
        :param InstrumentID:
        :param BranchPBU:
        :param OrderLocalID:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.OrderActionRef = int(OrderActionRef)
        self.OrderRef = OrderRef
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = ExchangeID
        self.ActionFlag = ActionFlag
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.UserID = UserID
        self.InstrumentID = InstrumentID
        self.BranchPBU = BranchPBU
        self.OrderLocalID = OrderLocalID


class CSecurityFtdcSpecificInstrumentField(Base):
    def __init__(self, InstrumentID, ExchangeID):
        """

        :param InstrumentID:
        :param ExchangeID:
        :return:
        """
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID


class CSecurityFtdcSpecificExchangeField(Base):
    def __init__(self, ExchangeID):
        """

        :param ExchangeID:
        :return:
        """
        self.ExchangeID = ExchangeID


class CSecurityFtdcMarketDataBaseField(Base):
    """

    """

    def __init__(self, TradingDay, PreSettlementPrice, PreClosePrice, PreOpenInterest, PreDelta):
        """

        :param TradingDay:
        :param PreSettlementPrice:
        :param PreClosePrice:
        :param PreOpenInterest:
        :param PreDelta:
        :return:
        """
        self.TradingDay = TradingDay
        self.PreSettlementPrice = float(PreSettlementPrice)
        self.PreClosePrice = float(PreClosePrice)
        self.PreOpenInterest = float(PreOpenInterest)
        self.PreDelta = float(PreDelta)


class CSecurityFtdcMarketDataStaticField(Base):
    """

    """

    def __init__(self, OpenPrice, HighestPrice, LowestPrice, ClosePrice, UpperLimitPrice, LowerLimitPrice,
                 SettlementPrice, CurrDelta):
        """

        :param OpenPrice:
        :param HighestPrice:
        :param LowestPrice:
        :param ClosePrice:
        :param UpperLimitPrice:
        :param LowerLimitPrice:
        :param SettlementPrice:
        :param CurrDelta:
        :return:
        """
        self.OpenPrice = float(OpenPrice)
        self.HighestPrice = float(HighestPrice)
        self.LowestPrice = float(LowestPrice)
        self.ClosePrice = float(ClosePrice)
        self.UpperLimitPrice = float(UpperLimitPrice)
        self.LowerLimitPrice = float(LowerLimitPrice)
        self.SettlementPrice = float(SettlementPrice)
        self.CurrDelta = float(CurrDelta)


class CSecurityFtdcMarketDataLastMatchField(Base):
    """

    """

    def __init__(self, LastPrice, Volume, Turnover, OpenInterest):
        """

        :param LastPrice:
        :param Volume:
        :param Turnover:
        :param OpenInterest:
        :return:
        """
        self.LastPrice = float(LastPrice)
        self.Volume = int(Volume)
        self.Turnover = float(Turnover)
        self.OpenInterest = float(OpenInterest)


class CSecurityFtdcMarketDataBestPriceField(Base):
    """

    """

    def __init__(self, BidPrice1, BidVolume1, AskPrice1, AskVolume1):
        """

        :param BidPrice1:
        :param BidVolume1:
        :param AskPrice1:
        :param AskVolume1:
        :return:
        """
        self.BidPrice1 = float(BidPrice1)
        self.BidVolume1 = int(BidVolume1)
        self.AskPrice1 = float(AskPrice1)
        self.AskVolume1 = int(AskVolume1)


class CSecurityFtdcMarketDataBid23Field(Base):
    """

    """

    def __init__(self, BidPrice2, BidVolume2, BidPrice3, BidVolume3):
        """

        :param BidPrice2:
        :param BidVolume2:
        :param BidPrice3:
        :param BidVolume3:
        :return:
        """
        self.BidPrice2 = float(BidPrice2)
        self.BidVolume2 = int(BidVolume2)
        self.BidPrice3 = float(BidPrice3)
        self.BidVolume3 = int(BidVolume3)


class CSecurityFtdcMarketDataAsk23Field(Base):
    """

    """

    def __init__(self, AskPrice2, AskVolume2, AskPrice3, AskVolume3):
        """

        :param AskPrice2:
        :param AskVolume2:
        :param AskPrice3:
        :param AskVolume3:
        :return:
        """
        self.AskPrice2 = float(AskPrice2)
        self.AskVolume2 = int(AskVolume2)
        self.AskPrice3 = float(AskPrice3)
        self.AskVolume3 = int(AskVolume3)


class CSecurityFtdcMarketDataBid45Field(Base):
    """

    """

    def __init__(self, BidPrice4, BidVolume4, BidPrice5, BidVolume5):
        """

        :param BidPrice4:
        :param BidVolume4:
        :param BidPrice5:
        :param BidVolume5:
        :return:
        """
        self.BidPrice4 = float(BidPrice4)
        self.BidVolume4 = int(BidVolume4)
        self.BidPrice5 = float(BidPrice5)
        self.BidVolume5 = int(BidVolume5)


class CSecurityFtdcMarketDataAsk45Field(Base):
    """

    """

    def __init__(self, AskPrice4, AskVolume4, AskPrice5, AskVolume5):
        """

        :param AskPrice4:
        :param AskVolume4:
        :param AskPrice5:
        :param AskVolume5:
        :return:
        """
        self.AskPrice4 = float(AskPrice4)
        self.AskVolume4 = int(AskVolume4)
        self.AskPrice5 = float(AskPrice5)
        self.AskVolume5 = int(AskVolume5)


class CSecurityFtdcMarketDataUpdateTimeField(Base):
    """

    """

    def __init__(self, InstrumentID, UpdateTime, UpdateMillisec, ActionDay):
        """

        :param InstrumentID:
        :param UpdateTime:
        :param UpdateMillisec:
        :param ActionDay:
        :return:
        """
        self.InstrumentID = InstrumentID
        self.UpdateTime = UpdateTime
        self.UpdateMillisec = int(UpdateMillisec)
        self.ActionDay = ActionDay


class CSecurityFtdcMarketDataAveragePriceField(Base):
    """

    """

    def __init__(self, AveragePrice):
        """

        :param AveragePrice:
        :return:
        """
        self.AveragePrice = float(AveragePrice)


class CSecurityFtdcMarketDataExchangeField(Base):
    """

    """

    def __init__(self, ExchangeID):
        """

        :param ExchangeID:
        :return:
        """
        self.ExchangeID = ExchangeID


class CSecurityFtdcDisseminationField(Base):
    """

    """

    def __init__(self, SequenceSeries, SequenceNo):
        """

        :param SequenceSeries:
        :param SequenceNo:
        :return:
        """
        self.SequenceSeries = int(SequenceSeries)
        self.SequenceNo = int(SequenceNo)


class CSecurityFtdcInputFundTransferField(Base):
    """

    """

    def __init__(self, BrokerID, InvestorID, AccountID, Password, UserID, TradeAmount, Digest, AccountType):
        """

        :param BrokerID:
        :param InvestorID:
        :param AccountID:
        :param Password:
        :param UserID:
        :param TradeAmount:
        :param Digest:
        :param AccountType:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.AccountID = AccountID
        self.Password = Password
        self.UserID = UserID
        self.TradeAmount = float(TradeAmount)
        self.Digest = Digest
        self.AccountType = AccountType


class CSecurityFtdcFundTransferField(Base):
    """

    """

    def __init__(self, BrokerID, InvestorID, AccountID, Password, UserID, TradeAmount, Digest, SessionID, LiberSerial,
                 PlateSerial, TransferSerial, TradingDay, TradeTime, FundDirection, ErrorID, ErrorMsg):
        """

        :param BrokerID:
        :param InvestorID:
        :param AccountID:
        :param Password:
        :param UserID:
        :param TradeAmount:
        :param Digest:
        :param SessionID:
        :param LiberSerial:
        :param PlateSerial:
        :param TransferSerial:
        :param TradingDay:
        :param TradeTime:
        :param FundDirection:
        :param ErrorID:
        :param ErrorMsg:
        :return:
        """
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.AccountID = AccountID
        self.Password = Password
        self.UserID = UserID
        self.TradeAmount = float(TradeAmount)
        self.Digest = Digest
        self.SessionID = int(SessionID)
        self.LiberSerial = int(LiberSerial)
        self.PlateSerial = int(PlateSerial)
        self.TransferSerial = TransferSerial
        self.TradingDay = TradingDay
        self.TradeTime = TradeTime
        self.FundDirection = FundDirection
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg


class CSecurityFtdcQryFundTransferSerialField(Base):
    """

    """

    def __init__(self, BrokerID, AccountID, AccountType):
        """

        :param BrokerID:
        :param AccountID:
        :param AccountType:
        :return:
        """
        self.BrokerID = BrokerID
        self.AccountID = AccountID
        self.AccountType = AccountType


RspInfo = CSecurityFtdcRspInfoField
Exchange = CSecurityFtdcExchangeField
Product = CSecurityFtdcProductField
Instrument = CSecurityFtdcInstrumentField
Broker = CSecurityFtdcBrokerField
PartBroker = CSecurityFtdcPartBrokerField
Investor = CSecurityFtdcInvestorField
TradingCode = CSecurityFtdcTradingCodeField
SuperUser = CSecurityFtdcSuperUserField
SuperUserFunction = CSecurityFtdcSuperUserFunctionField
BrokerUser = CSecurityFtdcBrokerUserField
BrokerUserFunction = CSecurityFtdcBrokerUserFunctionField
TradingAccount = CSecurityFtdcTradingAccountField
LoginForbiddenUser = CSecurityFtdcLoginForbiddenUserField
DepthMarketData = CSecurityFtdcDepthMarketDataField
InstrumentTradingRight = CSecurityFtdcInstrumentTradingRightField
InvestorPositionDetail = CSecurityFtdcInvestorPositionDetailField
BondInterest = CSecurityFtdcBondInterestField
MarketRationInfo = CSecurityFtdcMarketRationInfoField
InstrumentCommissionRate = CSecurityFtdcInstrumentCommissionRateField
ExcessStockInfo = CSecurityFtdcExcessStockInfoField
TraderOffer = CSecurityFtdcTraderOfferField
MDTraderOffer = CSecurityFtdcMDTraderOfferField
FrontStatus = CSecurityFtdcFrontStatusField
UserSession = CSecurityFtdcUserSessionField
Order = CSecurityFtdcOrderField
OrderAction = CSecurityFtdcOrderActionField
ErrOrder = CSecurityFtdcErrOrderField
ErrOrderAction = CSecurityFtdcErrOrderActionField
Trade = CSecurityFtdcTradeField
InvestorPosition = CSecurityFtdcInvestorPositionField
SyncDeposit = CSecurityFtdcSyncDepositField
QryExchange = CSecurityFtdcQryExchangeField
QryProduct = CSecurityFtdcQryProductField
QryInstrument = CSecurityFtdcQryInstrumentField
QryBroker = CSecurityFtdcQryBrokerField
QryPartBroker = CSecurityFtdcQryPartBrokerField
QryInvestor = CSecurityFtdcQryInvestorField
QryTradingCode = CSecurityFtdcQryTradingCodeField
QrySuperUser = CSecurityFtdcQrySuperUserField
QrySuperUserFunction = CSecurityFtdcQrySuperUserFunctionField
QryBrokerUser = CSecurityFtdcQryBrokerUserField
QryBrokerUserFunction = CSecurityFtdcQryBrokerUserFunctionField
QryTradingAccount = CSecurityFtdcQryTradingAccountField
QryLoginForbiddenUser = CSecurityFtdcQryLoginForbiddenUserField
QryDepthMarketData = CSecurityFtdcQryDepthMarketDataField
QryInstrumentTradingRight = CSecurityFtdcQryInstrumentTradingRightField
QryInvestorPositionDetail = CSecurityFtdcQryInvestorPositionDetailField
QryBondInterest = CSecurityFtdcQryBondInterestField
QryMarketRationInfo = CSecurityFtdcQryMarketRationInfoField
QryInstrumentCommissionRate = CSecurityFtdcQryInstrumentCommissionRateField
QryExcessStockInfo = CSecurityFtdcQryExcessStockInfoField
QryTraderOffer = CSecurityFtdcQryTraderOfferField
QryMDTraderOffer = CSecurityFtdcQryMDTraderOfferField
QryFrontStatus = CSecurityFtdcQryFrontStatusField
QryUserSession = CSecurityFtdcQryUserSessionField
QryOrder = CSecurityFtdcQryOrderField
QryOrderAction = CSecurityFtdcQryOrderActionField
QryErrOrder = CSecurityFtdcQryErrOrderField
QryErrOrderAction = CSecurityFtdcQryErrOrderActionField
QryTrade = CSecurityFtdcQryTradeField
QryInvestorPosition = CSecurityFtdcQryInvestorPositionField
QrySyncDeposit = CSecurityFtdcQrySyncDepositField
UserPasswordUpdate = CSecurityFtdcUserPasswordUpdateField
TradingAccountPasswordUpdate = CSecurityFtdcTradingAccountPasswordUpdateField
ManualSyncBrokerUserOTP = CSecurityFtdcManualSyncBrokerUserOTPField
BrokerUserPassword = CSecurityFtdcBrokerUserPasswordField
TradingAccountPassword = CSecurityFtdcTradingAccountPasswordField
UserRight = CSecurityFtdcUserRightField
InvestorAccount = CSecurityFtdcInvestorAccountField
UserIP = CSecurityFtdcUserIPField
BrokerUserOTPParam = CSecurityFtdcBrokerUserOTPParamField
ReqUserLogin = CSecurityFtdcReqUserLoginField
RspUserLogin = CSecurityFtdcRspUserLoginField
UserLogout = CSecurityFtdcUserLogoutField
LogoutAll = CSecurityFtdcLogoutAllField
ForceUserLogout = CSecurityFtdcForceUserLogoutField
InputOrder = CSecurityFtdcInputOrderField
InputOrderAction = CSecurityFtdcInputOrderActionField
SpecificInstrument = CSecurityFtdcSpecificInstrumentField
SpecificExchange = CSecurityFtdcSpecificExchangeField
MarketDataBase = CSecurityFtdcMarketDataBaseField
MarketDataStatic = CSecurityFtdcMarketDataStaticField
MarketDataLastMatch = CSecurityFtdcMarketDataLastMatchField
MarketDataBestPrice = CSecurityFtdcMarketDataBestPriceField
MarketDataBid23 = CSecurityFtdcMarketDataBid23Field
MarketDataAsk23 = CSecurityFtdcMarketDataAsk23Field
MarketDataBid45 = CSecurityFtdcMarketDataBid45Field
MarketDataAsk45 = CSecurityFtdcMarketDataAsk45Field
MarketDataUpdateTime = CSecurityFtdcMarketDataUpdateTimeField
MarketDataAveragePrice = CSecurityFtdcMarketDataAveragePriceField
MarketDataExchange = CSecurityFtdcMarketDataExchangeField
Dissemination = CSecurityFtdcDisseminationField
InputFundTransfer = CSecurityFtdcInputFundTransferField
FundTransfer = CSecurityFtdcFundTransferField
QryFundTransferSerial = CSecurityFtdcQryFundTransferSerialField
