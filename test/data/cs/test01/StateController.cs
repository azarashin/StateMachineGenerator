public class StateController
{
    private IControllee _controllee;
    private IState? _currentState; 
    public IState InstanceOfStateState1 {get; private set;}
    public IState InstanceOfStateState2 {get; private set;}
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
        } else {
            _controllee.OverTransition("Command1");
        }
    }
    public void ExecCommand2()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitCommand2();
        } else {
            _controllee.OverTransition("Command2");
        }
    }
    public void ExecCommand3()
    {
        if(_currentState != null)
        {
            _currentState = _currentState.TransitCommand3();
        } else {
            _controllee.OverTransition("Command3");
        }
    }
}
