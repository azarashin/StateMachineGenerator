public class StateIdle : BaseState
{
    private StateController _stateController;
    private IControllee _controllee;
    public StateIdle(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override BaseState? TransitEvConfig()
    {
        _controllee.DoAction1();
        _stateController.InstanceOfConfiguring.Setup(false, false);
        return _stateController.InstanceOfConfiguring;
    }
    public override string GetStateName()
    {
        return "NotShooting.Idle";
    }
    public override BaseState? GetParent()
    {
        return _stateController.InstanceOfNotShooting;
    }
    public override int GetStateID()
    {
        return 2;
    }
}