#include "StateState2.h"
StateState2::StateState2(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateState2::~StateState2()
{
}
BaseState* StateState2::TransitAborted()
{
    return 0;
}
BaseState* StateState2::TransitDeepResume()
{
    _stateController->InstanceOfState3->Setup(true, true);
    return _stateController->InstanceOfState3;
}
BaseState* StateState2::TransitResume()
{
    _stateController->InstanceOfState3->Setup(true, false);
    return _stateController->InstanceOfState3;
}
BaseState* StateState2::TransitSucceeded()
{
    _stateController->InstanceOfState3->Setup(false, false);
    return _stateController->InstanceOfState3;
}
const char* StateState2::GetStateName()
{
    return "State2";
}
BaseState* StateState2::GetParent()
{
    return 0;
}
int StateState2::GetStateID()
{
    return 2;
}