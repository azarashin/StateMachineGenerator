public class StateState4 : BaseState
{
    private StateController _stateController;
    private IControllee _controllee;
    public StateState4(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override string GetStateName()
    {
        return "State4";
    }
    public override BaseState? GetParent()
    {
        return null;
    }
}