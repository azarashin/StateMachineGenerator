#include "StateNotShooting.h"
StateNotShooting::StateNotShooting(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateNotShooting::~StateNotShooting()
{
}
void StateNotShooting::Setup()
{
        SetupSubState(_stateController->InstanceOfIdle);
}
BaseState* StateNotShooting::TransitEscape()
{
    _controllee->DoAction3();
    _stateController->InstanceOfEscaped->Setup();
    return _stateController->InstanceOfEscaped;
}
BaseState* StateNotShooting::TransitEvConfig()
{
    BaseState* currentSubState = CurrentSubState();
    if(currentSubState != 0)
    {
        BaseState* nextState = currentSubState->TransitEvConfig();
        return TransitBySubState(nextState);
    }
    return 0;
}
const char* StateNotShooting::GetStateName()
{
    BaseState* currentSubState = CurrentSubState();
    if(currentSubState == 0)
    {
        return "NotShooting(end)";
    }
    return currentSubState->GetStateName();
}
BaseState* StateNotShooting::GetParent()
{
    return 0;
}