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
    _stateController->InstanceOfConfiguring->Setup(false, false);
    return _stateController->InstanceOfConfiguring;
}
const char* StateIdle::GetStateName()
{
    return "NotShooting.Idle";
}
BaseState* StateIdle::GetParent()
{
    return _stateController->InstanceOfNotShooting;
}
int StateIdle::GetStateID()
{
    return 2;
}