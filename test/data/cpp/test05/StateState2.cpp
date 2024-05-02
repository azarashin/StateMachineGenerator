#include "StateState2.h"
StateState2::StateState2(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateState2::~StateState2()
{
}
void StateState2::Setup(bool resume, bool deepResume)
{
    if(!deepResume)
    {
        SetupSubState(_stateController->InstanceOfState21, resume);
    }
}
BaseState* StateState2::TransitEvent42()
{
    _controllee->DoAction42();
    _stateController->InstanceOfState4->Setup(false, false);
    return _stateController->InstanceOfState4;
}
BaseState* StateState2::TransitEvent421()
{
    BaseState* currentSubState = CurrentSubState();
    if(currentSubState != 0)
    {
        BaseState* nextState = currentSubState->TransitEvent421();
        return TransitBySubState(nextState);
    }
    return 0;
}
BaseState* StateState2::TransitEvent431()
{
    BaseState* currentSubState = CurrentSubState();
    if(currentSubState != 0)
    {
        BaseState* nextState = currentSubState->TransitEvent431();
        return TransitBySubState(nextState);
    }
    return 0;
}
const char* StateState2::GetStateName()
{
    BaseState* currentSubState = CurrentSubState();
    if(currentSubState == 0)
    {
        return "State2(end)";
    }
    return currentSubState->GetStateName();
}
BaseState* StateState2::GetParent()
{
    return 0;
}