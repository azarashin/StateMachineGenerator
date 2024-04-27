abstract public class BaseState
{
    private IControllee _controllee; 
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
    public virtual BaseState? TryTransitWithoutEvent()
    {
        return this;
    }
    public abstract string GetStateName();

}
