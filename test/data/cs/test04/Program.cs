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
    Console.WriteLine("1. Escape");
    Console.WriteLine("2. EvConfig");
    Console.WriteLine("3. GoInTo");
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
                stateController.TransitEscape();
                break;
            case 2:
                stateController.TransitEvConfig();
                break;
            case 3:
                stateController.TransitGoInTo();
                break;
            default:
                Console.WriteLine($"Invalid number: {number}");
                break;
        }
    }
}