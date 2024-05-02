#include "StateController.h"
StateController::StateController(IControllee* controllee)
{
    _controllee = controllee;
    InstanceOfProcessData = new StateProcessData(this, _controllee);
    InstanceOfState1 = new StateState1(this, _controllee);
    InstanceOfState2 = new StateState2(this, _controllee);
    InstanceOfState3 = new StateState3(this, _controllee);
    InstanceOfState4 = new StateState4(this, _controllee);
    InstanceOflong1 = new Statelong1(this, _controllee);
    InstanceOflong2 = new Statelong2(this, _controllee);
    _currentState = InstanceOfState1;
}
StateController::~StateController()
{
    delete InstanceOfProcessData;
    delete InstanceOfState1;
    delete InstanceOfState2;
    delete InstanceOfState3;
    delete InstanceOfState4;
    delete InstanceOflong1;
    delete InstanceOflong2;
}
bool StateController::TryTransitWithoutEvent()
{
    if(_currentState == 0)
    {
        return false;
    }
    BaseState* current = _currentState;
    _currentState = _currentState->TryTransitWithoutEvent();
    if(_currentState != 0)
    {
        _currentState = _currentState->OutlineState();
    }
    return (current != _currentState);
}
void StateController::TransitAborted()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitAborted();
        if(_currentState != 0)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Aborted");
    }
}
void StateController::TransitDeepResume()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitDeepResume();
        if(_currentState != 0)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("DeepResume");
    }
}
void StateController::TransitEnoughData()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitEnoughData();
        if(_currentState != 0)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("EnoughData");
    }
}
void StateController::TransitFailed()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitFailed();
        if(_currentState != 0)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Failed");
    }
}
void StateController::TransitNewData()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitNewData();
        if(_currentState != 0)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("NewData");
    }
}
void StateController::TransitPause()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitPause();
        if(_currentState != 0)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Pause");
    }
}
void StateController::TransitResume()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitResume();
        if(_currentState != 0)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Resume");
    }
}
void StateController::TransitSucceeded()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitSucceeded();
        if(_currentState != 0)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Succeeded");
    }
}
const char* StateController::GetCurrentStateName()
{
    if(_currentState == 0)
    {
        return "(end)";
    }
    else
    {
        return _currentState->GetStateName();
    }
}