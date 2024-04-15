public class StateIdle : BaseState
{
    private StateController _stateController; 
    private IControllee _controllee; 
    public StateIdle(StateController stateController, IControllee controllee) : base(controllee)
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
        _controllee.DoAction1();
        return _stateController.InstanceOfConfiguring; 
    }
    protected override string GetStateName()
    {
        return "NotShooting.Idle"; 
    }
}
