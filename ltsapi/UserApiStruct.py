# -*- coding=utf-8 -*-
"""
生成结构化的代码

"""


class Base(object):
    def __repr__(self):
        """
        :return:
        """
        return "<%s>" % ",".join(["%s:%s" % (item, value) for item, value in self.__dict__.iteritems()])


class CSecurityFtdcRspInfoField(Base):
    def __init__(self, ErrorID, ErrorMsg):
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg


class CSecurityFtdcExchangeField(Base):
    def __init__(self, ExchangeID, ExchangeName, ExchangeProperty):
        self.ExchangeID = ExchangeID
        self.ExchangeName = ExchangeName
        self.ExchangeProperty = ExchangeProperty


class CSecurityFtdcProductField(Base):
    def __init__(self, ProductID, ProductName, ExchangeID, ProductClass, VolumeMultiple, PriceTick,
                 MaxMarketOrderVolume, MinMarketOrderVolume, MaxLimitOrderVolume, MinLimitOrderVolume, PositionType,
                 PositionDateType, EFTMinTradeVolume):
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
    def __init__(self, InstrumentID, ExchangeID, InstrumentName, ExchangeInstID, ProductID, ProductClass, DeliveryYear,
                 DeliveryMonth, MaxMarketOrderVolume, MinMarketOrderVolume, MaxLimitOrderVolume, MinLimitOrderVolume,
                 VolumeMultiple, PriceTick, CreateDate, OpenDate, ExpireDate, StartDelivDate, EndDelivDate,
                 InstLifePhase, IsTrading, PositionType, OrderCanBeWithdraw, MinBuyVolume, MinSellVolume, RightModelID,
                 PosTradeType, MarketID):
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
    def __init__(self, BrokerID, BrokerAbbr, BrokerName, IsActive):
        self.BrokerID = BrokerID
        self.BrokerAbbr = BrokerAbbr
        self.BrokerName = BrokerName
        self.IsActive = int(IsActive)


class CSecurityFtdcPartBrokerField(Base):
    def __init__(self, BrokerID, ExchangeID, ParticipantID, IsActive):
        self.BrokerID = BrokerID
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.IsActive = int(IsActive)


class CSecurityFtdcInvestorField(Base):
    def __init__(self, InvestorID, BrokerID, InvestorGroupID, InvestorName, IdentifiedCardType, IdentifiedCardNo,
                 IsActive, SHBranchID, SZBranchID):
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
    def __init__(self, InvestorID, BrokerID, ExchangeID, ClientID, IsActive, AccountID, PBU, ClientType):
        self.InvestorID = InvestorID
        self.BrokerID = BrokerID
        self.ExchangeID = ExchangeID
        self.ClientID = ClientID
        self.IsActive = int(IsActive)
        self.AccountID = AccountID
        self.PBU = PBU
        self.ClientType = ClientType


class CSecurityFtdcSuperUserField(Base):
    def __init__(self, UserID, UserName, Password, IsActive):
        self.UserID = UserID
        self.UserName = UserName
        self.Password = Password
        self.IsActive = int(IsActive)


class CSecurityFtdcSuperUserFunctionField(Base):
    def __init__(self, UserID, FunctionCode):
        self.UserID = UserID
        self.FunctionCode = FunctionCode


class CSecurityFtdcBrokerUserField(Base):
    def __init__(self, BrokerID, UserID, UserName, UserType, IsActive, IsUsingOTP):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.UserName = UserName
        self.UserType = UserType
        self.IsActive = int(IsActive)
        self.IsUsingOTP = int(IsUsingOTP)


class CSecurityFtdcBrokerUserFunctionField(Base):
    def __init__(self, BrokerID, UserID, BrokerFunctionCode):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.BrokerFunctionCode = BrokerFunctionCode


class CSecurityFtdcTradingAccountField(Base):
    def __init__(self, BrokerID, AccountID, PreMortgage, PreCredit, PreDeposit, PreBalance, PreMargin, InterestBase,
                 Interest, Deposit, Withdraw, FrozenMargin, FrozenCash, FrozenCommission, CurrMargin, CashIn,
                 Commission, Balance, Available, WithdrawQuota, Reserve, TradingDay, Credit, Mortgage, ExchangeMargin,
                 DeliveryMargin, ExchangeDeliveryMargin, FrozenTransferFee, FrozenStampTax, TransferFee, StampTax,
                 ConversionAmount, CreditAmount, StockValue, BondRepurchaseAmount, ReverseRepurchaseAmount,
                 CurrencyCode, AccountType, MarginTradeAmount, ShortSellAmount, MarginTradeProfit, ShortSellProfit,
                 SSStockValue, CreditRatio):
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
    def __init__(self, BrokerID, UserID):
        self.BrokerID = BrokerID
        self.UserID = UserID


