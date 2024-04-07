public class StateState1 : BaseState
{
    private StateController _stateController; 
    private IControllee _controllee; 
    public StateState1(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override BaseState? TransitCommand1()
    {
        _controllee.DoAction1();
        return null;
    }
    public override BaseState? TransitCommand2()
    {
        _controllee.DoAction2();
        return _stateController.InstanceOfState2;
    }
    protected override string GetStateName()
    {
        return "State1"; 
    }
}
