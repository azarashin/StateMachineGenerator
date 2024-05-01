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
        printf("1. Event2\n");
        printf("2. Event21\n");
        printf("3. Event31\n");
        printf("4. Event42\n");
        printf("5. Event421\n");
        printf("6. Event431\n");
        printf("\n");
        printf("0. exit\n");
        scanf_s("%d", &number);
        switch(number)
        {
            case 0:
                break;
            case 1:
                stateController->TransitEvent2();
                break;
            case 2:
                stateController->TransitEvent21();
                break;
            case 3:
                stateController->TransitEvent31();
                break;
            case 4:
                stateController->TransitEvent42();
                break;
            case 5:
                stateController->TransitEvent421();
                break;
            case 6:
                stateController->TransitEvent431();
                break;
            default:
                printf("Invalid number: %d\n", number);
                break;
        }
    }
    delete controllee;
    delete stateController;
}