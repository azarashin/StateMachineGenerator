public class StateEscaped : BaseState
{
    private StateController _stateController; 
    private IControllee _controllee; 
    public StateEscaped(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override BaseState? TryTransitWithoutEvent()
    {
        return this;
    }
    protected override string GetStateName()
    {
        return "Escape"; 
    }
}
