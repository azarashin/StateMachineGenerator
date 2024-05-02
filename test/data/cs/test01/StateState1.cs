/// <summary>
/// this is a string
/// this is another string
/// </summary>
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
        _stateController.InstanceOfState2.Setup(false, false);
        return _stateController.InstanceOfState2;
    }
    public override string GetStateName()
    {
        return "State1";
    }
    public override BaseState? GetParent()
    {
        return null;
    }
}