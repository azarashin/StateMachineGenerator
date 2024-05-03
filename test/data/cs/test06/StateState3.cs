public class StateState3 : BaseState
{
    private StateController _stateController;
    private IControllee _controllee;
    public StateState3(StateController stateController, IControllee controllee) : base(controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public override void Setup(bool resume, bool deepResume)
    {
        if(!deepResume)
        {
            SetupSubState(_stateController.InstanceOflong1, resume);
        }
    }
    public override BaseState? TransitAborted()
    {
        return null;
    }
    public override BaseState? TransitFailed()
    {
        _stateController.InstanceOfState3.Setup(false, false);
        return _stateController.InstanceOfState3;
    }
    public override BaseState? TransitPause()
    {
        _stateController.InstanceOfState2.Setup(false, false);
        return _stateController.InstanceOfState2;
    }
    public override BaseState? TransitSucceeded()
    {
        _controllee.DoSaveResult();
        return null;
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
            return "State3(end)";
        }
        return currentSubState.GetStateName();
    }
    public override BaseState? GetParent()
    {
        return null;
    }
    public override int GetStateID()
    {
        return 3;
    }
}