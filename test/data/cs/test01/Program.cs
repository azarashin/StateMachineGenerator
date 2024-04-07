// See https://aka.ms/new-console-template for more information
IControllee controllee = new ConsoleOutControllee();
StateController stateController = new StateController(controllee);

stateController.TransitCommand2();
stateController.TransitCommand2();
stateController.TransitCommand1();
stateController.TransitCommand1();
stateController.TransitCommand3();
stateController.TransitCommand3();
stateController.TransitCommand1();
stateController.TransitCommand1();
