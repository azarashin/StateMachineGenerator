#include "StateEscaped.h"
StateEscaped::StateEscaped(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateEscaped::~StateEscaped()
{
}
const char* StateEscaped::GetStateName()
{
    return "Escaped";
}