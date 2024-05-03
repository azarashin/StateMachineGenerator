#include "Statelong1.h"
Statelong1::Statelong1(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
Statelong1::~Statelong1()
{
}
BaseState* Statelong1::TransitEnoughData()
{
    _stateController->InstanceOfState4->Setup(false, false);
    return _stateController->InstanceOfState4;
}
BaseState* Statelong1::TransitNewData()
{
    _stateController->InstanceOflong1->Setup(false, false);
    return _stateController->InstanceOflong1;
}
const char* Statelong1::GetStateName()
{
    return "State3.long1";
}
BaseState* Statelong1::GetParent()
{
    return _stateController->InstanceOfState3;
}
int Statelong1::GetStateID()
{
    return 5;
}