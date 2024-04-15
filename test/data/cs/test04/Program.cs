// See https://aka.ms/new-console-template for more information
IControllee controllee = new ConsoleOutControllee();
StateController stateController = new StateController(controllee);

stateController.TryTransitWithoutEvent();
stateController.TransitGoInTo();
stateController.TryTransitWithoutEvent();
stateController.TransitEvConfig();
stateController.TryTransitWithoutEvent();
stateController.TransitEvConfig();
stateController.TryTransitWithoutEvent();
stateController.TransitEscape();
