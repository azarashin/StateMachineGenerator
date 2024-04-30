public class StateNotShooting : BaseState
{
    private StateController _stateController; 
    private IControllee _controllee; 
    private BaseState? _currentState; 
    public StateNotShooting(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override void Setup()
    {
        _currentState = _stateController.InstanceOfIdle; 
        return;
    }
    public override BaseState? TransitEscape()
    {
        _controllee.DoAction3();
        _stateController.InstanceOfEscaped.Setup();
        return _stateController.InstanceOfEscaped; 
    }
    public override BaseState? TransitEvConfig()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitEvConfig();
            return this; 
        }
        return null; 
    }
    public override string GetStateName()
    {
        return "NotShooting"; 
    }
}
