#include <Python.h>
#include "SecurityFtdcMdApi.h"


class MdSpiWrapper : public CSecurityFtdcMdSpi {
public:

    MdSpiWrapper(PyObject *parent);

    virtual ~MdSpiWrapper();

    virtual void OnFrontConnected();

    virtual void OnFrontDisconnected(int nReason);

    virtual void OnHeartBeatWarning(int nTimeLapse);

    virtual void OnRspError(CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

    virtual void OnRspUserLogin(CSecurityFtdcRspUserLoginField *pRspUserLogin, CSecurityFtdcRspInfoField *pRspInfo,
                                int nRequestID, bool bIsLast);

    virtual void OnRspUserLogout(CSecurityFtdcUserLogoutField *pUserLogout, CSecurityFtdcRspInfoField *pRspInfo,
                                 int nRequestID, bool bIsLast);

    virtual void OnRspSubMarketData(CSecurityFtdcSpecificInstrumentField *pSpecificInstrument,
                                    CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

    virtual void OnRspUnSubMarketData(CSecurityFtdcSpecificInstrumentField *pSpecificInstrument,
                                      CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);

    virtual void OnRtnDepthMarketData(CSecurityFtdcDepthMarketDataField *pDepthMarketData);

private:
    PyObject *py_spi;
};