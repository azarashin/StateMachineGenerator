import {BaseState} from "./BaseState"
import {IControllee} from "./IControllee"
import {StateController} from "./StateController"
export class StateState1 extends BaseState
{
    private _stateController: StateController;
    private _controlleeImp: IControllee;
    public constructor(stateController: StateController, controllee: IControllee)
    {
        super(controllee);
        this._stateController = stateController;
        this._controlleeImp = controllee;
    }
    public TransitAborted(): BaseState | null
    {
        return null;
    }
    public TransitSucceeded(): BaseState | null
    {
        this._stateController.InstanceOfState2.Setup(false, false);
        return this._stateController.InstanceOfState2;
    }
    public  GetStateName(): string
    {
        return "State1";
    }
    public GetParent(): BaseState | null
    {
        return null;
    }
}