#include "BaseState.h"
BaseState::BaseState(IControllee* controllee)
{
    _controllee = controllee;
}
BaseState::~BaseState()
{
}
void BaseState::Setup(bool resume, bool deepResume)
{
}
BaseState* BaseState::TransitEvent2()
{
    _controllee->NoTransition(GetStateName(), "Event2");
    return this;
}
BaseState* BaseState::TransitEvent21()
{
    _controllee->NoTransition(GetStateName(), "Event21");
    return this;
}
BaseState* BaseState::TransitEvent31()
{
    _controllee->NoTransition(GetStateName(), "Event31");
    return this;
}
BaseState* BaseState::TransitEvent42()
{
    _controllee->NoTransition(GetStateName(), "Event42");
    return this;
}
BaseState* BaseState::TransitEvent421()
{
    _controllee->NoTransition(GetStateName(), "Event421");
    return this;
}
BaseState* BaseState::TransitEvent431()
{
    _controllee->NoTransition(GetStateName(), "Event431");
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
    if(_currentSubState != 0)
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