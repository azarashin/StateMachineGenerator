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
        printf("1. Escape\n");
        printf("2. EvConfig\n");
        printf("3. GoInTo\n");
        printf("\n");
        printf("0. exit\n");
        printf("-1. ShowStateIDs then resume\n");
        scanf_s("%d", &number);
        switch(number)
        {
            case 0:
                break;
            case 1:
                stateController->TransitEscape();
                break;
            case 2:
                stateController->TransitEvConfig();
                break;
            case 3:
                stateController->TransitGoInTo();
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