class CSecurityFtdcDepthMarketDataField(Base):
    def __init__(self, TradingDay, InstrumentID, ExchangeID, ExchangeInstID, LastPrice, PreSettlementPrice,
                 PreClosePrice, PreOpenInterest, OpenPrice, HighestPrice, LowestPrice, Volume, Turnover, OpenInterest,
                 ClosePrice, SettlementPrice, UpperLimitPrice, LowerLimitPrice, PreDelta, CurrDelta, UpdateTime,
                 UpdateMillisec, BidPrice1, BidVolume1, AskPrice1, AskVolume1, BidPrice2, BidVolume2, AskPrice2,
                 AskVolume2, BidPrice3, BidVolume3, AskPrice3, AskVolume3, BidPrice4, BidVolume4, AskPrice4, AskVolume4,
                 BidPrice5, BidVolume5, AskPrice5, AskVolume5, AveragePrice, ActionDay):
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
    def __init__(self, InstrumentID, InvestorRange, BrokerID, InvestorID, Direction, TradingRight, ExchangeID,
                 InstrumentRange):
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.Direction = Direction
        self.TradingRight = TradingRight
        self.ExchangeID = ExchangeID
        self.InstrumentRange = InstrumentRange


class CSecurityFtdcInvestorPositionDetailField(Base):
    def __init__(self, InstrumentID, BrokerID, InvestorID, HedgeFlag, Direction, OpenDate, TradeID, Volume, OpenPrice,
                 TradingDay, TradeType, ExchangeID, Margin, ExchMargin, LastSettlementPrice, SettlementPrice,
                 CloseVolume, CloseAmount, TransferFee, StampTax, Commission, AccountID, PledgeInPosition,
                 PledgeInFrozenPosition, RepurchasePosition, Amount):
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
    def __init__(self, TradingDay, ExchangeID, InstrumentID, Interest):
        self.TradingDay = TradingDay
        self.ExchangeID = ExchangeID
        self.InstrumentID = InstrumentID
        self.Interest = float(Interest)


class CSecurityFtdcMarketRationInfoField(Base):
    def __init__(self, BrokerID, InvestorID, ExchangeID, RationVolume):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID
        self.RationVolume = int(RationVolume)


class CSecurityFtdcInstrumentCommissionRateField(Base):
    def __init__(self, ExchangeID, InstrumentID, InvestorRange, BrokerID, InvestorID, Direction, StampTaxRateByMoney,
                 StampTaxRateByVolume, TransferFeeRateByMoney, TransferFeeRateByVolume, TradeFeeByMoney,
                 TradeFeeByVolume, MarginByMoney, MinTradeFee):
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
        self.FrontID = int(FrontID)
        self.LastReportDate = LastReportDate
        self.LastReportTime = LastReportTime
        self.IsActive = int(IsActive)


class CSecurityFtdcUserSessionField(Base):
    def __init__(self, FrontID, SessionID, BrokerID, UserID, LoginDate, LoginTime, IPAddress, UserProductInfo,
                 InterfaceProductInfo, ProtocolInfo, MacAddress):
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
        self.DepositSeqNo = DepositSeqNo
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.Deposit = float(Deposit)
        self.IsForce = int(IsForce)
        self.AccountID = AccountID


class CSecurityFtdcQryExchangeField(Base):
    def __init__(self, ExchangeID):
        self.ExchangeID = ExchangeID


class CSecurityFtdcQryProductField(Base):
    def __init__(self, ProductID):
        self.ProductID = ProductID


class CSecurityFtdcQryInstrumentField(Base):
    def __init__(self, InstrumentID, ExchangeID, ExchangeInstID, ProductID):
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.ExchangeInstID = ExchangeInstID
        self.ProductID = ProductID


class CSecurityFtdcQryBrokerField(Base):
    def __init__(self, BrokerID):
        self.BrokerID = BrokerID


class CSecurityFtdcQryPartBrokerField(Base):
    def __init__(self, ExchangeID, BrokerID, ParticipantID):
        self.ExchangeID = ExchangeID
        self.BrokerID = BrokerID
        self.ParticipantID = ParticipantID


class CSecurityFtdcQryInvestorField(Base):
    def __init__(self, BrokerID, InvestorID):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class CSecurityFtdcQryTradingCodeField(Base):
    def __init__(self, BrokerID, InvestorID, ExchangeID, ClientID):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID
        self.ClientID = ClientID


