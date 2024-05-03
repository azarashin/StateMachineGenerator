public class StateState31 : BaseState
{
    private StateController _stateController;
    private IControllee _controllee;
    public StateState31(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override BaseState? TransitEvent431()
    {
        _controllee.DoAction431();
        _stateController.InstanceOfState4.Setup(false, false);
        return _stateController.InstanceOfState4;
    }
    public override string GetStateName()
    {
        return "State2.State21.State31";
    }
    public override BaseState? GetParent()
    {
        return _stateController.InstanceOfState21;
    }
    public override int GetStateID()
    {
        return 3;
    }
}