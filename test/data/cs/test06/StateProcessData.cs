public class StateProcessData : BaseState
{
    private StateController _stateController;
    private IControllee _controllee;
    public StateProcessData(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override string GetStateName()
    {
        return "State3.State4.ProcessData";
    }
    public override BaseState? GetParent()
    {
        return _stateController.InstanceOfState4;
    }
    public override int GetStateID()
    {
        return 0;
    }
}