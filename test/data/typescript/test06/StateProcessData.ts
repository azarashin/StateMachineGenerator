import {BaseState} from "./BaseState"
import {IControllee} from "./IControllee"
import {StateController} from "./StateController"
export class StateProcessData extends BaseState
{
    private _stateController: StateController;
    private _controlleeImp: IControllee;
    public constructor(stateController: StateController, controllee: IControllee)
    {
        super(controllee);
        this._stateController = stateController;
        this._controlleeImp = controllee;
    }
    public  GetStateName(): string
    {
        return "State3.State4.ProcessData";
    }
    public GetParent(): BaseState | null
    {
        return this._stateController.InstanceOfState4;
    }
    public GetStateID(): number
    {
        return 0;
    }
}