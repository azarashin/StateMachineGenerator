#include "StateState21.h"
StateState21::StateState21(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateState21::~StateState21()
{
}
void StateState21::Setup(bool resume, bool deepResume)
{
    if(!deepResume)
    {
        SetupSubState(_stateController->InstanceOfState31, resume);
    }
}
BaseState* StateState21::TransitEvent421()
{
    _controllee->DoAction421();
    _stateController->InstanceOfState4->Setup(false, false);
    return _stateController->InstanceOfState4;
}
BaseState* StateState21::TransitEvent431()
{
    BaseState* currentSubState = CurrentSubState();
    if(currentSubState != 0)
    {
        BaseState* nextState = currentSubState->TransitEvent431();
        return TransitBySubState(nextState);
    }
    return 0;
}
const char* StateState21::GetStateName()
{
    BaseState* currentSubState = CurrentSubState();
    if(currentSubState == 0)
    {
        return "State2.State21(end)";
    }
    return currentSubState->GetStateName();
}
BaseState* StateState21::GetParent()
{
    return _stateController->InstanceOfState2;
}
int StateState21::GetStateID()
{
    return 2;
}