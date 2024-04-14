public class StateState2 : BaseState
{
    private StateController _stateController; 
    private IControllee _controllee; 
    public StateState2(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override BaseState? TryTransitWithoutEvent()
    {
        _controllee.DoAction3();
        return null;
    }
    protected override string GetStateName()
    {
        return "State2"; 
    }
}
