public class StateEscaped : BaseState
{
    private StateController _stateController; 
    private IControllee _controllee; 
    public StateEscaped(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    protected override string GetStateName()
    {
        return "Escaped"; 
    }
}
