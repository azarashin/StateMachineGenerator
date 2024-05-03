public class StateController
{
    private IControllee _controllee;
    private BaseState? _currentState;
    public BaseState InstanceOfConfiguring {get; private set;}
    public BaseState InstanceOfEscaped {get; private set;}
    public BaseState InstanceOfIdle {get; private set;}
    public BaseState InstanceOfInitial {get; private set;}
    public BaseState InstanceOfNotShooting {get; private set;}
    private BaseState[] _stateList;
    public int MaxNumberOfStateIDs {get; private set;} = 5;
    public StateController(IControllee controllee)
    {
        _controllee = controllee;
        InstanceOfConfiguring = new StateConfiguring(this, _controllee);
        InstanceOfEscaped = new StateEscaped(this, _controllee);
        InstanceOfIdle = new StateIdle(this, _controllee);
        InstanceOfInitial = new StateInitial(this, _controllee);
        InstanceOfNotShooting = new StateNotShooting(this, _controllee);
        _currentState = InstanceOfInitial;
        _stateList = new BaseState[] {
            InstanceOfConfiguring,
            InstanceOfEscaped,
            InstanceOfIdle,
            InstanceOfInitial,
            InstanceOfNotShooting
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
    public void TransitEscape()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitEscape();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("Escape");
        }
    }
    public void TransitEvConfig()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitEvConfig();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("EvConfig");
        }
    }
    public void TransitGoInTo()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitGoInTo();
            if(_currentState != null)
            {
                _currentState = _currentState.OutlineState();
            }
        } else {
            _controllee.OverTransition("GoInTo");
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