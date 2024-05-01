public class StateController
{
    private IControllee _controllee;
    private BaseState? _currentState;
    public BaseState InstanceOfState1 {get; private set;}
    public BaseState InstanceOfState2 {get; private set;}
    public BaseState InstanceOfState21 {get; private set;}
    public BaseState InstanceOfState31 {get; private set;}
    public BaseState InstanceOfState4 {get; private set;}
    public StateController(IControllee controllee)
    {
        _controllee = controllee;
        InstanceOfState1 = new StateState1(this, _controllee);
        InstanceOfState2 = new StateState2(this, _controllee);
        InstanceOfState21 = new StateState21(this, _controllee);
        InstanceOfState31 = new StateState31(this, _controllee);
        InstanceOfState4 = new StateState4(this, _controllee);
        _currentState = InstanceOfState1;
    }
    public bool TryTransitWithoutEvent()
    {
        if(_currentState == null)
        {
            return false;
        }
        BaseState? current = _currentState;
        _currentState = _currentState.TryTransitWithoutEvent();
        if(_currentState != null)
        {
            _currentState = _currentState.OutlineState();
        }
        return (current != _currentState);
    }
    public void TransitEvent2()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitEvent2();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("Event2");
        }
    }
    public void TransitEvent21()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitEvent21();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("Event21");
        }
    }
    public void TransitEvent31()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitEvent31();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("Event31");
        }
    }
    public void TransitEvent42()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitEvent42();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("Event42");
        }
    }
    public void TransitEvent421()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitEvent421();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("Event421");
        }
    }
    public void TransitEvent431()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitEvent431();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("Event431");
        }
    }
    public string GetCurrentStateName()
    {
        if(_currentState == null)
        {
            return "(end)";
        }
        else
        {
            return _currentState.GetStateName();
        }
    }
}