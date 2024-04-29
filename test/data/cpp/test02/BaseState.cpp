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

BaseState* BaseState::TryTransitWithoutEvent()
{
    return this;
}