#include "StateProcessData.h"
StateProcessData::StateProcessData(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateProcessData::~StateProcessData()
{
}
const char* StateProcessData::GetStateName()
{
    return "State3.State4.ProcessData";
}
BaseState* StateProcessData::GetParent()
{
    return _stateController->InstanceOfState4;
}