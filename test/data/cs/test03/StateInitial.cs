public class StateInitial : BaseState
{
    private StateController _stateController;
    private IControllee _controllee;
    public StateInitial(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override BaseState? TransitGoInTo()
    {
        _controllee.DoAction0();
        _stateController.InstanceOfNotShooting.Setup(false, false);
        return _stateController.InstanceOfNotShooting;
    }
    public override string GetStateName()
    {
        return "Initial";
    }
    public override BaseState? GetParent()
    {
        return null;
    }
}