#include "ConsoleOutControllee.h"
#include "StateController.h"
#include <stdio.h>
int main(int argc, const char** argv)
{
    IControllee* controllee = new ConsoleOutControllee();
    StateController* stateController = new StateController(controllee);
    int number = 1;
    while(number != 0)
    {
        printf("current state: %s\n", stateController->GetCurrentStateName());
        if(stateController->TryTransitWithoutEvent())
        {
            continue;
        }
        printf("1. Aborted\n");
        printf("2. DeepResume\n");
        printf("3. EnoughData\n");
        printf("4. Failed\n");
        printf("5. NewData\n");
        printf("6. Pause\n");
        printf("7. Resume\n");
        printf("8. Succeeded\n");
        printf("\n");
        printf("0. exit\n");
        printf("-1. ShowStateIDs then resume\n");
        scanf_s("%d", &number);
        switch(number)
        {
            case 0:
                break;
            case 1:
                stateController->TransitAborted();
                break;
            case 2:
                stateController->TransitDeepResume();
                break;
            case 3:
                stateController->TransitEnoughData();
                break;
            case 4:
                stateController->TransitFailed();
                break;
            case 5:
                stateController->TransitNewData();
                break;
            case 6:
                stateController->TransitPause();
                break;
            case 7:
                stateController->TransitResume();
                break;
            case 8:
                stateController->TransitSucceeded();
                break;
            case -1:
            {
                int stateId = stateController->GetCurrentIdFromStateId(-1);
                printf("Top State ID: %d - %s\n", stateId, stateController->StateName(stateId));
                int* subStateIds = new int[stateController->MaxNumberOfStateIDs];
                for(int i=0;i<stateController->MaxNumberOfStateIDs;i++)
                {
                    subStateIds[i] = stateController->GetCurrentIdFromStateId(i);
                    printf("Sub State ID: %d - %s\n", subStateIds[i], stateController->StateName(subStateIds[i]));
                }
                delete stateController;
                stateController = new StateController(controllee);
                printf("StateController has been reset.\n");
                stateController->ResumeState(-1, stateId);
                for(int i=0;i<stateController->MaxNumberOfStateIDs;i++)
                {
                    stateController->ResumeState(i, subStateIds[i]);
                }
                stateId = stateController->GetCurrentIdFromStateId(-1);
                printf("Top State ID: %d - %s\n", stateId, stateController->StateName(stateId));
                for(int i=0;i<stateController->MaxNumberOfStateIDs;i++)
                {
                    subStateIds[i] = stateController->GetCurrentIdFromStateId(i);
                    printf("Sub State ID: %d - %s\n", subStateIds[i], stateController->StateName(subStateIds[i]));
                }
                delete[] subStateIds;
            }
            break;
            default:
                printf("Invalid number: %d\n", number);
                break;
        }
    }
    delete controllee;
    delete stateController;
}