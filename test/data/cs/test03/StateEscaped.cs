public class StateEscaped : BaseState
{
    private StateController _stateController;
    private IControllee _controllee;
    public StateEscaped(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override string GetStateName()
    {
        return "Escaped";
    }
    public override BaseState? GetParent()
    {
        return null;
    }
    public override int GetStateID()
    {
        return 1;
    }
}