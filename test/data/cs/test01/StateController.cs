public class StateController
{
    private IControllee _controllee;
    private State? _currentState; 
    public State InstanceOfStateState1 {get; private set;}
    public State InstanceOfStateState2 {get; private set;}
    public StateController(IControllee controllee)
    {
        _controllee = controllee;
        InstanceOfStateState1 = new StateState1(this, _controllee);
        InstanceOfStateState2 = new StateState2(this, _controllee);
        _currentState = InstanceOfStateState1; 
    }
    public void ExecCommand1()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitCommand1();
        }
    }
    public void ExecCommand2()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitCommand2();
        }
    }
    public void ExecCommand3()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitCommand3();
        }
    }
}
