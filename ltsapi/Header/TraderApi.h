#include "Python.h"
#include "SecurityFtdcTraderApi.h"


class CTraderSpi : public CSecurityFtdcTraderSpi {
public:

    CTraderSpi();

    ~CTraderSpi();

    virtual void OnFrontConnected();

    virtual void OnFrontDisconnected(int nReason);

    virtual void OnHeartBeatWarning(int nTimeLapse);

    virtual void OnRspError(CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

    virtual void OnRspUserLogin(CSecurityFtdcRspUserLoginField *pRspUserLogin, CSecurityFtdcRspInfoField *pRspInfo,
                                int nRequestID, bool bIsLast);

    virtual void OnRspUserLogout(CSecurityFtdcUserLogoutField *pUserLogout, CSecurityFtdcRspInfoField *pRspInfo,
                                 int nRequestID, bool bIsLast);

    virtual void OnRspOrderInsert(CSecurityFtdcInputOrderField *pInputOrder, CSecurityFtdcRspInfoField *pRspInfo,
                                  int nRequestID, bool bIsLast);

    virtual void OnRspOrderAction(CSecurityFtdcInputOrderActionField *pInputOrderAction,
                                  CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

    virtual void OnRspUserPasswordUpdate(CSecurityFtdcUserPasswordUpdateField *pUserPasswordUpdate,
                                         CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

    virtual void OnRspTradingAccountPasswordUpdate(
            CSecurityFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate,
            CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

    virtual void OnRspQryExchange(CSecurityFtdcExchangeField *pExchange, CSecurityFtdcRspInfoField *pRspInfo,
                                  int nRequestID, bool bIsLast);

    virtual void OnRspQryInstrument(CSecurityFtdcInstrumentField *pInstrument, CSecurityFtdcRspInfoField *pRspInfo,
                                    int nRequestID, bool bIsLast);

    virtual void OnRspQryInvestor(CSecurityFtdcInvestorField *pInvestor, CSecurityFtdcRspInfoField *pRspInfo,
                                  int nRequestID, bool bIsLast);

    virtual void OnRspQryTradingCode(CSecurityFtdcTradingCodeField *pTradingCode, CSecurityFtdcRspInfoField *pRspInfo,
                                     int nRequestID, bool bIsLast);

    virtual void OnRspQryTradingAccount(CSecurityFtdcTradingAccountField *pTradingAccount,
                                        CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

    virtual void OnRspQryDepthMarketData(CSecurityFtdcDepthMarketDataField *pDepthMarketData,
                                         CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

    virtual void OnRspQryBondInterest(CSecurityFtdcBondInterestField *pBondInterest,
                                      CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

    virtual void OnRspQryMarketRationInfo(CSecurityFtdcMarketRationInfoField *pMarketRationInfo,
                                          CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

    virtual void OnRspQryInstrumentCommissionRate(CSecurityFtdcInstrumentCommissionRateField *pInstrumentCommissionRate,
                                                  CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

    virtual void OnRspQryOrder(CSecurityFtdcOrderField *pOrder, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID,
                               bool bIsLast);

    virtual void OnRspQryTrade(CSecurityFtdcTradeField *pTrade, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID,
                               bool bIsLast);

    virtual void OnRspQryInvestorPosition(CSecurityFtdcInvestorPositionField *pInvestorPosition,
                                          CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

    virtual void OnRtnOrder(CSecurityFtdcOrderField *pOrder);

    virtual void OnRtnTrade(CSecurityFtdcTradeField *pTrade);

    virtual void OnErrRtnOrderInsert(CSecurityFtdcInputOrderField *pInputOrder, CSecurityFtdcRspInfoField *pRspInfo);

    virtual void OnErrRtnOrderAction(CSecurityFtdcOrderActionField *pOrderAction, CSecurityFtdcRspInfoField *pRspInfo);

    virtual void OnRspFundOutByLiber(CSecurityFtdcInputFundTransferField *pInputFundTransfer,
                                     CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

    virtual void OnRtnFundOutByLiber(CSecurityFtdcFundTransferField *pFundTransfer);

    virtual void OnErrRtnFundOutByLiber(CSecurityFtdcInputFundTransferField *pInputFundTransfer,
                                        CSecurityFtdcRspInfoField *pRspInfo);

    virtual void OnRtnFundInByBank(CSecurityFtdcFundTransferField *pFundTransfer);

    virtual void OnRspQryFundTransferSerial(CSecurityFtdcFundTransferField *pFundTransfer,
                                            CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

private:
    PyObject *self;
};