class CSecurityFtdcQrySuperUserField(Base):
    def __init__(self, UserID):
        self.UserID = UserID


class CSecurityFtdcQrySuperUserFunctionField(Base):
    def __init__(self, UserID):
        self.UserID = UserID


class CSecurityFtdcQryBrokerUserField(Base):
    def __init__(self, BrokerID, UserID):
        self.BrokerID = BrokerID
        self.UserID = UserID


class CSecurityFtdcQryBrokerUserFunctionField(Base):
    def __init__(self, BrokerID, UserID):
        self.BrokerID = BrokerID
        self.UserID = UserID


class CSecurityFtdcQryTradingAccountField(Base):
    def __init__(self, BrokerID, InvestorID):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class CSecurityFtdcQryLoginForbiddenUserField(Base):
    def __init__(self, BrokerID, UserID):
        self.BrokerID = BrokerID
        self.UserID = UserID


class CSecurityFtdcQryDepthMarketDataField(Base):
    def __init__(self, InstrumentID):
        self.InstrumentID = InstrumentID


class CSecurityFtdcQryInstrumentTradingRightField(Base):
    def __init__(self, ExchangeID, BrokerID, InvestorID, InstrumentID):
        self.ExchangeID = ExchangeID
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID


class CSecurityFtdcQryInvestorPositionDetailField(Base):
    def __init__(self, BrokerID, InvestorID, InstrumentID):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID


class CSecurityFtdcQryBondInterestField(Base):
    def __init__(self, ExchangeID, InstrumentID):
        self.ExchangeID = ExchangeID
        self.InstrumentID = InstrumentID


class CSecurityFtdcQryMarketRationInfoField(Base):
    def __init__(self, BrokerID, InvestorID, ExchangeID):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID


class CSecurityFtdcQryInstrumentCommissionRateField(Base):
    def __init__(self, ExchangeID, BrokerID, InvestorID, InstrumentID, Direction):
        self.ExchangeID = ExchangeID
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.Direction = Direction


class CSecurityFtdcQryExcessStockInfoField(Base):
    def __init__(self, BrokerID, InvestorID, ExchangeID, InstrumentID):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID
        self.InstrumentID = InstrumentID


class CSecurityFtdcQryTraderOfferField(Base):
    def __init__(self, ExchangeID, ParticipantID, BranchPBU):
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.BranchPBU = BranchPBU


class CSecurityFtdcQryMDTraderOfferField(Base):
    def __init__(self, ExchangeID, ParticipantID, BranchPBU):
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.BranchPBU = BranchPBU


class CSecurityFtdcQryFrontStatusField(Base):
    def __init__(self, FrontID):
        self.FrontID = int(FrontID)


class CSecurityFtdcQryUserSessionField(Base):
    def __init__(self, FrontID, SessionID, BrokerID, UserID):
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.BrokerID = BrokerID
        self.UserID = UserID


class CSecurityFtdcQryOrderField(Base):
    def __init__(self, BrokerID, InvestorID, InstrumentID, ExchangeID, OrderSysID, InsertTimeStart, InsertTimeEnd):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.OrderSysID = OrderSysID
        self.InsertTimeStart = InsertTimeStart
        self.InsertTimeEnd = InsertTimeEnd


class CSecurityFtdcQryOrderActionField(Base):
    def __init__(self, BrokerID, InvestorID, ExchangeID):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID


class CSecurityFtdcQryErrOrderField(Base):
    def __init__(self, BrokerID, InvestorID):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class CSecurityFtdcQryErrOrderActionField(Base):
    def __init__(self, BrokerID, InvestorID):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class CSecurityFtdcQryTradeField(Base):
    def __init__(self, BrokerID, InvestorID, InstrumentID, ExchangeID, TradeID, TradeTimeStart, TradeTimeEnd):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.TradeID = TradeID
        self.TradeTimeStart = TradeTimeStart
        self.TradeTimeEnd = TradeTimeEnd


class CSecurityFtdcQryInvestorPositionField(Base):
    def __init__(self, BrokerID, InvestorID, InstrumentID):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID


class CSecurityFtdcQrySyncDepositField(Base):
    def __init__(self, BrokerID, DepositSeqNo):
        self.BrokerID = BrokerID
        self.DepositSeqNo = DepositSeqNo


class CSecurityFtdcUserPasswordUpdateField(Base):
    def __init__(self, BrokerID, UserID, OldPassword, NewPassword):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.OldPassword = OldPassword
        self.NewPassword = NewPassword


