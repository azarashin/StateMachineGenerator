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
    _stateController->InstanceOfIdle->Setup();
    return _stateController->InstanceOfIdle;
}
const char* StateConfiguring::GetStateName()
{
    return "NotShooting.Configuring";
}