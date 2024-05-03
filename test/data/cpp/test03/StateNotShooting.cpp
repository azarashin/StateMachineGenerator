#include "StateNotShooting.h"
StateNotShooting::StateNotShooting(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateNotShooting::~StateNotShooting()
{
}
void StateNotShooting::Setup(bool resume, bool deepResume)
{
    if(!deepResume)
    {
        SetupSubState(_stateController->InstanceOfIdle, resume);
    }
}
BaseState* StateNotShooting::TransitEscape()
{
    _controllee->DoAction3();
    _stateController->InstanceOfEscaped->Setup(false, false);
    return _stateController->InstanceOfEscaped;
}
BaseState* StateNotShooting::TransitEvConfig()
{
    BaseState* currentSubState = CurrentSubState();
    if(currentSubState != nullptr)
    {
        BaseState* nextState = currentSubState->TransitEvConfig();
        return TransitBySubState(nextState);
    }
    return nullptr;
}
const char* StateNotShooting::GetStateName()
{
    BaseState* currentSubState = CurrentSubState();
    if(currentSubState == nullptr)
    {
        return "NotShooting(end)";
    }
    return currentSubState->GetStateName();
}
BaseState* StateNotShooting::GetParent()
{
    return nullptr;
}
int StateNotShooting::GetStateID()
{
    return 4;
}