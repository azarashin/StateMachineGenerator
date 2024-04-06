public class StateState1 : State
{
    private StateController _stateController; 
    private IControllee _controllee; 
    public StateState1(StateController stateController, IControllee controllee)
    {
        _stateController = stateController;
        _controllee = controllee;
    }
    public State? TransitCommand1()
    {
        _controllee.DoAction1();
        return null;
    }
    public State? TransitCommand2()
    {
        _controllee.DoAction2();
        return _stateController.InstanceOfStateState2;
    }
    public State? TransitCommand3()
    {
        _controllee.NoTransition("State1", "Command3");
        return this;
    }
}
