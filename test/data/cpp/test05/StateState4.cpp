#include "StateState4.h"
StateState4::StateState4(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateState4::~StateState4()
{
}
const char* StateState4::GetStateName()
{
    return "State4";
}
BaseState* StateState4::GetParent()
{
    return nullptr;
}
int StateState4::GetStateID()
{
    return 4;
}