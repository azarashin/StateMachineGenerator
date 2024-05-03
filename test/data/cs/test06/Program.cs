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
    Console.WriteLine("1. Aborted");
    Console.WriteLine("2. DeepResume");
    Console.WriteLine("3. EnoughData");
    Console.WriteLine("4. Failed");
    Console.WriteLine("5. NewData");
    Console.WriteLine("6. Pause");
    Console.WriteLine("7. Resume");
    Console.WriteLine("8. Succeeded");
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
                stateController.TransitAborted();
                break;
            case 2:
                stateController.TransitDeepResume();
                break;
            case 3:
                stateController.TransitEnoughData();
                break;
            case 4:
                stateController.TransitFailed();
                break;
            case 5:
                stateController.TransitNewData();
                break;
            case 6:
                stateController.TransitPause();
                break;
            case 7:
                stateController.TransitResume();
                break;
            case 8:
                stateController.TransitSucceeded();
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