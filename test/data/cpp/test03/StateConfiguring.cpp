#include "StateConfiguring.h"
StateConfiguring::StateConfiguring(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateConfiguring::~StateConfiguring()
{
}
BaseState* StateConfiguring::TransitEvConfig()
{
    _controllee->DoAction2();
    _stateController->InstanceOfIdle->Setup(false, false);
    return _stateController->InstanceOfIdle;
}
const char* StateConfiguring::GetStateName()
{
    return "NotShooting.Configuring";
}
BaseState* StateConfiguring::GetParent()
{
    return _stateController->InstanceOfNotShooting;
}
int StateConfiguring::GetStateID()
{
    return 0;
}