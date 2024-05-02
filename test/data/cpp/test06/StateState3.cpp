#include "StateState3.h"
StateState3::StateState3(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateState3::~StateState3()
{
}
void StateState3::Setup(bool resume, bool deepResume)
{
    if(!deepResume)
    {
        SetupSubState(_stateController->InstanceOflong1, resume);
    }
}
BaseState* StateState3::TransitAborted()
{
    return 0;
}
BaseState* StateState3::TransitFailed()
{
    _stateController->InstanceOfState3->Setup(false, false);
    return _stateController->InstanceOfState3;
}
BaseState* StateState3::TransitPause()
{
    _stateController->InstanceOfState2->Setup(false, false);
    return _stateController->InstanceOfState2;
}
BaseState* StateState3::TransitSucceeded()
{
    _controllee->DoSaveResult();
    return 0;
}
BaseState* StateState3::TransitEnoughData()
{
    BaseState* currentSubState = CurrentSubState();
    if(currentSubState != 0)
    {
        BaseState* nextState = currentSubState->TransitEnoughData();
        return TransitBySubState(nextState);
    }
    return 0;
}
BaseState* StateState3::TransitNewData()
{
    BaseState* currentSubState = CurrentSubState();
    if(currentSubState != 0)
    {
        BaseState* nextState = currentSubState->TransitNewData();
        return TransitBySubState(nextState);
    }
    return 0;
}
const char* StateState3::GetStateName()
{
    BaseState* currentSubState = CurrentSubState();
    if(currentSubState == 0)
    {
        return "State3(end)";
    }
    return currentSubState->GetStateName();
}
BaseState* StateState3::GetParent()
{
    return 0;
}