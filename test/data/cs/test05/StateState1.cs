public class StateState1 : BaseState
{
    private StateController _stateController;
    private IControllee _controllee;
    public StateState1(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override BaseState? TransitEvent2()
    {
        _controllee.DoAction2();
        _stateController.InstanceOfState2.Setup(false, false);
        return _stateController.InstanceOfState2;
    }
    public override BaseState? TransitEvent21()
    {
        _controllee.DoAction21();
        _stateController.InstanceOfState21.Setup(false, false);
        return _stateController.InstanceOfState21;
    }
    public override BaseState? TransitEvent31()
    {
        _controllee.DoAction31();
        _stateController.InstanceOfState31.Setup(false, false);
        return _stateController.InstanceOfState31;
    }
    public override string GetStateName()
    {
        return "State1";
    }
    public override BaseState? GetParent()
    {
        return null;
    }
    public override int GetStateID()
    {
        return 0;
    }
}