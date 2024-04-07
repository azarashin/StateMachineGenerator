public class StateState2 : IState
{
    private StateController _stateController; 
    private IControllee _controllee; 
    public StateState2(StateController stateController, IControllee controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public IState? TransitCommand1()
    {
        _controllee.NoTransition("State2", "Command1");
        return this;
    }
    public IState? TransitCommand2()
    {
        _controllee.NoTransition("State2", "Command2");
        return this;
    }
    public IState? TransitCommand3()
    {
        _controllee.DoAction3();
        return null;
    }
}
