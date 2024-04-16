public class StateController
{
    private IControllee _controllee;
    private BaseState? _currentState; 
    public BaseState InstanceOfState1 {get; private set;}
    public BaseState InstanceOfState2 {get; private set;}
    public StateController(IControllee controllee)
    {
        _controllee = controllee;
        InstanceOfState1 = new StateState1(this, _controllee);
        InstanceOfState2 = new StateState2(this, _controllee);
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
        return (current != _currentState);
    }
    public void TransitCommand1()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitCommand1();
        } else {
            _controllee.OverTransition("Command1");
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
