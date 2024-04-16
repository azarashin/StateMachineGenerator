public class StateConfiguring : BaseState
{
    private StateController _stateController; 
    private IControllee _controllee; 
    public StateConfiguring(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override BaseState? TransitEscape()
    {
        _controllee.DoAction3();
        return _stateController.InstanceOfEscaped; 
    }
    public override BaseState? TransitEvConfig()
    {
        _controllee.DoAction2();
        return _stateController.InstanceOfIdle; 
    }
    public override string GetStateName()
    {
        return "NotShooting.Configuring"; 
    }
}
