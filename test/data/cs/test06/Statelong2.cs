public class Statelong2 : BaseState
{
    private StateController _stateController;
    private IControllee _controllee;
    public Statelong2(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override BaseState? TransitEnoughData()
    {
        _stateController.InstanceOfProcessData.Setup(false, false);
        return _stateController.InstanceOfProcessData;
    }
    public override BaseState? TransitNewData()
    {
        _stateController.InstanceOflong2.Setup(false, false);
        return _stateController.InstanceOflong2;
    }
    public override string GetStateName()
    {
        return "State3.State4.long2";
    }
    public override BaseState? GetParent()
    {
        return _stateController.InstanceOfState4;
    }
}