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
BaseState* BaseState::TransitEscape()
{
    _controllee->NoTransition(GetStateName(), "Escape");
    return this;
}
BaseState* BaseState::TransitEvConfig()
{
    _controllee->NoTransition(GetStateName(), "EvConfig");
    return this;
}
BaseState* BaseState::TransitGoInTo()
{
    _controllee->NoTransition(GetStateName(), "GoInTo");
    return this;
}
BaseState* BaseState::TryTransitWithoutEvent()
{
    return this;
}
void BaseState::SetupSubState(BaseState* child)
{
    _currentSubState = child;
    _currentSubState->Setup();
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
void BaseState::TransitForChild(BaseState* child)
{
    _currentSubState = child;
    BaseState* parent = GetParent();
    if(parent != 0)
    {
        parent->TransitForChild(this);
    }
}