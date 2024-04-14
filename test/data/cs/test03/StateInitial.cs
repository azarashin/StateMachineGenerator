/// <summary>
/// this is a string
/// this is another string
/// </summary>
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
    public override BaseState? TryTransitWithoutEvent()
    {
        return this; 
    }
    protected override string GetStateName()
    {
        return "Initial"; 
    }
}