class CSecurityFtdcTradingAccountPasswordUpdateField(Base):
    def __init__(self, BrokerID, AccountID, OldPassword, NewPassword):
        self.BrokerID = BrokerID
        self.AccountID = AccountID
        self.OldPassword = OldPassword
        self.NewPassword = NewPassword


class CSecurityFtdcManualSyncBrokerUserOTPField(Base):
    def __init__(self, BrokerID, UserID, OTPType, FirstOTP, SecondOTP):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.OTPType = OTPType
        self.FirstOTP = FirstOTP
        self.SecondOTP = SecondOTP


class CSecurityFtdcBrokerUserPasswordField(Base):
    def __init__(self, BrokerID, UserID, Password):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.Password = Password


class CSecurityFtdcTradingAccountPasswordField(Base):
    def __init__(self, BrokerID, AccountID, Password):
        self.BrokerID = BrokerID
        self.AccountID = AccountID
        self.Password = Password


class CSecurityFtdcUserRightField(Base):
    def __init__(self, BrokerID, UserID, UserRightType, IsForbidden):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.UserRightType = UserRightType
        self.IsForbidden = int(IsForbidden)


class CSecurityFtdcInvestorAccountField(Base):
    def __init__(self, BrokerID, InvestorID, AccountID, IsDefault, AccountType, IsActive):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.AccountID = AccountID
        self.IsDefault = int(IsDefault)
        self.AccountType = AccountType
        self.IsActive = int(IsActive)


class CSecurityFtdcUserIPField(Base):
    def __init__(self, BrokerID, UserID, IPAddress, IPMask, MacAddress):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.IPAddress = IPAddress
        self.IPMask = IPMask
        self.MacAddress = MacAddress


class CSecurityFtdcBrokerUserOTPParamField(Base):
    def __init__(self, BrokerID, UserID, OTPVendorsID, SerialNumber, AuthKey, LastDrift, LastSuccess, OTPType):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.OTPVendorsID = OTPVendorsID
        self.SerialNumber = SerialNumber
        self.AuthKey = AuthKey
        self.LastDrift = int(LastDrift)
        self.LastSuccess = int(LastSuccess)
        self.OTPType = OTPType


class CSecurityFtdcReqUserLoginField(Base):
    def __init__(self, TradingDay, BrokerID, UserID, Password, UserProductInfo, InterfaceProductInfo, ProtocolInfo,
                 MacAddress, OneTimePassword, ClientIPAddress, AuthCode):
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
    def __init__(self, TradingDay, LoginTime, BrokerID, UserID, SystemName, FrontID, SessionID, MaxOrderRef):
        self.TradingDay = TradingDay
        self.LoginTime = LoginTime
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.SystemName = SystemName
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.MaxOrderRef = MaxOrderRef


class CSecurityFtdcUserLogoutField(Base):
    def __init__(self, BrokerID, UserID):
        self.BrokerID = BrokerID
        self.UserID = UserID


class CSecurityFtdcLogoutAllField(Base):
    def __init__(self, FrontID, SessionID, SystemName):
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.SystemName = SystemName


class CSecurityFtdcForceUserLogoutField(Base):
    def __init__(self, BrokerID, UserID):
        self.BrokerID = BrokerID
        self.UserID = UserID


class CSecurityFtdcInputOrderField(Base):
    def __init__(self, BrokerID, InvestorID, InstrumentID, OrderRef, UserID, ExchangeID, OrderPriceType, Direction,
                 CombOffsetFlag, CombHedgeFlag, LimitPrice, VolumeTotalOriginal, TimeCondition, GTDDate,
                 VolumeCondition, MinVolume, ContingentCondition, StopPrice, ForceCloseReason, IsAutoSuspend,
                 BusinessUnit, RequestID, UserForceClose):
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
    def __init__(self, BrokerID, InvestorID, OrderActionRef, OrderRef, RequestID, FrontID, SessionID, ExchangeID,
                 ActionFlag, LimitPrice, VolumeChange, UserID, InstrumentID, BranchPBU, OrderLocalID):
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
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID


class CSecurityFtdcSpecificExchangeField(Base):
    def __init__(self, ExchangeID):
        self.ExchangeID = ExchangeID


class CSecurityFtdcMarketDataBaseField(Base):
    def __init__(self, TradingDay, PreSettlementPrice, PreClosePrice, PreOpenInterest, PreDelta):
        self.TradingDay = TradingDay
        self.PreSettlementPrice = float(PreSettlementPrice)
        self.PreClosePrice = float(PreClosePrice)
        self.PreOpenInterest = float(PreOpenInterest)
        self.PreDelta = float(PreDelta)


