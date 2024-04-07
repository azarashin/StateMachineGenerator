// See https://aka.ms/new-console-template for more information
IControllee controllee = new ConsoleOutControllee();
StateController stateController = new StateController(controllee);

stateController.ExecCommand2();
stateController.ExecCommand2();
stateController.ExecCommand1();
stateController.ExecCommand1();
stateController.ExecCommand3();
stateController.ExecCommand3();
stateController.ExecCommand1();
stateController.ExecCommand1();
