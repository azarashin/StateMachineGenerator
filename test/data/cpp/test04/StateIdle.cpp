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
    _stateController->InstanceOfEscaped->Setup();
    return _stateController->InstanceOfEscaped;
}
BaseState* StateIdle::TransitEvConfig()
{
    _controllee->DoAction1();
    _stateController->InstanceOfConfiguring->Setup();
    return _stateController->InstanceOfConfiguring;
}
const char* StateIdle::GetStateName()
{
    return "NotShooting.Idle";
}