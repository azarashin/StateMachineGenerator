#include "StateConfiguring.h"

StateConfiguring::StateConfiguring(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateConfiguring::~StateConfiguring()
{
}
BaseState* StateConfiguring::TransitEscape()
{
    _controllee->DoAction3();
    return _stateController->InstanceOfEscaped;
}
BaseState* StateConfiguring::TransitEvConfig()
{
    _controllee->DoAction2();
    return _stateController->InstanceOfIdle;
}
const char* StateConfiguring::GetStateName()
{
    return "NotShooting.Configuring";
}