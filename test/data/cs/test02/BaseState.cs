abstract public class BaseState
{
    private IControllee _controllee; 
    public BaseState(IControllee controllee)
    {
        _controllee = controllee;
    }
    public virtual BaseState? TransitCommand1()
    {
        _controllee.NoTransition(GetStateName(), "Command1");
        return this;
    }
    public virtual BaseState? TryTransitWithoutEvent()
    {
        return this;
    }
    protected abstract string GetStateName();

}
