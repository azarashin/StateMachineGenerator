#include "StateState2.h"
StateState2::StateState2(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateState2::~StateState2()
{
}
BaseState* StateState2::TryTransitWithoutEvent()
{
    _controllee->DoAction3();
    return nullptr;
}
const char* StateState2::GetStateName()
{
    return "State2";
}
BaseState* StateState2::GetParent()
{
    return nullptr;
}
int StateState2::GetStateID()
{
    return 1;
}