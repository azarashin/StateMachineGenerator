public class StateController
{
    private IControllee _controllee;
    private BaseState? _currentState;
    public BaseState InstanceOfState1 {get; private set;}
    public BaseState InstanceOfState2 {get; private set;}
    private BaseState[] _stateList;
    public int MaxNumberOfStateIDs {get; private set;} = 2;
    public StateController(IControllee controllee)
    {
        _controllee = controllee;
        InstanceOfState1 = new StateState1(this, _controllee);
        InstanceOfState2 = new StateState2(this, _controllee);
        _currentState = InstanceOfState1;
        _stateList = new BaseState[] {
            InstanceOfState1,
            InstanceOfState2
        };
    }
    public int GetCurrentIdFromStateId(int parentStateId)
    {
        if(parentStateId == -1)
        {
            return GetCurrentIdFromState(_currentState);
        }
        if(parentStateId < -1 || parentStateId >= MaxNumberOfStateIDs)
        {
            return -1;
        }
        return GetCurrentIdFromState(_stateList[parentStateId].CurrentSubState());
    }
    private int GetCurrentIdFromState(BaseState? state)
    {
        if(state == null)
        {
            return -1;
        }
    return state.GetStateID();
    }
    public void ResumeState(int parentStateId, int stateId)
    {
        BaseState? state = null;
        if(stateId >= 0 && stateId < MaxNumberOfStateIDs)
        {
            state = _stateList[stateId];
        }
        if(parentStateId == -1)
        {
            _currentState = state;
            return;
        }
        if(parentStateId < -1 || parentStateId >= MaxNumberOfStateIDs)
        {
            return;
        }
        _stateList[parentStateId].ResumeSubState(state);
    }
    public string StateName(int parentStateId)
    {
        if(parentStateId >= 0 && parentStateId < MaxNumberOfStateIDs)
        {
            return _stateList[parentStateId].GetStateName();
        }
        return "(None)";
    }
    public bool TryTransitWithoutEvent()
    {
        if(_currentState == null)
        {
            return false;
        }
        BaseState? current = _currentState;
        _currentState = _currentState.TryTransitWithoutEvent();
        if(_currentState != null)
        {
            _currentState = _currentState.OutlineState();
        }
        return (current != _currentState);
    }
    public void TransitCommand1()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitCommand1();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("Command1");
        }
    }
    public string GetCurrentStateName()
    {
        if(_currentState == null)
        {
            return "(end)";
        }
        else
        {
            return _currentState.GetStateName();
        }
    }
}