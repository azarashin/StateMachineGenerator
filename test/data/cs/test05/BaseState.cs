abstract public class BaseState
{
    private IControllee _controllee;
    private BaseState? _currentSubState;
    public BaseState(IControllee controllee)
    {
        _controllee = controllee;
    }
    public virtual void Setup()
    {
        return;
    }
    public virtual BaseState? TransitEvent2()
    {
        _controllee.NoTransition(GetStateName(), "Event2");
        return this;
    }
    public virtual BaseState? TransitEvent21()
    {
        _controllee.NoTransition(GetStateName(), "Event21");
        return this;
    }
    public virtual BaseState? TransitEvent31()
    {
        _controllee.NoTransition(GetStateName(), "Event31");
        return this;
    }
    public virtual BaseState? TransitEvent42()
    {
        _controllee.NoTransition(GetStateName(), "Event42");
        return this;
    }
    public virtual BaseState? TransitEvent421()
    {
        _controllee.NoTransition(GetStateName(), "Event421");
        return this;
    }
    public virtual BaseState? TransitEvent431()
    {
        _controllee.NoTransition(GetStateName(), "Event431");
        return this;
    }
    public virtual BaseState? TryTransitWithoutEvent()
    {
        return this;
    }
    public void SetupSubState(BaseState? child)
    {
        _currentSubState = child;
        if(_currentSubState != null)
        {
            _currentSubState.Setup();
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
    public abstract string GetStateName();
    public abstract BaseState? GetParent();
}