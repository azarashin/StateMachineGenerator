import {BaseState} from "./BaseState"
import {IControllee} from "./IControllee"
import {StateController} from "./StateController"
export class StateState4 extends BaseState
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
        return "State4";
    }
    public GetParent(): BaseState | null
    {
        return null;
    }
    public GetStateID(): number
    {
        return 4;
    }
}