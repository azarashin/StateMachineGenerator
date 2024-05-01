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
            default:
                printf("Invalid number: %d\n", number);
                break;
        }
    }
    delete controllee;
    delete stateController;
}