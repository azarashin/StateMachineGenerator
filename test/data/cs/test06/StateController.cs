public class StateController
{
    private IControllee _controllee;
    private BaseState? _currentState;
    public BaseState InstanceOfProcessData {get; private set;}
    public BaseState InstanceOfState1 {get; private set;}
    public BaseState InstanceOfState2 {get; private set;}
    public BaseState InstanceOfState3 {get; private set;}
    public BaseState InstanceOfState4 {get; private set;}
    public BaseState InstanceOflong1 {get; private set;}
    public BaseState InstanceOflong2 {get; private set;}
    public StateController(IControllee controllee)
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
    public void TransitAborted()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitAborted();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("Aborted");
        }
    }
    public void TransitDeepResume()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitDeepResume();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("DeepResume");
        }
    }
    public void TransitEnoughData()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitEnoughData();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("EnoughData");
        }
    }
    public void TransitFailed()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitFailed();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("Failed");
        }
    }
    public void TransitNewData()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitNewData();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("NewData");
        }
    }
    public void TransitPause()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitPause();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("Pause");
        }
    }
    public void TransitResume()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitResume();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("Resume");
        }
    }
    public void TransitSucceeded()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitSucceeded();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("Succeeded");
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