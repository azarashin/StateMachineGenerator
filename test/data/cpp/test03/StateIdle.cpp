#include "StateIdle.h"

StateIdle::StateIdle(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateIdle::~StateIdle()
{
}
BaseState* StateIdle::TransitEscape()
{
    _controllee->DoAction3();
    return _stateController->InstanceOfEscaped;
}
BaseState* StateIdle::TransitEvConfig()
{
    _controllee->DoAction1();
    return _stateController->InstanceOfConfiguring;
}
const char* StateIdle::GetStateName()
{
    return "NotShooting.Idle";
}