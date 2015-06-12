#include "MdAPI.h"


MdSpiWrapper::MdSpiWrapper(PyObject *parent):CSecurityFtdcMdSpi()
{
    py_spi = parent;
    Py_INCREF(py_spi);
}


void MdSpiWrapper::OnFrontConnected()
{
  PyGILState_STATE gstate;
  gstate=PyGILState_Ensure();

  if(!PyObject_CallMethod(py_spi,(char *)"OnFrontConnected",NULL))
  {
  PyErr_Print();
  }

  PyGILState_Release(gstate);

}

void MdSpiWrapper::OnFrontDisconnected(int nReason)
{
  PyGILState_STATE gstate;
  gstate=PyGILState_Ensure();
  if(!PyObject_CallMethod(py_spi,(char*)"OnFrontDisconnected",(char*)"i",nReason))
  {
  PyErr_Print();
  }
  PyGILState_Release(gstate);
}
void  MdSpiWrapper::OnHeartBeatWarning(int nTimeLapse)
{
PyGILState_STATE gstate;
  gstate=PyGILState_Ensure();
  if(!PyObject_CallMethod(py_spi,(char*)"OnHeartBeatWarning",(char*)"i",nTimeLapse))
  {
  PyErr_Print();
  }

  PyGILState_Release(gstate);

}

void MdSpiWrapper::OnRspError(CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{

PyGILState_STATE gstate;
  gstate=PyGILState_Ensure();
  if(!PyObject_CallMethod(py_spi,(char*)"OnRspError",(char*)"Nib",new_CSecurityFtdcRspInfoField(pRspInfo),nRequestID,bIsLast)){
  PyErr_Print();
  }

  PyGILState_Release(gstate);
}

void  MdSpiWrapper::OnRspUserLogin(CSecurityFtdcRspUserLoginField *pRspUserLogin, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{

  PyGILState_STATE gstate;
  gstate=PyGILState_Ensure();
if(!PyObject_CallMethod(py_spi,(char*)"OnRspUserLogin",(char*)"NNib",new_CSecurityFtdcRspUserLoginField(pRspUserLogin),new_CSecurityFtdcRspInfoField(pRspInfo),nRequestID,bIsLast))
{
PyErr_Print();
}
  PyGILState_Release(gstate);
}

void  MdSpiWrapper::OnRspUserLogout(CSecurityFtdcUserLogoutField *pUserLogout, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{

PyGILState_STATE gstate;
  gstate=PyGILState_Ensure();
  if(!PyObject_CallMethod(py_spi,(char*)"OnRspUserLogout",(char*)"NNib",new_CSecurityFtdcUserLogoutField(pUserLogout),new_CSecurityFtdcRspInfoField(pRspInfo),nRequestID,bIsLast))
  {
  PyErr_Print();
  }

  PyGILState_Release(gstate);
}

void MdSpiWrapper::OnRspSubMarketData(CSecurityFtdcSpecificInstrumentField *pSpecificInstrument, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{

PyGILState_STATE gstate;
  gstate=PyGILState_Ensure();

  if(!PyObject_CallMethod(py_spi,(char*)"OnRspSubMarketData",(char*)"NNib",new_CSecurityFtdcSpecificInstrumentField(pSpecificInstrument),new_CSecurityFtdcRspInfoField(pRspInfo),nRequestID,bIsLast))
  {
  PyErr_Print();
  }


  PyGILState_Release(gstate);

}
void MdSpiWrapper::OnRspUnSubMarketData(CSecurityFtdcSpecificInstrumentField *pSpecificInstrument, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{

PyGILState_STATE gstate;
  gstate=PyGILState_Ensure();
  if(!PyObject_CallMethod(py_spi,(char*)"OnRspUnSubMarketData",(char*)"NNib",new_CSecurityFtdcSpecificInstrumentField(pSpecificInstrument),new_CSecurityFtdcRspInfoField(pRspInfo),nRequestID,bIsLast))
  {
  PyErr_Print();
  }

  PyGILState_Release(gstate);

}
