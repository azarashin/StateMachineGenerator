public class StateController
{
    private IControllee _controllee;
    private BaseState? _currentState; 
    public BaseState InstanceOfConfiguring {get; private set;}
    public BaseState InstanceOfEscaped {get; private set;}
    public BaseState InstanceOfIdle {get; private set;}
    public BaseState InstanceOfInitial {get; private set;}
    public StateController(IControllee controllee)
    {
        _controllee = controllee;
        InstanceOfConfiguring = new StateConfiguring(this, _controllee);
        InstanceOfEscaped = new StateEscaped(this, _controllee);
        InstanceOfIdle = new StateIdle(this, _controllee);
        InstanceOfInitial = new StateInitial(this, _controllee);
        _currentState = InstanceOfInitial; 
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
    public void TransitEscape()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitEscape();
        } else {
            _controllee.OverTransition("Escape");
        }
    }
    public void TransitEvConfig()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitEvConfig();
        } else {
            _controllee.OverTransition("EvConfig");
        }
    }
    public void TransitGoInTo()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitGoInTo();
        } else {
            _controllee.OverTransition("GoInTo");
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
