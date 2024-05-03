#include "StateState4.h"
StateState4::StateState4(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateState4::~StateState4()
{
}
void StateState4::Setup(bool resume, bool deepResume)
{
    if(!deepResume)
    {
        SetupSubState(_stateController->InstanceOflong2, resume);
    }
}
BaseState* StateState4::TransitEnoughData()
{
    BaseState* currentSubState = CurrentSubState();
    if(currentSubState != nullptr)
    {
        BaseState* nextState = currentSubState->TransitEnoughData();
        return TransitBySubState(nextState);
    }
    return nullptr;
}
BaseState* StateState4::TransitNewData()
{
    BaseState* currentSubState = CurrentSubState();
    if(currentSubState != nullptr)
    {
        BaseState* nextState = currentSubState->TransitNewData();
        return TransitBySubState(nextState);
    }
    return nullptr;
}
const char* StateState4::GetStateName()
{
    BaseState* currentSubState = CurrentSubState();
    if(currentSubState == nullptr)
    {
        return "State3.State4(end)";
    }
    return currentSubState->GetStateName();
}
BaseState* StateState4::GetParent()
{
    return _stateController->InstanceOfState3;
}
int StateState4::GetStateID()
{
    return 4;
}