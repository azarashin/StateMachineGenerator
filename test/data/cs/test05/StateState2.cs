public class StateState2 : BaseState
{
    private StateController _stateController;
    private IControllee _controllee;
    public StateState2(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override void Setup(bool resume, bool deepResume)
    {
        if(!deepResume)
        {
            SetupSubState(_stateController.InstanceOfState21, resume);
        }
    }
    public override BaseState? TransitEvent42()
    {
        _controllee.DoAction42();
        _stateController.InstanceOfState4.Setup(false, false);
        return _stateController.InstanceOfState4;
    }
    public override BaseState? TransitEvent421()
    {
        BaseState? currentSubState = CurrentSubState();
        if(currentSubState != null)
        {
            BaseState? nextState = currentSubState.TransitEvent421();
            return TransitBySubState(nextState);
        }
        return null;
    }
    public override BaseState? TransitEvent431()
    {
        BaseState? currentSubState = CurrentSubState();
        if(currentSubState != null)
        {
            BaseState? nextState = currentSubState.TransitEvent431();
            return TransitBySubState(nextState);
        }
        return null;
    }
    public override string GetStateName()
    {
        BaseState? currentSubState = CurrentSubState();
        if(currentSubState == null)
        {
            return "State2(end)";
        }
        return currentSubState.GetStateName();
    }
    public override BaseState? GetParent()
    {
        return null;
    }
}