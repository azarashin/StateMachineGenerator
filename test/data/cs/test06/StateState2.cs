public class StateState2 : BaseState
{
    private StateController _stateController;
    private IControllee _controllee;
    public StateState2(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override BaseState? TransitAborted()
    {
        return null;
    }
    public override BaseState? TransitDeepResume()
    {
        _stateController.InstanceOfState3.Setup(true, true);
        return _stateController.InstanceOfState3;
    }
    public override BaseState? TransitResume()
    {
        _stateController.InstanceOfState3.Setup(true, false);
        return _stateController.InstanceOfState3;
    }
    public override BaseState? TransitSucceeded()
    {
        _stateController.InstanceOfState3.Setup(false, false);
        return _stateController.InstanceOfState3;
    }
    public override string GetStateName()
    {
        return "State2";
    }
    public override BaseState? GetParent()
    {
        return null;
    }
}