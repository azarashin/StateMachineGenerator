abstract public class BaseState
{
    private IControllee _controllee; 
    public BaseState(IControllee controllee)
    {
        _controllee = controllee;
    }
    public virtual BaseState? TransitGoInTo()
    {
        _controllee.NoTransition(GetStateName(), "GoInTo");
        return this;
    }
    public virtual BaseState? TransitEvConfig()
    {
        _controllee.NoTransition(GetStateName(), "EvConfig");
        return this;
    }
    public virtual BaseState? TransitEscape()
    {
        _controllee.NoTransition(GetStateName(), "Escape");
        return this;
    }
    public virtual BaseState? TryTransitWithoutEvent()
    {
        return this;
    }
    protected abstract string GetStateName();

}
