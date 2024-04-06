public class StateState2 : State
{
    private StateController _stateController; 
    private IControllee _controllee; 
    public StateState2(StateController stateController, IControllee controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public State? TransitCommand1()
    {
        _controllee.NoTransition("State2", "Command1");
        return this;
    }
    public State? TransitCommand2()
    {
        _controllee.NoTransition("State2", "Command2");
        return this;
    }
    public State? TransitCommand3()
    {
        _controllee.DoAction3();
        return null;
    }
}
