abstract public class BaseState
{
    private IControllee _controllee;
    private BaseState? _currentSubState;
    public BaseState(IControllee controllee)
    {
        _controllee = controllee;
    }
    public virtual void Setup(bool resume, bool deepResume)
    {
        return;
    }
    public virtual BaseState? TransitEscape()
    {
        _controllee.NoTransition(GetStateName(), "Escape");
        return this;
    }
    public virtual BaseState? TransitEvConfig()
    {
        _controllee.NoTransition(GetStateName(), "EvConfig");
        return this;
    }
    public virtual BaseState? TransitGoInTo()
    {
        _controllee.NoTransition(GetStateName(), "GoInTo");
        return this;
    }
    public virtual BaseState? TryTransitWithoutEvent()
    {
        return this;
    }
    public void SetupSubState(BaseState? child, bool resume)
    {
        if(!resume)
        {
            _currentSubState = child;
        }
        if(_currentSubState != null)
        {
            _currentSubState.Setup(false, false);
        }
    }
    public BaseState? CurrentSubState()
    {
        return _currentSubState;
    }
    public BaseState? TransitBySubState(BaseState? nextState)
    {
        if(nextState == null || _currentSubState == null)
        {
            return nextState;
        }
        BaseState? parentOfNextState = _currentSubState.GetParent();
        BaseState? parentOfCurrentState = nextState.GetParent();
        if(parentOfNextState is not null && parentOfCurrentState is not null && parentOfNextState == parentOfCurrentState)
        {
            _currentSubState = nextState;
            return this;
        }
        return nextState;
    }
    public BaseState? TransitForChild(BaseState? child)
    {
        _currentSubState = child;
        BaseState? parent = GetParent();
        if(parent != null)
        {
            return parent.TransitForChild(this);
        }
        return this;
    }
    public BaseState? OutlineState()
    {
        BaseState? parent = GetParent();
        if(parent != null)
        {
            return parent.TransitForChild(this);
        }
        return this;
    }
    public void ResumeSubState(BaseState? subState)
    {
        _currentSubState = subState;
    }
    public abstract string GetStateName();
    public abstract BaseState? GetParent();
    public abstract int GetStateID();
}