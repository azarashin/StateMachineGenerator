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
        _currentState.Setup();
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
        if(_currentState == null)
        {
            return null;
        }
        BaseState? nextState = _currentState.TransitEvConfig();
        if(nextState == null)
        {
            return nextState;
        }
        BaseState? parentOfNextState = _currentState.GetParent();
        BaseState? parentOfCurrentState = nextState.GetParent();
        if(parentOfNextState is not null && parentOfCurrentState is not null && parentOfNextState == parentOfCurrentState)
        {
            return this;
        }
        return nextState;
    }
    public override string GetStateName()
    {
        if(_currentState == null)
        {
            return "NotShooting(end)";
        }
        return _currentState.GetStateName();
    }
    public override BaseState? GetParent()
    {
        return null;
    }
}