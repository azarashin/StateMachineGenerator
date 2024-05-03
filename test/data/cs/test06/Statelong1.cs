public class Statelong1 : BaseState
{
    private StateController _stateController;
    private IControllee _controllee;
    public Statelong1(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override BaseState? TransitEnoughData()
    {
        _stateController.InstanceOfState4.Setup(false, false);
        return _stateController.InstanceOfState4;
    }
    public override BaseState? TransitNewData()
    {
        _stateController.InstanceOflong1.Setup(false, false);
        return _stateController.InstanceOflong1;
    }
    public override string GetStateName()
    {
        return "State3.long1";
    }
    public override BaseState? GetParent()
    {
        return _stateController.InstanceOfState3;
    }
    public override int GetStateID()
    {
        return 5;
    }
}