#include "MdAPI.h"
#include "trader_struct.h"

MdSpiWrapper::MdSpiWrapper(PyObject * parent): CSecurityFtdcMdSpi() {
    py_spi = parent;
    Py_INCREF(py_spi);
}


void MdSpiWrapper::OnFrontConnected() {
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();

    Py_Initialize();
    if (!PyObject_CallMethod(py_spi, "OnFrontConnected", NULL)) {
        PyErr_Print();
    }
    Py_Finalize();
    PyGILState_Release(gstate);

}

void MdSpiWrapper::OnFrontDisconnected(int nReason) {
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    Py_Initialize();
    if (!PyObject_CallMethod(py_spi, "OnFrontDisconnected", "i", nReason)) {
        PyErr_Print();
    }
    Py_Finalize();
    PyGILState_Release(gstate);
}

void  MdSpiWrapper::OnHeartBeatWarning(int nTimeLapse) {
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    Py_Initialize();
    if (!PyObject_CallMethod(py_spi, "OnHeartBeatWarning", "i", nTimeLapse)) {
        PyErr_Print();
    }
    Py_Finalize();
    PyGILState_Release(gstate);

}

void MdSpiWrapper::OnRspError(CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {

    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    Py_Initialize();
    if (!PyObject_CallMethod(py_spi, "OnRspError", "Nib", new_CSecurityFtdcRspInfoField(pRspInfo),
                             nRequestID, bIsLast)) {
        PyErr_Print();
    }
    Py_Finalize();

    PyGILState_Release(gstate);
}

void  MdSpiWrapper::OnRspUserLogin(CSecurityFtdcRspUserLoginField *pRspUserLogin, CSecurityFtdcRspInfoField *pRspInfo,
                                   int nRequestID, bool bIsLast) {

    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    Py_Initialize();
    if (!PyObject_CallMethod(py_spi, "OnRspUserLogin", "NNib",
                             new_CSecurityFtdcRspUserLoginField(pRspUserLogin), new_CSecurityFtdcRspInfoField(pRspInfo),
                             nRequestID, bIsLast)) {
        PyErr_Print();
    }
    Py_Finalize();
    PyGILState_Release(gstate);
}

void  MdSpiWrapper::OnRspUserLogout(CSecurityFtdcUserLogoutField *pUserLogout, CSecurityFtdcRspInfoField *pRspInfo,
                                    int nRequestID, bool bIsLast) {

    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    Py_Initialize();
    if (!PyObject_CallMethod(py_spi, "OnRspUserLogout", "NNib",
                             new_CSecurityFtdcUserLogoutField(pUserLogout), new_CSecurityFtdcRspInfoField(pRspInfo),
                             nRequestID, bIsLast)) {
        PyErr_Print();
    }
    Py_Finalize();
    PyGILState_Release(gstate);
}

void MdSpiWrapper::OnRspSubMarketData(CSecurityFtdcSpecificInstrumentField *pSpecificInstrument,
                                      CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {

    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    Py_Initialize();
    if (!PyObject_CallMethod(py_spi, "OnRspSubMarketData", "NNib",
                             new_CSecurityFtdcSpecificInstrumentField(pSpecificInstrument),
                             new_CSecurityFtdcRspInfoField(pRspInfo), nRequestID, bIsLast)) {
        PyErr_Print();
    }
    Py_Finalize();

    PyGILState_Release(gstate);

}

void MdSpiWrapper::OnRspUnSubMarketData(CSecurityFtdcSpecificInstrumentField *pSpecificInstrument,
                                        CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {

    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    Py_Initialize();
    if (!PyObject_CallMethod(py_spi, "OnRspUnSubMarketData", "NNib",
                             new_CSecurityFtdcSpecificInstrumentField(pSpecificInstrument),
                             new_CSecurityFtdcRspInfoField(pRspInfo), nRequestID, bIsLast)) {
        PyErr_Print();
    }
    Py_Finalize();
    PyGILState_Release(gstate);

}
