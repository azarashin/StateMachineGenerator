public class StateConfiguring : BaseState
{
    private StateController _stateController;
    private IControllee _controllee;
    public StateConfiguring(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override BaseState? TransitEvConfig()
    {
        _controllee.DoAction2();
        _stateController.InstanceOfIdle.Setup();
        return _stateController.InstanceOfIdle;
    }
    public override string GetStateName()
    {
        return "NotShooting.Configuring";
    }
    public override BaseState? GetParent()
    {
        return _stateController.InstanceOfNotShooting;
    }
}