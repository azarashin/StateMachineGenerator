#include "Statelong2.h"
Statelong2::Statelong2(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
Statelong2::~Statelong2()
{
}
BaseState* Statelong2::TransitEnoughData()
{
    _stateController->InstanceOfProcessData->Setup(false, false);
    return _stateController->InstanceOfProcessData;
}
BaseState* Statelong2::TransitNewData()
{
    _stateController->InstanceOflong2->Setup(false, false);
    return _stateController->InstanceOflong2;
}
const char* Statelong2::GetStateName()
{
    return "State3.State4.long2";
}
BaseState* Statelong2::GetParent()
{
    return _stateController->InstanceOfState4;
}
int Statelong2::GetStateID()
{
    return 6;
}