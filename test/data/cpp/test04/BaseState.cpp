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