class CSecurityFtdcMarketDataStaticField(Base):
    def __init__(self, OpenPrice, HighestPrice, LowestPrice, ClosePrice, UpperLimitPrice, LowerLimitPrice,
                 SettlementPrice, CurrDelta):
        self.OpenPrice = float(OpenPrice)
        self.HighestPrice = float(HighestPrice)
        self.LowestPrice = float(LowestPrice)
        self.ClosePrice = float(ClosePrice)
        self.UpperLimitPrice = float(UpperLimitPrice)
        self.LowerLimitPrice = float(LowerLimitPrice)
        self.SettlementPrice = float(SettlementPrice)
        self.CurrDelta = float(CurrDelta)


class CSecurityFtdcMarketDataLastMatchField(Base):
    def __init__(self, LastPrice, Volume, Turnover, OpenInterest):
        self.LastPrice = float(LastPrice)
        self.Volume = int(Volume)
        self.Turnover = float(Turnover)
        self.OpenInterest = float(OpenInterest)


class CSecurityFtdcMarketDataBestPriceField(Base):
    def __init__(self, BidPrice1, BidVolume1, AskPrice1, AskVolume1):
        self.BidPrice1 = float(BidPrice1)
        self.BidVolume1 = int(BidVolume1)
        self.AskPrice1 = float(AskPrice1)
        self.AskVolume1 = int(AskVolume1)


class CSecurityFtdcMarketDataBid23Field(Base):
    def __init__(self, BidPrice2, BidVolume2, BidPrice3, BidVolume3):
        self.BidPrice2 = float(BidPrice2)
        self.BidVolume2 = int(BidVolume2)
        self.BidPrice3 = float(BidPrice3)
        self.BidVolume3 = int(BidVolume3)


class CSecurityFtdcMarketDataAsk23Field(Base):
    def __init__(self, AskPrice2, AskVolume2, AskPrice3, AskVolume3):
        self.AskPrice2 = float(AskPrice2)
        self.AskVolume2 = int(AskVolume2)
        self.AskPrice3 = float(AskPrice3)
        self.AskVolume3 = int(AskVolume3)


class CSecurityFtdcMarketDataBid45Field(Base):
    def __init__(self, BidPrice4, BidVolume4, BidPrice5, BidVolume5):
        self.BidPrice4 = float(BidPrice4)
        self.BidVolume4 = int(BidVolume4)
        self.BidPrice5 = float(BidPrice5)
        self.BidVolume5 = int(BidVolume5)


class CSecurityFtdcMarketDataAsk45Field(Base):
    def __init__(self, AskPrice4, AskVolume4, AskPrice5, AskVolume5):
        self.AskPrice4 = float(AskPrice4)
        self.AskVolume4 = int(AskVolume4)
        self.AskPrice5 = float(AskPrice5)
        self.AskVolume5 = int(AskVolume5)


class CSecurityFtdcMarketDataUpdateTimeField(Base):
    def __init__(self, InstrumentID, UpdateTime, UpdateMillisec, ActionDay):
        self.InstrumentID = InstrumentID
        self.UpdateTime = UpdateTime
        self.UpdateMillisec = int(UpdateMillisec)
        self.ActionDay = ActionDay


class CSecurityFtdcMarketDataAveragePriceField(Base):
    def __init__(self, AveragePrice):
        self.AveragePrice = float(AveragePrice)


class CSecurityFtdcMarketDataExchangeField(Base):
    def __init__(self, ExchangeID):
        self.ExchangeID = ExchangeID


class CSecurityFtdcDisseminationField(Base):
    def __init__(self, SequenceSeries, SequenceNo):
        self.SequenceSeries = int(SequenceSeries)
        self.SequenceNo = int(SequenceNo)


class CSecurityFtdcInputFundTransferField(Base):
    def __init__(self, BrokerID, InvestorID, AccountID, Password, UserID, TradeAmount, Digest, AccountType):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.AccountID = AccountID
        self.Password = Password
        self.UserID = UserID
        self.TradeAmount = float(TradeAmount)
        self.Digest = Digest
        self.AccountType = AccountType


class CSecurityFtdcFundTransferField(Base):
    def __init__(self, BrokerID, InvestorID, AccountID, Password, UserID, TradeAmount, Digest, SessionID, LiberSerial,
                 PlateSerial, TransferSerial, TradingDay, TradeTime, FundDirection, ErrorID, ErrorMsg):
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
    def __init__(self, BrokerID, AccountID, AccountType):
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
