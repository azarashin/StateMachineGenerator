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
    public virtual BaseState? TransitCommand1()
    {
        _controllee.NoTransition(GetStateName(), "Command1");
        return this;
    }
    public virtual BaseState? TransitCommand2()
    {
        _controllee.NoTransition(GetStateName(), "Command2");
        return this;
    }
    public virtual BaseState? TransitCommand3()
    {
        _controllee.NoTransition(GetStateName(), "Command3");
        return this;
    }
    public virtual BaseState? TryTransitWithoutEvent()
    {
        return this;
    }
    public void SetupSubState(BaseState child)
    {
        _currentSubState = child;
        _currentSubState.Setup();
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
    public void TransitForChild(BaseState? child)
    {
        _currentSubState = child;
        BaseState? parent = GetParent();
        if(parent != null)
        {
            parent.TransitForChild(this);
        }
    }
    public abstract string GetStateName();
    public abstract BaseState? GetParent();
}