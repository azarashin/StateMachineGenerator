IControllee controllee = new ConsoleOutControllee();
StateController stateController = new StateController(controllee);

int number = 1; 
while(number != 0)
{
    BaseState? currentState = stateController.GetCurrentState();
    if(currentState == null)
    {
        Console.WriteLine($"current state: (end)");
    }
    else
    {
        Console.WriteLine($"current state: {currentState.GetStateName()}");
    }
    if(stateController.TryTransitWithoutEvent())
    {
        continue; 
    }
    Console.WriteLine("1. TransitCommand1");
    Console.WriteLine("2. TransitCommand2");
    Console.WriteLine("3. TransitCommand3");
    Console.WriteLine("");
    Console.WriteLine("0. exit");
    string? line = Console.ReadLine();
    if(int.TryParse(line, out number))
    {
        switch(number)
        {
            case 0:
                break;
            case 1:
                stateController.TransitCommand1();
                break;
            case 2:
                stateController.TransitCommand2();
                break;
            case 3:
                stateController.TransitCommand3();
                break;
            default:
                Console.WriteLine($"Invalid number: {number}");
                break;
        }
    }
}
