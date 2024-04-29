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
