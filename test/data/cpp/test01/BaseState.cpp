#include "BaseState.h"
BaseState::BaseState(IControllee* controllee)
{
    _controllee = controllee;
}
BaseState::~BaseState()
{
}
void BaseState::Setup()
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
void BaseState::SetupSubState(BaseState* child)
{
    _currentSubState = child;
    if(_currentSubState != 0)
    {
        _currentSubState->Setup();
    }
}
BaseState* BaseState::CurrentSubState()
{
    return _currentSubState;
}
BaseState* BaseState::TransitBySubState(BaseState* nextState)
{
    if(nextState == 0 || _currentSubState == 0)
    {
        return nextState;
    }
    BaseState* parentOfNextState = _currentSubState->GetParent();
    BaseState* parentOfCurrentState = nextState->GetParent();
    if(parentOfNextState != 0 && parentOfCurrentState != 0 && parentOfNextState == parentOfCurrentState)
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
    if(parent != 0)
    {
        return parent->TransitForChild(this);
    }
    return this;
}
BaseState* BaseState::OutlineState()
{
    BaseState* parent = GetParent();
    if(parent != 0)
    {
        return parent->TransitForChild(this);
    }
    return this;
}