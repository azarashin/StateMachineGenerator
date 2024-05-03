#include "BaseState.h"
BaseState::BaseState(IControllee* controllee)
{
    _controllee = controllee;
    _currentSubState = nullptr;
}
BaseState::~BaseState()
{
}
void BaseState::Setup(bool resume, bool deepResume)
{
}
BaseState* BaseState::TransitCommand1()
{
    _controllee->NoTransition(GetStateName(), "Command1");
    return this;
}
BaseState* BaseState::TransitCommand2()
{
    _controllee->NoTransition(GetStateName(), "Command2");
    return this;
}
BaseState* BaseState::TransitCommand3()
{
    _controllee->NoTransition(GetStateName(), "Command3");
    return this;
}
BaseState* BaseState::TryTransitWithoutEvent()
{
    return this;
}
void BaseState::SetupSubState(BaseState* child, bool resume)
{
    if(!resume)
    {
        _currentSubState = child;
    }
    if(_currentSubState != nullptr)
    {
        _currentSubState->Setup(false, false);
    }
}
BaseState* BaseState::CurrentSubState()
{
    return _currentSubState;
}
BaseState* BaseState::TransitBySubState(BaseState* nextState)
{
    if(nextState == nullptr || _currentSubState == nullptr)
    {
        return nextState;
    }
    BaseState* parentOfNextState = _currentSubState->GetParent();
    BaseState* parentOfCurrentState = nextState->GetParent();
    if(parentOfNextState != nullptr && parentOfCurrentState != nullptr && parentOfNextState == parentOfCurrentState)
    {
        _currentSubState = nextState;
        return this;
    }
    return nextState;
}
BaseState* BaseState::TransitForChild(BaseState* child)
{
    _currentSubState = child;
    BaseState* parent = GetParent();
    if(parent != nullptr)
    {
        return parent->TransitForChild(this);
    }
    return this;
}
BaseState* BaseState::OutlineState()
{
    BaseState* parent = GetParent();
    if(parent != nullptr)
    {
        return parent->TransitForChild(this);
    }
    return this;
}
void BaseState::ResumeSubState(BaseState* subState)
{
    _currentSubState = subState;
}