public class StateState4 : BaseState
{
    private StateController _stateController;
    private IControllee _controllee;
    public StateState4(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override void Setup(bool resume, bool deepResume)
    {
        if(!deepResume)
        {
            SetupSubState(_stateController.InstanceOflong2, resume);
        }
    }
    public override BaseState? TransitEnoughData()
    {
        BaseState? currentSubState = CurrentSubState();
        if(currentSubState != null)
        {
            BaseState? nextState = currentSubState.TransitEnoughData();
            return TransitBySubState(nextState);
        }
        return null;
    }
    public override BaseState? TransitNewData()
    {
        BaseState? currentSubState = CurrentSubState();
        if(currentSubState != null)
        {
            BaseState? nextState = currentSubState.TransitNewData();
            return TransitBySubState(nextState);
        }
        return null;
    }
    public override string GetStateName()
    {
        BaseState? currentSubState = CurrentSubState();
        if(currentSubState == null)
        {
            return "State3.State4(end)";
        }
        return currentSubState.GetStateName();
    }
    public override BaseState? GetParent()
    {
        return _stateController.InstanceOfState3;
    }
    public override int GetStateID()
    {
        return 4;
    }
}