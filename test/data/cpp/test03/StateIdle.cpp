#include "StateIdle.h"

StateIdle::StateIdle(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateIdle::~StateIdle()
{
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