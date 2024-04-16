IControllee controllee = new ConsoleOutControllee();
StateController stateController = new StateController(controllee);

int number = 1; 
while(number != 0)
{
    Console.WriteLine($"current state: {stateController.GetCurrentStateName()}");
    if(stateController.TryTransitWithoutEvent())
    {
        continue; 
    }
    Console.WriteLine("1. Command1");
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
            default:
                Console.WriteLine($"Invalid number: {number}");
                break;
        }
    }
}
