public class StateInitial : BaseState
{
    private StateController _stateController; 
    private IControllee _controllee; 
    public StateInitial(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override BaseState? TransitGoInTo()
    {
        _controllee.DoAction0();
        return _stateController.InstanceOfIdle; 
    }
    public override string GetStateName()
    {
        return "Initial"; 
    }
}
