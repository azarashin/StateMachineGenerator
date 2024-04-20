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
        printf("1. Command1\n");
        printf("2. Command2\n");
        printf("3. Command3\n");
        printf("\n");
        printf("0. exit\n");
        scanf_s("%d", &number);
        switch(number)
        {
            case 0:
                break;
            case 1:
                stateController->TransitCommand1();
                break;
            case 2:
                stateController->TransitCommand2();
                break;
            case 3:
                stateController->TransitCommand3();
                break;
            default:
                printf("Invalid number: %d\n", number);
                break;
        }
    }
    delete controllee; 
    delete stateController; 
}
