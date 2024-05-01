#include "StateState1.h"
StateState1::StateState1(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateState1::~StateState1()
{
}
BaseState* StateState1::TransitCommand1()
{
    _controllee->DoAction1();
    return 0;
}
BaseState* StateState1::TransitCommand2()
{
    _controllee->DoAction2();
    _stateController->InstanceOfState2->Setup();
    return _stateController->InstanceOfState2;
}
const char* StateState1::GetStateName()
{
    return "State1";
}
BaseState* StateState1::GetParent()
{
    return 0;
}