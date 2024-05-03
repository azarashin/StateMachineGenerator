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
    Console.WriteLine("2. Command2");
    Console.WriteLine("3. Command3");
    Console.WriteLine("");
    Console.WriteLine("0. exit");
    Console.WriteLine("-1. ShowStateIDs then resume");
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
            case -1:
            {
                int stateId = stateController.GetCurrentIdFromStateId(-1);
                Console.WriteLine($"Top State ID: {stateId} - {stateController.StateName(stateId)}");
                int[] subStateIds = new int[stateController.MaxNumberOfStateIDs];
                for(int i=0;i<stateController.MaxNumberOfStateIDs;i++)
                {
                    subStateIds[i] = stateController.GetCurrentIdFromStateId(i);
                    Console.WriteLine($"Sub State ID: {subStateIds[i]} - {stateController.StateName(subStateIds[i])}");
                }
                stateController = new StateController(controllee);
                Console.WriteLine($"StateController has been reset.");
                stateController.ResumeState(-1, stateId);
                for(int i=0;i<stateController.MaxNumberOfStateIDs;i++)
                {
                    stateController.ResumeState(i, subStateIds[i]);
                }
                stateId = stateController.GetCurrentIdFromStateId(-1);
                Console.WriteLine($"Top State ID: {stateId} - {stateController.StateName(stateId)}");
                for(int i=0;i<stateController.MaxNumberOfStateIDs;i++)
                {
                    subStateIds[i] = stateController.GetCurrentIdFromStateId(i);
                    Console.WriteLine($"Sub State ID: {subStateIds[i]} - {stateController.StateName(subStateIds[i])}");
                }
            }
                break;
            default:
                Console.WriteLine($"Invalid number: {number}");
                break;
        }
    }
}