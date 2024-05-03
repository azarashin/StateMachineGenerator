public class StateNotShooting : BaseState
{
    private StateController _stateController;
    private IControllee _controllee;
    public StateNotShooting(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override void Setup(bool resume, bool deepResume)
    {
        if(!deepResume)
        {
            SetupSubState(_stateController.InstanceOfIdle, resume);
        }
    }
    public override BaseState? TransitEscape()
    {
        _controllee.DoAction3();
        _stateController.InstanceOfEscaped.Setup(false, false);
        return _stateController.InstanceOfEscaped;
    }
    public override BaseState? TransitEvConfig()
    {
        BaseState? currentSubState = CurrentSubState();
        if(currentSubState != null)
        {
            BaseState? nextState = currentSubState.TransitEvConfig();
            return TransitBySubState(nextState);
        }
        return null;
    }
    public override string GetStateName()
    {
        BaseState? currentSubState = CurrentSubState();
        if(currentSubState == null)
        {
            return "NotShooting(end)";
        }
        return currentSubState.GetStateName();
    }
    public override BaseState? GetParent()
    {
        return null;
    }
    public override int GetStateID()
    {
        return 4;
    }
}